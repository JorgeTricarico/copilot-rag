# Módulo 04: Interceptores de Ciclo de Vida y Seguridad (Hooks)

## 1. Arquitectura de Hooks (`.github/hooks/hooks.json`)

Los interceptores de ciclo de vida proporcionan compuertas de seguridad deterministas que se ejecutan antes y después de que cualquier arnés de agente invoque herramientas o despache subagentes.

```
                  ┌──────────────────────┐
                  │    Agent Decision    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   hook: preToolUse   │ ──(Falla)──> [Invocación Bloqueada]
                  └──────────┬───────────┘
                             │ (Pasa)
                             ▼
                  ┌──────────────────────┐
                  │   Tool Execution     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  hook: postToolUse   │ ──(Falla)──> [Alerta / Rollback]
                  └──────────┬───────────┘
                             │ (Pasa)
                             ▼
                  ┌──────────────────────┐
                  │    Next Agent Step   │
                  └──────────────────────┘
```

---

## 2. Especificación Formal de `hooks.json`

```json
{
  "hooks": {
    "preToolUse": [
      {
        "matcher": "terminal|bash|pwsh|cmd",
        "command": "python scripts/security_check.py --cmd \"$TOOL_INPUT_COMMAND\""
      },
      {
        "matcher": "editFiles|write_file",
        "command": "python scripts/verify_write_permission.py --target \"$TOOL_INPUT_PATH\""
      }
    ],
    "postToolUse": [
      {
        "matcher": "editFiles|applyDiff",
        "command": "pytest tests/test_fast_linter.py"
      }
    ],
    "subagentStart": [
      {
        "command": "echo '[AUDIT] Inicializando subagente con contexto acotado...'"
      }
    ],
    "subagentStop": [
      {
        "command": "python scripts/validate_subagent_output.py"
      }
    ]
  }
}
```

---

## 3. Prácticas de Mitigación de Vulnerabilidades
- **Prevención de Prompt Injection**: Nunca permitas que una herramienta descargue texto no confiable y lo ejecute directamente en terminal sin pasar por `preToolUse`.
- **Aislamiento de Subagentes**: En `subagentStart`, poda el historial superfluo para evitar que ataques de suplantación de prompt se propaguen por el grafo de agentes.
