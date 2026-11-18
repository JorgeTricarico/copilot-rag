**MetaDescription**: Add files, symbols, images, browser content, and other context to AI prompts in Visual Studio Code for more relevant responses.

# Add context to chat

Providing relevant context helps the AI give more accurate responses. Add files, folders, symbols, images, web content, and other information directly to your prompt when you want the AI to consider specific details.

> [!NOTE]
> Unless otherwise noted, the features on this page work in both the [Chat view](/docs/agents/run/chat-view.md) and the [Agents window](/docs/agents/run/agents-window.md).

For background on what context is and how VS Code assembles it, see [Context concepts](/docs/agents/concepts/context.md).

## #-mentions

You can explicitly add context to your prompt by typing `#` followed by the context item you want to mention. VS Code supports different types of context items: files, folders, code symbols, tools, terminal output, source control changes, and more.

Type the `#` symbol in the chat input field to see a list of available context items, or select **Add Context** (`+` icon) in the Chat view to open the context picker.

![Screenshot of VS Code Chat view, showing the chat variable picker.](./images/copilot-chat/copilot-chat-view-chat-variables.png)

For tool names and context references, see the [Tools and context reference](/docs/agents/reference/tools-reference.md).

### Add files as context

Agents can use workspace search and file-reading tools to gather relevant context. A workspace index helps locate code, but doesn't attach every file to the conversation. Add specific files, folders, or symbols by using #-mentions or the context picker when you know which sources the agent should consider.

To provide specific files, folders, or symbols as context, add them to the chat using the following methods:

* #-mention the file, folder, or symbol in your chat message by typing `#` followed by the name of the file, folder, or symbol.
    To reference a symbol, make sure to open the file containing the symbol in the editor first.

* Drag and drop files or folders from the Explorer view, Search view, or editor tabs onto the Chat view to add them as context.

* Select **Add Context** (`+` icon) and then **Files** to choose files from disk, or **Symbols** to select a code symbol.

Use `#codebase` to request a search for relevant code across the workspace. It doesn't add the entire codebase to the model's context. Learn about [workspace search and indexing](/docs/agents/reference/workspace-context.md).

#### Attach files from disk

Use the file chooser to attach files outside your workspace, such as a screenshot or UI mockup from your desktop. You don't need to add their folder to the workspace or open a workspace first.

1. Select **Add Context** (`+` icon) > **Files** in the chat input.

1. Choose one or more files, including text files or supported images, and then select **Attach**.

1. Confirm that the attachments appear in the chat input, then enter a prompt about them.

If the selected session supports only image attachments, **Files** filters the chooser to supported images. It doesn't enable ordinary local-file transfer for those sessions.

In sandboxed Copilot harness sessions, attaching a file can grant read access for the session without changing sandbox settings. It doesn't grant write permission or override organization restrictions. See [Read attached files and folders](/docs/agents/run/agent-sandboxing.md#read-attached-files-and-folders).

### Add project and GitHub context

When you start a session in the Agents window, the first folder or repository you select is the primary execution workspace. It determines where the agent runs and changes files.

You can attach project and GitHub context to a request:

* In the Agents window, select **Folder** or **Repository** to attach another project. An attached project provides request context and doesn't become another workspace root.

* In any chat input, select **Add Context** (`+` icon), and then select **Issue...** or **Pull Request...**. If multiple GitHub repositories are available, select a repository before you choose the issue or pull request.

* Paste a GitHub issue or pull request URL directly into the prompt. VS Code automatically adds the item as a context attachment.

You can attach multiple items. The attachments are preserved in a draft and included when you send the request. Learn more about [starting an agent session in the Agents window](/docs/agents/run/agents-window.md#start-an-agent-session).

With ``chat.inlineAttachments.enabled`` enabled (Experimental), you can preview GitHub items in your Chat view draft. Hover over a reference, or highlight it with the arrow keys, to see its title, status, and description. Select it or press ``Enter`` while highlighted to open the item without sending the draft. Press ``Escape`` to dismiss the preview.

### Reference content from the web

You can reference content from the web in your chat prompts, for example to get the latest API reference or code examples.

You can directly include a URL in your prompt to get information from that webpage, or use the `#fetch` tool to indicate that you want to retrieve content from the web. For example:

* `"What are the highlights of the latest VS Code release #fetch"`
* `"Update the asp.net app to .net 9 #fetch https://learn.microsoft.com/en-us/aspnet/core/migration/80-90"`

VS Code caches the content of the web page for a limited time to improve performance. If the content of the page changes, you can force a refresh by restarting VS Code. If the page cannot be reached, the cache will expire after a short time (approximately five minutes).

VS Code prompts for confirmation before accessing external URLs to protect your privacy and security. Learn more about [configuring URL auto-approval](/docs/agents/run/approvals.md#url-approval).

Learn more about [using tools with agents](/docs/agents/run/tools.md).

## @-mentions

Chat participants invoked with `@name` are deprecated and are not supported in the Copilot harness. They remain available for Local harness compatibility `feature(local-harness)`.

Ask Copilot directly about your code, terminal output, or editor settings and attach the relevant context. For domain-specific integrations, use plugins with skills and MCP tools, or extension tools when editor context is required. See [Replace chat participants](/docs/agent-customization/migrate-customizations.md#replace-chat-participants).

## Vision

Chat supports vision capabilities, which means you can attach an image as context to your chat prompt and ask questions about it. For example, attach a screenshot of a block of code and ask to explain it, or attach a sketch of a UI and ask the agent to implement it.

Select a model that supports images to ask questions about visual content. Vision analyzes image input and doesn't generate image output. To generate an image or ask an image model to edit one, use [image generation](/docs/chat/chat-overview.md#generate-and-edit-images) in a Copilot harness session. To highlight details yourself before sending an image, [mark up the attachment](#mark-up-an-image).

> [!TIP]
> You can drag and drop an image from a web browser onto the Chat view to add it as context.

### Capture the VS Code window

On desktop, capture the whole VS Code window or a selected area without saving an image file first:

1. Select a model that supports images. **Screenshot Window** is only available when the selected model and session support image attachments.
1. In the chat input, select **Add Context** (`+` icon) > **Screenshot Window**.
1. When the cursor becomes a camera, select anywhere in the window or press ``Enter`` to capture the whole window. Drag to capture an area instead. Press ``Escape`` to cancel.

The screenshot is attached to the chat input. Add a prompt describing the problem or change you want, then send it.

### Capture another app window

`feature(chat-app-window-screenshots)`

On desktop, attach a screenshot of another app, such as a browser or simulator, to show the agent what you're building.

1. Enable ``chat.appWindowScreenshots.enabled`` if needed. It is on by default in Insiders and off by default in Stable.
1. Focus the chat input where you want the screenshot, then switch to the app you want to capture.
1. Press ``Shortcut: workbench.action.chat.attachAppWindowScreenshot``. VS Code comes to the front with the screenshot attached. If you use the shortcut while VS Code is in front, it captures the app window you just left.

The shortcut works system-wide while the feature is enabled. To choose a window instead, select **Add Context** > **Screenshot App Window**, or run **Chat: Pick App Window to Screenshot** from the Command Palette.

On macOS, follow the setup dialog to grant Screen Recording permission, then restart VS Code. On Wayland, choose the window in the system's window picker.

> [!NOTE]
> The shortcut attaches to the chat input that last had focus. In the Agents window, this can differ from the session selected in the sessions list. Confirm the destination before sending.

### Mark up an image

On desktop, draw, add shapes, arrows, or text, and crop any image attached to the chat input. This works for screenshots and for images you paste or drop into chat.

1. Select **Mark Up** (pencil icon) at the end of the image attachment. Alternatively, open the image preview and select **Mark Up** in its toolbar.
1. Use the drawing and crop tools to highlight the relevant details.
1. Select **Done** to update the attached image, then add your prompt and send it.

Taking a screenshot or marking up an image doesn't send a chat request. Review the image for sensitive content before sending it.

## Add browser context

Use the [integrated browser](/docs/debugtest/integrated-browser.md) to preview web pages and attach information from the current page to a prompt.

The browser toolbar has an **Add to Chat** split button with actions that let you attach different types of context from the current page to your chat prompt:

* **Add Element to Chat**: select HTML elements from the page to add as context, including their CSS styles and screenshots.
* **Add Screenshot to Chat**: capture a screenshot of the current browser viewport and attach it as an image.
* **Add Console Logs to Chat**: capture console output from the page and attach it as context for debugging runtime errors.

Learn how to [add browser context to chat](/docs/debugtest/integrated-browser.md#add-context-to-ai-chat). To let an agent interact with a page instead of attaching it as prompt context, see [browser tools for agents](/docs/debugtest/integrated-browser.md#browser-tools-for-agents).

## Next steps

* [Adapt a prompt to your project](/docs/agents/guides/prompt-examples.md#adapt-an-example-to-your-project) with relevant files, errors, and expected results.
* [Explore a codebase](/docs/agents/guides/explore-a-codebase.md) and verify the explanation against source references.
* If the response misses your intent, [get the agent back on track](/docs/agents/guides/get-agent-back-on-track.md) with focused feedback or a fresh conversation.
