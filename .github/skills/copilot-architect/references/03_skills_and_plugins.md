# Módulo 03: Especificación de Agent Skills, Custom Agents y Plugins

## 1. Agent Skills (`SKILL.md`)

Las habilidades de agente constituyen la unidad modular de conocimiento declarativo bajo el estándar abierto adoptado por Anthropic y VS Code Copilot.

### Estructura de Directorio:
```
.github/skills/<skill-name>/
├── SKILL.md                 # Manifiesto obligatorio con YAML frontmatter y protocolo
├── references/              # Documentos de contexto técnico especializado
├── scripts/                 # Utilidades ejecutables auxiliares
└── examples/                # Casos de uso y patrones de referencia
```

### Especificación de `SKILL.md`:
```markdown
---
name: database-migrator
description: Ejecuta y valida migraciones seguras de base de datos PostgreSQL usando Alembic.
---

# Skill: Database Migrator

## Cuándo usar esta habilidad
Se activa cuando el usuario solicite crear modelos, ejecutar migraciones o verificar esquemas SQL.

## Protocolo de Ejecución
1. Inspeccionar revisiones previas en alembic/versions/.
2. Generar migración con --autogenerate y auditar sentencias DDL.
3. Ejecutar suite de pruebas de regresión.
```

---

## 2. Custom Agents (`*.agent.md`)

Define roles especializados con herramientas y modelos acotados en `.github/agents/<slug>.agent.md`:

```markdown
---
name: security-auditor
description: Auditor de dependencias y análisis estático de vulnerabilidades SAST.
tools:
  - codebase
  - runCommands
  - problems
infer: true
---

# Rol de Agente: Auditor de Seguridad

Eres un analista de seguridad que evalúa el código contra el OWASP Top 10.
No aplicas cambios directamente; generas informes detallados con remediaciones sugeridas.
```

---

## 3. Agent Plugins 1.0 (`plugin.json`)

Empaqueta habilidades, agentes y servidores MCP de forma portable:

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "enterprise-compliance-pack",
  "version": "1.0.0",
  "description": "Paquete integral de auditoría de arquitectura y seguridad.",
  "skills": ["skills/compliance-check"],
  "mcp": ".mcp.json"
}
```

Activación declarativa en `.github/copilot/settings.json`:
```json
{
  "enabledPlugins": ["enterprise-compliance-pack"],
  "extraKnownMarketplaces": []
}
```
