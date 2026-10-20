**MetaDescription**: Use AI beside your code in the Chat view, ask questions, run agents, and choose a layout.

# Use the Chat view

The Chat view runs agents beside your code in the main Visual Studio Code window. Use it when you want to collaborate over code in the current workspace while keeping the editor, debugger, tests, terminals, extensions, and notebooks available alongside the conversation.

In this article, you learn how to open the Chat view, choose a layout, understand its interface, and start a workspace-scoped session. Both the Chat view and [Agents window](/docs/agents/run/agents-window.md) let you direct agents and review their work. To choose an interface based on where you want to focus, see [Run agents in VS Code](/docs/agents/run/overview.md#choose-an-interface). For conversation mechanics shared by both interfaces, see [Use chat in VS Code](/docs/chat/chat-overview.md).

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
Follow a hands-on tutorial to build an app with AI agents in VS Code.

* [Start agentic coding tutorial](/docs/agents/agents-tutorial.md)

</div>

## Prerequisites

* Visual Studio Code installed. [Download VS Code](/download).
* Access to an AI model through a supported setup:
    * For models provided by GitHub Copilot, [set up GitHub Copilot in VS Code](/docs/setup/copilot.md).
    * To use [product.prodname_anthropic_claude], [product.prodname_openai_codex], or your own model credentials for supported workflows, review the [agent harness authentication options](/docs/agents/run/agent-harnesses.md#requirements-and-setup) and [language model setup](/docs/agent-customization/language-models.md).

## Open the Chat view

The Chat view opens in the Secondary Side Bar, next to your editor. To open the Chat view, use one of the following methods:

* Select the **Chat** menu in the VS Code title bar, and then select **Open Chat**.

* Use the keyboard shortcut ``Shortcut: workbench.action.chat.open``.

* Run `code chat` from the command line to start chat from outside VS Code. Learn more about [starting chat from the command line](/docs/configure/command-line.md#start-chat-from-the-command-line).

### Layout options

The Chat view offers several layout options within the main VS Code window. Choose the layout that best fits your workflow:

* **Side bar** (default): select **New Chat (+)** > **New Chat**, or run the **Chat: New Chat** command. Best for keeping chat visible alongside your code.

* **Editor tab**: select **New Chat (+)** > **New Chat Editor**, or run the **Chat: New Chat Editor** command. Best for giving chat more space or comparing sessions side by side.

* **Separate window**: select **New Chat (+)** > **New Chat Window**, or run the **Chat: New Chat Window** command. Best for multi-monitor setups.

## Interface overview

The Chat view keeps the agent next to your code, so you can prompt, review, and edit in the same window. The Chat view has the following main areas:

1. **Sessions list**: at the top of the view, where you can view and manage your sessions for the current workspace. Learn more about the [sessions list](/docs/agents/run/sessions/manage-sessions.md#sessions-list).

1. **Chat conversation**: in the center, where you see the conversation history and the agent's responses, including the changes it makes to your code.

1. **Chat input**: at the bottom, where you type prompts and configure the session with the **Session Target**, **Agent**, **Language model**, and **Permissions** controls.

![Screenshot showing the Chat view with the sessions list, conversation, and chat input.](../images/agents-overview/chat-view-expanded.png)

> [!TIP]
> To inspect a chat response with a keyboard or screen reader, run **Open Accessible View** (``Shortcut: editor.action.accessibleView``). Learn more about the [Accessible View](/docs/configure/accessibility/accessibility.md#accessible-view).

The Chat view operates in two modes: compact and side-by-side. Use the toggle control in the top-right corner of the Chat view to switch between them. In compact mode, the sessions list and conversation share the same panel. In side-by-side mode, the sessions list stays visible next to the conversation. Learn more about [sessions list layout options](/docs/agents/run/sessions/manage-sessions.md#sessions-list).

### Switch chats within a session

With a harness that supports multiple chats, such as Copilot or Claude, a session can contain a main chat and additional peer chats. In the **Sessions** view, expand the main chat row and select a peer to open its conversation in the Chat view.

You can continue peer chats created in the Agents window without starting a new session. For creation steps, navigation options, and interface-specific controls, see [Run multiple chats in a session](/docs/agents/run/sessions/manage-sessions.md#run-multiple-chats-in-a-session).

## Start a session

To start a workspace-scoped session, select **New Chat** (`+`) or press ``Shortcut: workbench.action.chat.newChat``. Before you send the first prompt, use the chat input controls to choose a **Session Target**, **Agent**, **Language model**, and **Permissions**. For a first coding task, use **Copilot**, **Agent**, **Auto**, and **Manual permissions**, as shown in the [agents quickstart](/docs/agents/quickstart.md). Available choices depend on your account, installed providers, and organization policies. Learn how to [identify your current harness](/docs/agents/run/agent-harnesses.md#identify-your-current-harness) or [compare agent harnesses](/docs/agents/run/agent-harnesses.md#compare-agent-harnesses).

Type a prompt and press ``Shortcut: workbench.action.chat.submit``. For shared request, context, and conversation controls, see [Use chat in VS Code](/docs/chat/chat-overview.md). For session context, history, and organization, see [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md).

## Work with the agent

Because the Chat view runs in the main VS Code window, you can inspect agent edits in the editor, follow terminal activity, debug the application, and run tasks or tests without switching surfaces. The agent also has access to supported extensions and can [work with Jupyter notebooks](/docs/agents/guides/notebooks-with-ai.md). When you connect to a [remote workspace](/docs/remote/remote-overview.md), the session uses the same remote project context and tools.

The Copilot harness applies and saves edits directly to the selected folder or worktree. Select a changed file in the response to inspect its diff, or set ``chat.checkpoints.showFileChanges`` to show a changed-files summary after each request. For revisions, checkpoints, harness-specific review workflows, and integrating changes, see [Review AI-generated code edits](/docs/agents/run/review-code-edits.md).

## Next steps

* [Chat interaction controls](/docs/chat/chat-overview.md) - send and steer requests, add context, and navigate a conversation.
* [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md) - organize, archive, and fork sessions.
* [Use the Agents window](/docs/agents/run/agents-window.md) - work with agents across multiple projects.
