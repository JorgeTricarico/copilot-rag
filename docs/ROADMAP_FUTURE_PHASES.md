# Roadmap Técnico de Fases Futuras (Fases 4, 5 y 6)

Este documento especifica el diseño técnico, la arquitectura de integración y las limitaciones operativas de las fases avanzadas del pipeline determinista de VS Code Copilot para su mantenimiento y evolución continua.

---

## 1. Fase 4: Sincronización Zero-Touch con Google NotebookLM en GitHub Actions

### 1.1. Propósito y Alcance Técnico
El objetivo de la Fase 4 es cerrar el ciclo de actualización continua sin requerir intervención humana: cada vez que el sincronizador (`scripts/copilot_docs_sync.py`) detecta cambios semánticos en la documentación oficial, genera compendios actualizados y emite el archivo de metadatos `copilot_rag_workspace/dirty_bundles.json`. 

El módulo [`scripts/notebooklm_auto_sync.py`](../scripts/notebooklm_auto_sync.py) opera como el agente de sincronización remota:
1. Lee `dirty_bundles.json`. Si `has_changes: false` o no hay compendios marcados como sucios, finaliza inmediatamente con código `0` sin realizar llamadas a red.
2. Si existen compendios modificados:
   - Restaura el perfil de sesión en `~/.notebooklm/storage_state.json` a partir del secreto `NOTEBOOKLM_AUTH_JSON`.
   - Consulta el inventario de fuentes del cuaderno mediante `notebooklm source list -n <NOTEBOOK_ID> --json`.
   - Elimina la versión previa del compendio modificado (`notebooklm source delete <SOURCE_ID>`).
   - Sube la nueva versión del archivo (`notebooklm source add <PATH>`).
   - Monitorea el estado de procesamiento hasta que el estado del documento sea `READY` (`notebooklm source wait <NEW_SOURCE_ID>`).

### 1.2. Limitaciones Operativas y Mitigaciones
- **Autenticación Basada en Sesión**: Google NotebookLM no ofrece actualmente una API REST pública oficial con claves de servicio OAuth clásicas de Google Cloud. Por ello, la autenticación depende de la extracción de cookies y tokens de sesión de navegador.
  - *Mitigación*: Se utiliza la biblioteca `notebooklm-py` que emula el protocolo de almacenamiento de sesión (`storage_state.json`). Para renovar la sesión, el administrador ejecuta `notebooklm login` en su estación de trabajo local y copia el JSON resultante en el secreto de repositorio `NOTEBOOKLM_AUTH_JSON`.
- **Expiración de Sesión**: Las cookies de sesión pueden expirar cada 30 a 90 días dependiendo de las políticas de seguridad de la cuenta de Google.
  - *Mitigación*: El script `notebooklm_auto_sync.py` captura los fallos de autenticación (código de error de sesión inválida) y envía una alerta vía `webhook_notifier.py` para avisar al administrador que se requiere refrescar el secreto.

---

## 2. Fases 5 y 6: Expansión de Cobertura y CI/CD Avanzado

### 2.1. Monitoreo Continuo de Repositorios Periféricos
Además de `microsoft/vscode-docs`, `github/docs`, `microsoft/vscode`, `github/awesome-copilot` y `anthropics/skills`, existen repositorios periféricos cruciales para el ecosistema de agentes:
- **`microsoft/vscode-pull-request-github`**: Contiene la lógica de integración de revisiones de código asistidas por Copilot, chat en diffs y herramientas de Pull Request.
- **`microsoft/vscode-dev-containers`**: Especificaciones de entornos de ejecución aislados para agentes (Dev Containers, devcontainer.json).

#### Integración Planificada:
Se agregarán reglas a `REPO_RULES` en `scripts/copilot_docs_sync.py`:
```python
RepoTreeRule(
    owner="microsoft",
    repo="vscode-pull-request-github",
    branch="main",
    path_prefixes=["docs/copilot/", "README.md"],
    web_base_url="https://github.com/microsoft/vscode-pull-request-github/blob/main/",
    bundle_router={"": "05_Workflows_Planning_And_Remote_AHP"},
    allowed_extensions=(".md",),
),
```

### 2.2. CI/CD Avanzado y Empaquetado Determinista con Repomix
- **Ejecución de Pruebas Unitarias en GitHub Actions**: Toda ejecución en el workflow `.github/workflows/sync-copilot-rag.yml` ejecuta obligatoriamente `pytest tests/ -v` antes de iniciar la sincronización. Si alguna prueba falla (por ejemplo, por cambios en la gramática de Liquid o en las macros de VS Code), el flujo se aborta de inmediato para evitar propagar compendios corruptos.
- **Empaquetado Repomix Optimizado**: Mediante [`repomix.config.json`](../repomix.config.json), el empaquetado del repositorio para asistentes de IA y agentes móviles (`repo celu`) excluye de forma estricta las carpetas de caché masiva (`copilot_rag_workspace/`, `clean_sources/`, `notebooklm_bundles/`), reduciendo el volumen de salida a menos de **50.000 tokens** e impidiendo cualquier truncamiento de código fuente o scripts de automatización.

### 2.3. Limitaciones Actuales y Estrategia de Escalado
- **Límites de Tasa de la API de GitHub (Rate Limits)**: Sin token autenticado, GitHub restringe a 60 peticiones/hora.
  - *Solución*: En CI/CD se provee siempre `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}` (5.000 req/hora). Para repositorios que superen los 100.000 nodos (como `github/docs`), el motor utiliza subárboles Git específicos (`trees/{branch}:content/copilot?recursive=1`), garantizando que una sincronización completa consuma menos de 10 peticiones a la API de GitHub.
