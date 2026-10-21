# Módulo 06: Copilot SDK, APIs Propuestas y Consumo de AI Credits

## 1. Integración con `@github/copilot-sdk`

El SDK permite incrustar el motor de agentes en cualquier servicio o aplicación cliente:

```typescript
import { CopilotAgentRuntime, ProviderConfig } from "@github/copilot-sdk";

const runtime = new CopilotAgentRuntime({
  provider: ProviderConfig.fromEndpoint("https://models.inference.ai.azure.com", {
    token: process.env.GITHUB_TOKEN,
    model: "gpt-4o",
  }),
  tools: [
    {
      name: "runSecurityScan",
      description: "Ejecuta análisis de vulnerabilidades en el proyecto.",
      parameters: { /* JSON Schema */ },
      handler: async (args) => { /* Implementación */ }
    }
  ]
});

const session = await runtime.createSession();
const stream = await session.send("Auditar dependencias de package.json");
for await (const chunk of stream) {
  process.stdout.write(chunk.text);
}
```

---

## 2. Consumo Inteligente de AI Credits y GitHub Models

- **Triage y Clasificación Rápida**: Asignar modelos ligeros (`gpt-4o-mini`, `phi-4`) a través del playground de GitHub Models con consumo despreciable de cuota.
- **Razonamiento Crítico y Planificación**: Reservar créditos para modelos avanzados (`o3-mini`, `claude-3-7-sonnet`, `gpt-4o`).
- **Zero-Credit Fallback**: Enrutar tareas offline o masivas hacia modelos locales servidos en Ollama (`deepseek-r1:8b`, `qwen2.5-coder:14b`).

---

## 3. Extensibilidad en VS Code (`vscode.lm`)

Puntos de contribución clave en `package.json`:
- `contributes.languageModelTools`: Registro declarativo de herramientas disponibles para agentes.
- `vscode.lm.registerTool(toolId, toolInstance)`: Implementa `prepareInvocation` (confirmación con el usuario) e `invoke` (ejecución real).
- `vscode.chat.createChatParticipant`: Crea participantes `@customAgent` en la vista de chat.
