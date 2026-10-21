# Módulo 01: Comparativa de Arneses y Roles de Agente en VS Code Copilot

## 1. Desacoplamiento Fundamental

| Dimensión | Definición Operativa | Configuración Asociada |
| :--- | :--- | :--- |
| **Language Model** | Motor de inferencia y razonamiento (Claude 3.7 Sonnet, GPT-4o, o3-mini, Gemini, Ollama). | `chat.planAgent.defaultModel`, `github.copilot.chat.implementAgent.model` |
| **Agent Role** | Conjunto de herramientas, prompt de sistema y restricciones (`Ask`, `Plan`, `Agent`, `*.agent.md`). | Selector en chat o prefijo `/plan`, `@agent` |
| **Agent Harness** | Runtime subyacente que orquesta el bucle de ejecución (Local, Copilot Agent Host, Claude, Cloud). | Configurable en `code --agents` o por perfil |
| **Execution Environment** | Dónde se ejecutan físicamente las herramientas (Local, Dev Container, SSH/Túnel AHP, GitHub Actions). | Conexión remota activa |

---

## 2. Comparativa de Arneses de Ejecución

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                            ARNESES DE AGENTE EN VS CODE                              │
├─────────────────────┬──────────────────────────┬──────────────────┬──────────────────┤
│ Arnés Local         │ Arnés Copilot (AgentHost)│ Arneses Claude   │ Arnés Cloud      │
├─────────────────────┼──────────────────────────┼──────────────────┼──────────────────┤
│ • En proceso editor │ • Proceso independiente  │ • Motor nativo   │ • GitHub Actions │
│ • Muere con ventana │ • Persiste en background │   Anthropic      │ • Timeout 59 min │
│ • Solo .vscode/mcp  │ • Lee .mcp.json portable │ • Requiere API   │ • Efímero        │
│ • Herramientas GUI  │ • CLI compatible         │   key directa    │ • copilot-setup  │
└─────────────────────┴──────────────────────────┴──────────────────┴──────────────────┘
```

### Arnés Local vs. Arnés Copilot (Agent Host)
- **Arnés Local**: Opera dentro del ciclo de vida de la ventana de VS Code. Adecuado para tareas rápidas y sincrónicas.
- **Arnés Copilot (Agent Host)**: Proceso desacoplado del editor. Al configurar `chat.mcp.autostart: "never"`, únicamente se desactiva el autoarranque en el editor, pero el Agent Host continúa administrando sus propios servidores MCP para sesiones desacopladas.

---

## 3. Protocolo Agent Host (AHP) y Sesiones Remotas
Para delegación hacia máquinas remotas, la ventana de Agentes (`code --agents`) utiliza cuatro herramientas de orquestación interna:
- `list_agent_hosts`: Descubre hosts conectados, modelos disponibles, memoria y carga.
- `create_remote_session`: Adjudica la sesión al host con menor número de tareas activas.
- `get_remote_session`: Inspecciona el estado y última respuesta.
- `send_remote_message`: Reporta resultados al chat de origen.
