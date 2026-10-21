# Arquitectura de Monitoreo Determinista e Ingeniería de Contexto RAG para VS Code Copilot

[![Deterministic VS Code Copilot Docs RAG Sync](https://github.com/microsoft/vscode-docs/actions/workflows/sync-copilot-rag.yml/badge.svg?branch=main)](.github/workflows/sync-copilot-rag.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![RAG Target: Google NotebookLM](https://img.shields.io/badge/RAG%20Target-Google%20NotebookLM-purple.svg)](https://notebooklm.google.com/)

Sistema automatizado de monitoreo determinista, canonicalización de contenido, detección diferencial de cambios mediante hashing criptográfico SHA-256 y empaquetado RAG estructurado para **Google NotebookLM** y arquitecturas de agentes autónomos en **Visual Studio Code Copilot**.

---

## 📌 Tabla de Contenidos

1. [Visión General y Propósito](#-visión-general-y-propósito)
2. [Evolución del Ecosistema de Agentes](#-evolución-del-ecosistema-de-agentes)
3. [Arquitectura del Sistema](#-arquitectura-del-sistema)
   - [Normalización Determinista y Hashing SHA-256](#normalización-determinista-y-hashing-sha-256)
   - [Los 7 Compendios Maestros para NotebookLM](#los-7-compendios-maestros-para-notebooklm)
4. [Estructura del Proyecto](#-estructura-del-proyecto)
5. [Instalación y Requisitos](#-instalación-y-requisitos)
6. [Guía de Uso](#-guía-de-uso)
   - [Ejecución Local](#ejecución-local)
   - [Opciones de Línea de Comandos](#opciones-de-línea-de-comandos)
7. [Automatización en CI/CD (GitHub Actions)](#-automatización-en-cicd-github-actions)
8. [Pruebas Automatizadas](#-pruebas-automatizadas)
9. [Documentación Técnica Detallada](#-documentación-técnica-detallada)

---

## 🚀 Visión General y Propósito

El ecosistema de inteligencia artificial en Visual Studio Code ha migrado de una extensión de autocompletado en línea (`GitHub.copilot`) hacia una plataforma distribuida de orquestación de agentes (`GitHub.copilot-chat`), con una estructura documental modularizada en `microsoft/vscode-docs` y `github/docs`.

Este proyecto resuelve el problema crítico de la **no-determinicidad** y los **falsos positivos** al sincronizar documentación técnica:
- **Scraping tradicional ruidoso**: Cambios en timestamps, banners publicitarios, cookies o espaciados generan alertas y reentrenamientos innecesarios.
- **Solución determinista**: Doble vía de canonicalización semántica (AST/Texto + variables Liquid + macros VS Code + normalización Unicode NFKC) y hashing SHA-256 sobre contenido canónico limpio.
- **Empaquetado RAG de alta fidelidad**: Distribuye más de 100 documentos oficiales en **7 Compendios Maestros**, respetando el límite estricto de 500,000 palabras de Google NotebookLM con metadatos de citación canónica inyectados.

---

## 🧠 Evolución del Ecosistema de Agentes

El sistema rastrea las 4 dimensiones arquitectónicas desacopladas de VS Code Copilot:

| Dimensión | Definición Operativa |
| :--- | :--- |
| **Language Model** | Motor de inferencia y razonamiento (Claude 3.7 Sonnet, GPT-4o, o3-mini, Gemini, etc.). |
| **Agent Role** | Instrucciones, herramientas y límites de comportamiento (`Ask`, `Plan`, `Agent`, o `*.agent.md`). |
| **Agent Harness** | Runtime y motor de coordinación (`Local`, `Copilot`, `Claude/Codex`, `Cloud`). |
| **Execution Environment** | Dónde se ejecutan las herramientas (Local, Dev Container, SSH/Túnel AHP, GitHub Actions). |

---

## 🏗️ Arquitectura del Sistema

### Normalización Determinista y Hashing SHA-256

```
 Fuentes Oficiales (Git Blobs & Web)
  ├── microsoft/vscode-docs (docs/agents/*, docs/agent-customization/*, api/extension-guides/ai/*)
  ├── github/docs (copilot/concepts/agents/*, copilot-sdk/*, hooks-reference.md)
  └── Feeds RSS / Páginas Web (Changelog de Copilot, Contribution Points API)
                      │
                      ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ ContentCanonicalizer (Motor de Normalización)               │
 │  1. Extracción de frontmatter clave (title, description)    │
 │  2. Eliminación de comentarios HTML y metadatos de auditoría│
 │  3. Resolución de variables Liquid ({% data variables.* %}) │
 │  4. Expansión de macros VS Code (kb(), kbstyle(), setting())│
 │  5. Normalización Unicode NFKC + saneamiento de whitespace  │
 │  6. Aislamiento semántico en HTML (<main>, sin ruido UI)    │
 └─────────────────────────────────────────────────────────────┘
                      │
                      ▼
         Hash Criptográfico SHA-256
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
[Hash Idéntico]             [Hash Modificado / Nuevo]
 Omitir procesamiento        1. Generar Diff semántico unificado
 (Cero falsos positivos)     2. Actualizar caché de texto limpio
                             3. Marcar bundle(s) como sucios
                             4. Recompilar compendio NotebookLM
                             5. Actualizar state_manifest.json
```

### Los 7 Compendios Maestros para NotebookLM

Los documentos limpios se consolidan y enrutan en 7 compendios modulares bajo `./copilot_rag_workspace/notebooklm_bundles/`:

1. **`01_Architecture_And_Agent_Harnesses.md`**: Conceptos de agente, arneses (Local, Copilot, Cloud), ciclo de vida, agentes personalizados y alineación de producto.
2. **`02_Context_Memory_And_Compaction.md`**: Gestión de ventana de contexto, subagentes aislados, `/compact`, puntos de control, Cache Explorer y arquitectura de memoria tripartita (`/memories/`, `/memories/repo/`, `/memories/session/`).
3. **`03_MCP_Servers_And_Tools_Execution.md`**: Configuración de servidores MCP (`.vscode/mcp.json`, `~/.copilot/mcp-config.json`), ejecución de herramientas, aprobación de permisos y límites de confianza.
4. **`04_Customization_Skills_Hooks_And_Plugins.md`**: Habilidades (`SKILL.md`), plugins, ciclo de vida de hooks (`preToolUse`, `postToolUse`, `sessionStart`), variables de entorno y modo estricto.
5. **`05_Workflows_Planning_And_Remote_AHP.md`**: Modos Plan y Autopilot, sesiones asíncronas en la nube, protocolo Agent Host Protocol (AHP) sobre túneles y distribución remota.
6. **`06_Extension_AI_APIs_And_Copilot_SDK.md`**: Puntos de contribución del Language Model API en VS Code (`vscode.lm`), Language Model Tools (`vscode.lm.tools`) y el Copilot SDK.
7. **`07_Release_Notes_And_Changelog_Radar.md`**: Feed RSS del Changelog oficial de Copilot y las últimas 3 versiones de notas de lanzamiento de VS Code (`release-notes/v1_*.md`).

---

## 📁 Estructura del Proyecto

```
vscode-copilot-rag-sync/
├── .github/
│   └── workflows/
│       └── sync-copilot-rag.yml        # Flujo de GitHub Actions (ejecución bi-diaria)
├── docs/
│   └── ARCHITECTURE.md                 # Documento técnico maestro exhaustivo (80k caracteres)
├── scripts/
│   └── copilot_docs_sync.py            # Motor principal de sincronización determinista
├── tests/
│   ├── __init__.py
│   ├── test_canonicalizer.py           # Pruebas unitarias de canonicalización, macros y hashes
│   └── test_synchronizer.py            # Pruebas unitarias de enrutamiento y estado
├── .gitignore
├── pyproject.toml                      # Configuración de paquete y pytest
├── requirements.txt                    # Dependencias de producción
├── requirements-dev.txt                # Dependencias de desarrollo
└── README.md                           # Documentación general del repositorio
```

---

## 🔧 Instalación y Requisitos

### Requisitos Previos
- Python 3.10 o superior.
- Conexión a Internet (para interactuar con las APIs públicas de GitHub).
- Token de GitHub (opcional, pero recomendado para evitar límites de tasa de la API: `export GITHUB_TOKEN="ghp_..."`).

### Configuración del Entorno

```bash
# Clonar o entrar al directorio del proyecto
cd vscode-copilot-rag-sync

# Crear un entorno virtual
python -m venv venv

# Activar en Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# O en Linux/macOS
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 💻 Guía de Uso

### Ejecución Local

Ejecutar la sincronización completa en el espacio de trabajo local:

```bash
python scripts/copilot_docs_sync.py --output-dir ./copilot_rag_workspace
```

### Sincronización Directa con Google Drive (NotebookLM)

Para sincronizar directamente con tu carpeta de **Google Drive** montada en Windows:

```powershell
# Opción 1: Mediante el script de PowerShell
.\sync_to_drive.ps1

# Opción 2: Con la bandera --drive
python scripts/copilot_docs_sync.py --drive

### Sincronización Automática en Segundo Plano (Sin intervención)

La sincronización ya ha sido programada como una **Tarea de Windows** en segundo plano (`VSCodeCopilotDocsSync`):

- **Frecuencia**: Se ejecuta automáticamente **cada 6 horas** sin abrir ventanas de terminal (`pythonw.exe`).
- **Verificación silenciosa**: En ausencia de cambios, la comprobación finaliza en solo 3-4 segundos con consumo mínimo de recursos.
- **Para cambiar el intervalo o verificarla:**
  ```powershell
  # Cambiar intervalo a cada 12 horas
  .\setup_autostart.ps1 -IntervalHours 12

  # Ver estado de la tarea en Windows
  Get-ScheduledTaskInfo -TaskName "VSCodeCopilotDocsSync"

  # Desinstalar la tarea automática si ya no la deseas
  .\uninstall_autostart.ps1
  ```

### Opciones de Línea de Comandos

| Parámetro | Tipo | Por Defecto | Descripción |
| :--- | :--- | :--- | :--- |
| `--output-dir` | Ruta | `./copilot_rag_workspace` | Carpeta de salida para el manifiesto, caché limpio, reportes diff y compendios. |
| `--force-recheck` | Flag | `False` | Fuerza la re-descarga y re-evaluación de todas las fuentes sin consultar el caché de Git blob SHA. |
| `--rebuild-all-bundles` | Flag | `False` | Reconstruye todos los compendios de NotebookLM incluso si ningún archivo cambió. |
| `--workers` | Entero | `8` | Número de hilos concurrentes para descarga acelerada en paralelo. |
| `--verify` | Flag | `False` | Verifica la integridad de los hashes criptográficos y archivos locales en disco sin llamadas remotas. |
| `-v`, `--verbose` | Flag | `False` | Activa la salida de registro detallada en nivel DEBUG. |

### Resultados Generados en `./copilot_rag_workspace/`

- **`state_manifest.json`**: Base de datos de estado con el hash SHA-256 de cada recurso, blob SHA de Git, conteo de palabras y URLs canónicas.
- **`clean_sources/`**: Archivos Markdown individuales, completamente limpios y normalizados.
- **`notebooklm_bundles/`**: Los 7 compendios maestros listos para arrastrar y soltar en Google NotebookLM.
- **`changelog_diffs/`**: Informes unificados en formato diff cuando se detectan modificaciones de contenido.

---

## 🔌 Servidor MCP y CLI Scaffolder de Agentes

### 1. Servidor Model Context Protocol (MCP)
El proyecto incluye un servidor MCP nativo sobre stdio ([`scripts/copilot_mcp_server.py`](scripts/copilot_mcp_server.py)) compatible con VS Code Copilot, Claude Desktop, Cursor y cualquier cliente MCP.

**Herramientas expuestas:**
- `search_copilot_docs(query, bundle, limit)`: Búsqueda semántica instantánea en las más de 1.800 fuentes oficiales indexadas.
- `get_copilot_document(doc_id)`: Recuperación del documento canónico limpio con URL y SHA-256.
- `list_copilot_bundles()`: Listado de compendios NotebookLM y estado de volumen de palabras.
- `scaffold_agent_asset(asset_type, name)`: Generación en vivo de plantillas arquitectónicas para agentes.

**Configuración en `.mcp.json` / `.vscode/mcp.json`:**
```json
{
  "mcpServers": {
    "copilot-rag": {
      "type": "stdio",
      "command": "python",
      "args": ["scripts/copilot_mcp_server.py"]
    }
  }
}
```

### 2. Scaffolder CLI de Arquitectura de Agentes
Genera instantáneamente boilerplates verificados y conformes con las especificaciones oficiales:

```bash
# Generar una habilidad de agente
python scripts/copilot_scaffold.py --type skill --name "performance-auditor"

# Generar un custom agent completo
python scripts/copilot_scaffold.py --type agent --name "architecture-guardian"

# Generar la suite completa (skill + agent + hooks + mcp + plugin)
python scripts/copilot_scaffold.py --type all --name "fullstack-agent"
```

### 3. Agent Skill Instalable: `copilot-architect`
El repositorio incluye una Agent Skill completa y modularizada ([`skills/copilot-architect/`](skills/copilot-architect/)) diseñada para que asistentes de IA (VS Code Copilot, Claude, Cursor, Antigravity) puedan **auditar, corregir y optimizar proyectos** utilizando todo el corpus técnico indexado como conocimiento experto sin saturar el contexto.

**Instalación Rápida:**
```bash
# Opción A: Instalar en el proyecto actual (.github/skills/copilot-architect)
python scripts/install_skill.py

# Opción B: Instalar en un proyecto externo específico
python scripts/install_skill.py --target-dir /ruta/a/mi-proyecto

# Opción C: Instalar globalmente en tu máquina (~/.agents/skills/)
python scripts/install_skill.py --global

# Opción D: Vía PowerShell en Windows
.\install_skill.ps1 -TargetDir "C:\Proyectos\MiApp"
```

**Capacidades de la Skill:**
- **Auditoría de Proyectos**: Ejecuta `python .github/skills/copilot-architect/scripts/audit_project.py` para obtener un *Readiness Score* (0-100%) con checklist y recomendaciones concretas.
- **Buscador Documental de Alta Velocidad**: Ejecuta `python .github/skills/copilot-architect/scripts/query_docs.py --query "preToolUse sandboxing"` para recuperar fragmentos exactos sin saturar la ventana de tokens.
- **Módulos de Referencia Rápida en `references/`**: Arneses y roles, configuración dual MCP con sandboxing, Agent Skills (`SKILL.md`), Custom Agents (`*.agent.md`), Hooks (`hooks.json`), memoria y Copilot SDK.

---

## ⚙️ Automatización en CI/CD (GitHub Actions)

El archivo [`.github/workflows/sync-copilot-rag.yml`](.github/workflows/sync-copilot-rag.yml) automatiza el proceso:

- **Programación**: Se ejecuta cada 12 horas mediante cron (`0 */12 * * *`).
- **Disparador manual**: Soporta `workflow_dispatch` con opción `force_recheck`.
- **Commit inteligente**: Realiza `git commit` y `push` **únicamente** si los hashes SHA-256 de los compendios o manifiesto han cambiado.

---

## 🧪 Pruebas Automatizadas

El proyecto incluye una suite de pruebas con cobertura exhaustiva para validar la invariancia semántica:

```bash
# Instalar dependencias de pruebas
pip install -r requirements-dev.txt

# Ejecutar la suite completa con pytest
pytest
```

---

## 📚 Documentación Técnica Detallada

Para una inmersión completa en la arquitectura de agentes, gestión de memoria multinivel, protocolos de comunicación AHP, especificaciones de servidores MCP y diseño de prompts deterministas, consulte el documento maestro en:

👉 [**docs/ARCHITECTURE.md**](docs/ARCHITECTURE.md)
