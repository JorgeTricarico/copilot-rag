> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build checklist for the Functional API

> Decide how to compose entrypoints, tasks, streaming, interrupts, and memory with the Functional API.

This guide walks through the decisions you make when building with the Functional API. For install and an end-to-end agent example, see the [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart.md). For a design walkthrough, see [Thinking in the Functional API](https://docs.langchain.com/oss/python/langgraph/thinking-in-functional-api.md). For concepts, see the [Functional API overview](https://docs.langchain.com/oss/python/langgraph/functional-api.md). To choose between the Graph API and the Functional API, see [Choosing between Graph and Functional APIs](https://docs.langchain.com/oss/python/langgraph/choosing-apis.md).

## Build your workflow

Work through these decisions in order. Each step links to the how-to for full recipes.

**1. Compose the workflow**

Define an entrypoint, wrap units of work in tasks, and choose how steps connect.

* Start from a single entrypoint and pass inputs as one argument (often a dict).
* Use tasks for discrete work that should checkpoint and retry independently.
* Fan out with parallel tasks when steps are independent.
* Call a compiled [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api.md) graph or another entrypoint when you need composition.

See [Compose Functional API workflows](https://docs.langchain.com/oss/python/langgraph/functional-api-workflows.md).

**2. Configure tasks**

Add reliability controls when steps can fail, hang, or repeat.

* Retries for transient failures
* Timeouts for slow tasks or entrypoints
* Caching for expensive repeated work
* Resume after an error without redoing completed tasks

See [Configure Functional API tasks](https://docs.langchain.com/oss/python/langgraph/functional-api-tasks.md).

**3. Stream progress**

Stream updates, model tokens, or custom data while the workflow runs.

See [Stream with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-streaming.md).

**4. Add human-in-the-loop**

Pause for approval or tool-call review with interrupts, then resume with `Command`.

See [Add human-in-the-loop with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-human-in-the-loop.md).

**5. Add memory**

Keep short-term thread state with a checkpointer, and long-term data with a store.

See [Add memory with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-memory.md).

## Next steps

* [Thinking in the Functional API](https://docs.langchain.com/oss/python/langgraph/thinking-in-functional-api.md)
* [Functional API overview](https://docs.langchain.com/oss/python/langgraph/functional-api.md)
* [Compose Functional API workflows](https://docs.langchain.com/oss/python/langgraph/functional-api-workflows.md)
* [Configure Functional API tasks](https://docs.langchain.com/oss/python/langgraph/functional-api-tasks.md)
* [Stream with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-streaming.md)
* [Add human-in-the-loop with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-human-in-the-loop.md)
* [Add memory with the Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api-memory.md)
* [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart.md)
* [Choosing between Graph and Functional APIs](https://docs.langchain.com/oss/python/langgraph/choosing-apis.md)

***

[Connect these docs](https://docs.langchain.com/use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/use-functional-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
