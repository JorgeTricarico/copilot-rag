> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build checklist for the Graph API

> Decide state, control flow, Send, Command, and node options as you build with the Graph API.

This guide walks through the decisions you make when building a graph. For install and an end-to-end agent example, see the [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart.md). For a design walkthrough, see [Thinking in the Graph API](https://docs.langchain.com/oss/python/langgraph/thinking-in-graph-api.md). For concepts, see the [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api.md).

## Build your graph

Work through these decisions in order. Each step includes a short example and links to the how-to for full recipes.

**1. Define shared state**

Decide what data nodes share and how updates merge.

* Pick a schema (`TypedDict`, dataclass, or `StateSchema` in TypeScript).
* Add a [reducer](https://docs.langchain.com/oss/python/langgraph/graph-api.md#reducers) for any key that multiple nodes write (for example, appending messages).
* Use private or input/output schemas when the graph should hide internal channels from callers.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import operator
from typing import Annotated

from typing_extensions import TypedDict

class State(TypedDict):
    foo: int
    bar: Annotated[list[str], operator.add]
```

Here `foo` overwrites. `bar` appends with `operator.add`.

For schemas, reducers, messages, and private state, see [Define and update state](https://docs.langchain.com/oss/python/langgraph/graph-api-state.md).

**2. Choose control flow**

Decide how work moves between nodes.

* **Sequence**: Fixed steps in order.
* **Branch**: Conditional edges pick the next node from state.
* **Parallel**: Fan-out to several nodes, then fan-in (often with reducers).
* **Loop**: Cycle until a termination condition, or cap runs with a [recursion limit](https://docs.langchain.com/oss/python/langgraph/graph-api.md#recursion-limit).

This sequence checks whether a number is even, then formats a message:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph

class State(TypedDict):
    number: int
    is_even: bool
    message: str

def check_even(state: State):
    return {"is_even": state["number"] % 2 == 0}

def format_message(state: State):
    return {
        "message": (
            "The number is even." if state["is_even"] else "The number is odd."
        )
    }

workflow = StateGraph(State)
workflow.add_node("check_even", check_even)
workflow.add_node("format_message", format_message)
workflow.add_edge(START, "check_even")
workflow.add_edge("check_even", "format_message")
workflow.add_edge("format_message", END)
graph = workflow.compile()

graph.invoke({"number": 7})
```

For branches, parallel paths, and loops, see [Build sequences, branches, and loops](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow.md).

**3. Decide if you need Send or Command**

Most graphs only need nodes, edges, and conditional edges. Keep routing in edges unless you hit one of the cases below. For patterns and examples, see [Use Send and Command](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command.md).

Reach for the extras when the default model is not enough:

* Use [`Send`](https://reference.langchain.com/python/langgraph/types/Send) when you must run the same node once per item, each with its own input, and the item count is only known at runtime (map-reduce / orchestrator-worker).
* Use [`Command`](https://reference.langchain.com/python/langgraph/types/Command) when one step must both update state and choose the next node, resume after an [interrupt](https://docs.langchain.com/oss/python/langgraph/interrupts.md), or update state from a tool.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Literal

from langgraph.types import Command, Send

# Send: fan out one worker per item
def continue_to_jokes(state: OverallState):
    return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]

# Command: update state and route in one return
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        update={"foo": "bar"},
        goto="my_other_node",
    )
```

**4. Configure nodes as needed**

Add runtime options when reliability or cost matters:

* Retries and timeouts for flaky or slow steps
* Error handlers and graph-wide node defaults
* Caching for expensive repeated work
* Runtime context or config for dependencies that do not belong in state

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import RetryPolicy

builder.add_node(
    "node_name",
    node_function,
    retry_policy=RetryPolicy(),
)
```

See [Configure nodes](https://docs.langchain.com/oss/python/langgraph/graph-api-nodes.md).

**5. Visualize the graph**

Render a Mermaid or PNG diagram to review topology and debug routing.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
print(graph.get_graph().draw_mermaid())
```

See [Visualize your graph](https://docs.langchain.com/oss/python/langgraph/graph-api-visualize.md).

## Next steps

* [Thinking in the Graph API](https://docs.langchain.com/oss/python/langgraph/thinking-in-graph-api.md): Design walkthrough with the email agent
* [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api.md): Concepts for state, nodes, edges, `Send`, and `Command`
* [Define and update state](https://docs.langchain.com/oss/python/langgraph/graph-api-state.md)
* [Build sequences, branches, and loops](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow.md)
* [Use Send and Command](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command.md)
* [Configure nodes](https://docs.langchain.com/oss/python/langgraph/graph-api-nodes.md)
* [Visualize your graph](https://docs.langchain.com/oss/python/langgraph/graph-api-visualize.md)
* [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart.md): End-to-end calculator agent

***

[Connect these docs](https://docs.langchain.com/use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/use-graph-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
