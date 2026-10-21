# COMPENDIO RAG NOTEBOOKLM: 01_Architecture_And_Agent_Harnesses
- **Generado (UTC)**: 2026-10-21T19:55:00.204145+00:00
- **Total Palabras**: 25,323 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::.github/skills/docs-product-alignment/SKILL.md
- **CANONICAL_URL**: https://github.com/microsoft/vscode-docs/blob/main/.github/skills/docs-product-alignment/SKILL.md
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/.github/skills/docs-product-alignment/SKILL.md
- **SHA256_FINGERPRINT**: `c84f7b6b0388f5f8d5ff9366bad79ea4f81693c6f7fb021ba642f5f7e73596b5`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.667457+00:00
---

**description**: Audit and update docs/copilot/ documentation to accurately reflect current VS Code AI capabilities. Use when: competitive analysis reveals gaps, product launches new features, docs use outdated framing, or keyword coverage needs strengthening for discoverability by users and AI agents. Produces a gap analysis plus targeted edits across affected files.

# Documentation Product Alignment

Audit VS Code Copilot documentation against current product capabilities and produce targeted, style-compliant edits. Follow the [docs-writing style guide](../../instructions/docs-writing.instructions.md) for all writing rules.

## Guardrails

- **Factual only.** Every claim must map to something the product does today. No superlatives, no competitive comparisons, no invented terminology.
- **Content framing.** Establish each page's primary persona, reader intent, and article purpose by following the [content-framing guidance](../../instructions/docs-writing.instructions.md#content-framing). Ask the writer before editing when the framing is ambiguous and would change the audit or recommendations.
- **Two consumers.** The primary persona reads the prose; AI agents and search crawlers index Keywords, MetaDescriptions, and opening paragraphs. Both matter.
- **Minimal edits.** Change only what is inaccurate, outdated, or missing. One precise sentence beats a rewritten section.
- **Verifiable.** If you cannot point to a UI element, setting, or documented behavior, do not write it.

## Workflow

1. **Gather context and frame each page.** Read the latest [release notes](/release-notes/), check [github.com/features/copilot](https://github.com/features/copilot), and review any competitive claims or feature matrices the user provides. For each page, record its primary persona, reader intent, and article purpose before proposing edits.
2. **Audit high-traffic pages.** Read each page and compare against current product truth. Focus on MetaDescriptions, Keywords, opening paragraphs, and terminology.
3. **Gap analysis.** List what is inaccurate, outdated, or missing. Map each gap to a file and location. Include the page framing in the analysis, and prioritize by page traffic and impact on the primary persona's intent.
4. **Edit.** Apply targeted changes that support the recorded framing. Vary phrasing across pages to avoid repetition.
5. **Verify.** Search changed files for banned words, em-dashes, and MetaDescription length violations. Confirm that each changed page still serves its recorded primary persona and reader intent.

**High-traffic pages to always check:**
- [docs/copilot/overview.md](/docs/copilot/overview.md), [docs/copilot/concepts/overview.md](/docs/agents/concepts/overview.md), [docs/agents/reference/ai-features-cheat-sheet.md](/docs/agents/reference/ai-features-cheat-sheet.md)
- [docs/copilot/getting-started.md](/docs/copilot/getting-started.md), [docs/agents/overview.md](/docs/agents/overview.md)
- [docs/agents/reference/workspace-context.md](/docs/agents/reference/workspace-context.md), [docs/agents/agent-troubleshooting/faq.md](/docs/agents/agent-troubleshooting/faq.md)

## Terminology

Use these terms consistently. The "Avoid" column lists terms that creep in but should not.

| Concept | Use | Avoid |
|---------|-----|-------|
| Autonomous coding sessions | agents | agent mode, agentic workflows |
| Running without user interaction | background agents | background agent mode |
| Code suggestions as you type | inline suggestions | code completions, autocomplete |
| Predicted next edit location | next edit suggestions (NES) | predictive edits |
| Understanding code across files | workspace context, cross-file reasoning | deep semantic understanding (overuse) |
| GitHub's search for code context | GitHub's code search | remote search |
| VS Code's type/symbol analysis | language intelligence (IntelliSense, LSP) | code intelligence |
| Multiple AI model options | multiple AI models | leading AI models |
| Plan then implement workflow | Plan agent, implementation agent | planning mode |

## Capability areas

When auditing, ensure docs accurately cover these areas:

- **Agents**: plan, implement, verify, parallel sessions, local/background/cloud, third-party support
- **Context**: semantic search, language intelligence (LSP), GitHub code search, cross-repo awareness
- **Multi-file editing**: coordinated changes, architecture-level refactoring, framework migrations
- **Enterprise**: organization policies, model access controls, content exclusions, trust boundaries
- **SDLC workflow**: Plan agent, implementation agent, Copilot code review, background/cloud handoff
- **Scale**: large codebases, monorepos, multi-root workspaces, remote indexing


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/best-practices.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/best-practices
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/best-practices.md
- **SHA256_FINGERPRINT**: `1d8f3b0c170a6edc0161d338dccb6ef36f421c908bb3c5fcc638729d2d87c81e`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.005879+00:00
---

**MetaDescription**: Use AI effectively in VS Code by choosing the right workflow, writing focused prompts, and reviewing results.

# Best practices for using AI in VS Code

This article covers good practices for using AI in Visual Studio Code. Start with a bounded task, provide relevant context, and verify the result. Configure custom instructions, agents, or tools later when you have a recurring need.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="How AI works in VS Code">
Learn about the agent loop, context window, tools, and other core concepts.

* [Read about core concepts](/docs/agents/concepts/agents.md)

</div>

## Pick the right tool for the task

AI in VS Code offers several interaction modes. Choosing the right one for the task at hand saves time and produces better results.

| Tool | Best for | Example |
|------|----------|---------|
| [Inline suggestions](/docs/editing/ai-powered-suggestions.md) | Staying in the flow while writing code | Inline suggestions, variable names, boilerplate |
| [Inline chat](/docs/chat/inline-chat.md) | Targeted, in-place edits without switching context | Refactoring a function, adding error handling |
| [Agents](/docs/agents/overview.md) | Multi-file changes that require autonomous planning and tool use | Implementing a feature end-to-end |
| [Plan](/docs/agents/run/planning.md) | Structured planning before implementation | Designing an architecture or migration strategy |
| [Smart actions](/docs/editing/copilot-smart-actions.md) | Built-in, specialized one-step tasks | Generating commit messages, fixing errors, renaming symbols |

## Apply the workflow to your project

When you're ready to use an agent in your own project, start with one bounded task in a project you know:

1. Open a trusted project. Commit or stash unrelated work so that you can distinguish the agent's edits from your own changes.

1. Choose a small task and define an observable result. If the approach is unclear, ask questions in chat or use the [Plan role](/docs/agents/run/planning.md) before implementation.

1. Provide the relevant files, errors, constraints, and existing test commands. For example:

    ```prompt
    Add empty-state text to the results view. Limit changes to the existing
    view and its tests. Follow the current component patterns, run the
    existing tests for this area, and summarize the behavior you verified.
    ```

1. In the [Chat view](/docs/agents/run/chat-view.md), select **Copilot** from the **Session Target** UI control, select the **Agent** role, and keep **Manual permissions** for an interactive first task.

1. Review each approval request. When the agent finishes, inspect every changed file and run the relevant tests yourself.

1. Commit only the intended changes. If the result is wrong, provide focused feedback or [restore a checkpoint](/docs/agents/run/review-code-edits.md#restore-a-checkpoint).

Checkpoints restore affected workspace files and chat history, but they don't reverse completed terminal commands, deployments, or changes to external services. Use Git and the external service's recovery controls for those effects.

For step-by-step guides in an existing project, [explore a codebase](/docs/agents/guides/explore-a-codebase.md), [add a feature](/docs/agents/guides/add-a-feature.md), or [refactor without changing behavior](/docs/agents/guides/refactor-safely.md).

## Write effective prompts

The quality of AI responses depends on the clarity and specificity of your prompt. Writing requests with a clear goal, constraints, and relevant context is often called *prompt engineering*. These techniques help you get better results.

* **Be specific about inputs, outputs, and constraints.** State the programming language, frameworks, and libraries you want to use. Describe expected behavior or include example input and output.

    ```prompt
    Write a TypeScript function that validates email addresses.
    Return true for valid addresses, false otherwise. Don't use regex.
    Example: validateEmail("user@example.com") returns true
    Example: validateEmail("invalid") returns false
    ```

* **Break down complex tasks.** Instead of asking for an entire feature at once, decompose it into smaller, well-scoped steps. This approach produces more reliable results and makes it easier to catch problems early.

* **Include expected output for verification.** Provide test cases, expected results, or acceptance criteria so the AI can verify its own work. This step is one of the highest-leverage things you can do.

    ```prompt
    Implement a rate limiter using the token bucket algorithm.
    Write unit tests that verify: 10 requests/second allowed,
    11th request rejected, bucket refills after 1 second.
    Run the tests after implementing.
    ```

* **Avoid vague prompts.** A prompt like "make this better" gives the AI no direction. Instead, specify what "better" means: "reduce the time complexity" or "add input validation for null values."

* **Iterate with follow-up prompts.** Refine responses by adding constraints or corrections in follow-up messages rather than rewriting the entire prompt.

* **Course-correct early.** If the AI is heading in the wrong direction, [steer it](/docs/chat/chat-overview.md#send-messages-while-a-request-is-running) with a follow-up message to redirect the current request, queue a follow-up request, or stop and send a new prompt.

    For help deciding whether to steer, restore changes, or start fresh, see [Get an agent back on track](/docs/agents/guides/get-agent-back-on-track.md).

* **Tell the AI to ask clarifying questions.** If a task is ambiguous, instruct the AI to ask you questions before proceeding. This leads to more accurate results than guessing at requirements.

* **Parallel tasks.** If you have multiple independent tasks, ask the AI to run them in parallel to save time. For example, "Perform isolated research about X and Y in parallel and summarize the findings."

Adapt the [prompt examples](/docs/agents/guides/prompt-examples.md) for your task, including the multi-turn examples for refining a result. For a video introduction, watch [Core principles of prompt engineering with GitHub Copilot](https://www.youtube.com/watch?v=hh1nOX14TyY).

## Provide the right context

The AI responds more accurately when it has relevant context. Use these techniques to point the AI at the right information:

* The AI automatically performs code search to gather relevant context. When your prompt is ambiguous, you can guide the AI by referencing specific files, folders, or symbols in your prompt with `#<file>`, `#<folder>`, or `#<symbol>`.

* To pull information from web pages or GitHub repositories, use `#fetch` to provide the AI with up-to-date information beyond your codebase or use tools from MCP servers like GitHub MCP.

* Reference VS Code environment context such as source control changes, terminal output, or test failures to help the AI understand the current state of your project and provide more relevant responses.

* Add images or screenshots to let the AI analyze visual content.

* Use the [integrated browser](/docs/debugtest/integrated-browser.md) to preview your app and manually add page elements, screenshots, or console logs as context.

* Give agents [browser tools](/docs/agents/run/browser-tools.md) to exercise user flows, inspect the result, fix problems, and verify their changes autonomously.

For more information, see [adding context to chat prompts](/docs/chat/copilot-chat-context.md) and [configuring tools](/docs/agents/run/tools.md).

## Choose the right model

Each AI model has different strengths. Some are better at reasoning, others excel at code generation or faster responses. Choosing the right model for your task improves results.

* **Match model to task complexity.** Use fast models for simple completions and boilerplate. Switch to reasoning-optimized models for planning, debugging, or architectural decisions.

* **Use latest models.** Newer models often have improved capabilities. VS Code continuously adds support for new models and model versions. Check the [available models](/docs/agent-customization/language-models.md) and use the latest models.

* **Pin models in prompt files and agents.** Specify preferred models in your prompt file or custom agent definitions to ensure the right model is used consistently for specific tasks.

* **Experiment and compare.** If you're not satisfied with a response, try a different model. Different models can produce significantly different results for the same prompt.

* **Adjust thinking effort for reasoning models.** Use the [thinking effort control](/docs/agent-customization/language-models.md#configure-thinking-effort) in the model picker to increase effort for complex tasks or reduce it for simpler ones.

* **Use BYOK for additional control.** Bring your own API key for more model choices and hosting options.

* **Consider credit consumption.** More capable models consume more [AI credits](/docs/agents/concepts/language-models.md#ai-credits-and-model-costs) per token. Auto model selection balances quality and cost automatically. For more tips, see [optimize AI credit usage](/docs/agents/guides/optimize-usage.md).

For more information, see [selecting AI models](/docs/agent-customization/language-models.md) and [available models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat).

## Plan first, then implement

For complex changes that span multiple files, separate planning from implementation. This approach prevents the AI from solving the wrong problem and avoids spending [AI credits](/docs/agents/concepts/language-models.md#ai-credits-and-model-costs) on code that needs to be thrown away.

1. **Explore.** Use chat for questions or use a subagent to read the relevant code and understand how it works before making changes.
1. **Plan.** Use the [Plan agent](/docs/agents/run/planning.md) to create a structured implementation plan. Review and refine the plan before executing.
1. **Implement.** Switch to agent mode and implement from the plan. Include tests or expected outputs so the agent can verify its own work. Run independent sessions that use the Copilot, Claude, or Codex harness in parallel, or hand off to a [cloud agent](/docs/agents/run/agent-harnesses.md#cloud-target) for remote execution.
1. **Review.** Use [checkpoints](/docs/agents/run/review-code-edits.md#edit-requests-and-restore-checkpoints) to review progress, rewind if the agent goes off track, or [request a Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) on the resulting pull request.

For more information, see the [context engineering workflow](/docs/agents/guides/context-engineering-guide.md).

## Review and verify AI output

AI-generated code can contain bugs, security issues, or subtle logic errors. Always treat AI output as a starting point that needs review.

* **Review before integrating.** Read through generated code before you commit or merge the changes. Pay attention to edge cases, error handling, and assumptions the AI might have made.

* **Run tests after AI changes.** Include test cases in your prompt so the AI can verify its own work. If the AI doesn't run tests automatically, run them yourself before moving on.

* **Use checkpoints to rewind file edits and chat.** If the agent goes off track, use [checkpoints](/docs/agents/run/review-code-edits.md#edit-requests-and-restore-checkpoints) to restore affected workspace files and chat history. Checkpoints don't reverse completed commands or changes to external services.

* **Check for security issues.** Review AI-generated code for common vulnerabilities such as injection flaws, hardcoded secrets, or missing input validation. Avoid pasting credentials or sensitive data into prompts.

For more information, see [GitHub Copilot security](/docs/agents/run/security.md) and the [GitHub Copilot Trust Center](https://copilot.github.trust.page/faq).

## Choose the right agent harness

When working with agents, choose the harness that matches your task and workflow. Each harness offers different provider capabilities, tools, and execution environments.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). Contact the IT team that deployed the settings to discuss access.

* **Use the Copilot harness for day-to-day coding.** The Copilot harness runs tools on your machine with access to your workspace and run-time context. It is a good default for most coding tasks. Tool execution location is separate from where the selected language model runs.

* **Use Claude or Codex for provider-specific capabilities.** These harnesses also run tools on your machine and provide their own SDK capabilities through the same VS Code session experience.

* **Use the Cloud target for team collaboration.** [Cloud sessions](/docs/agents/run/agent-harnesses.md#cloud-target) run remotely and create pull requests, making them well suited to tasks that benefit from team review or when you want to assign a GitHub issue directly to an agent.

* **Run parallel sessions for independent tasks.** Start multiple sessions with the Copilot, Claude, or Codex harness, or use cloud sessions, to work on unrelated tasks simultaneously. Monitor them from the [sessions list](/docs/agents/run/sessions/manage-sessions.md#sessions-list).

* **Hand off when another harness or Cloud better fits the next step.** [Continue with another harness or the Cloud target](/docs/agents/run/agent-harnesses.md#continue-with-a-different-harness) while preserving the conversation history and context.

For more information, see [choosing an agent harness](/docs/agents/run/agent-harnesses.md) and the [agentic coding tutorial](/docs/agents/agents-tutorial.md).

## Optimize your project for AI

Project customization is optional. Add it when you have conventions, project context, or workflows that the AI can't reliably infer from your code. Concise customization can also help [optimize AI credit usage](/docs/agents/guides/optimize-usage.md) by reducing repeated context gathering, corrections, and retries.

VS Code supports several mechanisms to configure AI behavior for your project. Enter `/init` in chat to generate a starter configuration.

| Mechanism | Best for | Get started |
|-----------|----------|-------------|
| [Custom instructions](/docs/agent-customization/custom-instructions.md) | Project-wide coding standards and architectural context | Type `/init` to generate always-on instructions for your project |
| [Custom agents](/docs/agent-customization/custom-agents.md) | Specialized workflows or personas (TDD, security audit) | Type `/create-agent <description>` to generate a custom agent |
| [Skills](/docs/agent-customization/agent-skills.md) | Domain-specific capabilities (testing, deployment) | Type `/create-skill <description>` to generate a skill |
| [Tools and MCP servers](/docs/agents/run/tools.md) | Connecting to external systems (databases, APIs, CLIs) | Configure in `mcp.json` |

Tips for effective project configuration:

* **Keep instruction files concise.** They load on every chat interaction. Focus on information the AI can't infer from code, such as non-default conventions, architectural decisions, or environment setup.
* **Scope instructions with `applyTo` patterns.** Enter `/instructions` to create language-specific or folder-specific instruction files instead of putting everything in one file.
* **Limit enabled tools.** Fewer active tools means faster, more relevant responses. Enable tools only when the task needs them.
* **Exclude generated and noisy files from search.** Configure ``search.exclude`` and ``files.exclude`` so agent text search and grep stay focused on source code. See [improve agent search with exclusion settings](/docs/agents/reference/workspace-context.md#improve-agent-search-with-exclusion-settings).

For full setup details, see [Customize agent behavior in VS Code](/docs/agent-customization/overview.md).

## Manage context and sessions

AI responses might degrade as the conversation fills with irrelevant context. Manage your sessions proactively.

* **Start new sessions for unrelated tasks.** Don't keep piling unrelated questions into one conversation. Context pollution reduces response quality and wastes tokens on irrelevant history.

* **Start a fresh chat for related work.** When the task still belongs in the same workspace but doesn't need the current conversation history, [start another chat in the session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session), where supported. It shares the session's files and code changes without inheriting the other chats' history.

* **Compact context.** Use [/compact](/docs/agents/run/sessions/manage-sessions.md#compact-conversation-context) and provide instructions to selectively compact the context and retain only the most relevant information. Compacting reduces the tokens sent with each subsequent request, which helps [manage AI credit usage](/docs/agents/guides/optimize-usage.md).

* **Verify cache performance.** Keep the early parts of your prompt stable across turns to reuse the prompt cache and reduce cost and latency. Use the [Cache Explorer](/docs/agents/agent-troubleshooting/cache-explorer.md) to check cache hit rates and find where the cache breaks.

* **Use subagents for investigation.** Hint the AI to perform research and exploration in isolation by using [subagents](/docs/agents/run/subagents.md) so the findings don't clutter your main context.

* **Choose the right harness and execution environment.** Start with the [Copilot harness](/docs/agents/run/agent-harnesses.md#copilot) for day-to-day work in a folder or isolated worktree. Choose the Local harness for the extension-host workflow in your current workspace, or the Cloud target for independent work on provider-managed infrastructure that returns a pull request.

* **Scale with parallel sessions.** Run multiple sessions in separate folders or worktrees to save time and keep contexts separate. You can switch among sessions that run on your machine, a connected host, in a Dev Container, or on provider-managed cloud infrastructure from the [sessions list](/docs/agents/run/sessions/manage-sessions.md#sessions-list) in VS Code.

* **Fork instead of re-prompting.** Use [`/fork`](/docs/agents/run/sessions/manage-sessions.md#fork-a-chat-session) to explore alternatives without losing context, instead of starting over and re-establishing context from scratch.

For more information, see [session management](/docs/agents/run/sessions/manage-sessions.md), [workspace indexing](/docs/agents/reference/workspace-context.md), and [optimize AI credit usage](/docs/agents/guides/optimize-usage.md).

## Optimize AI credit usage

Many of the practices in this article also help you control cost. More capable models, large contexts, and throwaway work all consume [AI credits](/docs/agents/concepts/language-models.md#ai-credits-and-model-costs). A few levers have the biggest impact:

* **Match the model to the task.** Use faster, cheaper models for simple work and reserve premium models for planning, debugging, and architectural decisions. Auto model selection balances quality and cost for you.

* **Keep context lean.** Send only relevant context, [compact](/docs/agents/run/sessions/manage-sessions.md#compact-conversation-context) long conversations, and start fresh sessions for unrelated tasks to avoid paying for irrelevant history on every request.

* **Plan before you implement.** Separating planning from implementation avoids spending credits on code you throw away.

For a complete set of techniques, see [optimize AI credit usage](/docs/agents/guides/optimize-usage.md).

## Work with large codebases

Copilot is designed to work effectively with large, complex, and multi-root workspaces. Use these practices to get the best results at scale.

* **Use workspace indexing.** VS Code automatically indexes your project using semantic search, language intelligence, and GitHub's code search for deep cross-file reasoning. This works for both small projects and large enterprise codebases. For large repositories, use [remote indexing](/docs/agents/reference/workspace-context.md#semantic-index-sources) for fast, comprehensive results across your repository and related repositories on GitHub.

* **Scope work with multi-root workspaces.** For monorepos or projects with multiple services, use [multi-root workspaces](/docs/editing/workspaces/multi-root-workspaces.md) to give the AI clear boundaries and focused context.

* **Provide project-level instructions.** Use [custom instructions](/docs/agent-customization/custom-instructions.md) to describe your project's architecture, module boundaries, and conventions that the AI can't infer from code alone. This gives the AI the context it needs for architecture-level changes.

* **Run parallel sessions for independent changes.** Break large tasks into independent subtasks and run them in [parallel sessions](/docs/agents/run/sessions/manage-sessions.md#sessions-list), each focused on a different area of the codebase.

* **Use the Plan agent for cross-cutting changes.** For changes that span many files or modules, start with the [Plan agent](/docs/agents/run/planning.md) to create a structured implementation plan before executing.

For more information, see [workspace context](/docs/agents/reference/workspace-context.md) and [agents](/docs/agents/overview.md).

## Related resources

* [Context engineering guide](/docs/agents/guides/context-engineering-guide.md)
* [Optimize AI credit usage](/docs/agents/guides/optimize-usage.md)
* [Customize agent behavior in VS Code](/docs/agent-customization/overview.md)
* [Cheat sheet](/docs/agents/reference/ai-features-cheat-sheet.md)
* [GitHub Copilot security](/docs/agents/run/security.md)
* [Best Practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot) in the GitHub Copilot documentation


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/agent-harnesses.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/agent-harnesses
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/agent-harnesses.md
- **SHA256_FINGERPRINT**: `627e7df85945645d475e47f2e2a2cebafc6e60187c04ec344ee83fc4eaa5c7a9`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.164634+00:00
---

**MetaDescription**: Understand agent harnesses, model access, execution environments, and code isolation in VS Code.

# Understand agent harnesses

An agent harness is the software layer that runs an agent session. It turns a language model into an agent by connecting the model to context and tools, coordinating the [agent loop](/docs/agents/concepts/agents.md#agent-loop), and maintaining session state as the work progresses.

VS Code supports multiple agent harnesses, including Copilot, [product.prodname_anthropic_claude], and [product.prodname_openai_codex]. The Copilot harness uses a shared runtime for core capabilities and more consistent behavior across VS Code, GitHub Copilot CLI, and the GitHub Copilot app.

The model provides the reasoning and decides what to say or which tool to request. The harness makes those decisions operate as a stateful workflow by preparing model requests, coordinating tool calls and approvals, returning results to the model, and tracking the conversation and changes.

This article explains what a harness does and how it differs from model access, a language model, an agent role, and an execution environment. It also explains how the **Session Target** UI control presents harnesses and the Cloud target. To compare harnesses and review their setup requirements, see [Choose an agent harness](/docs/agents/run/agent-harnesses.md).

![Diagram showing an agent harness coordinating the user interface, language model, tools, and conversation state. The model requests actions, while the harness prepares context, applies permissions, coordinates tools, and tracks state.](../images/concepts/agent-harness-relationships.svg)

The diagram shows responsibilities, not process or deployment boundaries. The model requests actions, and the harness applies the relevant permission rules and coordinates tool execution. The model and tools can run in different locations from the harness.

## Follow a turn through an agent harness

When you submit a prompt, the harness coordinates each step of the turn:

1. The harness receives your request and the current session state. It prepares the instructions, context, and available tool definitions for the language model.
1. The language model reasons over that information and returns either a response or a request to call a tool.
1. For a tool request, the harness applies the configured permission and approval rules, routes the call to the environment where the tool runs, and captures the result.
1. The harness returns the tool result to the model. The model decides whether to call another tool, ask for input, or finish the task.
1. The harness associates the messages, tool calls, results, and code changes with the session, and presents the current status in VS Code.

The model chooses the actions, while the harness coordinates the system that carries them out.

## How a harness differs from other agent concepts

Several choices determine how an agent works. They work together, but they are not interchangeable:

| Concept | What it determines | Relationship to the harness |
|---------|--------------------|-----------------------------|
| **Model access** | Which account, subscription, or credentials provide access to a model and how usage is billed. | Each harness supports particular models and access options. Changing the access source does not switch harnesses. |
| **Language model** | How the agent reasons and generates responses. | A harness can offer multiple models, and the same model might be available through more than one harness. The model can run in a different location from the harness. |
| **Agent role** | Which instructions, tools, and behavior apply to a task. Examples include Agent, Plan, Ask, and custom agents. | A role shapes the task behavior within a harness. Changing the role does not replace the harness. |
| **Execution environment** | Where workspace tools run and code changes are made, such as your machine, a connected host, a Dev Container, or cloud infrastructure. | The harness coordinates work in the selected environment. The environment is not the harness. |
| **Session Target** UI control | Which harness or the Cloud target VS Code uses for a session. | This UI control lists harnesses and the Cloud target. In the Agents window, use the workspace picker to select a machine or Dev Container separately from the harness. |

### Model access

You can access models through GitHub Copilot, another account supported by the selected harness, or a configured model provider that uses your API key. Access might require a subscription or usage-based billing. The service that provides access is not necessarily the model developer. For example, Copilot can provide access to Claude-family models developed by Anthropic.

Model access and harness choice are separate. A Copilot subscription can provide access to models in multiple supported harnesses, but signing in does not make every harness available. Each harness determines which models and access options it supports. Selecting a Claude model in the Copilot harness does not switch to the Claude harness. Your account and organization policies also affect availability. Learn how to [configure model access and choose a model](/docs/agent-customization/language-models.md).

### Harness and host

The harness determines agent behavior. The Copilot harness uses the [copilot.copilot_sdk_short] and runs in the Agent Host, while the Local harness runs in the editor's extension host. The Chat view and Agents window are interfaces that display and control supported sessions, not harnesses themselves.

To identify your session's harness and compare options, see [Select a harness](/docs/agents/run/agent-harnesses.md#select-a-harness) and [Compare agent harnesses](/docs/agents/run/agent-harnesses.md#compare-agent-harnesses). For process boundaries, session lifetime, and client-dependent tools, see the optional [Agent Host architecture reference](/docs/agents/concepts/agent-host.md#process-architecture).

## Understand what the harness choice changes

The selected harness defines the agent implementation. Depending on the harness and your configuration, this choice affects:

* **Tools and capabilities**: which built-in, extension-provided, [MCP](/docs/agent-customization/mcp-servers.md), or provider-specific tool integrations the agent supports, and how the harness routes tool calls.
* **Model options**: which language models the harness offers and how it configures requests to them.
* **Agent workflows**: which provider-specific commands, customizations, and session features are available.
* **Permissions**: which approval modes and tool permission settings the harness supports.

The harness choice does not by itself determine where the language model runs or whether code changes go into a folder or worktree. Those choices depend on the models, execution environments, and isolation options that the harness supports.

## Map Session Target choices to harnesses

VS Code provides common chat and session-management surfaces across harnesses. Available controls and workflows depend on the selected harness. The **Session Target** UI control includes both harnesses and the Cloud execution target:

| **Session Target** choice | Harness | Execution environment |
|-----------------------|---------|-----------------------|
| **Copilot** | The Copilot harness, which uses the shared runtime. | Your machine, a connected host, or a Dev Container. |
| **Claude or Codex** | The corresponding provider harness and its provider-specific capabilities. | Your machine, or a connected host or Dev Container where the integration supports it. Check the [harness setup and capabilities](/docs/agents/run/agent-harnesses.md#requirements-and-setup). |
| **Cloud** | The provider harness for the cloud agent that you select, such as Copilot, Claude, or Codex. | The provider's cloud infrastructure, working against a GitHub repository and returning the result through a pull request. |

> [!NOTE]
> **For Local harness sessions:** The Local harness works in the current workspace through the editor's extension host. **Local** is a session-target name, not the only way to run agents on your machine. See [Local setup and capabilities](/docs/agents/run/agent-harnesses.md#local).

> [!NOTE]
> Claude and Codex harness integrations are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). Contact the IT team that deployed the settings to discuss access. Selecting a Claude or OpenAI model in the Copilot harness is a separate choice and does not switch harnesses.

Cloud is an execution target that groups available cloud agents, not a single provider harness. After you select Cloud, you choose an available cloud agent.

## Relate execution environments and code isolation

The execution environment determines where the harness runs workspace tools and changes code. A Dev Container can run on your machine or on a connected host:

* **Your machine**: the harness works with a local folder or Git worktree and can access local context, such as test results and terminal output.
* **A connected host**: the harness runs next to the source code on an SSH, Tunnel, or WSL host. Learn more about [remote agent sessions](/docs/agents/run/remote-agent-sessions.md).
* **A Dev Container**: the agent runs workspace tools inside the project's container and uses its configured tools and dependencies. The container can be on your machine or on a supported SSH, Tunnel, or WSL host.
* **Cloud infrastructure**: the harness works with a GitHub repository and creates a pull request. It uses the tools and models configured in the cloud service instead of your local VS Code environment.

![Diagram showing session execution options grouped by your machine, a connected SSH, Tunnel, or WSL host, and provider-managed cloud infrastructure. Both your machine and a connected host can run sessions directly on the host or inside a Dev Container.](../images/concepts/session-execution-options.svg)

The diagram shows where sessions work on code, not where you connect from or where the language model runs. See [remote sessions and browser access](/docs/agents/run/remote-agent-sessions.md) for connection steps. Harness availability depends on the selected environment.

`feature(agent-host-dev-containers)`

Dev Container sessions require the desktop Agents window and a host that supports Dev Container execution. Selecting a container in the workspace picker changes the execution environment, not the harness. Learn how to [run a session in a Dev Container](/docs/agents/run/agents-window.md#run-a-session-in-a-dev-container).

For sessions that offer folder and worktree options, code isolation controls which working directory receives changes. Folder isolation applies edits directly to your current workspace, including its uncommitted changes. Worktree isolation gives the session a separate [Git worktree](/docs/sourcecontrol/branches-worktrees.md#understanding-worktrees) based on committed Git state. Dev Container sessions work directly in the container workspace and don't support **New Worktree**.

A worktree is a Git code-isolation boundary, not a security boundary. It does not restrict commands, network access, or access to files outside the worktree. Use [agent sandboxing](/docs/agents/run/agent-sandboxing.md) for operating system-level file system and network restrictions.

For ongoing work, the available [handoff options](/docs/agents/concepts/sessions.md#hand-off-a-session) depend on the selected harness. From a Local harness session, you can select another harness or Cloud from the **Session Target** UI control and carry conversation history and context to the new session. Learn how to [continue with a different harness](/docs/agents/run/agent-harnesses.md#continue-with-a-different-harness).

## Related resources

* [Choose an agent harness](/docs/agents/run/agent-harnesses.md)
* [Complete your first task with an agent](/docs/agents/quickstart.md)
* [Sessions and handoff](/docs/agents/concepts/sessions.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/agent-host.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/agent-host
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/agent-host.md
- **SHA256_FINGERPRINT**: `34a95a9d6f379705640678ffc8209bfb5e093ca4d7f37f29edc092aed6c984bd`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.211965+00:00
---

**MetaDescription**: Understand how the VS Code Agent Host manages sessions, execution environments, and connected clients.

# Agent Host architecture

The Agent Host is a dedicated process that runs agent harnesses and manages their sessions. Separating session execution from an individual window lets you work with the same session across interfaces and run agents close to your code and development tools.

This article explains the process boundaries, execution environments, session lifetime, and client dependencies for integrations that use the Agent Host. You don't need this architecture background to use agents. To identify the harness a session uses or compare Local and Copilot, see [Choose an agent harness](/docs/agents/run/agent-harnesses.md). For session-management tasks, see [Manage sessions](/docs/agents/run/sessions/manage-sessions.md).

## What this architecture enables

Separating the agent from the window that displays it provides these capabilities:

* **Shared sessions**: multiple clients can observe and control the same session, staying in sync.
* **Remote execution**: the host can run next to the workspace on another machine while clients connect from elsewhere.
* **Independent execution**: an agent session can continue without a connected editor while the host and its execution environment remain running. Tools provided by a client still require that client.
* **Multiple agent implementations**: different agent runtimes plug into one host-facing interface and present common session concepts to clients.
* **Dedicated process**: agents run in their own process, where they won't be blocked by busy extensions.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). Contact the IT team that deployed the settings to discuss access.

## Process architecture

The components have different responsibilities:

* **Client**: the Chat view, Agents window, or browser interface that displays a session and sends your requests.
* **Agent harness**: the implementation that coordinates the model, tools, and agent workflow.
* **Agent Host**: the process that runs supported harnesses and owns their sessions, independently of the clients displaying them.

The extension host remains responsible for extensions. Extensions can contribute tools, MCP servers, and custom agents without running the agent harness itself. Tools from extensions are available only in chats in an editor window where the extension is running.

![Screenshot showing VS Code communicating with extension-host customizations and the Agent Host, which contains adapters for Copilot, Claude, and Codex.](../images/concepts/agent-host-transition.svg)

The Agent Host can run as a local utility process or as a standalone server on a remote machine. VS Code uses a message port for local IPC and AHP JSON-RPC over WebSocket for remote connections.

Agent adapters run inside the Agent Host process. An adapter translates between its agent runtime and the common [Agent Host Protocol (AHP)](#agent-host-protocol) session model.

## Where sessions run

The Agent Host runs next to the workspace: on your machine, inside a Dev Container, or on a remote machine. Workspace file edits and commands use the environment that contains the host. This does not determine where the language model runs.

The desktop Agents window can connect to an Agent Host on the same machine or on a connected SSH, Tunnel, or WSL host. The [browser-based Agents window](/docs/agents/run/remote-agent-sessions.md#use-the-agents-window-in-the-browser) connects to your development machine through a dev tunnel. The browser is a client, not the host that runs the session.

![Screenshot showing desktop and browser clients connecting to Agent Hosts. The desktop client can use a host workspace or a Dev Container, while the browser connects to a development machine through a dev tunnel.](../images/concepts/agent-host-deployment.svg)

Clients display and control sessions. The Agent Host owns them. Desktop and browser clients can connect to the same tunnel host.

`feature(agent-host-dev-containers)`

For a Dev Container session, the Agent Host runs inside the project's container. The container can run on your machine or on a supported SSH, Tunnel, or WSL host, while the desktop Agents window remains on your machine. Workspace file edits and commands use the tools and dependencies inside the container, rather than those installed directly on the source host.

Dev Container execution is an environment choice, not a different harness. See the [session execution options diagram](/docs/agents/concepts/agent-harnesses.md#relate-execution-environments-and-code-isolation) for how local, connected-host, container, and cloud execution relate. For setup steps, see [Run an agent session in a Dev Container](/docs/agents/run/agents-window.md#run-a-session-in-a-dev-container).

Like [VS Code Remote Development](/docs/remote/remote-overview.md), the user interface stays on the client while workspace operations run close to the source code and development tools.

The **Cloud** target is a separate choice that uses provider-managed infrastructure. Connecting to an Agent Host on another machine does not turn the session into a cloud-agent session.

## Session lifetime and client dependencies

The Agent Host includes the baseline capabilities needed to manage sessions and work with the workspace without a connected client. A client can disconnect and reconnect to the same session.

An active turn can continue after its project window closes while the Agent Host remains running. For sessions managed by desktop VS Code on your machine, keep the application running. Closing a project folder is different from quitting the application.

For remote sessions, keep the remote machine and the process serving the session running. Reconnecting to a session does not mean that active work continued while its host process was stopped or its machine was shut down.

Connected clients can contribute tools, such as browser tools or tools from installed extensions. The Agent Host adds those definitions to the session and routes each tool call back to the contributing client. These tools require that client to remain connected. Learn how to [manage tool availability](/docs/agents/run/tools.md#manage-tool-availability-for-the-copilot-harness).

## Agent Host Protocol

[Agent Host Protocol](https://microsoft.github.io/agent-host-protocol/) is an open, agent-agnostic protocol between a host and its clients. It uses JSON-RPC for communication and immutable state with pure reducers for synchronized session data.

The host is the source of truth. Each client subscribes to URI-addressed channels for resources such as sessions, chats, terminals, and changesets. The client receives an initial state snapshot followed by ordered actions. If the connection drops, the client reconnects and receives missed actions or a fresh snapshot.

For protocol definitions and implementation details, see the [Agent Host Protocol source repository](https://github.com/microsoft/agent-host-protocol).

## Run a standalone host

To run your own standalone Agent Host, use `code agent host`. By default, the command starts a server on localhost and protects it with a connection token. Use the `--tunnel` option to expose it through a dev tunnel.

## Local and existing extension-host sessions

Not every agent session uses the Agent Host. Sessions use the extension host in these cases:

* You select the **Local** harness when you create a session.
* You continue a session that was created with the earlier extension-host architecture, before Agent Host-backed sessions were available.

Extension-host sessions are closely integrated with the current editor window and its extensions. This integration comes with a tradeoff: the window owns the session, so closing the window stops ongoing work, and you can't continue the session from another interface.

Agent Host sessions are owned by a dedicated process instead of an individual editor window. They can continue after you close the window and can be reopened from supported interfaces while the host remains running. Running agents in a separate process also prevents a busy extension host from blocking them. However, tools contributed by an editor window, such as tools from installed extensions, remain available only while that window is connected.

The process boundary also affects how you review edits, configure the agent, and continue sessions. For task-specific differences, see the following guides:

| Task | Guidance |
|------|----------|
| Review saved edits | [Review Local harness session changes](/docs/agents/run/review-code-edits.md#review-local-harness-session-changes). |
| Configure instructions and custom agents | [Choose customization scope and locations](/docs/agent-customization/overview.md#choose-a-customization-scope) or [move existing customizations](/docs/agent-customization/migrate-customizations.md). |
| Configure hooks | [Choose the hook implementation for your session](/docs/agent-customization/hooks.md#choose-the-hook-implementation-for-your-session). Sharing a host does not give harnesses a shared hook schema. |
| Set permissions and Autopilot behavior | [Manage approvals and permissions](/docs/agents/run/approvals.md#permission-levels). |
| Continue sessions across interfaces | [Sessions across surfaces](/docs/agents/concepts/sessions.md#sessions-across-surfaces). |
| Configure tools and MCP servers | [Manage available tools](/docs/agents/run/tools.md#manage-available-tools) and [MCP configuration formats](/docs/agents/reference/mcp-configuration.md#configuration-file). |

## Related resources

* [Remote agent sessions](/docs/agents/run/remote-agent-sessions.md)
* [Agent harness concepts](/docs/agents/concepts/agent-harnesses.md)
* [VS Code Remote Development architecture](/docs/remote/remote-overview.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/agents.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/agents
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/agents.md
- **SHA256_FINGERPRINT**: `6a21dc55a3f249f6cbc568643ddbb85719898a2175111729f64bcda071b644b8`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.173646+00:00
---

**MetaDescription**: Understand how agents in VS Code use models, context, and tools to complete coding tasks.

# Understand AI agents

An agent is an AI system that uses a language model and [tools](/docs/agents/concepts/tools.md) to complete a goal on your behalf. A language model generates responses based on the information in a prompt. An agent goes further by gathering context, taking actions in your development environment, evaluating the results, and repeating these steps as needed.

You choose the goal, control which actions require approval, and review the resulting changes. This article explains how the agent loop works and introduces the sessions, planning, subagents, memory, and customizations that support agentic work.

For an overview of AI workflows in VS Code and where to work with agents, see [Build with AI in VS Code](/docs/agents/overview.md).

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
Complete a short quickstart to create and validate an app with an agent in VS Code.

* [Start the agents quickstart](/docs/agents/quickstart.md)

</div>

## How the concepts fit together

The core concepts work together each time you send a request:

1. **Request:** You describe a goal and provide any requirements or constraints.
1. **Context and reasoning:** VS Code assembles relevant [context](/docs/agents/concepts/context.md), such as files and conversation history. A [language model](/docs/agents/concepts/language-models.md) reasons over that information and determines the next action.
1. **Tool action:** The agent uses [tools](/docs/agents/concepts/tools.md) to gather more information or act on your environment, such as reading a file, editing code, or running a command.
1. **Validation:** The result of the tool call returns to the model as context. The agent evaluates its progress and decides whether to take another action.
1. **Review:** When the task is complete, you review the response, code changes, and validation results.

The repeated reasoning, action, and validation steps form the **agent loop**. A [session](/docs/agents/concepts/sessions.md) keeps the conversation and task state together. An [agent harness](/docs/agents/concepts/agent-harnesses.md) coordinates the loop, while the execution environment determines where tools run and code changes are made.

## Agent loop

The agent loop enables an agent to work through a task instead of producing a single response. At each step, the agent evaluates its progress and chooses the next action. The output of that action informs the next decision.

![Screenshot showing a diagram of the agentic loop from the user prompt through reasoning, tool calls, updates, and final review.](../images/concepts/agent-loop.png)

For example, when you ask an agent to add validation to a form, the loop typically includes these stages:

1. **Understand:** The agent finds the form, reads related code and tests, and identifies the project's existing validation patterns.
1. **Act:** The agent updates the form and adds or modifies tests.
1. **Validate:** The agent runs the relevant tests and checks for errors. If validation fails, it diagnoses the result, makes another change, and validates again.

Simple questions might require only a few file reads. Larger implementation tasks might repeat the loop many times as the agent edits code, runs tests, and fixes problems.

## Stay in control

An agent can take actions, but you remain responsible for directing the task and deciding which changes to keep. During a session, you can:

* Choose which tools are available and which tool calls require approval.
* Review an approval request before an action runs.
* Send another message to add context or redirect the work.
* Stop the agent if it is taking the wrong approach.
* Review changed files and validation results before you keep the changes.

Learn more about [trust and safety controls](/docs/agents/concepts/trust-and-safety.md).

## Sessions

A session is the unit of work with an agent. It brings together the workspace, code changes, and execution state for a task. Depending on the harness, a session can contain multiple chats, each with its own conversation history.

Sessions can run in parallel. Both the [Chat view](/docs/agents/run/chat-view.md) and the [Agents window](/docs/agents/run/agents-window.md) support agents, but the harness determines whether you can continue the same session in both interfaces. For example, Local harness sessions are editor-only. Sessions can use the same folder or separate worktrees, so separate conversations don't necessarily isolate code changes. Learn about [session compatibility, execution environments, and handoff](/docs/agents/concepts/sessions.md).

## Agent harnesses and execution environments

An agent harness is the runtime that coordinates the agent loop. It manages the session, connects the language model to tools, and provides provider-specific capabilities. VS Code supports harnesses such as Copilot, Claude, and Codex.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). Contact the IT team that deployed the settings to discuss access.

The execution environment is where the harness runs workspace tools and changes code. Depending on the available harness, this can be your machine, a connected host, a Dev Container on either host, or cloud infrastructure. A Dev Container provides the project's configured tools and dependencies without changing the harness. Learn more about [agent harnesses and execution environments](/docs/agents/concepts/agent-harnesses.md#relate-execution-environments-and-code-isolation).

## Capabilities that extend agent work

Agents can use additional capabilities for complex tasks and recurring workflows. These capabilities are not required for every request.

### Planning

Every agent decides which action to take next as part of the agent loop. For a complex task, use the built-in Plan agent to research the codebase, clarify requirements, and propose an implementation plan before code changes begin.

The Plan agent uses read-only tools while preparing the plan. After you review and approve the approach, you can hand off the plan to an implementation agent. Learn more about [planning with agents](/docs/agents/run/planning.md).

### Subagents

For complex tasks, the main agent can delegate focused work to subagents. A subagent performs a specific task, such as researching a topic or analyzing part of a codebase, and reports the result to the main agent.

Subagents are useful when independent research would add large amounts of intermediate information to the main agent's [context window](/docs/agents/concepts/language-models.md#context-window).

Key characteristics of subagents:

* **Context isolation**: each subagent works in its own context. The harness determines which instructions and conversation history it receives. In the Local harness, subagents receive the delegated task and applicable instructions, not the main conversation history.
* **Parallel execution**: independent subtasks can run in parallel when the harness supports concurrent subagents, such as separate correctness and performance reviews.
* **Focused results**: the main agent uses the subagent's result without adding all of its intermediate work to the main context.

Subagents make their own model requests, so a smaller main context doesn't necessarily mean lower total token usage or [cost](/docs/agents/concepts/language-models.md#ai-credits-and-model-costs).

You don't need to create a custom agent to use subagents. A [custom agent](/docs/agent-customization/custom-agents.md) defines reusable instructions, tools, and model preferences that a subagent can use.

For example, the [Plan agent](#planning) can use subagents to research independent parts of a task before creating a plan.

Learn more about [using subagents](/docs/agents/run/subagents.md).

### Memory

When the memory tool is available, an agent can store notes for use later in the same session or in future sessions. These notes can record preferences, lessons from previous tasks, or information about your codebase. Memory is separate from the conversation context that a session accumulates automatically.

The memory tool stores notes locally on your machine in three scopes:

* **User memory** (`/memories/`): persists across all workspaces and conversations. The first 200 lines are automatically loaded into every session.
* **Repository memory** (`/memories/repo/`): scoped to the current workspace and persists across conversations.
* **Session memory** (`/memories/session/`): scoped to the current conversation and cleared when it ends.

Learn more about [memory in VS Code agents](/docs/agents/run/memory.md).

### Customization

You can customize the agent loop for a project or workflow:

* A [**custom agent**](/docs/agent-customization/custom-agents.md) defines instructions, available tools, a language model, and optional handoffs for a specific workflow.
* [**Agent skills**](/docs/agent-customization/agent-skills.md) give an agent instructions and resources for a specialized task.
* [**Hooks**](/docs/agent-customization/hooks.md) run commands at specific points in the agent lifecycle.

Learn more about [customization concepts](/docs/agents/concepts/customization.md).

## Related resources

* [Tools](/docs/agents/concepts/tools.md)
* [Agent harnesses and execution environments](/docs/agents/concepts/agent-harnesses.md)
* [Trust and safety](/docs/agents/concepts/trust-and-safety.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/context.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/context
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/context.md
- **SHA256_FINGERPRINT**: `9153d2c432aa99315bd4d81a1e092a59ee2b2abe4a7dd3d261653cc7b81a7070`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:30.340388+00:00
---

**MetaDescription**: Understand how AI agents in VS Code use and manage context to produce relevant responses.

# Understand context in AI agents

Context is the information available to an AI agent and its language model while they work on your request. It can include conversation history, files from your workspace, tool outputs, custom instructions, and references you add to your prompt.

The language model reasons over this information to decide what to say or do next. The agent can use [tools](/docs/agents/concepts/tools.md) to gather more context, take actions, and evaluate the results. This article explains how VS Code assembles and discovers context, and how to work within context window limits.

## Why context matters

A prompt with relevant files, clear instructions, and focused history produces better results than a vague prompt with no context. The language model can only reason over information included in its current context.

You don't need to identify every relevant file before you start. During the [agent loop](/docs/agents/concepts/agents.md#agent-loop), the agent can search your workspace, read files, run commands, and add the results to the context for its next step. Explicit references are useful when you already know which information the agent should consider.

Conversation history is scoped to a chat and isn't automatically shared with other chats or sessions. Context can be passed explicitly, such as in a delegated task or a [handoff](/docs/agents/concepts/sessions.md#hand-off-a-session). Persistent sources, such as [custom instructions](/docs/agent-customization/custom-instructions.md) or [agent memory](/docs/agents/concepts/agents.md#memory), can also provide information across conversations.

## How VS Code assembles context

Each time the agent sends a request to the language model, VS Code assembles a prompt from multiple sources:

![Diagram showing the context window as a container with seven layers: system instructions, customizations, user message, conversation history, implicit context, explicit references, and tool outputs, with an arrow sending the assembled prompt to the language model.](../images/concepts/context-assembly.png)

* **System instructions**: built-in guidelines that define the agent's behavior.
* **Customizations**: AI customizations you set up, including custom agents, skills, and custom instructions.
* **User message**: the current request or follow-up message you send to the agent.
* **Conversation history**: the messages exchanged so far in the current chat.
* **Implicit context**: editor information, such as the active file or selection, when the interface, harness, and context settings include it.
* **Explicit references**: files, editor context, web content, and other sources you reference with `#`-mentions.
* **Tool outputs**: results from file reads, terminal commands, codebase search results, and other tool calls during agent sessions.

The context changes as the agent works. For example, the output of a code search can lead the agent to read a file, and that file can then inform the next model request. Information that isn't included in a request is unavailable to the model, but the agent can use tools to discover and add more information.

## Workspace indexing

VS Code uses a semantic index to find code by meaning rather than only by exact keywords. The index helps the agent locate relevant snippets quickly, especially in a large codebase. It doesn't add your entire workspace to every model request.

VS Code builds and maintains the index automatically. If a semantic index isn't available yet, the agent can still find context by using text search, file search, and language intelligence.

Learn more about [workspace indexing](/docs/agents/reference/workspace-context.md).

## Implicit context

VS Code can use your editor activity to provide context to a request or suggest an attachment. This behavior depends on the interface, harness, and context settings:

* In the Chat view, the active file, notebook, or selected text can provide editor context.
* With the Local harness and the default context settings, **Ask** includes active editor context. **Agent** suggests the active file as an attachment, while selected text is included.
* Agent Host sessions, such as Copilot, can also receive active editor context automatically. The Local harness behavior doesn't apply to every agent.
* In the Agents window, implicit editor context is off by default. Add the files or project context that the request needs.

A suggested attachment isn't the same as an explicitly attached file. When a source is important, [add it to the request](/docs/chat/copilot-chat-context.md#add-files-as-context) instead of assuming that an open editor supplies the full file. The agent can also gather more context through its tools.

## Explicit context

Add explicit context when you want to ensure that the agent considers a specific file, folder, symbol, image, web page, or other source. Type `#` in the chat input to choose a context item, or select **Add Context** (`+` icon) in the chat input field.

Explicit context guides the agent toward relevant information but still counts toward the context window. Add only the sources that help the agent complete the current task. Learn more about [adding context to chat](/docs/chat/copilot-chat-context.md).

> [!TIP]
> Providing focused context up front might reduce the searches and file reads the agent needs, which can lower AI credit use. Avoid adding unrelated or large sources because they also consume context window tokens. Learn more about [optimizing AI credit usage](/docs/agents/guides/optimize-usage.md).

## Context window and compaction

The context window is the maximum amount of information a language model can process in one request. The user message, conversation history, instructions, referenced files, and tool outputs all use space in this window.

When a conversation approaches the limit, VS Code automatically compacts older parts of the conversation into a summary. Compaction makes room for new information, but details from earlier messages might be summarized or omitted. You can also enter `/compact` in the chat input to compact the conversation manually.

To start with fresh conversation history while keeping the same workspace and code changes, [create another chat in the session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session), where supported. Start a new session for an unrelated task or a different project. Neither action removes saved files, applicable custom instructions, or persistent memory. If an instruction should apply across conversations, store it in [custom instructions](/docs/agent-customization/custom-instructions.md). Learn more about [managing conversation context](/docs/agents/run/sessions/manage-sessions.md#compact-conversation-context).

## Context isolation with subagents

An agent can delegate a focused task to a [subagent](/docs/agents/concepts/agents.md#subagents) that works in its own context and returns a result. This keeps intermediate work separate from the main conversation. Compaction, by contrast, summarizes content already in that conversation.

Context isolation is not code isolation. It doesn't by itself create a separate worktree or sandbox. An agent's access to files and tools depends on the [execution environment](/docs/agents/concepts/agent-harnesses.md#relate-execution-environments-and-code-isolation) and [permission controls](/docs/agents/concepts/trust-and-safety.md).

Learn how to [delegate work to subagents](/docs/agents/run/subagents.md).

## Working effectively with context

* **Describe the goal and constraints.** Explain the outcome you want and any requirements the agent should follow.
* **Let the agent discover context.** The agent can search your workspace and read related files as it works. You don't need to attach the entire codebase.
* **Reference important sources.** Explicitly add files, symbols, errors, or documentation that the agent must consider.
* **Keep each conversation focused.** Use a new chat for related work that doesn't need the current history, or a separate session for an unrelated task.

### How context improves a response

Consider asking an agent to explain how authentication works in your project.

Without relevant workspace context:

```prompt
How does authentication work?
```

The model has no way to know which project you mean and gives a generic answer about authentication patterns.

After attaching `src/auth.ts` to the request as context:

```prompt
Explain the authentication flow and identify where tokens are validated.
```

The referenced file gives the agent a starting point. The agent can then search for related code and explain the implementation with specific functions and configuration values.

## Related resources

* [Language models](/docs/agents/concepts/language-models.md)
* [Prompt examples](/docs/agents/guides/prompt-examples.md)
* [Context engineering guide](/docs/agents/guides/context-engineering-guide.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/customization.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/customization
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/customization.md
- **SHA256_FINGERPRINT**: `62a2280ff21f56de079df803c5ab3e8f29762dc7cdc81b0720f91f0cc6bc871c`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.322695+00:00
---

**MetaDescription**: Choose instructions, skills, custom agents, and other customizations for your workflow in VS Code.

# Understand agent customization

AI models have broad knowledge, but they don't know your codebase, team practices, or development systems. Agent customization adapts an agent to your environment by adding persistent context, repeatable workflows, specialized roles, external tools, and deterministic controls.

This article explains how customizations change an agent, how the customization types differ, and how you can combine them. To create and manage customizations, see [Customize agent behavior in Visual Studio Code](/docs/agent-customization/overview.md).

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with customizations">
Follow a hands-on tutorial to discover the customization options and configure them for your project.

* [Customize AI for your project](/docs/agents/guides/customize-copilot-guide.md)

</div>

## How customization changes an agent

Without customization, the agent works from your prompt, the current conversation, and the context it gathers from your workspace. Customizations add information or capabilities that persist beyond a single prompt. They can change different parts of the agent's work:

* **Provide context**: [instructions](/docs/agent-customization/custom-instructions.md) describe coding standards, architecture decisions, and other rules the agent should follow.
* **Define repeatable work**: [agent skills](/docs/agent-customization/agent-skills.md) and [prompt files](/docs/agent-customization/prompt-files.md) package task-specific guidance so you don't have to describe the same process in every conversation.
* **Configure a role**: [custom agents](/docs/agent-customization/custom-agents.md) combine instructions, tools, and a language model into a specialized agent persona.
* **Add capabilities**: [MCP servers](/docs/agent-customization/mcp-servers.md) give the agent tools for interacting with external systems such as databases, browsers, and APIs.
* **Automate lifecycle actions**: [hooks](/docs/agent-customization/hooks.md) run commands at specific points in the agent loop, independent of whether the model chooses to run them.
* **Adopt a ready-made setup**: [agent plugins](/docs/agent-customization/agent-plugins.md) let you install multiple related customization types as one package.

These mechanisms affect different layers of the agent. Instructions guide the model's decisions, tools expand the actions it can take, and hooks run outside the model's decision-making. Adding a rule to an instructions file is not equivalent to executing a validation script. Neither mechanism alone establishes a security boundary.

Relevant customizations can reduce back-and-forth and rework by giving the agent project context from the start. Avoiding corrective turns and discarded implementations can help reduce [AI credit usage](/docs/agents/guides/optimize-usage.md). Keep customizations focused because their content also consumes space in the model's context window.

## Customization options at a glance

Start from an observed problem instead of adding customization by default. Define a representative task and its expected outcome. If the result already meets your needs, stop. Otherwise, try the smallest change that addresses the repeated problem.

Before creating files, [check the selected harness and supported locations](/docs/agent-customization/overview.md#check-harness-compatibility). Choosing a language model doesn't change the customization formats that a harness reads. For example, prompt files and reusable tool-set files are Local harness customizations; use skills for reusable workflows with other skills-compatible harnesses.

| Observed behavior | Smallest change to try |
|-------------------|------------------------|
| The agent misses a one-time requirement or relevant file | Add the requirement or [context](/docs/chat/copilot-chat-context.md) to the current request |
| The agent repeatedly misses a project-wide command, convention, or architecture decision | Add or refine project instructions |
| The problem only affects certain files, languages, or tasks | Add targeted instructions |
| Your team repeatedly explains the same multi-step process | Create an agent skill |
| A recurring role needs focused instructions or a restricted tool set | Create a custom agent |
| The agent needs to interact with an external system | Add an MCP server |
| An action must run at a lifecycle point independently of the model | Configure a hook |
| Your team wants to install and maintain a packaged set of customizations | Use an agent plugin |

Ask the following questions when choosing a customization:

* Does the selected harness support the format, file location, and scope you need?
* Should it apply automatically, or only when you request it?
* Are you providing guidance, defining a workflow, adding a capability, or enforcing an action?
* Should the model decide when to use it?

The following table compares the customization types by purpose and activation.

| Need | Use | Example | Activation |
|------|-----|---------|------------|
| Apply standards across a project | [Always-on instructions](/docs/agent-customization/custom-instructions.md) | Require a specific logging library and error-handling pattern | Automatically included in each request |
| Apply guidance to specific code or tasks | [File-based instructions](/docs/agent-customization/custom-instructions.md) | Apply React conventions when the agent works with `.tsx` files | Included when files match a pattern or the task matches the description |
| Teach the agent a workflow with supporting resources | [Agent skills](/docs/agent-customization/agent-skills.md) | Create a service from instructions, template files, and a setup script | The agent loads the skill when the task matches, or you invoke it directly |
| Run a saved task on demand | [Prompt files](/docs/agent-customization/prompt-files.md) | Scaffold a React component | You invoke the prompt as a slash command (Local harness sessions only) |
| Use a specialized role and tool configuration | [Custom agents](/docs/agent-customization/custom-agents.md) | Review code with read-only tools | You select the agent, use it as a subagent, or another agent delegates to it |
| Connect to an external system | [MCP](/docs/agent-customization/mcp-servers.md) | Query a database or update an issue | The agent calls an MCP tool when the task requires it |
| Run code at a lifecycle event | [Hooks](/docs/agent-customization/hooks.md) | Run a formatter after a file edit or block a risky command | VS Code runs the hook when the configured event occurs |
| Install a packaged customization setup | [Agent plugins](/docs/agent-customization/agent-plugins.md) | Add a testing workflow with a skill, agent, hooks, and MCP server | Each bundled customization follows its own activation rules |

Start with instructions when your main goal is to stop repeating project context. Add other customization types when you identify a recurring task, specialized role, missing capability, or action that must always run.

## Model-driven vs. deterministic behavior

Most customizations guide the model or give it more options. The model interprets instructions, decides whether a skill is relevant, and chooses when to call an available tool. The result depends on the request, available context, and model reasoning.

Hooks are dispatched by the runtime when a supported, configured lifecycle event occurs. Use a hook for actions such as validating a tool call or starting a formatter after an edit. Discovery, trust, filters, timeouts, and error handling still affect execution. Use instructions when you want to guide how the agent reasons or writes code.

For example, an instruction that says "run the formatter after editing a file" asks the model to remember and perform that action. A hook configured for the corresponding lifecycle event runs regardless of whether the model remembers the instruction.

For new Copilot hooks, use the [shared runtime guidance](/docs/agent-customization/hooks.md). Existing hooks in personal folders, settings, repositories, agents, or plugins need a [compatibility review](/docs/agent-customization/migrate-customizations.md#migrate-hooks) when migrating from Local.

## How customizations combine

Customization types are building blocks rather than mutually exclusive alternatives. Consider an agent that prepares a pull request for your project:

1. **Instructions** provide the repository's coding standards and pull request conventions.
1. A **custom agent** gives the agent a focused role and limits it to the tools needed for the task.
1. An **agent skill** supplies the steps, scripts, and templates for preparing the pull request.
1. An **MCP server** provides tools to retrieve the related issue from an external issue tracker.
1. **Hooks** run required validation after the agent edits files and block disallowed commands.

Each layer has a separate responsibility. You can update the coding standards without changing the workflow, or replace the external system without rewriting the agent's role.

A plugin can distribute the complete configuration, for example within your organization, so that other developers can install the same skills and MCP servers.

## Customization scope

Where you define a customization determines who can use it and where it applies. Depending on the customization type, you can define it at one or more of these levels:

* **User**: available to you across workspaces.
* **Workspace or repository**: stored with the project and shared with contributors through source control.
* **Organization**: managed centrally and shared across repositories, where supported.

Choose the narrowest scope that matches the information. Personal preferences belong at the user level. Project architecture and team workflows belong in the repository. Organization-wide requirements belong at the organization level when the customization type supports it.

Agent [memory](/docs/agents/run/memory.md) is separate from project customization. Use local memory for personal preferences or emerging observations that aren't ready to share. Put reviewed project rules and workflows that contributors depend on in repository documentation or customizations so your team can review and maintain them.

Not every customization type supports every scope or agent harness. See the individual customization guide for supported locations and environments.

## Related resources

* [Customize agent behavior in VS Code](/docs/agent-customization/overview.md)
* [Customize AI for your project](/docs/agents/guides/customize-copilot-guide.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/language-models.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/language-models
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/language-models.md
- **SHA256_FINGERPRINT**: `cc491a46c1e51f63583c8351bac7aaed93e56aa7c63d5e307aae58eec3c332f5`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.336184+00:00
---

**MetaDescription**: Understand language models in VS Code, including model access, characteristics, context windows, and selection.

# Understand language models

Visual Studio Code uses large language models (LLMs) to power its AI features. You have flexibility in which models you use and how you access them:

* **Models from your GitHub Copilot plan**: choose from multiple models by different providers, such as Anthropic, Google, and OpenAI, included with your plan.
* **Other accounts**: use an [account supported by the selected harness](/docs/agents/run/agent-harnesses.md#cloud-target), such as a ChatGPT account for Codex. Model availability, usage limits, and billing depend on that account's plan and the harness.
* **Bring your own key (BYOK)**: add models from other providers with your own API key, or host your own models, including local models that run offline. With BYOK, you can use agents in VS Code without a GitHub Copilot plan.
* **On-device models** `feature(on-device-models)`: download a [Copilot-provided coding model](/docs/agent-customization/language-models.md#use-on-device-models-experimental) and run it on a supported NVIDIA GPU in Copilot harness sessions.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), even when you use separate provider credentials. Contact the IT team that deployed the settings to discuss access. This harness restriction does not itself disable Claude or OpenAI models in the Copilot harness.

This article explains how language models work, their characteristics, and how to think about model selection.

![Screenshot of the Language Models editor, showing the list of available models.](../images/language-models/language-models-editor.png)

## How language models work

A language model processes text input (a "prompt") and generates text output. In VS Code, the prompt is assembled from multiple sources: your message, conversation history, file contents, tool outputs, and custom instructions. The model generates responses that can include explanations, code edits, or requests to call [tools](/docs/agents/concepts/tools.md).

Language models don't execute code or access files directly. Instead, they generate text that the [agent loop](/docs/agents/concepts/agents.md#agent-loop) interprets as actions. When a model requests a tool call, VS Code executes the tool and feeds the result back to the model for the next iteration.

Some key characteristics of language models include:

* **Nondeterministic**: the same prompt can produce different results each time. This is by design and reflects how the model samples from probability distributions.
* **Context-dependent**: the quality of the response depends on the quality and relevance of the [context](/docs/agents/concepts/context.md) provided in the prompt.
* **Knowledge boundaries**: models are trained on data up to a certain date and might produce outdated or incorrect information for topics beyond their training data. VS Code mitigates this with tools and workspace indexing.

## Context window

The context window is the total amount of information a model can process in a single request. It includes everything: the system prompt, custom instructions, conversation history, file contents, tool outputs, and your current message. Different models have different context window sizes.

When the context window fills up, VS Code automatically summarizes older parts of the conversation to make room. This means important details from early in a long conversation might be compressed or lost. You can also type `/compact` in the chat input to manually trigger compaction at any time. Optionally, add custom instructions after the command to guide the summary, for example `/compact focus on the API design decisions`.

Learn more about [how VS Code assembles context](/docs/agents/concepts/context.md) and [context compaction](/docs/agents/run/sessions/manage-sessions.md#compact-conversation-context).

## Thinking and reasoning

Some language models can perform extended reasoning, also called "thinking", before producing a response. Instead of generating an answer immediately, a reasoning model first works through the problem internally, considering multiple approaches, evaluating trade-offs, and building a step-by-step chain of thought. This internal reasoning happens in dedicated thinking tokens that are separate from the final output.

Reasoning models are especially effective for complex tasks like multi-step debugging, architectural planning, code refactoring, and mathematical or scientific analysis. For simpler tasks like generating boilerplate or answering basic questions, the extra reasoning adds latency without significant benefit.

### Thinking effort

Thinking effort controls how much reasoning a model applies to each request. Higher effort levels produce more thorough internal reasoning, which improves quality for complex problems. Lower effort levels reduce latency and token usage by limiting or skipping the thinking step.

The available effort levels and their default values vary by model and provider. Some models also support *adaptive thinking*, where the model dynamically decides whether and how much to reason based on the complexity of each request, rather than always using a fixed thinking budget.

VS Code sets default effort levels based on evaluations and online performance data, and has adaptive reasoning enabled where supported. For most use cases, the defaults work well without changes.

### Thinking tokens

Thinking tokens count toward the model's context window, even though they are not visible in the response. The actual thinking output is typically returned in summarized form or can be omitted entirely for lower latency. Keep in mind that higher thinking effort levels can produce more thinking tokens, which can increase latency.

Learn how to [configure the thinking effort level](/docs/agent-customization/language-models.md#configure-thinking-effort) in VS Code.

## Choose the right model

Each model has different strengths. Some are optimized for speed and work well for quick edits and simple questions. Others have larger context windows or better reasoning capabilities, making them ideal for complex tasks. As a general guideline:

* **Fast models** are best for quick code edits, boilerplate generation, and straightforward questions.
* **Reasoning models** excel at complex refactoring, architectural decisions, multi-step debugging, and tasks that require analyzing trade-offs.
* **Large context models** work well for large codebases or long conversations where retaining more information matters.

You can switch models at any time, based on your needs for a particular task. For a detailed comparison, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task) in the GitHub Copilot documentation.

### Auto model selection

Auto model selection in GitHub Copilot combines two systems to route each request to the optimal model. One system tracks real-time model health and availability, while the other evaluates task complexity. Together, they match each task to the model that can solve it most efficiently, reserving higher-cost reasoning models for problems that need them and routing simpler tasks to faster models.

Auto selects from multiple models and respects your organization's [model access settings](https://docs.github.com/en/copilot/how-tos/use-ai-models/configure-access-to-ai-models). Auto won't select models excluded by administrator policies or models restricted by data-residency policies.

When you turn on **Use in Auto** for an [on-device model](/docs/agent-customization/language-models.md#use-on-device-models-experimental), Auto can route some requests to that model on your device, with cloud fallback.

For more details, see [About Copilot auto model selection](https://docs.github.com/en/copilot/concepts/auto-model-selection) in the GitHub documentation.

### AI credits and model costs

Each Copilot plan includes a monthly allowance of [AI credits](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals). Different models consume AI credits at different rates, based on the model and the number of tokens processed. More capable models cost more per token, while lighter models extend your usage further. When you use auto model selection, VS Code routes each request to an efficient model that balances quality and cost.

Other factors also affect credit consumption, such as [thinking effort](/docs/agent-customization/language-models.md#configure-thinking-effort) (higher effort produces more thinking tokens), context window size, and tool usage. Prompt caching lowers the effective cost of a request by reusing tokens from a previous one. You can inspect cache hit rates with the [Cache Explorer](/docs/agents/agent-troubleshooting/cache-explorer.md). For practical tips on reducing credit consumption, see [optimize AI credit usage](/docs/agents/guides/optimize-usage.md).

Learn how to [choose and configure language models](/docs/agent-customization/language-models.md) in VS Code.

## Bring your own language model key

If the built-in models don't meet your needs, you can bring your own language model API key (BYOK) to use models from other providers or to run models locally. BYOK lets you connect to any compatible model provider while still using the VS Code chat and agentic coding features. VS Code has a built-in list of supported providers or you can add more providers from the [product.prodname_vs_marketplace].

You can use BYOK for both the agent experience and utility tasks, such as commit message generation.

### Why bring your own key

* **Model choice**: access hundreds of models from different providers, beyond the built-in models.
* **Experimentation**: try new models or features that are not yet available in the built-in models.
* **Local compute**: use your own compute for one of the models already supported in GitHub Copilot or to run models not yet available.
* **Greater control**: bypass the standard rate limits and restrictions imposed on the built-in models.
* **Offline and air-gapped environments**: use AI chat features with a local model like Ollama without a GitHub account, a Copilot plan, or an internet connection.

### Considerations

* BYOK only applies to the chat experience and utility tasks. Inline suggestions (code completions) and features that rely on embeddings, such as semantic search, still require a GitHub Copilot plan.
* Capabilities are model-dependent and might differ from the built-in models, for example, support for tool calling, vision, or thinking.
* There is no guarantee that responsible AI filtering is applied to the model's output when using BYOK.

Learn how to [add your own language model key](/docs/agent-customization/language-models.md#bring-your-own-language-model-key) in VS Code.

## Related resources

* [Context](/docs/agents/concepts/context.md)
* [AI language models in VS Code](/docs/agent-customization/language-models.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/sessions.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/sessions
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/sessions.md
- **SHA256_FINGERPRINT**: `9772eeb4d4e59be95a537d900ddbea80dd504666aa9d38469103b4fcbaefb54d`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:54.228509+00:00
---

**MetaDescription**: Understand sessions and chats in VS Code, and choose when to start a chat, fork, or create a session.

# Understand sessions and chats

A session is the unit of work with an agent in Visual Studio Code. It brings together the workspace and code changes for a task. A chat is a conversation within that session, and a session can contain multiple chats when the harness supports them.

This article helps you choose between starting a new chat, forking a conversation, and creating a new session. It explains what chats share, how to finish individual conversations, and how to continue work across surfaces or hand it off to another agent.

To create and organize sessions, see [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md).

## What is a session?

A session contains one or more chats. Each chat records your prompts, the agent's responses, the tool calls it makes, and the [context](/docs/agents/concepts/context.md) it accumulates along the way. Its conversation history contributes to the language model's [context window](/docs/agents/concepts/language-models.md#context-window) and isn't automatically shared with other chats or sessions.

Use a session to organize related conversations, follow their progress, and review their combined results.

The session's [execution environment](/docs/agents/concepts/agent-harnesses.md#relate-execution-environments-and-code-isolation) determines where it works on code. Depending on the harness, a session can use a workspace on your machine or a connected host. It can also work inside a Dev Container in either location. A container changes the development environment, not how the session organizes the conversation and task.

## Chats within a session

A session can contain more than one chat. Each chat is an independent conversation with its own history, title, status, and agent or model selection, but all chats in a session share the same workspace and code isolation. A new chat starts blank and doesn't inherit the conversation history of the other chats in the session.

The session has a main chat. Additional interactive conversations are called **peer chats**. You can prompt each peer chat independently. This differs from a [subagent](/docs/agents/run/subagents.md), which an agent starts to perform delegated work.

Running several chats in one session lets you work on related tasks against the same codebase at the same time without switching sessions. Multiple chats in one session are available with Copilot and Claude. Learn how to [run multiple chats in a session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session).

For example, you're adding a sign-in form. Use one chat to build the form and another chat in the same session to write tests. The test-writing chat can read the implementation files once they're saved, but it doesn't inherit the first chat's conversation. Include requirements such as rejecting an empty email address in the second chat's prompt, rather than relying on your earlier discussion.

Both chats can edit the same files. When you need separate working directories, use separate sessions with [worktree isolation](/docs/agents/run/agents-window.md#choose-where-an-agent-makes-changes), where available.

## Choose a new chat, a fork, or a new session

Continue in the same chat when you're working on the same task and its conversation history is still relevant. When you need a separate conversation, choose based on whether you want to retain that history and share the same workspace.

If the task needs another folder or a new Git worktree, you don't have to start a new conversation. In supported single-chat sessions in the Agents window, you can [move the existing chat](/docs/agents/run/sessions/manage-sessions.md#move-a-chat-to-another-folder-or-worktree) and continue with its conversation history intact.

| Choose | When to use it | Conversation history | Workspace and code changes |
|--------|----------------|----------------------|----------------------------|
| [New chat in the same session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session) | Work on a related task with a fresh conversation, such as writing tests for the feature another chat is implementing. | Starts without the other chats' history. | Shares the session's workspace and worktree. |
| [Fork a conversation](/docs/agents/run/sessions/manage-sessions.md#fork-a-chat-session) | Explore an alternative approach while retaining the requirements and discussion so far. | Inherits the source conversation up to the fork point. The original conversation remains available. | Can share the original session and worktree. Forking doesn't guarantee separate code changes. |
| [New session](/docs/agents/run/sessions/manage-sessions.md#start-an-agent-session) | Start an unrelated task, work in another project, or choose a separate execution environment or worktree. | Starts without the previous chat's history. | Uses the folder or worktree selected for the new session. |

A fork can open as another chat in the same session or as a new session, depending on the harness. Forking a conversation isn't the same as creating a Git branch or a separate worktree. For example, a fork of a Copilot worktree session continues to use the original worktree.

> [!IMPORTANT]
> Separate conversations don't guarantee separate files. If two chats or sessions use the same folder or worktree, their edits affect the same files. Use separate sessions with [worktree isolation](/docs/agents/run/agents-window.md#choose-where-an-agent-makes-changes), where available, when changes must stay separate.

Sessions can run in parallel and keep running when you switch between them. To return an existing conversation and affected workspace files to an earlier point instead of branching the conversation, see [Restore a checkpoint](/docs/agents/run/review-code-edits.md#restore-a-checkpoint).

## Sessions across surfaces

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). Existing sessions are not deleted by this restriction. Contact the IT team that deployed the settings to discuss access.

You can access and continue the same live **Copilot** or **Claude** session in the [Chat view](/docs/agents/run/chat-view.md) and the [Agents window](/docs/agents/run/agents-window.md). To use **Codex** in both interfaces, configure the [experimental Codex integration](/docs/agents/run/agent-harnesses.md#codex). Switching between these interfaces doesn't create a session, fork the conversation, or change its harness, workspace, or worktree.

Both interfaces provide access to the session's main chat and, for harnesses that support them, interactive peer chats. Their navigation and management controls differ. For the steps in each interface, see [Run multiple chats in a session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session).

> [!NOTE]
> **For Local harness sessions:** Use the Chat view in an editor window. These sessions aren't available in the Agents window. Sessions from the OpenAI Codex extension are also editor-only.

VS Code can also discover supported local sessions created in Copilot CLI, the GitHub Copilot app, Claude Code, and Codex. A discovered session is external until you send a message from VS Code. After you send a message, the **External** filter no longer controls whether it appears. Learn how to [view sessions from other applications](/docs/agents/run/sessions/manage-sessions.md#view-sessions-from-other-applications).

With Copilot or Claude, or with Codex through the [experimental integration](/docs/agents/run/agent-harnesses.md#codex), an agent can also coordinate work across sessions. It can list sessions, create new sessions or chats, read another session's recent context, and send follow-up messages between sessions.

## Hand off a session

Handoff continues ongoing work with a different agent configuration and carries the full conversation history and context with it. A handoff can change the [harness](/docs/agents/concepts/agent-harnesses.md), execution environment, or agent role. Use handoff when another configuration is a better fit for the next part of the task.

Common handoffs include:

* **Plan to implementation**: use the [Plan agent](/docs/agents/run/planning.md) to produce a reviewed plan, then hand off to an implementation agent.
* **Continue in the cloud**: in a Copilot harness session, enter `/delegate` to continue a well-scoped task with a [cloud agent](/docs/agents/run/agent-harnesses.md#cloud-target) for remote execution and a pull request workflow.

> [!NOTE]
> **For Local harness sessions:** You can also use the **Session Target** dropdown to hand off an ongoing task to Copilot, Claude, Codex, or Cloud. This dropdown is available only when starting the handoff from a Local harness session. The destination session uses the selected harness's tools, permissions, and models.

Learn how to [hand off an ongoing session](/docs/agents/run/agent-harnesses.md#continue-with-a-different-harness).

## Remote and synced sessions

A session doesn't have to run on your local machine, and it doesn't have to stay on one device:

* **Remote sessions** run on a machine other than the one you work from. You can connect the Agents window to a remote host over SSH or a dev tunnel, or use Copilot remote control (`/remote on`) to monitor and steer a running Copilot harness session from GitHub. Learn more about [connecting to a remote machine](/docs/agents/run/remote-agent-sessions.md) and [remote control for Copilot harness sessions](/docs/agents/run/remote-agent-sessions.md#remote-control-copilot-harness-sessions).
* **Synced sessions** are backed up to your GitHub account so you can access them across devices. Learn more about [syncing sessions](/docs/agents/run/sessions/session-history.md).
* **Session insights** let you query your session history to review what you worked on. Learn more about [session insights](/docs/agents/run/sessions/session-history.md#query-session-history-with-chronicle).

## Close a chat or finish work

Closing, marking done, and deleting serve different purposes:

* **Close a chat tab**: hide the chat from the chat area without deleting its conversation. You can reopen it later.
* **Mark a chat as done**: remove a completed conversation from the active sessions list while retaining its title and history. Restore it when you want to continue.
* **Delete a chat**: permanently remove the conversation. Unlike closing or marking done, deletion can't be undone.

In the Agents window, supported additional chats can be marked as done independently. This doesn't mark the main chat, other chats, or the owning session as done. Main chats, side chats, and subagent chats don't support being marked as done independently.

For the steps and available actions, see [Manage chats within a session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session) and [Mark an individual chat as done](/docs/agents/run/sessions/manage-sessions.md#mark-an-individual-chat-as-done).

## Related resources

* [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md)
* [Agent harnesses](/docs/agents/concepts/agent-harnesses.md)
* [Agents](/docs/agents/concepts/agents.md)
* [VS Code Agent Host architecture](/docs/agents/concepts/agent-host.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/tools.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/tools
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/tools.md
- **SHA256_FINGERPRINT**: `31225c07e679e659bbc03976551fbf197fc26a273988189625f17d8c9b98695f`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:30.337098+00:00
---

**MetaDescription**: Understand how tools let AI agents act in VS Code, including built-in, MCP, and extension tools.

# Understand tools in AI agents

A tool is a capability that lets an [agent](/docs/agents/concepts/agents.md) gather information or take an action. Without tools, a [language model](/docs/agents/concepts/language-models.md) can only generate text. With tools, an agent can read files, edit code, run terminal commands, search your codebase, and connect to external services.

When the agent uses a tool, it makes a **tool call** with the inputs that the tool needs. The tool runs and returns **tool output**, which becomes part of the [context](/docs/agents/concepts/context.md) for the next step in the [agent loop](/docs/agents/concepts/agents.md#agent-loop).

This article explains how tools fit into the agent loop, the types of tools available in VS Code, and how you control their use.

## Tools in the agent loop

For example, when you ask an agent to fix a failing test, it might:

1. Call search and file-reading tools to find the test and related code.
1. Use the returned file contents to decide what to change.
1. Call an editing tool to apply the change.
1. Call the terminal tool to run the test.
1. Use the test output to decide whether the task is complete or another change is needed.

Each call gives the agent new information or changes the development environment. Depending on your [permission level](/docs/agents/run/approvals.md#permission-levels), VS Code might ask you to approve a tool call before it runs.

## Types of tools

VS Code supports three types of tools:

* **Built-in tools**: tools that ship with VS Code for common development tasks, like reading and writing files, running terminal commands, searching your codebase, and navigating the editor. These are available immediately without any setup.
* **MCP tools**: tools provided by [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers, an open standard for connecting AI models to external tools and data sources. MCP servers can run locally on your machine or be hosted remotely. Use MCP tools to connect to databases, APIs, and other external services.
* **Extension tools**: tools contributed by VS Code extensions through the Language Model Tools API. Extension tools integrate deeply with the editor and are available when you install the extension.

## How agents choose tools

By default, the agent chooses from the enabled tools based on your request and the current context. You can give the agent a high-level goal without naming each tool that it should use.

To direct the agent to a specific tool or group of tools, add a `#` reference to your prompt. Learn how to [use tools in a request](/docs/agents/run/tools.md#use-tools-in-a-request).

## Control which tools are available

An available tool comes from VS Code, an MCP server, or an installed extension. An enabled tool is one that the agent is permitted to choose for a request.

Limit enabled tools to the capabilities that are relevant to your task. A focused set helps the agent choose appropriate tools, reduces the chance of unnecessary actions, and limits the tool output added to the [context window](/docs/agents/concepts/language-models.md#context-window).

For Copilot harness sessions, your tool selection persists in the active [user profile](/docs/configure/profiles.md). Tools can also be fixed for a reusable [custom agent](/docs/agent-customization/custom-agents.md). Learn how to [manage available tools](/docs/agents/run/tools.md#manage-available-tools).

> [!NOTE]
> **For Local harness sessions:** The tool selection applies to one chat request rather than persisting across requests.

## Tool approval and trust

Tools can edit files, modify your environment, or access external services. VS Code provides controls for reviewing and limiting these actions:

* **Approval prompts**: based on your permission level, a tool call can require confirmation before it runs.
* **URL approval**: when a tool accesses a URL, a two-step process verifies both the request and the response content.
* **Permission levels**: the [permissions picker](/docs/agents/run/approvals.md#permission-levels) controls how much autonomy the agent has, from requiring manual approval to fully autonomous operation.

Review the tool name and inputs before you approve a call. Learn more about [trust and safety](/docs/agents/concepts/trust-and-safety.md).

## Related resources

* [Use tools with agents](/docs/agents/run/tools.md)
* [Manage approvals and permissions](/docs/agents/run/approvals.md)
* [Add MCP servers](/docs/agent-customization/mcp-servers.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/concepts/trust-and-safety.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/concepts/trust-and-safety
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/concepts/trust-and-safety.md
- **SHA256_FINGERPRINT**: `5e7c19f5ea9ce8f550752b55877589e86b2f83468c9c5525a2ee22b926764957`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:30.574816+00:00
---

**MetaDescription**: Understand approvals, review, sandboxing, and security considerations for AI agents in VS Code.

# Understand trust and safety for AI agents

AI-generated output requires review. Visual Studio Code includes multiple mechanisms to keep you in control of what changes reach your codebase. This article explains the control mechanisms, AI limitations, and security considerations you should be aware of.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Learn more about AI safety">
Understand the control mechanisms and safety considerations for using AI in VS Code.

* [Learn about AI safety](/docs/agents/run/security.md)

</div>

## Stay in control

Agents can read files, edit code, run terminal commands, and call external services. VS Code's trust model layers several control mechanisms so you remain in charge of what reaches your codebase:

* **Review before integrating.** Agents can save edits directly in the session folder or worktree. Inspect the changes in a diff before you commit, merge, or create a pull request. For supported sessions, [checkpoints](/docs/agents/run/review-code-edits.md#edit-requests-and-restore-checkpoints) restore affected workspace files and chat to an earlier point.
* **Approve sensitive actions.** With [Manual permissions](/docs/agents/run/approvals.md#permission-levels) in Copilot harness sessions, actions that aren't covered by your approval settings require confirmation. File edits might be auto-approved. Configure [sensitive-file approval](/docs/agents/run/review-code-edits.md#edit-sensitive-files) when an edit must require confirmation before it is applied.
* **Constrain autonomy.** [Permission levels](/docs/agents/run/approvals.md#permission-levels) decide how much the agent runs on its own, from per-call approvals to broad auto-approval, up to fully autonomous operation with Autopilot.
* **Enforce boundaries at the OS level.** [Agent sandboxing](#agent-sandboxing) restricts file system and network access for terminal commands so auto-approved actions cannot escape a defined scope.
* **Trust boundaries.** VS Code uses trust decisions for workspaces, extensions, MCP servers, and network domains. Workspace MCP servers inherit Workspace Trust.

For step-by-step configuration of these controls — approval rules, sensitive-file protection, sandboxing setup, organization policies — see [AI security in VS Code](/docs/agents/run/security.md).

Always review AI-generated code before committing. Verify that it handles edge cases, follows your project's conventions, and doesn't introduce security issues. Stopping a request or restoring workspace files doesn't reverse completed terminal commands, network requests, deployments, or changes to external services.

## Trust boundaries

VS Code's security model uses trust boundaries to limit the potential impact of untrusted code. Trust must be granted before a boundary is considered trusted. A single trust decision can cover related boundaries, such as a workspace and its MCP server configuration.

* **Workspace**: controls whether VS Code enables features like tasks, debugging, and workspace settings that can execute code from the project. An untrusted workspace runs in [restricted mode](/docs/editing/workspaces/workspace-trust.md), which also disables agents.
* **Extension publisher**: controls whether extensions from a given publisher can be installed and run. VS Code prompts you to [trust the publisher](/docs/configure/extensions/extension-runtime-security.md) before activating their extensions.
* **MCP server**: controls whether an MCP server can start and provide tools. Servers configured in `.vscode/mcp.json` or workspace-root `.mcp.json` inherit Workspace Trust. Servers from other sources can require a [separate MCP server trust decision](/docs/agents/run/manage-mcp-servers.md#mcp-server-trust) and prompt again after configuration changes.
* **Network domain**: controls whether the agent can fetch content from a URL. VS Code prompts you to trust a domain before making requests to it, integrated with the [Trusted Domains](/docs/editing/editingevolved.md#outgoing-link-protection) list. You can also enable ``chat.agent.networkFilter`` to restrict domains for the fetch tool and integrated browser. [Sandbox network controls](/docs/agents/run/agent-sandboxing.md#configure-network-access) apply separately to terminal commands.

You can revoke trust at any time through dedicated commands in the Command Palette. Changing Workspace Trust controls whether workspace MCP servers can run. For servers with a separate trust decision, run **MCP: Reset Trust**. For steps to configure these controls, see [AI security in VS Code](/docs/agents/run/security.md).

## Agent sandboxing

Agent sandboxing uses operating system-level isolation to restrict what terminal commands can access on the machine where they run. Instead of relying solely on approval prompts before each action, sandboxing enforces configured file system and network boundaries.

In Copilot sessions that use the default tools, sandboxing confines shell execution and child processes. It can also sandbox MCP servers and language servers started or managed for the session when the corresponding settings are active. Both settings are active by default. Built-in and other non-process tools remain outside this sandbox and use separate permission checks. Turning on sandboxing does not block outbound network access by default. Learn how to [configure agent sandboxing](/docs/agents/run/agent-sandboxing.md).

Sandboxing and approval are separate controls. A sandbox restricts the resources a process can access, while the session's permission settings determine whether an action requires confirmation.

> [!NOTE]
> **For Local harness sessions:** Sandboxing applies to terminal commands and their child processes. Its approval behavior and configuration differ from the Copilot harness's default tools. See [Local harness sandbox compatibility](/docs/agents/run/agent-sandboxing.md#local-harness-sessions-and-custom-terminal-tools).

### Why sandboxing matters

Approval-based security requires you to confirm each terminal command or tool call before it runs. While this provides control, it has practical limits:

* **Approval fatigue.** Repeatedly approving commands can cause you to pay less attention to what you're approving, especially during long agent sessions.

* **Parsing limitations.** Auto-approval rules use best-effort command parsing, which has known limitations. Shell aliases, quote concatenation, and complex shell syntax can bypass the rules and slip through undetected.

* **Prompt injection.** Malicious content in files, tool outputs, or web pages can attempt to trick the agent into running harmful commands. If you approve without careful review, it might result in unintended actions and security risks.

* **Unintended actions on external services.** Even without malicious intent, an agent with network access can perform actions on your behalf that are difficult to reverse. For example, the agent might provision cloud resources, modify infrastructure settings, push code to a remote repository, or call an API that triggers a deployment or a financial transaction. Blocking outbound connections, or limiting them to required domains where domain filtering is supported, reduces this risk for sandboxed commands.

Sandboxing addresses these challenges by enforcing boundaries at the OS level. The sandbox prevents auto-approved commands from accessing files or network resources outside the permitted scope. If additional permissions are required, VS Code prompts you to run the command outside the sandbox. You can configure VS Code to try the command inside the sandbox before showing that elevation prompt.

### How sandboxing works

Sandboxing enforces two types of isolation:

* **File system isolation** limits read and write access to configured paths. It protects sensitive locations, such as SSH keys and shell configuration, and applies to child processes such as package managers and build scripts.
* **Network isolation** blocks outbound connections or, where supported, limits them to configured domains. Domain-filtering capabilities vary by terminal implementation and platform.

Terminal and child-process boundaries use operating system protections. Other supported operations can use checks inside the process that runs the agent. You can configure file system and network access separately. For default behavior and configuration steps, see [Sandbox agent terminal commands](/docs/agents/run/agent-sandboxing.md).

### OS-level enforcement

Agent sandboxing relies on OS-level security primitives to enforce file system and network restrictions. Because the enforcement happens at the kernel level, sandboxed processes and all of their child processes cannot bypass these boundaries, even if a command is crafted to attempt it.

| Platform | Technology | Prerequisites |
|----------|-----------|---------------|
| macOS | Apple's sandboxing framework ("Seatbelt"), built into the operating system. Enforces fine-grained file system and network restrictions at the kernel level. | None. Works out of the box. |
| Linux and WSL2 | [bubblewrap](https://github.com/containers/bubblewrap) for file system isolation and `socat` for network proxying. | Install required packages: `sudo apt-get install bubblewrap socat` (Debian and Ubuntu) or `sudo dnf install bubblewrap socat` (Fedora). |
| Windows | Microsoft MXC process containers apply file system and network policies to the command process. | Install the applicable Windows security update. |

WSL version 1 is not supported because bubblewrap requires Linux kernel features (user namespaces) that are only available in WSL2.

### What sandboxing does not cover

Agent sandboxing is an added layer for the processes it covers. It is not a virtual machine or user-account boundary, a standalone security boundary, or a replacement for endpoint security. The sandbox does not protect credentials that you explicitly inject. Developer-tool configuration and caches, allowed paths, unrestricted or local network access, unsandboxed fallback, and bypass also weaken its isolation.

Built-in and other non-process tools are not covered by the process sandbox. The agent's read, edit, and write tools use VS Code's permission system directly.

> [!TIP]
> The ``chat.agent.networkFilter`` setting provides network domain filtering for the fetch tool and integrated browser, independently of terminal sandboxing. It does not add domain filtering to Copilot's built-in shell or the Windows terminal sandbox. See [sandbox network capabilities](/docs/agents/run/agent-sandboxing.md#configure-network-access).

Use the [review flow](/docs/agents/run/review-code-edits.md) and [sensitive file protection](/docs/agents/run/review-code-edits.md#edit-sensitive-files) to control these operations.

A [Dev Container session](/docs/agents/run/agents-window.md#run-a-session-in-a-dev-container) runs the agent and its workspace tools inside the project's container, on your machine or a supported connected host. This is different from a Git worktree, which separates code changes, and terminal sandboxing, which restricts command access.

A Dev Container does not automatically block all access to the host or network. Its boundary depends on the container configuration, including mounted host folders, permissions, and networking. Review that configuration and continue to use the applicable approval and security controls.

Agent sandboxing continues to evolve to cover more tools and scenarios.

## AI limitations to watch for

**Incorrect output.** Models can generate code that looks correct but contains bugs, uses deprecated APIs, or doesn't handle edge cases. Always test AI-generated code, especially for logic that affects security, data integrity, or critical flows.

**Prompt injection.** Malicious content in files, tool outputs, or web pages can attempt to redirect the agent's behavior. This is why VS Code includes tool approval gates and trust boundaries. Learn more about [AI security](/docs/agents/run/security.md).

Treat AI-generated output as a first draft: useful as a starting point, but always requiring your review and judgment. For more on how models work, including nondeterminism, knowledge boundaries, and context limits, see [Language models](/docs/agents/concepts/language-models.md).

## Related resources

* [AI security considerations](/docs/agents/run/security.md)
* [Terminal sandbox configuration](/docs/agents/run/agent-sandboxing.md)
* [Reviewing code edits](/docs/agents/run/review-code-edits.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/overview.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/overview
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/overview.md
- **SHA256_FINGERPRINT**: `5426ac4275a7d8f7fa0e490a1afc58b774f4711221df232cb0b9a0bad4c35fcc`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:30.857767+00:00
---

**MetaDescription**: Explore AI in Visual Studio Code, from code suggestions to agents that plan, edit, and test changes.

# Build with AI in VS Code

Use AI in Visual Studio Code to understand unfamiliar code, fix bugs, and build features. For a task that spans files and tools, an agent can find relevant code, make changes, and run checks without you directing each search, edit, and test run. You describe the outcome, review the changes, and verify the result.

Work with an agent in the same workspace as your editor, terminal, tests, and debugger. You can inspect its changes and investigate failures without moving code and command output to a separate chat application. For a question or focused edit, use chat, inline chat, or suggestions without delegating an entire task.

For day-to-day coding and agent tasks, start with the [Copilot harness](/docs/agents/run/agent-harnesses.md#copilot) to explore code, plan changes, implement features, and run tests. The harness uses a shared runtime for core capabilities and more consistent behavior across VS Code, GitHub Copilot CLI, and the GitHub Copilot app. You can continue the same live session in the Chat view or Agents window, and [discover and continue supported sessions created in GitHub Copilot CLI or the GitHub Copilot app](/docs/agents/run/sessions/manage-sessions.md#view-sessions-from-other-applications).

Choose another [agent harness](/docs/agents/concepts/agent-harnesses.md) when you need its tools or workflows, or delegate an independent task to a [cloud agent](/docs/agents/run/agent-harnesses.md#start-a-cloud-session).

<div class="docs-action" data-show-in-doc="true" data-show-in-sidebar="false" title="Try your first agent task">
Build and validate a small app in the Chat view, then review the result.

* [Start the agents quickstart](/docs/agents/quickstart.md)

</div>

If you're new to both VS Code and AI, first [install the editor and open a workspace](/docs/getstarted/overview.md). If you already use agents, skip the sample project and follow the [experienced-agent fast track](/docs/agents/guides/overview.md#experienced-agent-fast-track). For AI help without delegating a task, [choose between suggestions, focused edits, questions, and agents](/docs/agents/reference/ai-features-cheat-sheet.md#choose-a-feature).

The quickstart uses the [GitHub Copilot harness](/docs/agents/run/agent-harnesses.md#copilot). See the [Copilot setup guide](/docs/setup/copilot.md) for account, usage, and data-handling requirements. If provider, sign-in, or execution location affects your setup, [compare agent harnesses](/docs/agents/run/agent-harnesses.md#compare-agent-harnesses) and review their [requirements and setup](/docs/agents/run/agent-harnesses.md#requirements-and-setup).

## What you can do with AI

Choose a workflow based on the task, from help with a single line to a coordinated change across your project.

| Your goal | How AI helps |
|-----------|--------------|
| Implement a feature, fix a bug, or refactor across files | [Work with an agent](#how-you-work-with-an-agent) to find relevant code, make changes, and run tests. |
| Understand a codebase or explore an approach | [Ask questions in chat](/docs/chat/chat-overview.md) to get explanations grounded in your code and discuss alternatives. |
| Research a complex change before editing | [Plan with an agent](/docs/agents/run/planning.md) and review the proposed approach before implementation. |
| Make a focused edit without leaving your code | Use [inline chat](/docs/chat/inline-chat.md) to describe the change in the editor. |
| Get code suggestions while you type | Use [inline suggestions](/docs/editing/ai-powered-suggestions.md) for completions and suggested next edits. |
| Complete a common development task | Use [smart actions](/docs/editing/copilot-smart-actions.md) for tasks such as generating a commit message or explaining selected code. |

You use chat both to ask questions and to direct agents. You can ask **Agent** to propose an approach before editing, or select **Plan**, where available, for a dedicated planning workflow.

For a compact comparison, use the [AI features cheat sheet](/docs/agents/reference/ai-features-cheat-sheet.md#choose-a-feature) to choose the least autonomous option that fits your task.

## How you work with an agent

An agent uses a language model to reason about your request and [tools](/docs/agents/concepts/tools.md) to act on your development environment. It gathers [context](/docs/agents/concepts/context.md), such as code, error messages, and test results, rather than relying only on the words in your prompt.

For example, ask an agent to fix a failing test while preserving the intended behavior:

1. The agent finds the test and reads the related code to understand the failure.
1. It edits the implementation or tests based on the task and your constraints.
1. It runs the tests, inspects the results, and revises its changes if needed.
1. You review the diff and validation results, verify the behavior yourself, and decide which changes to keep.

This repeated reasoning, action, and validation is the **agent loop**. You can provide more context, redirect the work, or stop the agent along the way. Learn more about [how agents work](/docs/agents/concepts/agents.md).

The conversation and work for a task belong to a **session**. Sessions keep related context and changes together so you can return to a task or manage independent tasks separately. Learn about [sessions and handoff](/docs/agents/concepts/sessions.md).

## Ways to work with agents

Both the Chat view and the Agents window support agent workflows. Choose the Chat view for collaboration over code in your current workspace, or the Agents window for multi-project orchestration and higher-level task assignment. You can continue supported sessions between them rather than choosing one interface for every task.

For a path from your first request through planning, steering, review, and recovery, see [Run agents in VS Code](/docs/agents/run/overview.md).

### Work alongside your code

Use the [Chat view](/docs/agents/run/chat-view.md) when you're working in an open project. Keep the conversation beside your editor, inspect changes as they happen, and use the debugger, terminal, and tests as part of the same workflow. This is the starting point for the agents quickstart.

![Screenshot showing the Chat view with the sessions list, conversation, and chat input.](images/agents-overview/chat-view-expanded.png)

For keyboard, screen reader, and low-vision workflows, learn how to use the [Accessible View and other accessibility features](/docs/configure/accessibility/accessibility.md#accessible-view).

### Delegate and manage tasks

Use the [Agents window](/docs/agents/run/agents-window.md) when your focus is assigning tasks and reviewing their results. Manage multiple sessions across projects, follow their progress, and open the editor when you want to work directly with the code.

![Screenshot showing how to start a new agent session by selecting New at the top of the sidebar in the Agents window.](images/agents-overview/agents-window-hero.png)

### Other ways to access agents

For terminal-based work, use [GitHub Copilot CLI](/docs/agents/run/sessions/manage-sessions.md#use-copilot-cli-from-the-terminal). The [GitHub Copilot app](https://github.com/features/copilot) provides a dedicated desktop experience. You can [open and continue supported local sessions created in either application](/docs/agents/run/sessions/manage-sessions.md#view-sessions-from-other-applications) in VS Code. To continue a Copilot session in the CLI, right-click the session and select **Resume in Terminal**.

For work away from your machine, explore [cloud agents that return pull requests](/docs/agents/run/agent-harnesses.md#start-a-cloud-session) or [remote sessions and browser access](/docs/agents/run/remote-agent-sessions.md).

## Choose your models, agents, and tools

Start with the quickstart's recommended setup, then adjust individual choices to fit your task and project:

* **Models**: choose a [language model](/docs/agents/concepts/language-models.md) based on the reasoning capabilities, speed, and cost your task requires.
* **Agent harnesses**: use a supported [agent harness](/docs/agents/run/agent-harnesses.md), such as Copilot, [product.prodname_anthropic_claude], or [product.prodname_openai_codex], for its tools and workflows. The harness connects a model to tools and manages the session, so changing harnesses is different from switching models.
* **Model access**: use models from your GitHub Copilot plan, [bring your own API key (BYOK)](/docs/agent-customization/language-models.md#bring-your-own-language-model-key), or connect a supported local model. These options let you use an existing model provider account or keep model processing local.
* **Tools and customization**: share your coding standards and test commands through [project instructions](/docs/agents/guides/customize-copilot-guide.md). Connect external systems through [Model Context Protocol (MCP) servers](/docs/agent-customization/mcp-servers.md), package recurring tasks as [agent skills](/docs/agent-customization/agent-skills.md), or install [plugins](/docs/agent-customization/agent-plugins.md) that bundle tools and workflows. Compare the options in [agent customization concepts](/docs/agents/concepts/customization.md).

Available models, tools, and customizations depend on the selected harness, your account, and your organization's policies.

Where tools run and where the model is hosted are separate choices. An agent can edit files on your machine while sending model requests to a hosted provider.

## Stay in control

AI can produce incorrect code or misunderstand your intent. You remain responsible for deciding which changes reach your codebase.

* **Review before integrating.** Agents can save edits directly to the session folder or worktree. [Review the diff and validate the result](/docs/agents/run/review-code-edits.md) before you commit or merge changes.
* **Control actions and redirect work.** Use [permissions and approvals](/docs/agents/run/approvals.md) to decide which actions require confirmation. You can [steer or stop a request](/docs/chat/chat-overview.md#send-messages-while-a-request-is-running), but stopping doesn't undo completed actions or changes to external services.
* **Understand isolation.** A Git worktree keeps code changes separate, but isn't a security boundary. For file system and network restrictions on agent-run terminal commands, review the [platform-specific sandboxing options](/docs/agents/run/agent-sandboxing.md).

Before using agents on an existing project, review the [recommended security baseline](/docs/agents/run/security.md#recommended-security-baseline). On a managed device, your organization might restrict available agents, models, and tools through [enterprise AI policies](/docs/enterprise/manage-ai-settings.md). If agents don't appear in chat, review the [availability troubleshooting steps](/docs/agents/agent-troubleshooting/faq.md#agents-are-not-available-in-chat).

## Next steps

* **New to VS Code and AI:** [Install the editor, open a workspace, and choose a first task](/docs/getstarted/overview.md).
* **Already use VS Code, but new to agents:** [Complete a first agent task](/docs/agents/quickstart.md) with a recommended starting configuration.
* **Already use AI agents:** Follow the [experienced-agent fast track](/docs/agents/guides/overview.md#experienced-agent-fast-track) to work in your own repository.
* **Prefer lighter-weight AI:** [Choose an AI feature](/docs/agents/reference/ai-features-cheat-sheet.md#choose-a-feature) for suggestions, focused edits, questions, or delegated work.
* **Ready to improve a project workflow:** [Adapt agents to your project](/docs/agents/guides/customize-copilot-guide.md), then [compare quality, reliability, and usage](/docs/agents/guides/optimize-usage.md).


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/run/agent-harnesses.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/run/agent-harnesses
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/run/agent-harnesses.md
- **SHA256_FINGERPRINT**: `c78d91f27d721b2d89615c7055bc849e79b82a1c94ee98d64bb9aee90d98a4a3`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:55.365197+00:00
---

**MetaDescription**: Compare agent harnesses and built-in agents in Visual Studio Code, select one for a session, and review provider requirements.

# Choose an agent harness

VS Code supports multiple agent harnesses, each with its own tools, customizations, and workflows. An agent harness coordinates the language model, context, and tools that an agent uses to complete your task.

Use this guide to compare the available options, identify which harness your session uses, select a harness or the Cloud execution target, and review its setup requirements.

For a deeper explanation of how harnesses work and differ from models and hosts, [learn about agent harness concepts](/docs/agents/concepts/agent-harnesses.md).

## Compare agent harnesses

Start with the Copilot harness for day-to-day coding and agent tasks. Choose another harness or the Cloud target when you need different tools, customizations, or execution workflows.

| Harness | What runs | What this means for your work |
|----------------|-----------|-------------------------------|
| **Copilot** | Run tasks using the [copilot.copilot_sdk_short], which provides the shared agent experience across GitHub Copilot products. The agent works in the [Agent Host](/docs/agents/concepts/agent-host.md#session-lifetime-and-client-dependencies). | Sessions run independently of the editor window and can continue in the background after you close it, while the Agent Host stays running. You can also continue sessions across supported interfaces. See [Copilot requirements and limitations](#copilot). |
| **Local** | Run tasks within VS Code's built-in agent harness. The agent works in VS Code's [extension host](/docs/agents/concepts/agent-host.md#local-and-existing-extension-host-sessions). | The agent iterates via chat and works interactively to implement changes in your current workspace. The session is tied to the editor window: closing that window stops the agent's ongoing work. See [Local requirements](#local). |
| **Claude** | The [product.prodname_anthropic_claude] Agent SDK is integrated into VS Code. | Sessions use Claude project configuration and provider workflows in your current workspace or an isolated worktree. See [Claude requirements](#claude). |
| **Codex** | [product.prodname_openai_codex] runs through the [product.prodname_openai_codex] extension or the experimental Agent Host integration. | Sessions support interactive or background coding. Available interfaces depend on the integration. See [Codex requirements](#codex). |
| **Cloud** | An available provider harness runs on provider-managed remote infrastructure. Cloud is an execution target, not a single harness. | The selected provider works against a GitHub repository and returns a pull request. The session does not use local editor context. See [Cloud target requirements](#cloud-target). |

For Agent Host sessions managed by desktop VS Code on your machine, keep the application running. Closing an editor window is different from quitting the application. Tools provided by a window also require that window to stay connected.

Changing the model or agent role does not change the harness. For example, selecting a Claude model in a Copilot harness session still uses the Copilot harness. Opening the same session in another supported interface also keeps its harness.

**Local** is a harness name, not a synonym for running on your machine. The Copilot, Claude, and Codex harnesses can also run on your machine.

Available models depend on the harness and how you [access models](/docs/agent-customization/language-models.md), such as through a GitHub Copilot subscription, another supported account, or your own API key. Harness-specific customizations, including [hooks](/docs/agent-customization/hooks.md#choose-the-hook-implementation-for-your-session), follow the selected harness.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), including managed permission or sandbox settings. Contact the IT team that deployed the settings to discuss access. If you don't know the owner, ask your IT help desk to find the responsible administrator.

## Select a harness

Select a harness before you submit the first prompt for a session:

1. [Open the Chat view](/docs/agents/run/chat-view.md) or [open the Agents window](/docs/agents/run/agents-window.md).

1. Select **New Chat** (`+`) in the Chat view, or select **New** in the Agents window.

1. In the Agents window, select the folder or GitHub repository for the session.

1. Open the **Session Target** UI control and select an available harness or the Cloud target.

    ![Screenshot showing the Session Target UI control in the Agents window.](../images/agent-harnesses/agents-window-session-target.png)

The control only lists targets whose [requirements](#requirements-and-setup) are met in the current window.

### Choose a built-in agent

After selecting a harness, choose an available built-in agent from the agent picker. The available built-in agents depend on the harness:

| Harness | Built-in agents |
|---------|----------------|
| **Copilot** | <ul><li>**Ask** answers questions and researches your codebase without making changes. It only uses read-only tools and can't edit files or run state-changing commands.</li><li>**Agent** implements changes and validates the result.</li><li>**[Plan](/docs/agents/run/planning.md)** researches a task and creates an implementation plan for you to review. Invoke it with `/plan`.</li></ul> |
| **Local** | <ul><li>**Ask** answers questions without changing your code.</li><li>**Agent** implements changes and validates the result.</li><li>**Plan** researches a task and creates an implementation plan for you to review.</li></ul> |

Switching agents doesn't change the harness. You can also select [custom agents](/docs/agent-customization/custom-agents.md) from the same picker. In the Copilot harness, [Autopilot](/docs/agents/run/approvals.md#how-autopilot-works) is a mode with its own workflow, not an additional built-in agent.

Your harness choice is separate from where the session changes code. In the Agents window, you can also [choose between a folder and a worktree](/docs/agents/run/agents-window.md#choose-where-an-agent-makes-changes) or [run a session in a Dev Container](/docs/agents/run/agents-window.md#run-a-session-in-a-dev-container).

### Identify your current harness

To identify the current harness for a chat session, use one of the following methods:

* In the editor window, the active harness is shown as a prefix in the chat title.

* In the Agents window, the chat input box shows the active harness as the watermark.

* In the Agents window, hover over the session entry in the sessions list to see a tooltip showing the harness.

## Requirements and setup

Check the accounts, extensions, and settings needed for your chosen harness or the Cloud target. If a choice does not appear in the **Session Target** UI control, start with its requirements below.

### Copilot

For GitHub sign-in and account requirements, follow the [Copilot setup guide](/docs/setup/copilot.md). Copilot harness sessions use the same GitHub authentication context as chat in VS Code, including your GitHub Enterprise account when configured.

For managed user accounts on GHE.com, complete the setup in [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).

Before reusing a Local harness session's configuration, check [tool availability](/docs/agents/run/tools.md#manage-tool-availability-for-the-copilot-harness) and [MCP configuration compatibility](/docs/agents/reference/mcp-configuration.md#configuration-file). Copilot harness sessions don't have access to every built-in or extension-provided tool. The shared SDK runtime also does not imply identical tools, models, permissions, or customizations across products, or that all sessions and personal settings synchronize.

For enterprise SDK Policy Hooks requirements, see [enterprise hook configuration](/docs/enterprise/manage-ai-settings.md#enable-or-disable-hooks).

### Local

Local harness sessions use the models configured in VS Code. [Set up GitHub Copilot](/docs/setup/copilot.md) to use Copilot-provided models, or [configure your own model credentials](/docs/agent-customization/language-models.md#bring-your-own-language-model-key) for a supported model.

Select **Local** in the Chat view and keep the editor window open while the agent works. Local harness sessions use different [customization settings](/docs/agent-customization/custom-instructions.md) from Copilot harness sessions.

SDK Policy Hooks are not loaded in Local harness sessions. Check [hook compatibility](/docs/agent-customization/hooks.md#migrate-hooks-between-harnesses) before reusing hooks from another harness.

### Claude

Claude support is enabled by default unless [enterprise-managed settings disable the harness](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). When organization policy permits it, turn support on or off with ``github.copilot.chat.claudeAgent.enabled``.

To use Claude, configure one of these authentication and billing options:

* **GitHub Copilot subscription**: sign in to GitHub to use Copilot-routed models. Usage is billed through your Copilot subscription.
* **Bring your own key (BYOK)**: use a Claude API key or another supported Claude BYOK option. Usage is billed by your configured provider.

When both options are available, the model picker groups models by **Anthropic** and **Copilot**. The model you select determines the provider and billing method for the next turn. You can switch between BYOK-backed and Copilot-routed models in an existing Claude harness session.

To use Claude without signing in to GitHub _(Experimental)_, configure a Claude API key or another supported Claude BYOK option. For an Anthropic API key, set `ANTHROPIC_API_KEY` in your environment or in the `env` object in `~/.claude/settings.json`. Learn more about [Claude Code authentication](https://code.claude.com/docs/en/authentication).

Enable ``chat.agentHost.allowSignedOutWhenUsable`` to open the Agents window while signed out of GitHub. The model picker only shows models from your Claude BYOK configuration until you sign in. After you sign in to GitHub, Copilot-routed models are also available.

See [Claude permission modes](/docs/agents/run/approvals.md#claude-permission-modes) for approval behavior and related cautions.

### Codex

Codex is not listed by default. Choose one of the following integrations. You don't need both.

#### Extension-based integration

To use Codex in the Chat view, install and enable the [OpenAI Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt). Follow the extension's documentation for authentication and permissions.

#### Agent Host integration (Experimental)

> [!NOTE]
> The Codex Agent Host integration is disabled when [enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), even with a ChatGPT account or the integration's user setting set to `true`. Contact the IT team that deployed the settings to discuss access.

Enable ``chat.agentHost.codexAgent.enabled`` to make Codex available in the Agents window without the [product.prodname_openai_codex] extension.

To also use this integration in the Chat view, enable ``chat.editor.codex.preferAgentHost`` and restart VS Code when prompted. Only one Codex implementation appears in each window. In the **Session Target** UI control, this setting replaces the **Codex** choice contributed by the OpenAI extension.

Sign in with one of these accounts for the Agent Host integration:

* **GitHub Copilot subscription**: sign in to GitHub to use Copilot-backed models. This option requires [copilot.copilot_pro_plus_short].
* **ChatGPT subscription**: open the account menu and select **Sign in to ChatGPT**. A free ChatGPT account is sufficient.

When both accounts are signed in, the model picker groups models by **Copilot** and **ChatGPT**. Your selection determines which subscription is used, and VS Code saves that provider with the session.

To use Codex without signing in to GitHub _(Experimental)_, sign in to ChatGPT and enable ``chat.agentHost.allowSignedOutWhenUsable``. The desktop Agents window then shows ChatGPT-backed models while signed out. Copilot-backed models prompt you to sign in to GitHub, and the browser-based Agents window still requires GitHub sign-in.

See [Codex approval presets](/docs/agents/run/approvals.md#codex-approval-presets) for approval behavior and related cautions.

### Cloud target

Cloud sessions require a GitHub repository and access to an available cloud provider. VS Code supports the Copilot cloud agent and Claude and Codex cloud agents (Preview).

To use Claude or Codex in the cloud, turn on support in your Copilot account settings. See [Managing policies for third-party Copilot cloud agents](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies#enabling-or-disabling-third-party-coding-agents-in-your-repositories). You don't need the provider's VS Code extension for a cloud session.

Select **Cloud** from the **Session Target** UI control, then choose the cloud provider and, when available, a custom agent and model. In the Agents window, select a GitHub repository when you [start the session](/docs/agents/run/agents-window.md#start-an-agent-session).

Configure tools, MCP servers, and models in the cloud service. Cloud sessions can't use VS Code built-in tools or local development context.

## Continue with a different harness

A handoff continues an ongoing task with a different harness or execution environment and carries the conversation history and context with it. The tools, permissions, and models might change because the new configuration provides different capabilities.

In a Copilot harness session, enter `/delegate` to continue a well-scoped task with a cloud agent.

### Hand off from a Local harness session

From a Local harness session, you can select another harness or Cloud after work starts. Sessions that use the Copilot or Claude harness, and sessions that use the [experimental Codex integration](#codex), can receive these handoffs but do not show a **Session Target** dropdown after the session starts.

To hand off a Local harness session:

1. Open the session.

1. In the chat input, open the **Session Target** dropdown.

1. Select Copilot, Claude, Codex, or Cloud to continue the work.

VS Code carries the conversation history and context to the destination session. To implement a plan or continue it with another supported session, see [planning with agents](/docs/agents/run/planning.md).

> [!NOTE]
> Enterprise-managed sandbox or permission settings might automatically move a Local session to the Copilot harness so the Agent Host can enforce the policy. This policy-driven move preserves the conversation history and unsent input without submitting a prompt, and archives the original Local session as read-only. It is different from a user-initiated handoff. Learn more about [Agent Host policy enforcement](/docs/enterprise/manage-ai-settings.md#enforce-runtime-policies-with-copilot-agent-host).

Changing a harness is different from starting another conversation or opening the same session in another interface. Learn more about [sessions, forks, and handoffs](/docs/agents/concepts/sessions.md).

## Use canvases with the Copilot harness

`feature(canvases)`

Canvases are interactive visual surfaces shared by you and the agent. For example, you can inspect a diagram that the agent updates or adjust controls whose values flow back to the agent. Every canvas is provided by a canvas extension.

![Screenshot of a kanban canvas showing tasks and columns in the editor.](../images/agent-harnesses/kanban-canvas.png)

Before you create a new supported Copilot session, turn on ``chat.canvases.enabled``. To get a canvas, use one of these options:

* **Create a canvas extension**: When the `/create-canvas` skill is available, enter `/create-canvas` in the chat input and describe the user interface you want for your project. The skill creates a canvas extension in your workspace and opens its canvas.

* **Install a chat plugin**: In the GitHub Copilot app, install a chat plugin that includes a canvas extension. Switch to VS Code and ask the agent in chat to list the available canvases and have it open one.

To open an available canvas without asking the agent, use one of these menus:

* In the editor window, select **New Chat (+)** > **Canvas** in the Chat view.
* In the Agents window, select **Add Tab (+)** > **Canvas** in the editor area.

In the editor window, the **Canvas** submenu appears after your first message in a supported Copilot harness session, when canvas support is enabled and canvas extensions are installed.

Whether you or the agent opens a canvas, it appears in an editor tab and remains associated with its owning chat. You can interact with the canvas directly. Depending on the extension, your interactions can update the session, and the agent can invoke actions exposed by the canvas to inspect or update its state. You can close and reopen a live canvas when the canvas supports it.

Canvas extensions are also supported in the GitHub Copilot app. Learn how to [work with canvas extensions in the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-canvas-extensions). To explore examples, browse [sample canvas extensions](https://awesome-copilot.github.com/extensions/).

> [!NOTE]
> Canvases are available only on desktop in supported local Copilot Agent Host sessions. They aren't supported for Claude, Codex, extension-host Local sessions, remote Agent Host sessions, browser or web clients, or auxiliary-window hosting.

## Frequently asked questions

### What is the difference between Local and Copilot?

Both harnesses can run on your machine. **Local** uses VS Code's built-in proprietary agent harness and works in VS Code's extension host. **Copilot** uses the [copilot.copilot_sdk], which is the agent experience shared consistently across GitHub Copilot products.

Both harnesses support tools, model selection, and agent customizations, but the available capabilities and configuration differ.

The Copilot harness provides these benefits:

* **A shared runtime across Copilot products**: core capabilities and behavior are more consistent across VS Code, GitHub Copilot CLI, and the GitHub Copilot app.

* **Continuity between interfaces and machines**: you can continue the same live session in the Chat view, the Agents window, and other GitHub Copilot interfaces. You can also [connect remotely from another machine](/docs/agents/run/remote-agent-sessions.md) while the session continues to run on its host. Local sessions are available only in the editor's Chat view.

* **Work independent of an editor window**: ongoing work can continue after you close the editor window, while the Agent Host remains running. Closing a Local harness session's editor window stops its ongoing work.

### Which harness should I choose?

Start with **Copilot** for day-to-day coding and agent tasks, especially when you want to continue work between the Chat view and Agents window, or keep work running after closing an editor window.

If your workflow depends on specific tools or customizations that aren't supported by the Copilot harness, please [let us know](https://github.com/microsoft/vscode/issues). Before moving an existing workflow, check [tool availability](/docs/agents/run/tools.md#manage-tool-availability-for-the-copilot-harness), [MCP configuration compatibility](/docs/agents/reference/mcp-configuration.md#configuration-file), and [hook compatibility](/docs/agent-customization/hooks.md#migrate-hooks-between-harnesses).

### Does running locally mean the language model runs on my machine?

No. The harness coordinates the session and its tools, but the language model can run elsewhere. A session that edits files and runs commands on your machine can still send model requests to a hosted service. The **Local** harness name does not mean that the model runs locally or that the session works offline. Learn how [harnesses differ from models and execution environments](/docs/agents/concepts/agent-harnesses.md#how-a-harness-differs-from-other-agent-concepts).

### Does selecting a different model change the harness?

No. Selecting a model changes the model used within the current harness. For example, selecting a Claude model in a Copilot session does not switch to the Claude harness. Changing the agent role, such as Ask or Agent, also does not change the harness. To check which harness you are using, see [Identify your current harness](#identify-your-current-harness).

### Can I continue an existing Local session with Copilot?

Yes. In the Local session's chat input, open the **Session Target** dropdown and select **Copilot**. The handoff carries the conversation history and context to the destination session, but the available tools, permissions, and models might change. See [Hand off from a Local harness session](#hand-off-from-a-local-session).

## Related resources

* [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md), including [continuing in the terminal](/docs/agents/run/sessions/manage-sessions.md#use-copilot-cli-from-the-terminal).
* [Remote control for Copilot harness sessions](/docs/agents/run/remote-agent-sessions.md#remote-control-copilot-harness-sessions)
* [Approvals and permissions](/docs/agents/run/approvals.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/setup/copilot.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/setup/copilot
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/setup/copilot.md
- **SHA256_FINGERPRINT**: `6dda2b1666d2dbc20b3540065239da18b939efc7fcd39908b5b991dc3cb5f8da`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:56.276107+00:00
---

**MetaDescription**: Set up GitHub Copilot in VS Code, understand billing and data use, and manage your account.

# Set up GitHub Copilot in VS Code

This guide walks you through setting up GitHub Copilot in Visual Studio Code. To use Copilot in VS Code, you need access to GitHub Copilot with your GitHub account.

This article covers the GitHub Copilot setup path. To use Claude, Codex, or your own model credentials for supported agent workflows, compare the [agent harness authentication and billing options](/docs/agents/run/agent-harnesses.md#requirements-and-setup). Some agent workflows without GitHub sign-in are experimental.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with AI">
Complete your first coding task with an AI agent in VS Code.

* [Start quickstart](/docs/agents/quickstart.md)

</div>

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), even with separate provider credentials. Contact the IT team that deployed the settings to discuss access.

## Before you start

Review these account, usage, and data-handling details before you send project content to an AI model:

* **Account access**: the recommended setup uses a GitHub account with a Copilot plan. If your employer provides Copilot, use the account and policies for your organization. Without a plan, signing in enrolls an eligible account in Copilot Free.
* **Usage and billing**: models included with Copilot consume AI credits from your Copilot plan. If you use a Claude bring-your-own-key (BYOK) configuration, a ChatGPT subscription, or your own model credentials, that provider manages usage and billing instead. Compare the [authentication and billing options for each agent harness](/docs/agents/run/agent-harnesses.md#requirements-and-setup).
* **Monitor usage**: open the Copilot status dashboard from the VS Code Status Bar to view the percentage of your monthly allowance that you used. Learn [how to monitor usage and what happens when you reach a limit](/docs/agents/agent-troubleshooting/faq.md#how-can-i-monitor-my-copilot-usage).
* **Data handling**: review the [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center/) and your organization's policies before you send work code. Models that use third-party credentials or your own API key follow that provider's terms. VS Code [telemetry settings](/docs/configure/telemetry.md) are separate from AI-provider data handling.

To use chat with your own model instead, [bring your own language model key](/docs/agent-customization/language-models.md#bring-your-own-language-model-key). This path doesn't require a Copilot plan, but some features, including inline suggestions, semantic search, and embeddings, still require the GitHub Copilot service.

## Set up GitHub Copilot

Follow these steps to get started with Copilot in VS Code:

1. Hover over the Copilot icon in the Status Bar and select **Use AI Features**.

1. Choose a sign-in method and follow the prompts.

    * If you already have a Copilot subscription for your account, VS Code will use that subscription.

    * If you don't have a Copilot subscription yet, you'll be signed up for the [Copilot Free plan](https://github.com/github-copilot/signup) and get a monthly allowance of inline suggestions and AI credits. Learn more about the different [GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans).

1. Start using Copilot in VS Code!

    Learn the basics with the [agents quickstart](/docs/agents/quickstart.md).

> [!IMPORTANT]
> Telemetry in your free version of GitHub Copilot is currently enabled. By default, code suggestions that match public code, including code references in the VS Code and [github.com](http://github.com/copilot) experience, are allowed. You can opt out of telemetry data collection by disabling telemetry in VS Code by setting ``telemetry.telemetryLevel`` to `off`, or you can adjust both telemetry and code suggestion settings in [Copilot Settings](https://github.com/settings/copilot).

## Prepare a project for AI (optional)

After you sign in, enter `/init` in a chat session to create starter [custom instructions](/docs/agent-customization/custom-instructions.md) for a project. The command analyzes the codebase and records coding practices that help AI-generated code match the project.

## Use Copilot with a GHE account

If your Copilot subscription is associated with a GitHub Enterprise (GHE) account, you can sign in to Copilot in VS Code with your GHE credentials.

1. If you haven't already, hover over the Copilot icon in the Status Bar and select **Use AI Features**.

1. In the sign in dialog, choose **Continue with GHE.com** and provide your GHE instance URL and credentials.

If you need to switch between a GitHub.com account and a GHE account, see [Use a different GitHub account per workspace or profile](#use-a-different-github-account-per-workspace-or-profile) for instructions.

## Use a different GitHub account with Copilot

If your Copilot subscription is associated with another GitHub account, follow these steps to sign out of your GitHub account in VS Code, and sign in with another account.

1. Select the **Accounts** menu in the Activity Bar, and then select **Sign out** for the account you're currently signed in with.

    ![Accounts menu in VS Code, showing the option to sign out of the current GitHub account.](images/copilot/vscode-accounts-menu-signout.png)

1. Sign in to your GitHub account using any of the following methods:

    * Select **Sign in to use Copilot** from the Copilot menu in the Status Bar.

        ![Sign in to use Copilot from the Copilot status menu.](images/copilot/copilot-signedout-sign-in.png)

    * Select the **Accounts** menu in the Activity Bar, and then select **Sign in with GitHub to use GitHub Copilot**.

        ![Accounts menu in VS Code, showing the option to sign in with GitHub to use GitHub Copilot.](images/copilot/vscode-accounts-menu.png)

    * Run the **GitHub Copilot: Sign in** command in the Command Palette (``Shortcut: workbench.action.showCommands``).

## Use a different GitHub account per workspace or profile

You can use different GitHub accounts for Copilot per VS Code workspace or profile. This is useful if you use Copilot with different accounts for work and personal projects, or if you want to use different accounts for different extensions that use GitHub authentication.

Follow these steps to configure which GitHub account to use for Copilot. This configuration is saved per workspace and per profile.

* For GitHub.com accounts:

    1. In the Accounts menu in the Activity Bar, select **Manage Extension Account Preferences**
    1. Select **GitHub Copilot Chat** from the list of extensions
    1. Choose the GitHub account you want to use for Copilot in the current workspace and profile

* For GHE.com accounts:

    > [!TIP]
    > If you only want to use a GHE account for Copilot, follow the steps in [Use Copilot with a GHE account](#use-copilot-with-a-ghe-account) to sign in with your GHE account.

    1. Run **Preferences: Open User Settings (JSON)** or **Preferences: Open Workspace Settings (JSON)** from the Command Palette (``Shortcut: workbench.action.showCommands``)

    1. Add the following setting to specify GitHub Enterprise as the authentication provider for Copilot:

        ```json
        "github.copilot.advanced": {
            "authProvider": "github-enterprise"
        }
        ```

    1. Re-sign in to your GitHub Enterprise account if you're not already signed in

## Remove AI features from VS Code

You can disable the built-in AI features in VS Code with the ``chat.disableAIFeatures`` setting, similar to how you configure other features in VS Code. This disables and hides features like chat or inline suggestions in VS Code and disables the Copilot extensions. You can configure the setting at the workspace or user level.

Alternatively, use the **Learn How to Hide AI Features** action from the Chat menu in the title bar to access the setting.

> [!NOTE]
> If you have previously disabled the built-in AI features, your choice is respected upon updating to a new version of VS Code.

## Disable AI features for a workspace

To disable AI features for a specific workspace, configure the ``chat.disableAIFeatures`` setting in workspace settings. This setting is available in the Settings editor (``Shortcut: workbench.action.openSettings``), or you can edit the `settings.json` file in the workspace.

## Next steps

* Continue with the [Quickstart for using AI](/docs/agents/quickstart.md) to discover the key features for AI-powered development in VS Code.


---
# DOCUMENT_SOURCE: microsoft_vscode::src/vs/workbench/contrib/chat/chatCodeOrganization.md
- **CANONICAL_URL**: https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/chatCodeOrganization.md
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/chat/chatCodeOrganization.md
- **SHA256_FINGERPRINT**: `186cf7f9de22d11facc1a4975f2ef9fb646b4147019a84b6f275776985b337fd`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:54:43.412272+00:00
---

# workbench/contrib/chat Code Organization

This contrib is, as of the end of 2025, the largest workbench contrib in VS Code by a substantial margin. Let's try to keep it organized! Here's a rough description of some of the key folders.

## Agents titlebar experiments

The desktop editor titlebar action reads the string treatment `chatOpenInAgentsTitleBarLabel` for users who have not created a session in the Agents Window. It replaces the expanding hover/focus label, tooltip, and accessible name; without a valid non-empty string, the existing localized copy is retained. Other commands and menus keep their existing labels.

Eligibility reads `AgentsWindowUsage.createdSessionCount`. The helper wraps the existing application-scoped `AGENTS_WINDOW_TOTAL_SESSIONS_STORAGE_KEY` counter (`agentSessions.telemetry.totalSessions`), defaults missing values to zero, and provides change notifications without callers needing the storage key or scope. No additional usage state is stored. When the count becomes positive, the action restores its default copy.

Onboarding tours, new-session composer tips and first-run notices, Agents Window launch handling, and lifecycle telemetry also read this count through the helper. The lifecycle tracker remains responsible for incrementing the existing counter when a new session starts.

For local testing, set `"experiments.override.chatOpenInAgentsTitleBarLabel": "Try Agents"` in user settings with a fresh profile/data directory. Assignments are refreshed through the assignment service. A triggered scorecard can use `monacoworkbench/experimentTrigger` with `treatmentName == "chatOpenInAgentsTitleBarLabel"`; eligible rendered actions log the trigger in both control and treatment.

The boolean treatment `chatOpenInAgentsTitleBarExpandOnHover` applies to all users, independently of the copy experiment. It defaults to `true`; `false` keeps the action icon-only on pointer hover, while keyboard focus still reveals the label. Tooltips, accessible names, and action behavior remain available. Set `"experiments.override.chatOpenInAgentsTitleBarExpandOnHover": false` to test locally. Its `experimentTrigger` fires on pointer hover in both arms after the assignment resolves.

## Key Folders

### `browser/`

- `accessibility/` - Screen reader support and accessible views.
- `actions/` - All chat action registrations.
- `attachments/` - Context attachment model, pickers, context widgets.
- `chatContentParts/` - Rendering components for different response content types (markdown, code blocks, tool output, etc.).
- `chatEditing/` - The edit session model, edit diff UI, edit snapshots.
- `chatSetup/` - Placeholder registrations before the chat extentension is set up. Running the chat auth/install flow.
- `contextContrib/` - The contribution point for chat context providers - note the difference from `attachments/`.
- `widget/` - The core files related to rendering parts of the ChatWidget, including the list, the input, the model/agent pickers, and other main UI parts. Must have direct references from ChatWidget itself.
- `widgetHosts/` - Hosts that embed chat widgets in other places (view pane, editor, quick chat).

### `common/`

- `chatService/` - IChatService interface, implementation, and related code.
- `model/` - Chat data model, view model, and session storage.
- `participants/` - Chat participant management (sometimes called "agents" in code).
- `tools/` - Language model tools infrastructure and services.
	- `builtinTools/` - Implementations of some built-in tools.

## Markdown file images

Response Markdown targets are resolved by the owning session content provider before rendering. Agent Host paths retain their connection identity in `vscode-agent-host:` URIs; relative image paths use the session or chat's advertised working directory. Recorded cloud history preserves this identity without requiring a live connection.

For Agent Host resources, chat permits parsed Markdown images only when they resolve to eligible local files on the owning connection. HTTP(S), network-file paths, and other connections remain disallowed before media sources are activated. Image eligibility is separate from byte delivery: the normal Markdown renderer uses `FileAccess` and the shared `IBrowserResourceService`, which reads through `IFileService`. Desktop and web embedders with a resource handler serve window-issued resource URLs; web hosts without a handler use render-scoped object URLs. The resource bridge does not connect to or resume a sandbox.


---
# DOCUMENT_SOURCE: microsoft_vscode::src/vs/workbench/contrib/chat/common/chatService/telemetry.md
- **CANONICAL_URL**: https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/chatService/telemetry.md
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/chat/common/chatService/telemetry.md
- **SHA256_FINGERPRINT**: `a4a618ac686422056d8c1a4b98d213e804c9963c08b1ccf8d3ece84586106ead`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:54:43.411115+00:00
---

# Request outcome context

`interactiveSessionProviderInvoked` reports workbench provider-invocation outcomes.
Its existing `result`, IDs, `model`, and once-per-invocation emission are unchanged.
It is not a model-attempt event or proof that the user saw an error.

## Request-start context

These additive fields describe context captured when `ChatRequestTelemetry` is
constructed, before invoking the provider:

| Field | Meaning |
| --- | --- |
| `requestStartCopilotSku` | The workbench's Copilot entitlement SKU, if known at request start. This does not identify the account or credential used by a remote host. |
| `selectedModelSource` | `copilot`, `byok`, `other`, or `unknown`, based on the selected model's registered metadata at request start. |

Explicit BYOK metadata, including a present Agent Host BYOK bridge identifier (even an empty string), takes
precedence over the catalog's vendor. A resolved Copilot catalog model or model
targeting a registered `copilotcli` host provider is `copilot`. A resolved model
from another non-host catalog or a known non-Copilot host provider is `other`.
Missing selection, unresolved metadata, and unresolved session providers are
`unknown`. Neither `other` nor `unknown` proves non-BYOK credentials; use `copilot`
to select the Copilot-classified population.
Only the category is emitted, not custom vendor names or BYOK bridge identifiers.

This is selection context, not an assertion about every model call: Auto,
HydraFusion, fallbacks, and provider-side model overrides can route differently.
The existing `model` field retains its completion-time lookup behavior.

## Reporting examples

- A request fails before producing any model-response telemetry: its terminal
  event can still carry the known SKU and selection source without an inner join
  that would drop the failure.
- A BYOK model is removed from the registry while a request is running: its
  selection source remains `byok`, even if the legacy `model` lookup is empty.
- Entitlement changes while a request is running: the outcome retains the
  request-start SKU. Missing initial entitlement stays missing.
- A request fails and is retried with the same ID: both existing invocation
  outcomes remain emitted. To count affected request identities, group by the
  appropriate device/session/request identity and test whether any outcome is
  `error` or `errorWithOutput`; do not overwrite an error with a later success.

Use the presence of `selectedModelSource` to identify enriched rows, distinguish
its explicit `unknown` value from absence, keep missing SKU context visible, and
verify field ingestion before updating a dashboard. This contract does not add
accepted-start coverage, execution IDs, retry provenance, internal-error
observation, or a user-facing interruption classification.


---
# DOCUMENT_SOURCE: microsoft_vscode::src/vs/workbench/contrib/chat/common/plugins/AGENTS_PLUGINS.md
- **CANONICAL_URL**: https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/plugins/AGENTS_PLUGINS.md
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/chat/common/plugins/AGENTS_PLUGINS.md
- **SHA256_FINGERPRINT**: `c27bacb0598f0a52ab2fe10fe5aec2a04dc5ebeadb739a04bb9d1f5740ee42b9`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:54:43.441409+00:00
---

# Agent Plugins Architecture

Agent plugins are a modular extension system that allows external packages of prompts, hooks, skills, agents, and MCP server definitions to be discovered, installed, and contributed into the chat experience. This document describes the architecture of the `src/vs/workbench/contrib/chat/common/plugins/` layer and its browser-side implementations.

## Directory Structure

### Common layer (`common/plugins/`)
| File | Role |
|------|------|
| `agentPluginService.ts` | Core interfaces (`IAgentPlugin`, `IAgentPluginService`, `IAgentPluginDiscovery`) and the discovery registry singleton |
| `agentPluginServiceImpl.ts` | `AgentPluginService` implementation, `AbstractAgentPluginDiscovery` base class, and workbench projections for all plugin formats |
| `agentPluginEnablement.ts` | Plugin collision enablement, canonical plugin identity, and enterprise-policy identity helpers |
| `agentPluginRepositoryService.ts` | `IAgentPluginRepositoryService` — abstract repository clone/pull/cache operations |
| `pluginMarketplaceService.ts` | `IPluginMarketplaceService` — marketplace metadata, installed-plugin storage, trusted-marketplace tracking, periodic update checks |
| `pluginInstallService.ts` | `IPluginInstallService` — install/update/uninstall orchestration interface |
| `pluginSource.ts` | `IPluginSource` — per-source-kind strategy interface (install path, ensure, update, cleanup) |

### Browser layer (`browser/`)
| File | Role |
|------|------|
| `agentPluginRepositoryService.ts` | Browser implementation of `IAgentPluginRepositoryService` (git clone/pull via Git service) |
| `pluginSources.ts` | Concrete `IPluginSource` implementations: `GitHubPluginSource`, `GitUrlPluginSource`, `NpmPluginSource`, `PipPluginSource`, `RelativePathPluginSource` |
| `pluginInstallService.ts` | Browser implementation of `IPluginInstallService` |
| `agentPluginsView.ts` | Installed-plugins tree view UI |
| `agentPluginActions.ts` | Context-menu actions for plugins |
| `agentPluginEditor/` | Rich editor for browsing a single plugin's contents |

## Core Interfaces

### IAgentPlugin

Represents a single discovered plugin:

```
uri              – Unique filesystem URI for the plugin root
label            – Human-readable display name
enablement       – Observable enable/disable state (ContributionEnablementState)
hooks            – Observable list of IAgentPluginHook
commands         – Observable list of IAgentPluginCommand  (*.md files in commands/)
skills           – Observable list of IAgentPluginSkill    (dirs with SKILL.md in skills/)
agents           – Observable list of IAgentPluginAgent    (*.md files in agents/)
mcpServerDefinitions – Observable list of IAgentPluginMcpServerDefinition
fromMarketplace  – Set when the plugin was installed from a marketplace
remove()         – Removes this plugin from its discovery source
```

### IAgentPluginService

Main entry point consumed by the rest of the workbench:

```
plugins          – IObservable<readonly IAgentPlugin[]>  (aggregate of all ready discoveries, sorted by URI)
enablementModel  – Shared IEnablementModel for plugin enable/disable state
```

Registered as `InstantiationType.Delayed` — only instantiated when first injected.

### IAgentPluginDiscovery

Strategy for finding plugins from a particular source:

```
plugins  – IObservable<readonly IAgentPlugin[] | undefined>
start(enablementModel) – Begin watching the source
```

Discoveries are registered into the global `agentPluginDiscoveryRegistry` singleton with a priority and instantiated by `AgentPluginService` on startup. A discovery reports `undefined` until its first scan completes; the service waits until every discovery has an initial result before exposing plugins.

## Discovery & Plugin Reading

### AbstractAgentPluginDiscovery

Shared base class that handles:

1. **Format detection** — recognizes strict Agent Plugins v1 by its root schema, then falls back to the Copilot, Claude, and Open Plugin path conventions.
2. **Content reading** — reads commands, skills, agents, hooks, and MCP server definitions from the filesystem.
3. **File watching** — by default, watches plugin directories for changes and re-reads their contents. Sources that own atomic replacement of plugin directories can opt out and rebuild entries from discovery-level events instead.
4. **Observable propagation** — sets the `plugins` observable on each refresh cycle.

Subclasses implement `_discoverPluginSources()` to determine *which* plugin URIs exist.

### Discovery Implementations

**ConfiguredAgentPluginDiscovery** — resolves `chat.pluginLocations` configuration entries (absolute, tilde-expanded, or workspace-relative paths) and watches for config changes. Redundant paths into the Copilot CLI-owned cache are ignored; committed CLI installations are owned by `CopilotCliAgentPluginDiscovery`.

**MarketplaceAgentPluginDiscovery** — resolves entries from `IPluginMarketplaceService.installedPlugins`, publishes only targets that still exist as directories, and delegates exact-URI removal and source cleanup to `IPluginInstallService`.

**CopilotCliAgentPluginDiscovery** — reads the Copilot CLI-managed `installedPlugins` records from `~/.copilot/config.json` and resolves their committed `cache_path` values. A correlated non-recursive watcher observes only the state file (or its nearest existing ancestor before first launch), and unchanged inventories are suppressed. CLI plugin entries do not create watchers inside their cache directories, so the CLI can atomically replace them on Windows. Uninstall delegates to the Copilot SDK so the runtime's cross-process lock and state writer own the complete transaction; direct installs carry the runtime-compatible opaque source ID needed to disambiguate same-name sources, and VS Code never deletes CLI-owned cache directories directly.

### Plugin Formats

Four format adapters share the discovery surface:

| | Agent Plugins v1 | Copilot | Claude | Open Plugin |
|-|------------------|---------|--------|-------------|
| Manifest | `plugin.json` with the exact Agent Plugins v1 schema | `plugin.json` | `.claude-plugin/plugin.json` | `.plugin/plugin.json` |
| Portable components | `skills/*/SKILL.md`, `mcp.json` | Host-specific components | Host-specific components | Open Plugin components |
| Hooks config | `com.github.copilot/hooks/hooks.json` client extension | `hooks.json` | `hooks/hooks.json` | `hooks/hooks.json` |
| Special handling | Compatible schema recognition, portable fixed paths, Copilot client extensions, package containment, `${PLUGIN_ROOT}` in Copilot hooks, and Agent Plugin MCP path semantics | Legacy permissive behavior and `${PLUGIN_ROOT}` hook replacement | `${CLAUDE_PLUGIN_ROOT}` token replacement | `${PLUGIN_ROOT}` token replacement |

Auto-detection first reads root `plugin.json`. The Agent adapter is selected when `$schema` uses the `agent-plugins.org` plugin schema namespace. Compatible schema revisions are accepted and known usable fields are read without rejecting unknown or malformed optional metadata. An Agent manifest wins over coexisting legacy metadata. Otherwise `.plugin/plugin.json` selects Open Plugin, a Claude path or manifest selects Claude, and the remaining packages use the Copilot adapter.

Agent Plugins use the shared plugin discovery pipeline and permissive component readers. Portable discovery scans only immediate children of `skills/` and root `mcp.json`. Copilot-specific commands, agents, rules, and hooks use the sanctioned `com.github.copilot` client extension namespace in both the manifest and filesystem. Their defaults are `com.github.copilot/commands/`, `com.github.copilot/agents/`, `com.github.copilot/rules/`, and `com.github.copilot/hooks/hooks.json`. Component path configuration under `extensions["com.github.copilot"]` resolves relative to the matching extension directory and supports the same string, string array, and `{ paths, exclusive }` forms as legacy plugin manifests. Inline hook and MCP definitions are also accepted there. Other extension namespaces and malformed optional metadata are ignored.

### Plugin Contents (Filesystem Layout)

```
<plugin-root>/
├── plugin.json                                    # Agent Plugins v1 or Copilot manifest
├── .claude-plugin/plugin.json                     # Claude manifest
├── .plugin/plugin.json                            # Open Plugin manifest
├── hooks.json   OR  hooks/hooks.json              # hook definitions
├── mcp.json                                       # Agent Plugins v1 MCP definitions
├── com.github.copilot/                            # Copilot Agent Plugin client extension
│   ├── commands/
│   │   └── do-thing.md
│   ├── agents/
│   │   └── helper.md
│   ├── rules/
│   │   └── project.instructions.md
│   └── hooks/
│       └── hooks.json
├── .mcp.json                                      # Legacy MCP server definitions
├── commands/
│   ├── do-thing.md                                # → IAgentPluginCommand
│   └── other.md
├── skills/
│   └── my-skill/
│       └── SKILL.md                               # → IAgentPluginSkill
└── agents/
    └── helper.md                                  # → IAgentPluginAgent
```

## Marketplace & Installation

### IPluginMarketplaceService

Manages the catalog of available and installed plugins:

- **Fetch** — reads `chat.plugins.marketplaces` config (GitHub shorthand, Git URLs, or file URIs), fetches `marketplace.json` from each, and returns parsed `IMarketplacePlugin` entries.
- **Installed storage** — persists `{ pluginUri, relativePath?, enablementUri?, marketplace, name? }` entries in `agent-plugins/installed.json`. Managed plugins resolve `relativePath` against the current plugin home so moving a portable installation does not invalidate them; external plugins retain absolute URIs. Escaping relative paths fall back to `pluginUri` and are removed or replaced with a valid managed path during migration. Descendant paths preserve plugin-directory casing and use the same casing policy as containment, including on macOS. Legacy entries under the current home and relocated absolute URIs are migrated at startup and after external edits. The store serializes its own file operations and preserves pending local changes instead of publishing stale migration results. Migration uses the file service's existing modification-time and etag checks; detected conflicts are reloaded and rescheduled. This is best-effort protection, not a cross-process transaction: same-size edits, unchanged timestamps, and changes after validation can still be overwritten. A stable `enablementUri` preserves each profile's enablement decisions through `IAgentPluginEnablementService`, including in-window profile switches and after another profile rewrites the shared manifest. Updates that move an installation transfer this identity from its previous recorded URI; a stale update whose source was already removed retains the target's established identity.
- **Trust** — marketplace canonical IDs must be explicitly trusted before install proceeds (`chat.plugins.trustedMarketplaces.v1`).
- **Auto-update** — checks eligible installed marketplaces approximately every 24 hours and reports their canonical IDs through `marketplacesWithUpdates`. Managed `extraKnownMarketplaces.<name>.autoUpdate` values override `extensions.autoUpdate` for that marketplace; undefined entries inherit the global setting. Checks and updates are restricted to enabled marketplaces and still enforce `strictKnownMarketplaces`.
- **GitHub caching** — caches raw GitHub API responses with an 8-hour TTL to avoid repeated fetches.

### Marketplace Definition Files

Checked in order per repository:
1. `marketplace.json` → `MarketplaceType.OpenPlugin`
2. `.plugin/marketplace.json` → `MarketplaceType.OpenPlugin`
3. `.github/plugin/marketplace.json` → `MarketplaceType.Copilot`
4. `.claude-plugin/marketplace.json` → `MarketplaceType.Claude`

### IPluginInstallService

Orchestrates install and update workflows:

- `installPlugin()` — checks marketplace trust, delegates to the appropriate source strategy to ensure files are locally available, and registers the plugin in installed storage.
- `installPluginFromSource()` — installs from a source string: GitHub shorthand (`owner/repo`), a git clone URL, or a local folder path (`file://` URI, absolute path, or `~`-prefixed path). Local folders are inspected to decide whether they are a marketplace (registered under `chat.plugins.marketplaces`) or a standalone plugin (registered under `chat.pluginLocations`).
- `updatePlugin()` / `updateAllPlugins()` — pulls latest changes for cloned repositories and re-runs package-manager installs where applicable.

### Plugin Source Strategies (IPluginSource)

Each `PluginSourceKind` has a strategy that knows how to compute cache paths, provision files, update, and clean up:

| Kind | Provisioning | Cache path |
|------|-------------|------------|
| `RelativePath` | No-op (lives inside marketplace repo) | `<marketplaceRepository>/<path>` |
| `GitHub` | `git clone` / `git pull` | `<cacheRoot>/github.com/<owner>/<repo>[/ref_<ref>]` |
| `GitUrl` | `git clone` / `git pull` | `<cacheRoot>/<host>/<path>[/ref_<ref>]` |
| `Npm` | `npm install` in terminal | `<cacheRoot>/npm/<sanitized-package>/` |
| `Pip` | `pip install` in terminal | `<cacheRoot>/pip/<package>/` |

Unpinned marketplace repositories use `<cacheRoot>/<host>/<path>`. Ref-specific marketplace repositories use the isolated `<cacheRoot>/.marketplace-repositories/<host>/<path>/ref_<ref>` namespace so one cache variant cannot delete another. Storage-indexed legacy locations remain usable while valid.

## Configuration & Storage Keys

### Configuration
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `chat.pluginsEnabled` | boolean | `true` | Master switch for the plugin system |
| `chat.pluginLocations` | `Record<string, boolean>` | `{}` | Local plugin directories to discover |
| `chat.pluginMarketplaces` | `string[]` | `[]` | Marketplace references to fetch from |

### Enterprise customization lockdown

The managed customization controls are complementary:

- `strictKnownMarketplaces` restricts which marketplace sources may provide plugins.
- `strictPluginOnlyCustomization` blocks standalone user and workspace skills, agents, hooks, instructions, and MCP servers. Eligible plugin contributions remain available.
- `allowManagedMcpServersOnly` makes the managed MCP allowlist authoritative; lower-layer allow entries cannot broaden it and deny entries remain restrictive.
- `allowManagedHooksOnly` permits plugin hooks only when managed `enabledPlugins` force-enables the plugin. User/workspace hooks and hooks from otherwise user-enabled plugins do not load.

`strictPluginOnlyCustomization` does not replace strict marketplace enforcement. Hardened deployments apply both controls when plugin source and standalone customization provenance must both be constrained.

In Copilot Agent Host sessions, the runtime reads `strictPluginOnlyCustomization` from Copilot managed settings, including its array form, and applies it to the customizations it discovers. The user and workspace skills and agents that VS Code forwards (for example, from configured skill locations), and every MCP server it forwards (for example, from VS Code's `mcp.json` or an extension), are bundled separately from other synced content. The host passes them through the SDK's `skillDirectories`, `customAgents`, and session `mcpServers` instead of `pluginDirectories`, so the runtime treats them as standalone customizations rather than plugin content. Extension and built-in skills and agents stay in the synced plugin, matching the workbench lockdown, which blocks only standalone prompt files.

### Storage (ApplicationScope, MachineTarget)
| Key | Description |
|-----|-------------|
| `chat.plugins.installed.v1` | Legacy installed marketplace plugins, migrated to `agent-plugins/installed.json` |
| `chat.plugins.trustedMarketplaces.v1` | User-trusted marketplace canonical IDs |
| `chat.plugins.lastFetchedPlugins.v2` | Last marketplace fetch results (persisted until next fetch) |
| `chat.plugins.marketplaces.githubCache.v1` | GitHub API response cache (8 hour TTL) |
| `chat.plugins.lastUpdateCheck.v1` | Timestamp of last periodic update check |

### Enablement Storage
| Key | Description |
|-----|-------------|
| `agentPlugins.enablement` | Per-plugin enable/disable state (shared `EnablementModel`) |

## Reactivity Model

The entire system is built on `IObservable`:

1. **Configuration observables** (`observableConfigValue`) — push changes when settings are modified.
2. **Discovery observables** — each `IAgentPluginDiscovery` exposes an `IObservable<readonly IAgentPlugin[] | undefined>` updated on filesystem changes after the first scan completes.
3. **Service-level derived** — `AgentPluginService.plugins` is a `derived()` that waits for all discovery observables, aggregates their plugin lists, and sorts by URI.
4. **Per-plugin observables** — each `IAgentPlugin` has observable properties for hooks, commands, skills, agents, and MCP definitions that update independently on file changes.
5. **UI bindings** — views and editors use `autorun()` / `derived()` to reactively render plugin state.

## Integration Points

- **Chat prompts** — plugin hooks are contributed to the prompt system via the hook infrastructure.
- **MCP servers** — plugins can define stdio and remote MCP servers. Agent Plugins v1 validates Streamable HTTP and legacy SSE declarations before passing remote servers to the existing MCP transport auto-detection.
- **AI Customization UI** — the AI customization views aggregate plugin stats alongside MCP servers, prompts, and other customization surfaces.
- **Extension API** — the plugin system is internal; there is no public `vscode` API surface for third-party access.

## Key Design Patterns

- **Strategy pattern** — the separate strict Agent Plugin and permissive legacy adapters, plus source strategies (`IPluginSource`), keep portable validation isolated from backward-compatible host behavior.
- **Discovery registry** — `agentPluginDiscoveryRegistry` decouples discovery implementations from the core service via priority-ordered `SyncDescriptor0<IAgentPluginDiscovery>` registration.
- **Disposable management** — plugin entries are tracked in a `Map` keyed by URI string, each with its own `DisposableStore` for file watchers. Removal or format changes dispose the store.
- **Debounced refresh** — filesystem changes trigger a 200 ms `RunOnceScheduler` to batch rapid edits into a single re-read.
- **Collision enablement** — multiple discoveries may produce equivalent plugins from different install roots; the service groups them by canonical identity so only the highest-priority copy is enabled by default, while enabling any copy disables the other copies in the same group.
- **Lazy instantiation** — the service is registered as `InstantiationType.Delayed` and only created on first injection.

Synthetic `.plugin/plugin.json` plus `.mcp.json` bundles created by customization synchronization remain legacy Open Plugin packages. Root Agent Plugin recognition is also used for direct standalone installs, but `MarketplaceType.OpenPlugin` and the existing marketplace protocol remain unchanged because Agent Plugins v1 defines no marketplace format.

Provider adapters do not delegate strict packages to legacy SDK plugin discovery. Copilot explicitly receives skills and MCP, Codex explicitly receives skills and MCP, and Claude explicitly receives remote MCP. Remote MCP transport selection remains the responsibility of each provider's existing auto-detection. The Claude SDK currently has no external skill-directory API or per-server stdio working-directory option, so strict Claude skills and stdio MCP are skipped rather than reinterpreted.
