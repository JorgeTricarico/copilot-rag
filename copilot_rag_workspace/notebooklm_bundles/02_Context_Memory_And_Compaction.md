# COMPENDIO RAG NOTEBOOKLM: 02_Context_Memory_And_Compaction
- **Generado (UTC)**: 2026-10-21T03:46:01.314112+00:00
- **Total Palabras**: 5,859 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/reference/workspace-context.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/reference/workspace-context
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/reference/workspace-context.md
- **SHA256_FINGERPRINT**: `989d2f1a1e5ec506c67d8a461d322754d0c67dbd6fdac8531a562f9882ae4797`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.139597+00:00
---

**MetaDescription**: Understand how Copilot agents search workspace code, gather context, and work within indexing and exclusion limits.

# How Copilot understands your workspace

Copilot agents use search and file-reading tools to find relevant workspace code. For prompts like "where is authentication handled?" or "add tests for the list endpoint", they can gather context from related files instead of relying only on the current editor. What they find depends on available tools, indexing, exclusions, and the information you provide. Review their answers and edits against the source.

This article explains the tools and indexes Copilot uses to discover workspace context, and the limits to consider when a result is incomplete. An index helps find relevant snippets; it doesn't put the entire workspace into each model request.

## Search and read tools

When you send a prompt, Copilot analyzes what information it needs and automatically selects the right combination of search tools to either answer your question or start generating code edits. Copilot runs multiple tools for this, reviews the results, and automatically performs follow-up searches until it has a good understanding of the problem.

For example, when asked to "add error handling to the payment service", the agent might:

1. Use **semantic search** to find payment-related code across the project.
1. Use **grep** to find existing error handling patterns in the codebase.
1. Use **usages** to trace how the payment functions are called.
1. Use **file search** to locate related configuration and test files.
1. Read the relevant files and make coordinated changes.

This iterative approach lets the agent follow relationships across the codebase. It doesn't guarantee that every relevant file is found. Reference important files explicitly when you know they are needed.

Agents have access to the following built-in search tools. You can also explicitly reference these tools in your prompts by typing `#` followed by the tool name.

| Tool | Description |
|------|-------------|
| **Semantic search** (`#codebase`) | Finds code that matches the meaning of your question, not just exact keywords. Requires a [workspace index](#semantic-index-sources). |
| **Text search** | Searches file content for text matches, such as specific keywords. |
| **Grep** | Searches for exact text or regex patterns across files. Works without an index. |
| **File search** | Finds files by name or glob pattern. |
| **Usages** | Combines Find All References, Find Implementation, and Go to Definition to trace how symbols are used across files. |
| **List directory** | Lists the contents of a directory to explore the project structure. |
| **Read file** | Reads the content of a specific file to examine its code in detail. |

These tools work for any workspace size. For small projects, the entire workspace can be read directly into the agent's context. For larger projects, the agent selects the most efficient search strategy based on your project size and available resources.

### Search GitHub repositories beyond your workspace

In addition to searching the current workspace, agents can search code in other GitHub repositories. This is useful when the agent needs to learn about a codebase that is not open locally, for example to look up an API in an upstream library or compare an implementation across repositories.

| Tool | Description |
|------|-------------|
| **Semantic Search GitHub Repository** (`#githubRepo`) | Semantic search a GitHub repository for relevant source code snippets. Specify a repository using `owner/repo`. |
| **GitHub Text Search** (`#githubTextSearch`) | Text search a GitHub repository or organization for files containing specific keywords or code patterns. |

For more advanced GitHub workflows, such as searching and managing issues or pull requests, use the [GitHub MCP server](https://github.com/github/github-mcp-server).

### What the agent has access to

Depending on the harness, tools, and context settings, agents can gather information from:

* [Indexable workspace files](#what-content-is-included-in-the-semantic-index), subject to indexing and exclusion rules
* Directory structure with nested folders and file names
* Code symbols and definitions (classes, functions, variables)
* [Editor context](/docs/agents/concepts/context.md#implicit-context), such as selected text, when included in the request
* Conversation history and previous tool results

> [!IMPORTANT]
> `.gitignore` is bypassed if you have a file open or have text selected within an ignored file.

### Improve agent search with exclusion settings

When an agent searches your workspace with text search or grep, every match returned becomes part of the conversation context, even if the agent never opens the file. Generated files, build artifacts, logs, and large datasets can produce many irrelevant matches that fill the context window with noise.

Configure exclusion settings to keep agent searches focused on source code you care about:

* **`.gitignore`**: excludes files from text search, grep, and the [semantic index](#what-content-is-included-in-the-semantic-index).
* **``files.exclude``**: hides files from the Explorer and excludes them from text search, grep, and the semantic index.
* **``search.exclude``**: excludes files from text search and grep while keeping them visible in the Explorer.

Strict exclusions improve search relevance, speed up searches over large workspaces, and reduce the tokens consumed by search results. This also helps [manage AI credit usage](/docs/agents/guides/optimize-usage.md#exclude-files-from-chat-context).

Add exclusion patterns to your [workspace settings](/docs/configure/settings.md). Patterns use [glob syntax](/docs/editor/glob-patterns.md).

> [!TIP]
> When a text search returns no results, the agent receives a hint that the pattern may be excluded, for example when investigating a dependency in `node_modules`.

## Semantic search

The semantic search tool (`#codebase`) finds code by meaning rather than exact keywords.

Semantic search requires building and maintaining an index so that it can run quickly, even on very large codebases. Copilot maintains this index for you automatically. Behind the scenes, parts of the index might be stored on your machine and parts might come from remote sources, but you don't need to manage this distinction.

You can view the indexing status in the Copilot status dashboard in the VS Code Status Bar.

![Screenshot showing the workspace index status in the Copilot status menu.](../images/workspace-context/workspace-index-status.png)

### Semantic index sources

Copilot builds and maintains a semantic index for any workspace automatically. The index source determines how quickly the index becomes available for the first time:

* **GitHub repositories**: GitHub indexes the GitHub repositories in your workspace. Sign in with your GitHub account to use them. This index only needs to be built once per repository, which means it is often instantly available. GitHub builds and updates this index when needed. This is fast for small and medium sized projects, but might take some time if your repository contains hundreds of thousands of files. Remote indexing works for repositories hosted on GitHub.com or GitHub Enterprise Cloud. It is not supported for GitHub Enterprise Server.

* **Azure DevOps repositories**: Indexes are automatically built and maintained. Sign in with your Microsoft account in VS Code for Copilot to start using the index. Check the Copilot Status Bar item for the current index status.

* **Other workspaces**: For any other workspace, including local folders not backed by a GitHub or Azure DevOps repository, Copilot builds the semantic index for you. The initial build can take a few minutes, after which the index is kept up to date in the background. This feature is currently enabled for personal accounts but off by default for organization and enterprise users. See the [GitHub docs](https://docs.github.com/en/copilot/concepts/context/repository-indexing#semantic-indexing-for-non-github-repositories) for more details about how to enable this feature using a policy.

To build or rebuild the index for the current workspace on demand, run the **Build Codebase semantic index** command from the Command Palette.

### What content is included in the semantic index

VS Code indexes relevant text files that are part of your current project. This is not limited to specific file types or programming languages. VS Code automatically skips some common file types that are typically not relevant, such as `.tmp` or `.out` files.

The workspace index also excludes files that are excluded from VS Code by the ``files.exclude`` setting or by a `.gitignore` file.

Binary files, such as images or PDFs, are not indexed.

## Tips for better results

The way you phrase your prompt influences which tools the agent uses and the quality of the results.

* **Be specific**: avoid vague terms like "what does this do", where "this" could mean the last answer, current file, or whole project.
* **Use code terms**: use function names, class names, and concepts that appear in your code so the agent can find exact matches.
* **Add context manually**: select code, reference files, or [#-mention context items](/docs/chat/copilot-chat-context.md) such as debug context, terminal output, and more.
* **Scope your request**: responses can draw from multiple references, such as "find exceptions without a catch block". But don't expect a full codebase analysis, such as "how many times is this function invoked?".
* **Use external tools for non-code questions**: for information like "who contributed to this file?", configure the relevant [tools or MCP servers](/docs/agents/run/tools.md).

## Private repositories

To use semantic search for private repositories, Copilot may need additional permission. If these permissions are not already granted, VS Code asks for them at startup. Once granted, the session is securely stored for the future.

![Modal window asking for additional authentication for a private repository.](../images/workspace-context/authentication.png)

Learn more about security, privacy, and transparency in the [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center/).

## Frequently asked questions

### Do I need to use `#codebase` in my prompts?

No. Agents automatically use semantic search when it makes sense. You don't need to add `#codebase` to your prompt.

The `#codebase` tool is always semantic and provides consistent results. If you want to force a semantic search for a specific prompt, you can still add `#codebase` as a [context item](/docs/chat/copilot-chat-context.md).

### What happens if my workspace is not semantically indexed?

Most workspaces are indexed automatically, but if the index isn't available yet (for example, while a new local workspace is still building its initial index), agents still search your code effectively by using text search, grep, file search, and language intelligence. The workspace index enables semantic search, which finds code by meaning rather than keywords. Without it, agents rely on the other search tools and can still provide accurate results for most prompts. We've found that these other tools still provide great results.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/chat/chat-overview.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/chat/chat-overview
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/chat/chat-overview.md
- **SHA256_FINGERPRINT**: `315201ce9f6409e860dfb9e27423dd82cc3a60e162e20ca8da4e8ac0bcf24d20`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.824223+00:00
---

**MetaDescription**: Use chat in VS Code to ask about code, send requests, add context, and review AI-generated changes.

# Use chat in VS Code

Chat in Visual Studio Code lets you use natural language for interacting with AI agents. Ask questions about your code, get help understanding complex logic, generate new features, fix bugs, and more, all through a conversational interface.

This article describes interaction mechanics shared by chat surfaces in VS Code, including how to send and steer requests, add context, navigate a conversation, and personalize the chat display. For an introduction to AI workflows, agents, and the available interfaces, see [Build with AI in VS Code](/docs/agents/overview.md).

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
Follow a hands-on tutorial to build an app with AI agents in VS Code.

* [Start agentic coding tutorial](/docs/agents/agents-tutorial.md)

</div>

## Choose where to chat

The interaction mechanics in this article apply to the Chat view, chat editor tabs, and the Agents window. Both the Chat view and the Agents window run agents. To choose between collaborating over code in your current workspace and coordinating work across projects, see [Run agents](/docs/agents/run/overview.md#choose-an-interface).

For lightweight interactions, use [inline chat](/docs/chat/inline-chat.md) to edit code or get terminal suggestions in place, or open [Quick Chat](/docs/chat/inline-chat.md#use-quick-chat) for a temporary conversation.

## Send a chat request

Type your message in the chat input box and press ``Enter`` or select the **Send** button. The agent can answer questions, analyze your code, run tools, make changes, and respond with a summary. You can then continue the conversation with follow-up messages. For example, you might ask an agent to make this change:

```prompt
Add input validation to the signup form
```

For a hands-free conversation, start [Voice Mode](/docs/configure/accessibility/voice.md#use-voice-mode) from the chat input. Voice Mode listens for follow-up requests and reads the agent's responses aloud. `feature(voice-mode)`

To give extra project-specific context, you can [add context to your prompt](#add-context-to-your-prompts) by referencing files, symbols, or other information with `#`-mentions.

For common tasks, you can use slash commands as shortcuts for frequently used prompts or to invoke [agent skills](/docs/agent-customization/agent-skills.md). Type `/` in the chat input to see all available commands.

You can run multiple sessions in parallel and switch between them without losing context. Learn more in [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md).

Each session has controls that shape how the agent responds: **Session Target**, **Agent**, **Language model**, and **Permissions**. Learn how to [compare agent harnesses](/docs/agents/run/agent-harnesses.md#compare-agent-harnesses) and [select one for a session](/docs/agents/run/agent-harnesses.md#select-a-harness).

> [!TIP]
> To get the best results, be specific about what you want, provide relevant context, and write clear instructions. For more information, see [Get better responses](#get-better-responses).

## Run terminal commands from chat

Start a message with `!` to run a terminal command directly from the Chat view or Agents window. The `!` must be the first character and must be followed by a command.

For example, enter the following message to run your tests:

```shell
!npm test
```

The command runs immediately in the session's default shell, without sending the message to the agent or asking for approval. It uses the session folder or worktree as the working directory. The command output and exit status appear in the chat transcript.

> [!NOTE]
> The `!` command isn't available in Local harness sessions, cloud sessions, or extension-based agent integrations. Use the [integrated terminal](/docs/terminal/getting-started.md) to run commands yourself instead.

## Send messages while a request is running

You don't have to wait for a response to finish before sending your next message. While a request is in progress, the **Send** button changes to a dropdown that gives you three options for how to handle the new message.

![Screenshot of the Send button dropdown menu showing options to queue, steer, or stop and send a new message.](images/chat-sessions/send-dropdown.png)

* **Add to Queue**: your message waits and sends automatically after the current response completes. The current response finishes uninterrupted.
* **Steer with Message**: signals the current request to yield after finishing the current tool execution. The current response stops and your new message processes immediately. Use this to redirect the agent when it's heading in the wrong direction.
* **Stop and Send**: cancels the current request entirely and sends your new message right away.

Stopping a request doesn't undo file edits, terminal commands, or other actions that already completed. To restore affected workspace files and chat history, [restore a checkpoint](/docs/agents/run/review-code-edits.md#restore-a-checkpoint). Checkpoints don't reverse changes to external services.

For examples of when to steer or stop a request and how to write a focused correction, see [Get an agent back on track](/docs/agents/guides/get-agent-back-on-track.md#redirect-a-running-request).

The default action for the **Send** button is configurable. Use ``chat.requestQueuing.defaultAction`` to set it to `steer` (default) or `queue`.

### Reorder pending messages

When you have multiple pending messages (queued or steering), you can drag and drop them to change the order in which they are processed. A drag handle appears on hover when more than one message of the same type is pending.

![Screenshot of pending messages in the chat input box with drag handles to reorder them.](images/chat-sessions/pending-messages.png)

## Add context to your prompts

Providing the right context helps the AI generate more relevant and accurate responses.

* **Implicit context**: VS Code can include or suggest editor context, such as the active file or selection. The behavior depends on the interface, harness, and context settings. Attach important files explicitly instead of assuming that opening a file adds its contents to the request. Learn how [implicit context works](/docs/agents/concepts/context.md#implicit-context).

* **`#`-mentions**: type `#` in the chat input to explicitly reference files (`#file`), folders, symbols, your codebase (`#codebase`), terminal output (`#terminalSelection`), or tools like `#fetch`.

* **Vision**: attach images, such as screenshots or UI mockups, as context for your prompt.

* **Browser elements**: select elements from the [integrated browser](/docs/debugtest/integrated-browser.md) to add HTML, CSS, and screenshot context to your prompt.

Learn more about [managing context for AI](/docs/chat/copilot-chat-context.md).

## Image carousel

You can select images or videos in chat responses to open a dedicated carousel view. Media files from tool results (such as the integrated browser, Playwright, or other MCP servers) and inlined in assistant messages are all accessible from the carousel.

![Screenshot showing the image carousel view with multiple images.](images/chat-sessions/image-carousel.png)

To disable the image carousel, set ``imageCarousel.chat.enabled`` to `false`.

## Review and manage changes

After the AI changes files, review and validate the result before you commit or integrate it. In the Chat view, select a changed file in the response to open its diff. In the Agents window, use the **Changes** panel.

For keyboard and screen reader access to a diff, use the [Accessible Diff Viewer](/docs/configure/accessibility/accessibility.md#diff-editor-accessibility).

For instructions about requesting revisions, restoring checkpoints, and integrating folder or worktree changes, see [Review AI-generated code edits](/docs/agents/run/review-code-edits.md).

## Get notified about chat responses

When you're working in another window or application, VS Code can send you OS notifications to let you know about important chat events, so you don't have to keep checking back.

Use ``chat.notifyWindowOnResponseReceived`` to configure when you receive an OS notification when a chat response is received. The notification includes a preview of the response, and selecting it brings focus to the chat session.

Use ``chat.notifyWindowOnConfirmation`` to configure when you receive an OS notification when the agent needs your input or confirmation to continue.

Both settings have three possible values:

* `off`: never show notifications
* `windowNotFocused` (default): show notifications only when the VS Code window is not focused
* `always`: show notifications even when the VS Code window is in focus

> [!TIP]
> Set the value to `always` if you want to stay aware of chat activity while working in other parts of VS Code, such as when running long agent tasks in the background.

## Find text in a chat session

Press ``Shortcut: workbench.action.chat.find`` to search the entire conversation. Find is available in the Chat view, chat editor tabs, and the Agents window. It searches prompts and responses, including off-screen content and code blocks.

Use ``Shortcut: workbench.action.chat.findNext`` and ``Shortcut: workbench.action.chat.findPrevious`` to navigate between matches. When a match is inside a collapsed **Completed N steps** section, navigating to the match expands the section. Use the **Match Case**, **Whole Word**, and **Regular Expression** options to refine the results.

> [!NOTE]
> Find is not available in Quick Chat or inline chat. It does not search text inside tool pills or collapsed reasoning.

## Navigate between prompts in a chat session

Use the following keyboard shortcuts to navigate between prompts in a chat session:

* ``Shortcut: workbench.action.chat.previousUserPrompt``: Go to the previous prompt in the chat session.
* ``Shortcut: workbench.action.chat.nextUserPrompt``: Go to the next prompt in the chat session.
* ``Shortcut: workbench.action.chat.previousCodeBlock``: Go to the previous code block in the chat session.
* ``Shortcut: workbench.action.chat.nextCodeBlock``: Go to the next code block in the chat session.

To inspect a chat response character by character or line by line with a keyboard or screen reader, run **Open Accessible View** (``Shortcut: editor.action.accessibleView``). Learn more about the [Accessible View](/docs/configure/accessibility/accessibility.md#accessible-view).

## Personalize chat

Adjust how chat content appears, add an interactive pet, or set a decorative background in the Agents window.

### Customize the chat display

Use these settings to adjust the chat transcript:

| Display option | Settings |
|----------------|----------|
| Markdown font | Set the font family with ``chat.fontFamily`` and the font size with ``chat.fontSize``. |
| Code block font and layout | Set the font family, size, weight, and line height with ``chat.editor.fontFamily``, ``chat.editor.fontSize``, ``chat.editor.fontWeight``, and ``chat.editor.lineHeight``. Control line wrapping with ``chat.editor.wordWrap``. |
| Sticky prompts | Use ``chat.stickyScroll.enabled`` to pin the current prompt to the top of the transcript while you scroll. |
| Request timestamps | Use ``chat.verbose`` to show or hide request and completion timestamps. Hover over a completion timestamp to view the elapsed response time. |
| Persistent progress (Experimental) | Use ``chat.experimental.persistentProgress`` to keep a progress indicator visible until an agent response finishes. Choose a colored or monochrome **Draw** animation, or turn the indicator off. |

With persistent progress, reasoning appears in separate collapsible previews and tool calls remain visible while they run. ``chat.experimental.persistentProgressVerbosity`` controls completed tool-call details. **Compact** replaces completed groups with expandable summaries when response text resumes or the response finishes. **Verbose** keeps the full details visible.

Persistent progress defaults to **Draw** in Insiders and **Off** in Stable.

For more chat preferences, see the [AI settings reference](/docs/agents/reference/ai-settings.md#chat-experience).

### Customize the Agents window chat background

`feature(agents-window-chat-backgrounds)`

Add a decorative background to the chat area of the Agents window without changing chat in the main VS Code window.

To set a background, run the **Chat: Set Background...** command from the Command Palette (``Shortcut: workbench.action.showCommands``) or right-click an empty area of the chat. Then, choose one of these options:

* **No Background**: remove the background for the current color theme.
* **Codicons**: use a theme-aware pattern of built-in VS Code icons.
* **Image...**: select an image from your machine.
* **Recently used**: reuse one of your five most recent background images.

For an image background, run **Chat: Change Background Layout...** to repeat, stretch, center, or position the image along an edge or in a corner for the current color theme. Moving through the layout options previews each one. Select an option to save it, or dismiss the picker to restore the previous layout.

> [!NOTE]
> Light and dark color themes have separate backgrounds and image layouts. These choices are stored on the current machine and don't sync across devices.

Backgrounds are hidden in high contrast themes to preserve chat readability. The background commands are also unavailable while a high contrast theme is active.

## Get better responses

Chat provides several ways to improve the quality and relevance of AI responses:

* **Write effective prompts**: be specific about what you want, reference relevant files and symbols, and use `/` commands for common tasks. Get inspired by [prompt examples](/docs/agents/guides/prompt-examples.md) or review the full [prompt engineering guide](/docs/agents/best-practices.md).

* **Customize the AI**: tailor the AI's behavior to your project by adding [custom instructions](/docs/agent-customization/custom-instructions.md), creating reusable [prompt files](/docs/agent-customization/prompt-files.md), or building [custom agents](/docs/agent-customization/custom-agents.md) for specialized workflows. For example, create a "Code Reviewer" agent that provides feedback on code quality and adherence to your team's coding standards.

* **Extend with tools**: connect [MCP servers](/docs/agent-customization/mcp-servers.md) or install extensions that contribute tools to give the agent access to external services, databases, or APIs.

For more information, see [Customize agent behavior in VS Code](/docs/agent-customization/overview.md).

## Troubleshoot chat interactions

Use [Agent Logs and the Chat Debug view](/docs/agents/agent-troubleshooting/chat-debug-view.md) to inspect what happens when you send a prompt. Agent Logs shows a chronological event log of tool calls, LLM requests, and prompt file discovery. The Chat Debug view shows the raw system prompt, user prompt, context, and tool payloads for each interaction. These tools are useful for understanding why the AI responded in a certain way or for troubleshooting unexpected results.

## Support

Support for GitHub Copilot Chat is provided by GitHub and can be reached at <https://support.github.com>.

To learn more about Copilot's security, privacy, compliance, and transparency, see the [GitHub Copilot Trust Center FAQ](https://copilot.github.trust.page/faq).

## Related resources

* [Create and manage agent sessions](/docs/agents/run/sessions/manage-sessions.md)

* [Choose an agent harness](/docs/agents/run/agent-harnesses.md)

* [Prompt examples](/docs/agents/guides/prompt-examples.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/chat/copilot-chat-context.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/chat/copilot-chat-context
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/chat/copilot-chat-context.md
- **SHA256_FINGERPRINT**: `ff16b068681721ba2318ebc79665da1f540d3fad11b9db11335e513c44341209`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:56.155105+00:00
---

**MetaDescription**: Add files, symbols, images, browser content, and other context to AI prompts in Visual Studio Code for more relevant responses.

# Add context to chat

Providing relevant context helps the AI give more accurate responses. Add files, folders, symbols, images, web content, and other information directly to your prompt when you want the AI to consider specific details.

> [!NOTE]
> Unless otherwise noted, the features on this page work in both the [Chat view](/docs/agents/run/chat-view.md) and the [Agents window](/docs/agents/run/agents-window.md).

For background on what context is and how VS Code assembles it, see [Context concepts](/docs/agents/concepts/context.md).

## #-mentions

You can explicitly add context to your prompt by typing `#` followed by the context item you want to mention. VS Code supports different types of context items: files, folders, code symbols, tools, terminal output, source control changes, and more.

Type the `#` symbol in the chat input field to see a list of available context items, or select **Add Context** in the Chat view to open the context picker.

![Screenshot of VS Code Chat view, showing the chat variable picker.](./images/copilot-chat/copilot-chat-view-chat-variables.png)

For tool names and context references, see the [Tools and context reference](/docs/agents/reference/tools-reference.md).

### Add files as context

Agents can use workspace search and file-reading tools to gather relevant context. A workspace index helps locate code, but doesn't attach every file to the conversation. Add specific files, folders, or symbols by using #-mentions or the context picker when you know which sources the agent should consider.

To provide specific files, folders, or symbols as context, add them to the chat using the following methods:

* #-mention the file, folder, or symbol in your chat message by typing `#` followed by the name of the file, folder, or symbol.
    To reference a symbol, make sure to open the file containing the symbol in the editor first.

* Drag and drop files or folders from the Explorer view, Search view, or editor tabs onto the Chat view to add them as context.

* Select **Add Context** in the Chat view and select **Files & Folders** or **Symbols** from the Quick Pick.

Use `#codebase` to request a search for relevant code across the workspace. It doesn't add the entire codebase to the model's context. Learn about [workspace search and indexing](/docs/agents/reference/workspace-context.md).

### Add project and GitHub context

When you start a session in the Agents window, the first folder or repository you select is the primary execution workspace. It determines where the agent runs and changes files.

You can attach project and GitHub context to a request:

* In the Agents window, select **Folder** or **Repository** to attach another project. An attached project provides request context and doesn't become another workspace root.
* In any chat input, select **Add Context**, and then select **Issue...** or **Pull Request...**. If multiple GitHub repositories are available, select a repository before you choose the issue or pull request.
* Paste a GitHub issue or pull request URL directly into the prompt. The URL remains in the prompt, and VS Code automatically adds the item as a context attachment.

You can attach multiple items. The attachments are preserved in a draft and included when you send the request. Learn more about [starting an agent session in the Agents window](/docs/agents/run/agents-window.md#start-an-agent-session).

### Reference content from the web

You can reference content from the web in your chat prompts, for example to get the latest API reference or code examples.

You can directly include a URL in your prompt to get information from that webpage, or use the `#fetch` tool to indicate that you want to retrieve content from the web. For example:

* `"What are the highlights of the latest VS Code release #fetch"`
* `"Update the asp.net app to .net 9 #fetch https://learn.microsoft.com/en-us/aspnet/core/migration/80-90"`

VS Code caches the content of the web page for a limited time to improve performance. If the content of the page changes, you can force a refresh by restarting VS Code. If the page cannot be reached, the cache will expire after a short time (approximately five minutes).

VS Code prompts for confirmation before accessing external URLs to protect your privacy and security. Learn more about [configuring URL auto-approval](/docs/agents/run/approvals.md#url-approval).

Learn more about [using tools with agents](/docs/agents/run/tools.md).

## @-mentions

Chat participants invoked with `@name` are deprecated and are not supported in the Copilot harness. They remain available for Local harness compatibility.

Ask Copilot directly about your code, terminal output, or editor settings and attach the relevant context. For domain-specific integrations, use plugins with skills and MCP tools, or extension tools when editor context is required. See [Replace chat participants](/docs/agent-customization/migrate-customizations.md#replace-chat-participants).

## Vision

Chat supports vision capabilities, which means you can attach an image as context to your chat prompt and ask questions about it. For example, attach a screenshot of a block of code and ask to explain it, or attach a sketch of a UI and ask the agent to implement it.

> [!TIP]
> You can drag and drop an image from a web browser onto the Chat view to add it as context.

## Add browser context

Use the [integrated browser](/docs/debugtest/integrated-browser.md) to preview web pages and attach information from the current page to a prompt.

The browser toolbar has an **Add to Chat** split button with actions that let you attach different types of context from the current page to your chat prompt:

* **Add Element to Chat**: select HTML elements from the page to add as context, including their CSS styles and screenshots.
* **Add Screenshot to Chat**: capture a screenshot of the current browser viewport and attach it as an image.
* **Add Console Logs to Chat**: capture console output from the page and attach it as context for debugging runtime errors.

Learn how to [add browser context to chat](/docs/debugtest/integrated-browser.md#add-context-to-ai-chat). To let an agent interact with a page instead of attaching it as prompt context, see [browser tools for agents](/docs/debugtest/integrated-browser.md#browser-tools-for-agents).

## Related resources

* [Use the Chat view](/docs/agents/run/chat-view.md)
* [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md)
* [Prompt examples](/docs/agents/guides/prompt-examples.md)
* [Prompt engineering guide](/docs/agents/best-practices.md)
* [Debug chat interactions](/docs/agents/agent-troubleshooting/chat-debug-view.md)
* [Diagnose prompt caching with the Cache Explorer](/docs/agents/agent-troubleshooting/cache-explorer.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/chat/inline-chat.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/chat/inline-chat
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/chat/inline-chat.md
- **SHA256_FINGERPRINT**: `69a4359742e1bd4d47734194818faede2dccc8513a39900b9ceb8c2de21bbd6d`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.878285+00:00
---

**MetaDescription**: Use inline chat and Quick Chat in Visual Studio Code for focused edits, terminal help, and short AI conversations.

# Inline chat and Quick Chat

Inline chat and Quick Chat provide lightweight ways to interact with AI without opening the full Chat view. Use inline chat to generate code or make edits directly in the editor, or to get help with shell commands in the integrated terminal. Use Quick Chat for short questions and interactions.

Use inline chat when you want to make quick, targeted edits within the visible code context. For multi-step tasks, multi-file changes, or broader codebase exploration, use the [Chat view](/docs/agents/run/chat-view.md) instead.

## Use editor inline chat

When you use editor inline chat, your prompt is scoped to the code in the active editor. Inline chat might use the content from other files in your workspace as context for your prompt.

To use editor inline chat:

1. Open a file in the editor.

1. Open editor inline chat by using the ``Shortcut: inlinechat.start`` keyboard shortcut or by selecting **Open Inline Chat** from the Chat menu in the title bar.

1. Type your prompt in the chat input field and press ``Enter``.

    ![Screenshot showing the inline chat control.](images/copilot-chat/inline-chat-control.png)

    > [!TIP]
    > Select a block of code in the editor to scope the prompt to that code.

1. VS Code shows a diff with the code suggestion inline in the editor. Use **Keep** or **Undo** to accept or reject the changes.

    ![Screenshot showing editor inline chat suggesting a non-recursive factorial implementation.](images/copilot-chat/inline-chat-recursion.png)

### Inline chat in active editing sessions

When a file belongs to an active chat editing session, pressing ``Shortcut: inlinechat.start`` opens "Ask in Chat" in the Chat view instead of regular inline chat. This routes your prompt into the existing session so it can use the full conversation context. The editor context menu also shows **Ask in Chat** instead of **Open Inline Chat** for these files.

To always use regular inline chat, even for files that belong to a chat session, set ``inlineChat.askInChat`` to `false`.

On files that don't belong to any chat session, ``Shortcut: inlinechat.start`` always opens regular inline chat, regardless of this setting.

### Show a visual hint on text selection (Experimental)

When you select text in the editor, VS Code can display a visual hint to help you start inline chat for the selected code. Use the ``inlineChat.affordance`` setting to control how this hint appears:

* `off`: no hint is shown when you select text
* `gutter`: the hint appears in the line number area next to your selection
* `editor`: the hint appears at the cursor position within your selection, integrated with the lightbulb for code actions

![Screenshot showing the inline chat hint in the gutter when text is selected in the editor.](images/copilot-chat/inline-chat-hint-gutter.png)

The hint displays an inline chat input box and actions for adding the selection to chat, explaining the code, and starting a code review of the selection.

> [!NOTE]
> This feature is experimental and works with the ``inlineChat.renderMode`` setting set to `hover`.

## Use terminal inline chat

You can bring up terminal inline chat in the [integrated terminal](/docs/terminal/basics.md) to get help with shell commands or ask terminal-related questions.

To use terminal inline chat:

1. Open the terminal in VS Code by selecting the **View** > **Terminal** menu item or using the ``Shortcut: workbench.action.terminal.toggleTerminal`` keyboard shortcut.

1. Start terminal inline chat by using the ``Shortcut: workbench.action.terminal.chat.start`` keyboard shortcut or running the **Terminal Inline Chat** command in the Command Palette.

1. Type your prompt in the chat input field and press ``Enter``.

    ![Screenshot showing that you can ask complex questions like "list the top 5 largest files in the src dir"](images/copilot-chat/terminal-chat.png)

1. Review the response and select the **Run** (``Shortcut: workbench.action.terminal.chat.runCommand``) to run the command in the terminal

    Alternatively, select **Insert** (``Shortcut: workbench.action.terminal.chat.insertCommand``) to insert the command into the terminal and modify it before running.

## Change the model for inline chat

You can change the language model that is used for editor inline chat. To configure the default model for inline chat, use the ``inlineChat.defaultModel`` setting. The setting lists all available models from the model picker.

If you change the model during an inline chat session, the selection persists for the remainder of the session. After you reload VS Code, the model resets to the value specified in the ``inlineChat.defaultModel`` setting.

Learn more about [choosing the right model for your task](/docs/agents/concepts/language-models.md#choose-the-right-model).

## Use Quick Chat

Quick Chat provides a lightweight chat panel that opens at the top of the editor. Use it for quick questions and short interactions without opening the full Chat view or leaving your current workflow.

> [!NOTE]
> Quick Chat in the editor window differs from [quick chats in the Agents window](/docs/agents/run/agents-window.md#start-a-quick-chat), which are workspace-free conversations that appear in the sessions list.

To open Quick Chat, press ``Shortcut: workbench.action.quickchat.toggle`` or select **Quick Chat** from the **Chat** menu in the title bar.

Type your prompt and press ``Enter`` to get a response. Quick Chat supports the same `#`-mentions and `@`-mentions as the Chat view for adding context. Select the **Open in Chat view** button to continue the conversation in the full Chat view.

## Related resources

* [Use chat in VS Code](/docs/chat/chat-overview.md)
* [Add context to your chat prompt](/docs/chat/copilot-chat-context.md)
* [Review AI-generated code edits](/docs/agents/run/review-code-edits.md)
* [AI language models in VS Code](/docs/agent-customization/language-models.md)
