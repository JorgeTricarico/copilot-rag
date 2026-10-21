# Ecosistema Moderno de Agentes: Copilot SDK, Graph-Flows, AI Credits y Orquestación Híbrida

Este documento constituye la guía técnica oficial para diseñar, implementar y orquestar sistemas multi-agente avanzados combinando el **GitHub Copilot SDK**, frameworks de grafos de ejecución (**LangGraph**, **AutoGen 0.4**, **LlamaIndex Workflows**, **CrewAI**) y el aprovechamiento eficiente de **GitHub AI Credits** y **GitHub Models**.

---

## 1. El Ecosistema Real de Frameworks de Grafos y Flujos de Agentes

Cuando se habla de *flujos de agentes encadenados*, *grafos de ejecución* o *graph-flows*, la industria moderna de IA ha convergido en cuatro arquitecturas principales:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    FRAMEWORKS MODERNOS DE AGENT ORCHESTRATION                   │
├─────────────────────┬──────────────────────┬─────────────────┬──────────────────┤
│ LangGraph           │ AutoGen 0.4          │ LlamaIndex      │ CrewAI Flows     │
│ (Stateful Graphs)   │ (Event-Driven Swarm) │ (Event Streams) │ (Task Pipelines) │
├─────────────────────┼──────────────────────┼─────────────────┼──────────────────┤
│ • Grafo cíclico/DAG │ • Mensajería asínc.  │ • Reactivo por  │ • Flujos         │
│ • StateGraph tipado │ • Eventos y tópicos  │   eventos @step │   jerárquicos    │
│ • Checkpointers     │ • GroupChat & Swarm  │ • Fan-out / in  │ • Roles fijos    │
│ • Human-in-the-loop │ • Magentic-One       │ • Tipado estricto│• Memoria común  │
└─────────────────────┴──────────────────────┴─────────────────┴──────────────────┘
```

### 1.1. LangGraph (LangChain Ecosystem)
- **Concepto Central**: Modela la ejecución de agentes como un autómata de estados finitos (`StateGraph`).
- **Nodos y Aristas**:
  - **Nodos**: Funciones o clases que reciben el estado global (`AgentState`), ejecutan inferencia o herramientas, y devuelven un delta que muta el estado.
  - **Aristas Condicionales (`conditional_edges`)**: Funciones de enrutamiento deterministas que evalúan el estado actual (por ejemplo, si el agente generó un schema válido o si solicitó más herramientas) y dirigen el flujo al siguiente nodo específico.
- **Persistencia y Time-Travel**: Utiliza `Checkpointer` (en memoria, SQLite o PostgreSQL) permitiendo pausar la ejecución para aprobación humana (*Human-in-the-loop*) y retroceder a estados previos.

### 1.2. Microsoft AutoGen 0.4 (AutoGen Core & AgentChat)
- **Concepto Central**: Arquitectura orientada a eventos y micro-agentes distribuidos. Desacopla la lógica del modelo del canal de transporte.
- **Patrones de Orquestación**:
  - **Swarm Pattern**: Agentes que pasan el control explícitamente mediante funciones de transferencia (`HandoffMessage`).
  - **Magentic-One**: Arquitectura multi-agente para trabajo complejo en la web y software:
    - *Orchestrator*: Administra el plan y delega.
    - *WebSurfer*: Navegación interactiva.
    - *FileSurfer*: Inspección de directorios y lectura de archivos.
    - *Coder*: Generación y análisis de código.
    - *ComputerTerminal*: Ejecución segura en sandbox.

### 1.3. LlamaIndex Workflows
- **Concepto Central**: Orquestación reactiva y asíncrona basada en eventos fuertemente tipados.
- **Mecanismo**: Cada paso se decora con `@step`. Un paso escucha uno o más tipos de eventos (`StartEvent`, `AnalysisCompleteEvent`, `ValidationEvent`) y emite nuevos eventos, permitiendo ramificaciones en paralelo (*Fan-Out*) y sincronización de barrera (*Fan-In*) sin requerir un planificador centralizado.

---

## 2. GitHub Copilot SDK (`github/copilot-sdk`)

El **Copilot SDK** es el runtime oficial de GitHub que permite incrustar las capacidades de agente de Copilot (las mismas que operan dentro de GitHub Copilot en VS Code y el Copilot CLI) directamente en aplicaciones independientes, CLIs corporativos o servicios backend.

### 2.1. Capacidades Nativas del Copilot SDK
1. **Loop Agentivo Out-of-the-Box**: Maneja de forma autónoma la planificación interna, multi-turn reasoning, streaming de tokens y llamadas recursivas a herramientas.
2. **Bring Your Own Key / Model Provider (BYOK)**: Mediante la interfaz `ProviderConfig`, permite enrutar las llamadas del agente hacia:
   - **GitHub Models** (consumiendo créditos de GitHub o tokens de cuenta Copilot).
   - **Azure AI Foundry / OpenAI / Anthropic**.
   - **Modelos Locales**: Endpoints compatibles con OpenAI como **Ollama**, **vLLM** o **LiteLLM**.
3. **Soporte Multilingüe**: Paquetes oficiales disponibles en TypeScript/Node.js (`@github/copilot-sdk`), Python y C#/.NET.

### 2.2. Diferencia: Copilot SDK vs. Copilot Extensions
- **Copilot Extensions**: Se ejecutan dentro de la interfaz de Copilot Chat en GitHub.com o VS Code para enriquecer el chat del usuario con contexto externo (vía `@copilot-extensions/preview-sdk.js` u Octokit).
- **Copilot SDK**: Es un motor autónomo. Permite crear **tu propia aplicación** o arnés donde tú controlas la interfaz, las herramientas y la orquestación.

---

## 3. Arquitectura Híbrida: Copilot SDK + Graph-Flows + AI Credits

Para construir aplicaciones de última generación sin costos prohibitivos de inferencia, se adopta una arquitectura en capas:

```
                               ┌────────────────────────────────┐
                               │     Usuario / Disparador       │
                               └────────────────┬───────────────┘
                                                │
                                                ▼
                               ┌────────────────────────────────┐
                               │  Orquestador de Grafo          │
                               │  (LangGraph / LlamaIndex /     │
                               │   AutoGen Swarm)               │
                               └───────┬────────────────┬───────┘
                                       │                │
            ┌──────────────────────────┘                └──────────────────────────┐
            ▼                                                                      ▼
┌───────────────────────────────────────┐              ┌───────────────────────────────────────┐
│ Nodo 1: Research & Triage Agent       │              │ Nodo 2: Plan & Architecture Agent     │
│ Runtime: Copilot SDK                  │              │ Runtime: Copilot SDK                  │
│ Modelo: GitHub Models (AI Credits)    │              │ Modelo: Razonamiento Profundo         │
│         gpt-4o-mini / claude-3-5-haiku│              │         o3-mini / claude-3-7-sonnet   │
│ Objetivo: Extracción y embeddings RAG │              │ Objetivo: Desglose DAG determinista   │
└───────────────────┬───────────────────┘              └───────────────────┬───────────────────┘
                    │                                                      │
                    └──────────────────────────┬───────────────────────────┘
                                               │
                                               ▼
                               ┌────────────────────────────────┐
                               │ Compuertade Validación (Hooks) │
                               │ onPostToolUse / Schema Zod     │
                               └───────────────┬────────────────┘
                                               │
                                               ▼
                               ┌────────────────────────────────┐
                               │ Nodo 3: Fleet Implementer Mode │
                               │ Subagentes Paralelos en Sandbox│
                               │ Runtime: Local / Copilot AHP   │
                               └────────────────────────────────┘
```

### 3.1. Estrategia de Consumo de AI Credits y GitHub Models
- **Triage y Clasificación de Intenciones**: Utiliza modelos de bajo consumo (`gpt-4o-mini`, `phi-4`) a través del endpoint de GitHub Models (`https://models.inference.ai.azure.com`).
- **Planificación Estructurada y Generación de Código Crítico**: Se asignan créditos para modelos de frontera (`o3-mini`, `claude-3-7-sonnet`, `gpt-4o`).
- **Ejecución Local / Offline**: Para entornos donde se requiere privacidad total o cero consumo de créditos, el arnés conmuta dinámicamente mediante `ProviderConfig` hacia modelos locales en Ollama (`deepseek-r1:8b`, `qwen2.5-coder:14b`).

---

## 4. Patrón de Flujo Determinista Encadenado (Graph-Flow Pipeline)

El flujo se estructura con 4 etapas fundamentales unidas por contratos de datos tipados (Pydantic / Zod):

```
[Research Agent] ──(Structured Payload)──> [Plan Agent] ──(DAG Tasks)──> [Fleet Implementers] ──(Diffs)──> [Reviewer]
       │                                         │                                    │                        │
       └── Hook: onPostToolUse (Valida AST)      └── Hook: onPreToolUse (Policy Check)└── Hook: onSubagentStop └── Final
```

### 4.1. Intercepción y Guardrails con Lifecycle Hooks del SDK
Los ganchos del ciclo de vida actúan como compuertas lógicas (*Decision Gates*):

1. **`onPreToolUse` (Guardrail de Entrada)**:
   - Inspecciona los parámetros antes de que cualquier herramienta de terminal o mutación de archivos se ejecute.
   - Aplica sandboxing (verifica que la ruta esté dentro del workspace permitido y que comandos destructivos como `rm -rf /` o formateos sean bloqueados).
2. **`onPostToolUse` (Validación de Salida)**:
   - Verifica que la salida generada cumpla con el formato técnico esperado (por ejemplo, que el JSON devuelto no esté truncado o que el archivo modificado compile sin errores de sintaxis).
3. **`onSubagentStart` (Aislamiento de Contexto)**:
   - Limpia el historial superfluo y entrega al subagente únicamente el contexto necesario para su tarea (evitando que el subagente herede miles de tokens de conversaciones previas).
4. **`onSubagentStop` (Control de Transición)**:
   - Valida que el artefacto producido por el subagente cumpla con la especificación requerida antes de devolver el turno al orquestador principal.

---

## 5. Implementación de Referencia en Python

A continuación se presenta una implementación de referencia de un orquestador híbrido con validación de hooks y grafo de estados:

```python
"""
Ejemplo de Orquestación Híbrida: Graph-Flow con Lifecycle Hooks y Copilot Engine
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import json


@dataclass
class WorkflowState:
    task_description: str
    research_summary: str = ""
    execution_plan: List[Dict[str, Any]] = field(default_factory=list)
    completed_steps: List[Dict[str, Any]] = field(default_factory=list)
    artifacts: List[str] = field(default_factory=list)
    status: str = "PENDING"


class AgentLifecycleInterceptor:
    """Implementa compuertas de seguridad y validación (Hooks)"""

    @staticmethod
    def on_pre_tool_use(tool_name: str, args: Dict[str, Any]) -> bool:
        print(f"[Hook: onPreToolUse] Validando invocación de '{tool_name}'...")
        if tool_name in ("bash", "runCommand"):
            cmd = args.get("command", "")
            if any(forbidden in cmd for forbidden in ["rm -rf", "drop database", "mkfs"]):
                print(f"[ALERTA SEGURIDAD] Comando peligroso bloqueado: {cmd}")
                return False
        return True

    @staticmethod
    def on_post_tool_use(tool_name: str, result: str) -> str:
        print(f"[Hook: onPostToolUse] Verificando salida de '{tool_name}'...")
        if not result or "ERROR:" in result:
            print("[AVISO] Salida de herramienta con errores detectados.")
        return result

    @staticmethod
    def on_subagent_start(agent_role: str, context: Dict[str, Any]) -> Dict[str, Any]:
        print(f"[Hook: onSubagentStart] Inicializando subagente: {agent_role}")
        # Aislamiento de contexto: compactar o podar claves no relevantes
        return {"task": context.get("task"), "constraints": context.get("constraints", [])}

    @staticmethod
    def on_subagent_stop(agent_role: str, output: Dict[str, Any]) -> bool:
        print(f"[Hook: onSubagentStop] Validando resultado de subagente: {agent_role}")
        return "result" in output and len(str(output["result"])) > 10


class GraphFlowOrchestrator:
    """Motor de Grafo de Ejecución con Nodos Especializados"""

    def __init__(self, hooks: AgentLifecycleInterceptor):
        self.hooks = hooks

    def step_research(self, state: WorkflowState) -> WorkflowState:
        print("\n--- [NODO 1: Research Agent] ---")
        # Simulación de extracción con Copilot RAG / SDK
        state.research_summary = (
            "Análisis de documentación: Se requiere implementar un endpoint MCP Stdio "
            "con soporte para JSON-RPC 2.0 y compatibilidad con las directivas de sandboxing."
        )
        return state

    def step_planning(self, state: WorkflowState) -> WorkflowState:
        print("\n--- [NODO 2: Plan Agent] ---")
        state.execution_plan = [
            {"step_id": 1, "action": "create_mcp_server", "target": "scripts/mcp_server.py"},
            {"step_id": 2, "action": "generate_tests", "target": "tests/test_mcp_server.py"},
            {"step_id": 3, "action": "register_vscode_config", "target": ".vscode/mcp.json"},
        ]
        return state

    def step_fleet_execution(self, state: WorkflowState) -> WorkflowState:
        print("\n--- [NODO 3: Fleet Implementer Mode] ---")
        for task in state.execution_plan:
            subagent_ctx = self.hooks.on_subagent_start("Implementer", task)
            
            # Ejecución supervisada
            can_run = self.hooks.on_pre_tool_use("editFiles", {"file": task["target"]})
            if can_run:
                # Simular aplicación de cambios
                tool_output = f"Archivo {task['target']} generado y validado con éxito."
                self.hooks.on_post_tool_use("editFiles", tool_output)
                
                sub_res = {"result": tool_output, "step_id": task["step_id"]}
                if self.hooks.on_subagent_stop("Implementer", sub_res):
                    state.completed_steps.append(sub_res)
                    state.artifacts.append(task["target"])
        return state

    def step_verification_and_review(self, state: WorkflowState) -> WorkflowState:
        print("\n--- [NODO 4: Synthesis & Verification Agent] ---")
        if len(state.completed_steps) == len(state.execution_plan):
            state.status = "SUCCESS"
            print("Todos los pasos del plan se ejecutaron y verificaron deterministamente.")
        else:
            state.status = "PARTIAL_FAILURE"
        return state

    def run(self, initial_task: str) -> WorkflowState:
        state = WorkflowState(task_description=initial_task)
        state = self.step_research(state)
        state = self.step_planning(state)
        state = self.step_fleet_execution(state)
        state = self.step_verification_and_review(state)
        return state


if __name__ == "__main__":
    orchestrator = GraphFlowOrchestrator(hooks=AgentLifecycleInterceptor())
    result_state = orchestrator.run("Implementar arquitectura MCP con validación estricta.")
    print(f"\nEstado Final del Pipeline: {result_state.status}")
    print(f"Artefactos Producidos: {result_state.artifacts}")
```

---

## 6. Recursos y Enlaces Oficiales del Ecosistema

- **Repositorio Oficial de Copilot SDK**: [github.com/github/copilot-sdk](https://github.com/github/copilot-sdk)
- **Documentación de Copilot Extensions**: [docs.github.com/en/copilot/building-copilot-extensions](https://docs.github.com/en/copilot/building-copilot-extensions)
- **GitHub Models Playground**: [github.com/marketplace/models](https://github.com/marketplace/models)
- **LangGraph Documentation**: [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)
- **Microsoft AutoGen 0.4**: [microsoft.github.io/autogen](https://microsoft.github.io/autogen/)
- **LlamaIndex Workflows**: [docs.llamaindex.ai/en/stable/module_guides/workflow](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
