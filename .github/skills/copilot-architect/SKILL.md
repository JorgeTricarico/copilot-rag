---
name: copilot-architect
description: Audita, diseña y optimiza arquitecturas de software para el ecosistema de VS Code Copilot, GitHub Copilot CLI y agentes autónomos. Utiliza la base de conocimiento oficial indexada para validar configuraciones MCP duales (.mcp.json y .vscode/mcp.json), Agent Skills (SKILL.md), Custom Agents (*.agent.md), Hooks (hooks.json), Plugins (plugin.json) y patrones de orquestación con Copilot SDK.
---

# Skill: Copilot Architect (Auditoría y Diseño de Agentes para VS Code Copilot)

Esta habilidad proporciona a los asistentes de inteligencia artificial y desarrolladores una metodología estructurada, determinista y respaldada por la documentación oficial para **auditar, corregir y construir proyectos con capacidades agentivas modernas en Visual Studio Code Copilot**.

---

## 🎯 Cuándo Activar Esta Habilidad

Invoca o activa esta skill cuando el usuario solicite:
- Auditar la preparación de un proyecto para interactuar óptimamente con agentes de VS Code Copilot o GitHub Copilot CLI.
- Configurar servidores Model Context Protocol (MCP) en formato dual (`.mcp.json` portable y `.vscode/mcp.json` con sandboxing y variables interactivas).
- Modularizar instrucciones creando Agent Skills (`SKILL.md`) o roles especializados (`*.agent.md`).
- Implementar barreras de seguridad, auditoría o compuertas lógicas mediante lifecycle hooks (`hooks.json`).
- Empaquetar y distribuir capacidades mediante el estándar formal **Agent Plugins 1.0** (`plugin.json`).
- Optimizar la ventana de contexto, caché de prompts y compactación de memoria persistente.
- Diseñar integraciones programáticas con **GitHub Copilot SDK** (`@github/copilot-sdk`) y APIs de modelos de lenguaje en VS Code (`vscode.lm`).

---

## 📋 Protocolo de Auditoría y Mejora en 5 Fases

Sigue rigurosamente las siguientes fases al analizar o mejorar un proyecto:

### Fase 1: Diagnóstico Automatizado de Primitivas
Ejecuta el script de auditoría provisto para evaluar el estado actual del espacio de trabajo:
```bash
python scripts/audit_project.py --project-dir .
```
El script evaluará:
1. Existencia y validez de configuraciones MCP (`.mcp.json` y `.vscode/mcp.json`).
2. Existencia de Agent Skills en `.github/skills/` o `.agents/skills/`.
3. Existencia de Custom Agents en `.github/agents/`.
4. Definición de interceptores de ciclo de vida en `.github/hooks/hooks.json`.
5. Manifiesto de plugin portable (`plugin.json`).
6. Políticas de aislamiento y sandboxing en terminal y herramientas.

### Fase 2: Configuración de Arneses y Estrategia MCP Dual
Aplica la separación arquitectónica oficial:
- **Arnés Copilot (Agent Host)**: Para tareas con herramientas de larga duración y persistencia entre ventanas.
- **Configuración Portable (`.mcp.json`)**: En la raíz del repositorio para el Agent Host y Copilot CLI.
- **Configuración Editor (`.vscode/mcp.json`)**: Para VS Code con variables seguras `${input:...}`, modo dev (`dev.watch`) y sandboxing obligatorio (`filesystem.allowWrite`, `network.allowedDomains`).
👉 *Consulta de referencia técnica:* [references/02_mcp_configuration.md](references/02_mcp_configuration.md).

### Fase 3: Desacoplamiento de Instrucciones en Agent Skills
Evita instrucciones monolíticas en el prompt del sistema o en archivos gigantescos:
- Modulariza tareas repetitivas o conocimiento de dominio (ej: migraciones SQL, reglas de diseño UI, pipelines TDD) en subcarpetas bajo `.github/skills/<nombre>/SKILL.md`.
- El arnés cargará las instrucciones únicamente cuando la intención del usuario lo requiera, ahorrando hasta un 80% de tokens de contexto por turno.
👉 *Consulta de referencia técnica:* [references/03_skills_and_plugins.md](references/03_skills_and_plugins.md).

### Fase 4: Guardrails con Lifecycle Hooks
Configura `.github/hooks/hooks.json` para proteger el proyecto:
- `preToolUse`: Bloquea comandos terminales destructivos o evalúa permisos antes de mutar el sistema de archivos.
- `postToolUse`: Valida que los cambios apliquen formato (linter) o pruebas automáticas tras la ejecución de herramientas.
- `subagentStart` y `subagentStop`: Garantiza que los subagentes ejecuten con contexto acotado y devuelvan esquemas estructurados conformes.
👉 *Consulta de referencia técnica:* [references/04_lifecycle_hooks.md](references/04_lifecycle_hooks.md).

### Fase 5: Integración y Flujos Híbridos con Copilot SDK
Para extensiones nativas o aplicaciones autónomas:
- Utiliza `@github/copilot-sdk` con `ProviderConfig` para conectar modelos de GitHub Models (consumiendo AI credits de forma eficiente) o modelos locales sin coste.
- Integra las herramientas de lenguaje mediante `vscode.lm.registerTool`.
👉 *Consulta de referencia técnica:* [references/06_copilot_sdk_and_apis.md](references/06_copilot_sdk_and_apis.md).

---

## 🔍 Consulta Profunda de Documentación

Si necesitas consultar especificaciones exactas, APIs propuestas o fragmentos de la documentación oficial normalizada, utiliza el script de consulta de alta velocidad sin saturar el contexto:
```bash
python scripts/query_docs.py --query "preToolUse sandboxing"
```
O busca en un compendio específico:
```bash
python scripts/query_docs.py --query "allowWrite" --bundle "03_MCP_Servers_And_Tools_Execution"
```

---

## 📚 Índice de Módulos de Referencia Rápida
- [01. Comparativa de Arneses y Roles de Agentes](references/01_harness_and_roles.md)
- [02. Especificación de Configuración MCP Dual y Sandboxing](references/02_mcp_configuration.md)
- [03. Especificación de Agent Skills, Custom Agents y Plugins](references/03_skills_and_plugins.md)
- [04. Interceptores de Ciclo de Vida y Seguridad (Hooks)](references/04_lifecycle_hooks.md)
- [05. Gestión de Contexto, Caché y Memoria Persistente](references/05_context_and_memory.md)
- [06. Copilot SDK, APIs Propuestas y Consumo de AI Credits](references/06_copilot_sdk_and_apis.md)
