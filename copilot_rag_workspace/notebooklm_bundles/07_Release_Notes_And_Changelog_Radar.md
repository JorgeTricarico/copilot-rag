# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-11-11T19:24:27.303705+00:00
- **Total Palabras**: 18,519 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_145.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_145
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_145.md
- **SHA256_FINGERPRINT**: `e9c0319f506900c85aa6f46f1900f802075b54fff14d437fdb441a35ac39ea26`
- **LAST_VERIFIED_UTC**: 2026-11-10T19:29:14.895709+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.145

# Visual Studio Code 1.145

**Update 1.145.1**: The update addresses these [issues](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aclosed+milestone%3A1.145.1).

**Update 1.145.2**: The update addresses these [issues](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aclosed+milestone%3A1.145.2).

**Update 1.145.3**: The update addresses these [security issues](https://github.com/microsoft/vscode/issues?q=milestone%3A1.145.3+state%3Aclosed+label%3Acandidate).

## Release highlights

This week, your remote agent sessions feel a bit more local. Preview apps and use canvases right in VS Code, fine-tune automation schedules with cron, and turn down the noise in chat. And when you need a break, Blobby is ready to play.

* [Remote agents](#remote-agents): Preview apps and use interactive canvases from remote agent sessions without leaving the Agents window.

* [Automations](#cron-schedules-and-custom-agents-for-local-automations): Run recurring agent tasks on custom schedules beyond the built-in presets with cron.

* [Agent verbosity](#choose-agent-verbosity): Keep chats concise or see the full details of the agent's reasoning and tool calls, your choice.

* [File exclusions](#show-specific-files-in-excluded-folders): Exclude folders while keeping the files you need visible and searchable.

* [Fun](#blobby-jump-game-experimental): Take a short break with a platform-jumping game starring Blobby, the VS Code pet.

## Remote agents

### Browse over remote agent host connections (Preview)

**Setting**: ``workbench.browser.enableRemoteProxy``

When an agent session runs on a [remote agent host](https://code.visualstudio.com/docs/agents/run/remote-agent-sessions), the integrated browser in the Agents window now loads pages through that host, as it already does in [remote workspaces](https://code.visualstudio.com/updates/v1_125#_browse-over-remote-connections-preview). When the agent starts a dev server on the remote machine, you can open it right in the Agents window to preview the app, validate the agent's changes, and give it feedback, as you would in a local session.

![Screenshot showing the URL bar in the integrated browser, showing 'Connected via kyles-mbp'.](images/1_145/remote-browser.webp)

Enable ``workbench.browser.enableRemoteProxy`` to try it out, and file any issues you encounter in the [VS Code repository](https://github.com/microsoft/vscode/issues).

### Remote canvases (Preview)

**Settings**: ``workbench.browser.enableRemoteProxy``, ``chat.canvases.enabled``

Thanks to the remote agent host connections support, you can now also use [canvases](https://code.visualstudio.com/docs/agents/run/canvases) that are hosted on a remote agent host.

Enable ``chat.canvases.enabled`` and ``workbench.browser.enableRemoteProxy`` to try it out, and file any issues you encounter in the [VS Code repository](https://github.com/microsoft/vscode/issues).

## Agents

### Mix and match agent harnesses in one session (Preview)

**Setting**: ``chat.agentHost.multipleChatProviders.enabled``

[Nested sessions](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions#_run-multiple-chats-in-a-session) let you keep related conversations together within a single main chat session. Previously, every nested session inherited its parent session's harness. If you wanted a second opinion from another agent, you had to start a separate session and lose that grouping.

In this release, nested sessions can use different harnesses than their parent session. For example, ask Claude to review the plan that a Copilot chat wrote, or give Codex the same task, side by side in the same session. When you create a new nested session, use the harness picker to switch to a different harness.

Each chat has its own model, agent, and permission levels, based on its harness. Changing them in one chat doesn't affect the others. When you move a chat, it keeps its history and continues with its selected harness. When you fork a nested session, it continues with the same configuration.

A chat that uses a different harness than its session names its harness when you hover over its chat tab or its row in the sessions list.

<video src="images/1_145/multi-harness-session.mp4" title="Video showing a Copilot session in the Agents window where Claude and Codex nested sessions are added through the harness picker, each answering with its own model and permissions." autoplay loop controls muted></video>

Enable ``chat.agentHost.multipleChatProviders.enabled`` to get started. Let us know what you think by [filing an issue](https://github.com/microsoft/vscode/issues).

### Cron schedules and custom agents for local automations

Instead of manually running agent tasks one by one, you can use [automations](https://code.visualstudio.com/docs/agents/run/automations) to schedule and run them automatically, either on demand or on a set schedule.

This release gives you more flexibility for local automations and keeps the Automations view focused on active work:

* **Use cron schedules:** Select **Cron** to enter a five-field cron expression when the other schedule presets aren't precise enough. The dialog validates the expression and describes the resulting schedule. Cron schedules are not available for cloud automations.

* **Use workspace custom agents:** Choose a custom agent from the selected workspace when you create or edit a local automation.

* **Focus on active automations:** Disabled automations appear in a collapsed **Disabled automations** section, so they don't obscure run history and active automations.

![Screenshot showing the Cron schedule editor for a local automation.](images/1_145/cron-automations.webp)

Learn more about [creating and managing agent automations](https://code.visualstudio.com/docs/agents/run/automations).

### Pin canvases to sidebar (Experimental)

**Setting**: ``chat.canvases.enabled``

To make it easier to access frequently used canvases, you can now pin a canvas to appear in the left sidebar. To pin a canvas, open it and select the **Add to Sidebar** button above the canvas. Pinned canvases remain accessible in the sidebar even when you navigate away from them.

<video src="images/1_145/pinned-canvases.mp4" title="Video showing how to pin a canvas to the sidebar in VS Code." autoplay loop controls muted></video>

### Copilot harness

The Copilot harness continues to be the default for new sessions in VS Code. It's our latest harness, built on the Copilot SDK, a shared foundation that helps align behavior, capabilities, and improvements across Copilot products.

When you start a new session, **Copilot** in the harness picker indicates that the session uses the Copilot harness. In VS Code, you can keep Copilot harness sessions running in the background and access them from both the VS Code editor window and the Agents window. These sessions run through the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host).

To help you adopt the Copilot harness with your existing workflows, we've added a [Local-to-Copilot harness transition guide](https://code.visualstudio.com/docs/agents/run/move-to-copilot). It covers customization compatibility, session continuity, and organization rollout and verification.

Thank you for the feedback that continues to shape these improvements. Please continue [filing issues](https://github.com/microsoft/vscode/issues) about your experience, especially if a workflow or integration prevents your organization from moving off the Local harness.

Learn how to [work with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses), or explore the architecture and workflows in the [agent host blog post](https://code.visualstudio.com/blogs/2026/08/26/agent-host-architecture).

### Working set improvements (Experimental)

**Setting**: ``chat.editor.workingSet.enabled``

Last release, we introduced the working set for Copilot harness sessions, letting you review pending agent edits. You can **keep** or **undo** changes, as you could do with the Local harness.

![Screenshot of the working set in Copilot harness sessions.](images/1_145/working-set.webp)

We are further improving the working set experience in Copilot harness sessions:

* Files in WSL, Dev Containers, and SSH workspaces open from the working set on the correct host.
* When several tool calls edit the same file in parallel, the working set tracks those edits and the editor's inline review controls remain available after editing finishes.

The working set functionality remains enabled by default in the editor window. Learn more about [reviewing agent edits with the working set](https://code.visualstudio.com/docs/agents/run/review-code-edits#_review-pending-edits-with-the-working-set), including which edits it tracks.

### Improved guidance when required sandboxing is unavailable

[Agent sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) limits what terminal commands can access, like the file system and network resources. Your organization can require it with managed settings that disallow bypassing the sandbox.

If your organization requires sandboxing but your machine can't run it, the warning banner explains why terminal commands are blocked and how to resolve the problem. It shows the specific cause, such as a missing dependency, and links to troubleshooting steps.

If your account and organization support [cloud sessions (Experimental)](https://code.visualstudio.com/docs/agents/run/cloud-agent-sessions), consider running agent tools in the cloud instead of on your machine.

## Chat

### Choose agent verbosity (Experimental)

**Setting**: ``chat.persistentProgressVerbosity``

Keep long chats readable, or follow the agent's reasoning and tool calls in detail when you need to understand its actions. Open the Chat view's **More Actions** menu and select **View Mode**:

* **Conversation**: Focus on the conversation. Reasoning and tool calls are grouped into collapsed sections between blocks of response text. Expand a section to inspect its details.
* **Verbose**: Follow each step with tool calls expanded, without an internal scrolling limit on tool groups.
* **Compact** (default): Preview tool calls while they run, then collapse completed groups to expandable summary rows.

You can switch modes without starting a new chat. The modes change how the conversation is displayed, not its context or the work the agent performs.

<video src="images/1_145/chat-view-modes.mp4" title="Video showing the same Copilot harness session with GPT-6.1 Terra at default model settings, Interactive mode, and Allow All permissions in Conversation, Verbose, and Compact chat views side by side." autoplay loop controls muted></video>

With persistent progress enabled, the active progress indicator stays above the chat input while you scroll back through a response. If you prefer an animated input border instead, enable ``chat.progressBorder.enabled``.

### Chat performance improvements

Reopen and browse long Copilot harness chats more smoothly. VS Code reuses existing reasoning titles and renders terminal output as you reveal it. Terminal output in restored tool calls is rendered when you expand or reveal it, rather than all at once.

This release also reduces repeated progress updates and layout measurements when restoring and navigating long conversations.

### Inline chat attachments (Experimental)

**Setting**: ``chat.inlineAttachments.enabled``

Keep file references and other context next to the instructions they belong to. Enable this setting to insert attachment pills at the cursor in your prompt, rather than in a separate row above the input.

Move across, select, or delete an attachment pill as a single character. Previous messages keep the pills inline, so references stay with the surrounding instructions.

Inline attachments are on by default in Insiders and off by default in Stable.

![Screenshot showing file and image attachment pills inline with the surrounding text in the chat input.](images/1_145/chat-inline-attachments.webp)

### Attach files from anywhere on your computer

Previously, to give chat a file outside your workspace, such as a screenshot or mockup on your desktop, you had to drag it in from your file manager or ask the agent to find it. Select **Add Context** (`+`) > **Files** to choose one or more files with the standard file dialog, even in a new chat without a workspace. In cloud sessions, the chooser lists only images.

![Screenshot showing the Add Context menu in chat with the Files entry above Image from Clipboard and Screenshot Window.](images/1_145/chat-attach-files-menu.webp)

When [sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) is enabled in Copilot harness sessions, the agent can read the files and folders you attach, even when they're outside the workspace. Each attached path is readable for the rest of the session, but the agent can't write to it, and the access isn't saved to your settings. With Manual permissions, the agent no longer asks before reading an attached file. If your organization's managed settings define their own list of readable paths, attachments aren't added to it.

## MCP

### Support for tools provided by MCP apps

MCP apps are interactive interfaces provided by MCP servers. They can now register tools that the language model can call in its next request.

For example, the [ShaderToy server](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/shadertoy-server) lets the model iterate on shaders in real time.

### Managed MCP allowlist precedence

For MCP servers started by VS Code, the enterprise-managed `allowedMcpServers` list takes precedence over registry-only access, so your organization can approve servers without publishing them to its registry. See the [Enterprise section on managed MCP allowlists](#managed-mcp-allowlists-take-precedence-over-registry-only-access) for configuration details and restrictions.

## Editor Experience

### Show specific files in excluded folders

**Settings**: ``files.exclude``, ``search.exclude``

You can filter which files and folders are shown in the Explorer, Search, and Quick Open by using the ``files.exclude`` and ``search.exclude`` settings.

To keep part of an excluded folder visible, prefix a pattern with `!` in ``files.exclude``. Matching files and folders show in the Explorer, Search, and Quick Open, even when another pattern or `.gitignore` excludes them. Exceptions in ``search.exclude`` apply only to Search and Quick Open.

```json
"files.exclude": {
    "node_modules": true,
    "!node_modules/@types": true
}
```

Exceptions never hide files. Patterns such as `!**/node_modules/@types` match at any depth but can make searches slower.

### Smart subgraph titles in Mermaid diagrams

Edges in [Mermaid diagrams](https://code.visualstudio.com/docs/languages/markdown#_mermaid-diagram-rendering) no longer cover subgraph titles. A title moves to the side when an edge would cross it. With the default `vscode` Mermaid theme, subgraphs are outlined instead of filled, so nested subgraphs stand out.

![Screenshot showing a Mermaid diagram with nested subgraphs before and after the change: edges no longer cross the subgraph titles, and the subgraphs are outlined instead of filled.](images/1_145/mermaid-subgraph-titles-before-after.webp)

## Enterprise

### Organization-required plugins can't be uninstalled

When your organization requires an [agent plugin](https://code.visualstudio.com/docs/agent-customization/agent-plugins), for example with the `enabledPlugins` managed setting, the **Customizations** views previously offered **Uninstall** for it. That action always failed and changed to **Retry Uninstall**, which also failed. The same happened for the prompts, skills, agents, hooks, and MCP servers that the plugin contributes.

```json
{
    "enabledPlugins": {
        "my-plugin@my-marketplace": true
    }
}
```

The **Uninstall** action for these plugins and their contributions is now disabled and a message is shown on hover and keyboard focus. This applies to **Browse**, the plugin details, the plugin editor, and the plugin and MCP server menus.

![Screenshot showing an organization-required plugin in Browse customizations with a disabled Uninstall button and a hover saying the plugin is managed by your organization.](images/1_145/managed-plugin-uninstall-disabled.webp)

### Managed MCP allowlists take precedence over registry-only access

Previously, when an organization limited MCP to servers from its registry and also defined an allowlist in managed settings, VS Code still required each server to be in the registry. Servers that the allowlist approved but that weren't published to the registry couldn't run.

The enterprise-managed `allowedMcpServers` list is now authoritative. A server that matches the list can run even if it isn't in the registry, and a registry server that doesn't match is blocked. For example, the following [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started) allow one remote server and one local server:

```json
{
    "allowedMcpServers": [
        { "serverUrl": "https://mcp.example.com/mcp" },
        { "serverCommand": ["node", "approved-server.js"] }
    ]
}
```

* An empty list (`[]`) blocks all servers. If the list is absent, the registry restriction applies as before.
* User and workspace allowlists can't add servers to the enterprise list.
* `deniedMcpServers` and turning off MCP still take precedence over the allowlist.
* Prefer `serverUrl` and `serverCommand` rules. A `serverName` rule matches a label that the server's author chooses.

> **Note**: This change applies to MCP servers that VS Code starts, not to servers managed by the Agent Host.

## Contributions to extensions

### GitHub Pull Requests

There has been more progress on the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension, which enables you to work on, create, and manage pull requests and issues. New features include:

* The pull request overview timeline shows more events, including label, milestone, and title changes, review requests and dismissals, draft and ready-for-review changes, force pushes, branch restores, auto-merge changes, and merge queue updates.
* Pull request description templates support issue variables such as `${issueTitle}`, `${issueNumber}`, and `${issueNumberLabel}`, filled in from the issue associated with the branch by "Start Working on Issue".
* When you stack pull requests, you're prompted to disable auto-merge on any pull request in the stack that has it enabled.

Review the [changelog for the 0.176.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01760) release of the extension to learn about everything in the release.

## Extension Authoring

### Timeline API finalized

Extensions published to the Marketplace can add their own history to the Timeline view, next to Git commits and Local History. Register providers with `workspace.registerTimelineProvider` for files and folders, or `workspace.registerWorkspaceTimelineProvider` for the whole workspace. Set `TimelineItem.resourceUri` to the resource's content as of that entry so users can compare it with other entries by using **Compare Selected**.

Learn more about the Timeline API in the [Timeline API documentation](https://code.visualstudio.com/api/extension-guides/timeline).

## Fun!

### Blobby jump game (Experimental)

Take a short break with Blobby, the VS Code pet. Enter `/vscode-pet` in chat to show Blobby. On the new-session screen in the Agents window, choose **Play Jump Game** from Blobby's context menu. Hold the spacebar to charge a jump and use the arrow keys to aim for the next platform. The game remembers your high score on this device.

<video src="images/1_145/blobby-jump-game.mp4" title="Video showing Blobby charging jumps, landing on platforms, and increasing the hop counter in the Agents window." autoplay loop controls muted></video>

## Deprecated features and settings

### New deprecations in this release

#### Install Extension tool removed from the Local harness

The **Install Extension** (`#installExtension`) agent tool is no longer available in Local agent sessions. When you create a new workspace from chat, the agent no longer installs extensions. Instead, it adds the extensions the project needs to `.vscode/extensions.json`, so you can review and install them from the Extensions view. When you run a Python cell in a Jupyter notebook without the Jupyter extension, the kernel picker prompts you to install it.

If your custom agents or prompt files reference `#installExtension`, remove that reference.

#### Run VS Code Command tool removed from the Local harness

The **Run VS Code Command** (`#runCommand`) agent tool is no longer available in Local agent sessions. Built-in workflows that relied on it now work without it. For example, when chat diagnoses network issues, it asks you to run **Developer: Chat Diagnostics** and share the report.

If your custom agents or prompt files reference `#runCommand`, remove that reference.

#### Workspace creation tool and slash command removed from the Local harness

The **Create New Workspace** (`#newWorkspace`, previously `#new`) agent tool and the `/new` slash command are no longer available in Local agent sessions. The **Generate New Workspace** link on the Welcome page is also no longer available. The dedicated project-setup skills are removed.

To create a project, open an empty folder and describe the project you want in an agent session. The agent uses its standard tools to create files, run scaffolding commands, and configure tasks.

Remove references to `#newWorkspace`, `#new`, `/new`, `project-setup-info-local`, and `project-setup-info-context7` from your custom agents and prompt files. The `github.copilot.chat.newWorkspaceCreation.enabled`, `github.copilot.chat.newWorkspace.useContext7`, and `github.copilot.chat.useProjectTemplates` settings are also removed. Notebook creation is unchanged.

### Upcoming deprecations

None

## Notable fixes

* When an organization turned off the Claude or Codex agent, users who had picked that agent before got a read-only chat with no input from **New Chat** (`+`), **New Chat Editor**, and new windows. New chats now fall back to the default harness, and an unsent prompt carries over. Your previous choice applies again if the policy is lifted. _[#345207](https://github.com/microsoft/vscode/pull/345207)_

* When an organization set MCP access to registry only in its GitHub Copilot policies, a failed policy refresh, for example from a network error or rate limiting, removed the restriction until the next successful refresh. VS Code now keeps the last known registry policy, and clears it only when GitHub reports that no registry applies. _[#344895](https://github.com/microsoft/vscode/pull/344895)_

## Thank you

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

### Pull requests

Contributions to `vscode`:

* [@bompus (Aaron Queen)](https://github.com/bompus): Refresh markdown preview html before a hidden panel is rebuilt [PR #334681](https://github.com/microsoft/vscode/pull/334681)
* [@cipheraxat (Akshat Anand)](https://github.com/cipheraxat): web: release `code -w -g file:line` once the file's editor closes [PR #344740](https://github.com/microsoft/vscode/pull/344740)
* [@denizguney (Deniz Güney Yıldırım)](https://github.com/denizguney): test: add mock reset configuration and test coverage support [PR #338159](https://github.com/microsoft/vscode/pull/338159)
* [@hardikkaurani (Hardik K)](https://github.com/hardikkaurani): fix(arrays): throw TypeError for negative indices in quickSelect [PR #342816](https://github.com/microsoft/vscode/pull/342816)
* [@hirossan4049 (hirose)](https://github.com/hirossan4049): editorFind: fix swapped findMatch foreground colors (#228782) [PR #270395](https://github.com/microsoft/vscode/pull/270395)
* [@kinqsradio (Anh Dang)](https://github.com/kinqsradio)
  * Fix requireLocalPort for range, regex, and host-and-port rules [PR #344185](https://github.com/microsoft/vscode/pull/344185)
  * Preserve inherited port protocol for exact-port attributes [PR #344764](https://github.com/microsoft/vscode/pull/344764)
* [@nathan-vincent-dev (nathan vincent)](https://github.com/nathan-vincent-dev): Fix typos "curent" and "filterd" [PR #345134](https://github.com/microsoft/vscode/pull/345134)
* [@Nikhil-4404 (Nikhil Kumar)](https://github.com/Nikhil-4404): Fix SSE stream-wide byte order mark handling [PR #344094](https://github.com/microsoft/vscode/pull/344094)
* [@pl4nty (Tom Plant)](https://github.com/pl4nty): win32: fix installer's context menu COM surrogate kill command [PR #344505](https://github.com/microsoft/vscode/pull/344505)
* [@rfeltis (Ralph Feltis)](https://github.com/rfeltis): Log telemetry when the closed-chat promo pip is armed [PR #337997](https://github.com/microsoft/vscode/pull/337997)
* [@RReverser (Ingvar Stepanyan)](https://github.com/RReverser): Fix copilot code reference output channel race [PR #342272](https://github.com/microsoft/vscode/pull/342272)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * fix: task system readiness races [PR #342418](https://github.com/microsoft/vscode/pull/342418)
  * fix: memory leak in terminal auto replies [PR #336022](https://github.com/microsoft/vscode/pull/336022)
* [@spencrr (Spencer Schoenberg)](https://github.com/spencrr): agentHost: add setting to turn off Copilot's Co-authored-by trailer [PR #339437](https://github.com/microsoft/vscode/pull/339437)
* [@VaggelisGian (Vaggelis Giannopoulos)](https://github.com/VaggelisGian): Progress: store scoped while state with start time and delay swapped [PR #332735](https://github.com/microsoft/vscode/pull/332735)
* [@vscodebot-pr (VS Code PR Bot)](https://github.com/vscodebot-pr): fix: guard ListView dynamic-height probe against shrunk model (fixes #333550) [PR #333563](https://github.com/microsoft/vscode/pull/333563)
* [@wozhenbang2004 (Kayokoi)](https://github.com/wozhenbang2004): testing: respect keybindings before type-to-filter [PR #344892](https://github.com/microsoft/vscode/pull/344892)
* [@wycats (Yehuda Katz)](https://github.com/wycats): Recognize userPromptTransformed plugin hooks in Copilot sessions [PR #345068](https://github.com/microsoft/vscode/pull/345068)

Contributions to `vscode-pull-request-github`:

* [@kinqsradio (Anh Dang)](https://github.com/kinqsradio): Fix orphan stack worktree cleanup through macOS path aliases [PR #9100](https://github.com/microsoft/vscode-pull-request-github/pull/9100)
* [@tamird (Tamir Duberstein)](https://github.com/tamird): Batch Git config reads for branch operations [PR #8978](https://github.com/microsoft/vscode-pull-request-github/pull/8978)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_146.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_146
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_146.md
- **SHA256_FINGERPRINT**: `8c558cdf823345cce7a49fab46171309c6a96cbf42f81b162e37ae3929036f26`
- **LAST_VERIFIED_UTC**: 2026-11-11T19:24:20.851579+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.146

# Visual Studio Code 1.146

## Release highlights

Save your brainpower for the work that needs it. Inbox mode keeps the right sessions on your radar while agents take on model comparisons. Shape your agent workspace around the task with chat windows and extensions.

* [Inbox mode (Experimental)](#inbox-mode-for-sessions-experimental): Focus on sessions that need your attention across all your projects, and snooze others for later.

* [Model comparison (Preview)](#model-comparison-improvements-preview): Compare results with Copilot Fusion in the mix, or let an agent run comparisons for you.

* [Chat windows (Preview)](#chat-windows-preview): Give chats their own windows and rearrange chats, editors, and terminals to fit the task.

* [Extensions in the Agents window (Experimental)](#install-and-manage-extensions-in-the-agents-window-experimental): Find and install extensions for a richer agent experience.

* [Local harness deprecation](#copilot-harness-and-deprecation-of-the-local-harness): Move to the Copilot harness before the Local harness is removed in February 2027.

Happy coding!

## Agents

### Copilot harness and deprecation of the Local harness

The Copilot harness is our latest agent harness and has been the default for new sessions since [VS Code 1.143](https://code.visualstudio.com/updates/v1_143#_copilot-harness-as-the-default). It's built on the Copilot SDK, a shared foundation that helps align behavior, capabilities, and improvements across Copilot products. Copilot harness sessions run through the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host), so you can keep them running in the background and access them from both the VS Code editor window and the Agents window. For organizations, the Copilot harness also enforces managed sandbox and permission policies that the Local harness doesn't.

Thank you to everyone who has shared feedback on using the Copilot harness as your default. Your feedback has shaped the harness experience, and it will continue to guide us through this next step. As of this release, the **Local harness is deprecated and will be removed in three months (February 2027)**:

* **Next three months**: You can still use the Local harness while you move your workflows, but it's functionally frozen. New features and improvements will focus on the Copilot harness and are not guaranteed to be supported by the Local harness.
* **After three months**: The Local harness will no longer be available. The `vscode.temporaryDefaultToLocalHarness` enterprise-managed setting, introduced in VS Code 1.142 to [keep the Local harness as the default](https://code.visualstudio.com/docs/enterprise/manage-ai-settings#_keep-local-harness-as-default), will also be removed.

Because the Copilot harness is already the default for new sessions, you might not need to take any new actions. To confirm you're using the Copilot harness, look for **Copilot** in the harness picker when you start a new session:

![Screenshot showing Copilot selected in the harness picker with a hover description of its Copilot SDK and Agent Host integration.](images/1_146/harness-copilot-description.webp)

If you still use the Local harness, plan to move completely to the Copilot harness before February 2027. The [Local-to-Copilot harness transition guide](https://code.visualstudio.com/docs/agents/run/move-to-copilot) covers customization compatibility, continuing existing Local conversations, and organization rollout and verification. If you run into any problems, let us know by [filing an issue](https://github.com/microsoft/vscode/issues).

### Inbox mode for sessions (Experimental)

**Setting**: ``sessions.list.inboxEnabled``

Keep track of your agents without checking each workspace. Inbox mode gives you one view of what needs your attention, what's still running, and what's ready to merge.

Enable the ``sessions.list.inboxEnabled`` setting (off by default), and then select **Grouping > Inbox Mode** in the Agents window's sessions list.

![Screenshot showing Inbox Mode selected in the Grouping menu in the Agents window.](images/1_146/sessions-inbox-mode.webp)

Sessions that need your attention appear at the top, above the **Working**, **Ready to merge**, **On hold**, and **Done** groups. If a session can wait, use **Dismiss from Inbox**, **Put on Hold**, or **Snooze** to set it aside. Select **Undo** if you change your mind.

Dismissing a session doesn't archive it. To archive it, select **Mark Session as Done**.

![Screenshot showing sessions needing attention in the Inbox above the Working, Ready to merge, On hold, and Done categories.](images/1_146/sessions-inbox.webp)

### Session list inline actions (Experimental)

**Setting**: ``sessions.list.inlineActions``

Fix failing checks and address review comments directly from the Agents window's sessions list. Enable this setting (off by default) to show inline actions for fixing checks, addressing comments, or both.

Each action sends a request to that row's session or nested session in the background without opening it. The setting does not enable Agent Merge or change action permissions.

![Screenshot showing an Address Comments button beneath a session in the Agents window's sessions list.](images/1_146/inline-session-actions.webp)

### Chat windows (Preview)

**Setting**: ``sessions.chatWindows.enabled``

When several chats run at once, keeping them all in one Agents window means switching between them and losing sight of the one you are waiting on. With chat windows, you can open a chat in a window of its own, and arrange that window so that the chat, its editors, and its terminals fit the task.

To try this preview feature in Stable, enable ``sessions.chatWindows.enabled``. It is enabled by default in VS Code Insiders, and off by default in Stable.

Learn more about [chat windows](https://code.visualstudio.com/docs/agents/run/agents-window#_open-chats-in-separate-windows) in our documentation.

To open a chat in a new window, right-click the session or chat in the sessions list and select **Open in** > **New Window**. You can also drag a chat out of the Agents window to create a new window. You can move it back with the **Move to Main Window** command.

The following video shows opening a chat in its own window.

<video src="images/1_146/chat-windows-open.mp4" title="Video showing a chat opened in a new window from the Agents window, with the chat beside its editors." autoplay loop controls muted></video>

A chat window can hold several chats from one or more sessions: pick another session in its title bar, drag a chat in from another window, or select **New Session** (``Shortcut: sessions.chatWindow.newSession``) at the left of the title bar to start a new session in that window. Chat windows reopen with their chats and editors after you restart VS Code.

The content within a chat window is organized into parts, which you can arrange freely to fit your workflow.

* **Move parts:** Drag a part by the grabber on the top edge of its card to another side of the window, or beside another part. You can also use **Move Part Left**, **Move Part Right**, **Move Part Up**, and **Move Part Down**.
* **Move tabs between parts:** Drag a tab to another part, or drop it on a part's edge to split that part. Use **Move Editor to Part** or **Move Editor into New Part Left/Right/Above/Below** to do the same from the Command Palette. Drag an editor tab onto the chat input to attach it to the chat as context.
* **Place the terminal:** Dragging the terminal under the editor or under the chat sets **Terminal Position** to **Under Editor** or **Under Chat**. Dropping it on the bottom edge of the window sets **Full Width**. You can also change the position from the **...** menu of the terminal.
* **Switch the layout:** Use **Configure Layout** in the title bar to show the chat, the editor, or both, side by side or stacked. In the stacked layout, **Agents: Toggle Chat Conversation** collapses the chat to only its input, so the editor takes the rest of the window.

Use **Developer: Reset Chat Window Layout** to return a window to how it first opened.

The following video shows rearranging a chat window and resetting its layout.

<video src="images/1_146/chat-windows-layout.mp4" title="Video showing parts and tabs of a chat window being rearranged, and the layout being reset." autoplay loop controls muted></video>

Let us know what you think by [filing an issue](https://github.com/microsoft/vscode/issues).

### Install and manage extensions in the Agents window (Experimental)

The **Extensions** section of Agent Customizations lets you choose which installed extensions run in the Agents window without changing their enablement in editor windows. Previously, adding an extension meant switching to an editor window to install it. In this release, you can find, install, and uninstall extensions without leaving the Agents window:

* **Install from the Marketplace**: Searching also queries the Marketplace and lists matching extensions that you don't have yet, with their publisher, install count, and rating. Installing an extension adds it to VS Code and enables it in the Agents window. To install a different version, such as a pre-release, use the dropdown next to **Install**.
* **Know what won't work before installing**: Extensions that contribute views, debuggers, status bar items, or walkthroughs without declaring support for the Agents window show a warning that lists the unsupported features. Extensions that can't be installed, for example because your organization doesn't allow them, show the reason.
* **Open with a keyboard shortcut**: Press ``Shortcut: workbench.view.extensions`` or run **Extensions: Manage Extensions** to open the section. If you changed the shortcut for the Extensions view in editor windows, your shortcut also works in the Agents window.

![Screenshot showing the Extensions section in the Agents window.](images/1_146/extensions-agents-window.webp)

### Model comparison improvements (Preview)

**Setting**: ``sessions.chat.compareAgents.tools.enabled``

[Compare Models](https://code.visualstudio.com/docs/agents/run/compare-models) in the Agents window lets you run the same prompt across models, evaluate their results with a judge, and combine their strengths with a synthesizer. This release makes comparisons easier to configure, organize, and automate:

* **Judge and synthesize chat-only responses**: Add a judge and synthesizer without selecting a workspace. Synthesis starts when you select **Synthesize** and creates a new chat without changing the original attempts.
* **Compare Copilot Fusion**: Select Fusion and its supported effort tiers for an attempt, the judge, or the synthesizer.
* **Let an agent run evaluations (Experimental)**: Enable ``sessions.chat.compareAgents.tools.enabled`` to let agents discover models, launch comparisons, and read results and conversation references to summarize findings across scenarios. The tools are off by default and require Compare Models to be enabled. Disabling them still leaves manual comparisons available.

### Canvases improvements (Preview)

**Setting**: ``chat.canvases.enabled``

[Canvases](https://code.visualstudio.com/docs/agents/run/canvases) are shared, interactive surfaces where you and Copilot work together on plans, dashboards, and other artifacts. This release adds permission prompts and improves canvas discovery and continuity:

* **Permissions for canvas extensions**: In Copilot harness sessions, canvas extensions ask for your approval before initializing privileged capabilities, such as hooks.
* **Find and reopen canvases**: Canvas menus distinguish **Running** canvases from **Available** canvases you can create new instances for. In the Agents window, actions to create or install canvases appear under **Discover More**.
* **Resume without another prompt**: When you return to an inactive Copilot harness session, its canvases restore without sending another message.
* **Smoother reconnection**: While a canvas provider restarts, the last canvas image stays visible with a reconnecting indicator.
* **Keep canvases with their chats**: In separate chat windows, canvas tabs close when their chat leaves the window and can reopen alongside it. Canvases also restore after a window reload without taking focus.

### Configure computer sharing (Experimental)

**Setting**: ``sessions.chat.experimental.remoteEnvironmentsThisComputer``

The Remote Environments editor in the Agents window is a central place for managing remote connections. In this release, you can now manage how this computer is shared with other clients. Regardless of whether sharing is enabled, local sessions continue to run directly on this computer.

Share this computer through GitHub Environments or Dev Tunnels, or turn sharing off. You can also change the computer name that other clients see.

Open the editor with **Manage Remote Environments** from the Environment picker in chat, the Command Palette, or the title bar's **Remote Connections** menu (antenna icon), which also offers the same sharing options.

![Screenshot showing the This Computer section of the Remote Environments editor, sharing via Dev Tunnels under the name dev-workstation, above the Other Environments table.](images/1_146/remote-environments-this-computer.webp)

Learn more about [making a host available for remote access](https://code.visualstudio.com/docs/agents/run/remote-agent-sessions#_make-a-host-available-for-remote-access).

### Agent Host support for virtual repositories

VS Code supports virtual workspaces, allowing you to do things like [viewing a GitHub repository without having to clone it](https://code.visualstudio.com/docs/sourcecontrol/github#_github-repositories-extension).

The Copilot harness previously did not work in virtual repositories. In this release, we added support for virtual repositories, so you can use the same Copilot features and workflows as you do in local folders.

## Chat

### Continue a Copilot CLI session in VS Code (Experimental)

When you're working with the [GitHub Copilot CLI](https://github.com/features/copilot/cli) in a terminal outside VS Code, you can now move the session into VS Code and keep going.

Enter `/code` in the CLI, or `/code-insiders` for VS Code Insiders. The CLI exits, and VS Code opens the same session in the Chat view of the window for the session's folder, starting VS Code if it isn't running. The session keeps its conversation history, its model and reasoning effort, and its mode and permissions.

<video src="images/1_146/copilot-cli-code.mp4" title="Video showing the /code-insiders command in the Copilot CLI launching VS Code Insiders, which opens the same session in the Chat view with its history, model, and permissions." autoplay loop controls muted></video>

The `/code` command is experimental in Copilot CLI. It requires Copilot CLI 1.0.107 or later, with experimental features turned on (`/settings experimental on`). Permissions that apply only to the CLI process, such as `--allow-tool` or approvals you granted for the session, don't carry over, and the CLI lists them before handing off. If another Copilot CLI process still has the session open, VS Code asks before opening it. To return to the CLI, run the `copilot --resume` command that the CLI shows when it hands off.

### Configurable shortcut for the background send action

**Setting**: ``chat.sendInBackgroundTip.enabled``

Start a new session without opening it by pressing ``Shortcut: sessions.sendInBackground`` in the Agents window composer. You can rebind or remove the shortcut for **Chat: Send in Background** in **Keyboard Shortcuts**.

An optional tip shows your configured shortcut and links to **Keyboard Shortcuts**. Enable it with ``chat.sendInBackgroundTip.enabled`` (Experimental, off by default).

## MCP

### Skills over MCP (Preview)

**Setting**: ``chat.agentHost.mcpSkills.enabled``

This release of VS Code adds support for SEP-2640 [Skills over MCP](https://github.com/modelcontextprotocol/ext-skills), allowing MCP servers to automatically provide skills to the model.

The first time you connect to an MCP server that provides skills, you are asked to allow them into your model context. Afterwards, the model can interact with these skills and you can see them on the **Skills** tab of the Agent Customizations editor.

## Trust and security

### Improved permission prompts

The Copilot harness previously suggested overly broad tool-level allowances for operations like web fetches, terminal commands, and file reads. For example, the default action for fetching a URL was "Allow in this Session", which would let the model access any URL during that session.

Now, permission prompts are more granular, by default adding allowances for specific domains, commands, and directories.

### Mask environment variables in the sandbox

**Setting**: ``chat.agent.sandbox.credentials.envVars``

To protect sensitive information, you can configure which environment variables are masked in sandboxed sessions and hidden from agent tools. Sandboxed tools receive placeholders, and the real values are supplied only to approved HTTPS destinations.

In this example, sandboxing replaces the value of the `API_TOKEN` environment variable with a placeholder. The real value is restored only in outgoing HTTPS requests to hosts listed in `injectHosts`, here `api.example.com`. Requests to other hosts retain the placeholder and don't receive the actual value.

```json
{
    "chat.agent.sandbox.credentials.envVars": {
        "API_TOKEN": {
            "injectHosts": ["api.example.com"]
        }
    }
}
```

Enter variable names, not secret values, in settings. On Windows, environment variable masking requires local-network access. On macOS and Windows, trust the sandbox CA certificate for tools that require OS certificate trust.

See [sandbox network access](https://code.visualstudio.com/docs/agents/run/agent-sandboxing#_configure-network-access) and [certificate trust](https://code.visualstudio.com/docs/agents/run/agent-sandboxing#_trust-the-sandbox-ca-certificate-on-windows-and-macos) for more information.

### Sandbox status in the chat input

See whether terminal sandboxing is enabled without opening the Permissions menu. In both the editor and the Agents window, the empty chat input shows **(sandbox enabled)** when **Sandboxing for terminal** is on. The placeholder stays in sync as you switch chats or change the setting.

![Screenshot showing the chat input placeholder reading Chat with Copilot (sandbox enabled).](images/1_146/sandbox-enabled-placeholder.webp)

## Accessibility

### Visible keyboard focus on Welcome

The Welcome page shows a visible outline when the page itself has keyboard focus, so you can track your position while navigating. The page remains focusable for screen reader users.

## Editor Experience

### Mermaid 12 support

VS Code now uses Mermaid 12 when rendering Mermaid diagrams in chat, Markdown previews, and notebooks. You can use new diagram types, including use-case diagrams, and benefit from updated automatic layout behavior.

| Before: Mermaid 11 | After: Mermaid 12 |
| --- | --- |
| ![Screenshot showing Mermaid 11 rendering with older flowchart and subgraph layouts and a use-case diagram error.](images/1_146/mermaid-11.png) | ![Screenshot showing Mermaid 12 rendering with updated flowchart and subgraph layouts and a rendered use-case diagram.](images/1_146/mermaid-12.png) |

### Copy the address of local HTML files in the Integrated Browser

When you preview a local HTML file in the [Integrated Browser](https://code.visualstudio.com/docs/debugtest/integrated-browser), you can select and copy its `file://` address to paste it into an external browser or a terminal.

## Enterprise

### Copilot sessions behind enterprise proxies

Copilot sessions follow VS Code's [proxy configuration](https://code.visualstudio.com/docs/setup/network), including proxy auto-configuration (PAC) and Kerberos authentication, when running locally, in WSL, or in a local Dev Container. Your organization's routing rules can select different proxies or a direct connection for each destination, rather than forcing requests through a single proxy.

### Organization help links for policy restrictions

Organizations can direct blocked developers to their own help page by setting `communication.support.url` in [enterprise-managed settings](https://code.visualstudio.com/docs/enterprise/manage-ai-settings). We recommend pointing this URL to a page where employees can find their organization's Copilot usage policies and support guidance. A valid absolute HTTP or HTTPS URL adds **Contact Admin** links to supported policy restrictions, such as disabled Agents or organization-disabled models.

For example, in your organization's managed settings:

```json
{
  "communication": {
    "support": {
      "url": "https://ai.example.com/your-companys-ai-landing-support-page"
    }
  }
}
```

### Enterprise controls for canvas extensions

In Copilot harness sessions, `strictPluginOnlyCustomization` already restricted standalone skills, agents, hooks, and MCP servers. It now also blocks standalone canvas extensions from user, project, and session directories, so administrators can require that any canvas extensions used come from eligible plugins.

In [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started), use `true` to block all supported standalone categories while allowing eligible plugin content:

```json
{
  "strictPluginOnlyCustomization": true
}
```

To restrict only selected categories, replace `true` with a list containing any of `"skills"`, `"agents"`, `"hooks"`, `"mcp"`, and `"extensions"`.

> **Note:** VS Code's boolean-only `ChatStrictPluginOnlyCustomization` policy does not control canvas extensions. The Copilot SDK manages them, so use the Copilot managed setting above.

See the [enterprise-managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings) for policy details.

## Deprecated features and settings

### New deprecations in this release

* [The Local harness is deprecated](#copilot-harness-and-deprecation-of-the-local-harness) and will be removed in February 2027.

### Upcoming deprecations

None

## Notable fixes

### Fixed overcounting in agent edit metrics

Agent edit metrics reported through [GitHub Copilot usage metrics](https://docs.github.com/en/copilot/reference/copilot-usage-metrics) no longer count unchanged text between edits as newly added or deleted code.

## Thank you

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

### Pull requests

Contributions to `vscode`:

* [@Aditya-kumar-yadav (Aditya Kumar Yadav)](https://github.com/Aditya-kumar-yadav): terminal: fix collapseTildePath substring collisions and exact home collapse [PR #343203](https://github.com/microsoft/vscode/pull/343203)
* [@alok-108 (Alok Pandey)](https://github.com/alok-108): debug: send the mode of exception breakpoints to the debug adapter [PR #341972](https://github.com/microsoft/vscode/pull/341972)
* [@andysalerno (Andy Salerno)](https://github.com/andysalerno): Show Copilot Fusion reasoning in the agent host chat [PR #346434](https://github.com/microsoft/vscode/pull/346434)
* [@Carrotstudiosoftwarehouse (Carrotstudio.it)](https://github.com/Carrotstudiosoftwarehouse): Keep the full URI reachable in the prompt URL confirmation dialog [PR #332937](https://github.com/microsoft/vscode/pull/332937)
* [@Chethan616 (Chethan Krishna)](https://github.com/Chethan616): Fix terminal not focusing when clicking blank space below inline chat widget [PR #334804](https://github.com/microsoft/vscode/pull/334804)
* [@ericbaum (Eric Baum)](https://github.com/ericbaum): mcp: use URI-backed defaultCwd for home-directory discovery adapters [PR #345650](https://github.com/microsoft/vscode/pull/345650)
* [@genius-0963 (Saurabh Sungh)](https://github.com/genius-0963): Fix #345692: Preserve draft open editors when replacing new draft session [PR #345807](https://github.com/microsoft/vscode/pull/345807)
* [@LuisPeixoto (Luis Peixoto)](https://github.com/LuisPeixoto): Fix Hooks section description [PR #346593](https://github.com/microsoft/vscode/pull/346593)
* [@maxteneff (Max Bartenev)](https://github.com/maxteneff): Fix parentTerminal being ignored for terminals that have already opened [PR #342420](https://github.com/microsoft/vscode/pull/342420)
* [@mcumming (Michael Cummings (MSFT))](https://github.com/mcumming)
  * Fix marketplace 403 responses prompting repeated sign-in [PR #343686](https://github.com/microsoft/vscode/pull/343686)
  * Private Marketplace extension blocking: add workbench UX and update gating [PR #341049](https://github.com/microsoft/vscode/pull/341049)
  * Do not forward request credentials across origins on redirects [PR #343690](https://github.com/microsoft/vscode/pull/343690)
  * Cache and coalesce marketplace protected resource discovery [PR #343687](https://github.com/microsoft/vscode/pull/343687)
* [@minwookshin (Minwook Shin)](https://github.com/minwookshin): Honor explicit inline edit gutter menu visibility [PR #339575](https://github.com/microsoft/vscode/pull/339575)
* [@monil-patel](https://github.com/monil-patel): Allow Policy Helper registration through VS Code settings [PR #345712](https://github.com/microsoft/vscode/pull/345712)
* [@nkramber](https://github.com/nkramber)
  * Keep terminal editors working after moving them to another editor group [PR #339488](https://github.com/microsoft/vscode/pull/339488)
  * Find terminal profiles at the login shell path when it's not on PATH [PR #339556](https://github.com/microsoft/vscode/pull/339556)
* [@RealThanhNguyxn (Thanh Nguyen)](https://github.com/RealThanhNguyxn): Preserve unresolved variables in process task command path (fixes #160891) [PR #316369](https://github.com/microsoft/vscode/pull/316369)
* [@rksharma-owg (RKS)](https://github.com/rksharma-owg)
  * tasks: pass task type through ITaskHandleDTO to prevent provider fanout [PR #336159](https://github.com/microsoft/vscode/pull/336159)
  * Flush final task markers before completion notification [PR #339551](https://github.com/microsoft/vscode/pull/339551)
  * Preserve distinct task errors from the same resource [PR #339550](https://github.com/microsoft/vscode/pull/339550)
* [@ShehabSherif0 (Shehab Sherif)](https://github.com/ShehabSherif0): Fix duplicated condition in accessibility signal property change detection [PR #303604](https://github.com/microsoft/vscode/pull/303604)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * perf: make the Test Explorer faster when running many tests [PR #345896](https://github.com/microsoft/vscode/pull/345896)
  * fix: memory leak in notebook text diff editor [PR #331805](https://github.com/microsoft/vscode/pull/331805)
  * fix: memory leak in color picker [PR #345461](https://github.com/microsoft/vscode/pull/345461)
  * fix: memory leak in aiSearchModel [PR #342528](https://github.com/microsoft/vscode/pull/342528)
  * fix: memory leak in file search listeners [PR #345781](https://github.com/microsoft/vscode/pull/345781)
  * fix: memory leak in terminal find widget [PR #346139](https://github.com/microsoft/vscode/pull/346139)
  * fix: memory leak in search progress emitter [PR #346126](https://github.com/microsoft/vscode/pull/346126)
  * perf: reduce memory usage by 24 kB [PR #342397](https://github.com/microsoft/vscode/pull/342397)
  * fix: task provider counter bug [PR #339387](https://github.com/microsoft/vscode/pull/339387)
  * fix: memory leak in marker resource maps [PR #346501](https://github.com/microsoft/vscode/pull/346501)
  * fix: memory leak in debouncedObservable [PR #346498](https://github.com/microsoft/vscode/pull/346498)
  * fix: memory leak in keybindings search [PR #346268](https://github.com/microsoft/vscode/pull/346268)
* [@sumit-2007-git (Sumit kumar)](https://github.com/sumit-2007-git): fix(chat): truncate suggested prompt titles to prevent overflow in narrow chat (fixes #275257) [PR #345436](https://github.com/microsoft/vscode/pull/345436)
* [@vscodebot-pr (VS Code PR Bot)](https://github.com/vscodebot-pr)
  * fix: guard terminal scroll operations before renderer is attached (fixes #339313) [PR #339330](https://github.com/microsoft/vscode/pull/339330)
  * fix: guard notebook cursor-selection reveal during cell disposal (fixes #328986) [PR #329000](https://github.com/microsoft/vscode/pull/329000)
* [@xingsy97 (xingsy97)](https://github.com/xingsy97): terminal: fix type-ahead prediction incorrectly rejecting valid style sequences [PR #305103](https://github.com/microsoft/vscode/pull/305103)
* [@zohnannor](https://github.com/zohnannor): fix: remove regression causing minimap to always have opacity [PR #311689](https://github.com/microsoft/vscode/pull/311689)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_147.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_147
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_147.md
- **SHA256_FINGERPRINT**: `539f4bd59be7a55fc9cf4fbf43403dd940782111a8e5e40d97224bea1983a35c`
- **LAST_VERIFIED_UTC**: 2026-11-11T05:26:59.728729+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.147 (Insiders)

# Visual Studio Code 1.147

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: November 10, 2026_

Welcome to the 1.147  release of Visual Studio Code.

Happy Coding!

---

## November 10, 2026

* Group **On hold** sessions by workspace in inbox mode (Experimental). _[#347140: On Hold is too limiting. I'm gonna end up having many many things "on hold"](https://github.com/microsoft/vscode/issues/347140)_
* Add an inline **Merge Pull Request** action for eligible sessions in inbox mode (Experimental). _[#346936: Inbox mode: Ready to Merge sessions have no inline Merge action](https://github.com/microsoft/vscode/issues/346936)_
* Hide empty categories in inbox mode (Experimental), while keeping **Inbox** visible. _[#346938: Inbox mode: Empty sections take up too much vertical space](https://github.com/microsoft/vscode/issues/346938)_
* Hover over a Compare Models (Preview) parent chat in the Agents window to see its original settings. _[#347109: Model compare: show original settings on hover of the parent chat](https://github.com/microsoft/vscode/issues/347109)_
* Shorten worktree cleanup confirmations while retaining the session restoration reminder. _[#347134: Worktree cleanup confirmation is unncessarily wordy](https://github.com/microsoft/vscode/issues/347134)_
* Add a one-time custom-agent tip in **Add Context**. _[#347399: Show a one-time tip for custom agents in the Add Context menu](https://github.com/microsoft/vscode/issues/347399)_

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_340685
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/340685
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/340685
- **SHA256_FINGERPRINT**: `438282fc27afeb01c2d44ec01629bb43339cc5959e6595f8c153584d05c387e8`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.169852+00:00
---

# VS Code Insiders Roadmap: 1.142.0 Endgame
- **Issue Number**: #340685
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/340685

[Endgame guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md)

# Before Monday 6AM Zurich time

`@team`:
- Update endgame availability
- Test plan items created
- Milestone only has TPIs. All other issues need to be closed
- All closed issues in milestone labeled `on-testplan`, `bug`, or `verification-needed`
- Verification steps added to `bug` and `verification-needed` issues

# Monday morning  (Zurich)

`@endgame-champ`:
- [x] Unpin the previous endgame plan from the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Pin this endgame plan in the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Assign TPIs
  - [x] Create TPI's for all verification needed bugs. Visit `Testing and Verification` on tools site, and generate groupings, then create TPIs. The TPI section below  will update with all of the generated items.
- [x] Pause automatic releases (this also ensures chat-pre-release isn't released) after 10am. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=383))
- [x] Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow

  - PRs opened with auto-merge enabled — ensure they get reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/340991
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/340990

  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [ ] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.142.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.142.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [x] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
- [ ] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [x] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [x] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [x] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [x] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [x] Build stable from release/<x.y> and release to MSFT folks
  - [x] Reenable automatic releases
    - A build is scheduled for 7:00 PM Zurich time (`19:00 GMT+2`); make sure automatic releases are reenabled before then so we get an Insiders build from `main` on Tuesday evening.

# Tuesday afternoon/Wednesday morning

- In extreme cases, accept candidate changes
    - [x] Build stable from `release/<x.y>`. Do *not* bump the VS Code version.
    - [x] Release stable to MSFT folks

# Wednesday
`@endgame-champ`:
- [x] Publish website so that in-product release notes are ready
- [x] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [x] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [x] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
- [x] Publish socials (ping Cynthia)
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [x] Create an official release
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [x] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [x] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_341510
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/341510
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/341510
- **SHA256_FINGERPRINT**: `91a5fdaa0a2097e17e5773dcfa339cef278e82b284fdbe6a8ed7d46754263b69`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.168782+00:00
---

# VS Code Insiders Roadmap: 1.141.2 Endgame
- **Issue Number**: #341510
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/341510

- [x] Create a milestone `1.141.2` **@alexr00**
- [x] Bump the version number & run `npm i` to bump `package-lock.json` as well. Ensure there are no other `package-lock.json` changes. **@alexr00**
- [x] [🔖candidate issues](https://github.com/issues?q=org%3Amicrosoft%20is%3Aissue%20milestone%3A%221.141.2%22%20label%3Acandidate)
- [x] Assign candidate issues to the recovery milestone **team**
- [x] Review the `candidate` issues, and if they pass the review assign them to the recovery milestone **team**
- [x] All `candidate` fixes are peer reviewed and pushed to `main` and then cherry-picked into the release branch **team**
- [x] Initiate `insiders` build from `main`
- [x] Issues are tested in the `insiders` **team**
- [ ] Build and manually release Insider from main branch for vscode.dev (if there were vscode.dev candidates)
  - [ ] Issues are tested in the `insiders` **team**
- [x] Build `stable` for all platforms from release branch **@alexr00**
- [x] Issues are verified on `stable` build and the `verified` label is added **@alexr00**
- [x] Check `https://github.com/Microsoft/vscode/compare/release/<x.y>` to ensure no other commits have been made in the release branch **@alexr00**
- [x] The `insiders` build with all candidate fixes needs to be in the wild for 24 hours before recovery release, unless explicitly approved by @kieferrm
- [x] Update the release notes and include a link to a query for the fixed issues @ntrogh
- [x] Publish website @ntrogh
- [x] Publish stable build **@alexr00**
- [ ] (if there were vscode.dev candidates) Trigger the [vscode.dev Deploy pipeline](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) for `release/x.y` for the `prod` deployment target. **@alexr00**
  - [ ] Request approval from another team member at the necessary step to deploy the vscode.dev build. **@alexr00**
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals) **@alexr00**
- [x] Create an official release **@alexr00**
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z> release/<x.y>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right `... > Create Release`. Use the correct title and description from our release notes. [Example](https://github.com/microsoft/vscode/releases/tag/1.81.1)
- [x] Close the milestone on [GitHub](https://github.com/microsoft/vscode/milestones) **@alexr00**


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_342482
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/342482
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/342482
- **SHA256_FINGERPRINT**: `2a890fa1bfd88d4f3d5a78550370cb3eac60947d8af3c060aa0b0f156dd1e49d`
- **LAST_VERIFIED_UTC**: 2026-10-22T16:53:38.324435+00:00
---

# VS Code Insiders Roadmap: 1.143.0 Endgame
- **Issue Number**: #342482
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/342482

[Endgame guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md)

# Before Monday 6AM Zurich time

`@team`:
- Update endgame availability
- Test plan items created
- Milestone only has TPIs. All other issues need to be closed
- All closed issues in milestone labeled `on-testplan`, `bug`, or `verification-needed`
- Verification steps added to `bug` and `verification-needed` issues

# Monday morning  (Zurich)

`@endgame-champ`:
- [x] Unpin the previous endgame plan from the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Pin this endgame plan in the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Assign TPIs
  - [x] Create TPI's for all verification needed bugs. Visit `Testing and Verification` on tools site, and generate groupings, then create TPIs. The TPI section below  will update with all of the generated items.
- [x] Pause automatic releases (this also ensures chat-pre-release isn't released) after 10am. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=383))
  - [486055](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486055&view=results) succeeded.
- [x] Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow
  - [Start Endgame run](https://github.com/microsoft/vscode-engineering/actions/runs/39207024336) succeeded.

  - PRs opened with auto-merge enabled — ensure they get reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/342485
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/342484

  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [ ] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.143.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.143.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [x] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
- [ ] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [x] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [x] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
      - [Acknowledgements commit](https://github.com/microsoft/vscode-docs/commit/7a1efd2c6c2c4dbc283759f337c5d52669ff07c3).
    - [ ] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [x] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
    - [Build 486707](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486707&view=results) published (sanity failures); [release 486751](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486751&view=results) succeeded.
  - [x] Build stable from release/<x.y> and release to MSFT folks
    - [Build 486708](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486708&view=results) published (sanity failures); [internal release 486750](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486750&view=results) succeeded.
  - [x] Reenable automatic releases
    - [486752](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=486752&view=results) succeeded.
    - A build is scheduled for 7:00 PM Zurich time (`19:00 GMT+2`); make sure automatic releases are reenabled before then so we get an Insiders build from `main` on Tuesday evening.

# Tuesday afternoon/Wednesday morning

- In extreme cases, accept candidate changes
    - [x] Build stable from `release/<x.y>`. Do *not* bump the VS Code version.
      - [487217](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487217&view=results) published `2d0b7506` with warnings.
    - [x] Release stable to MSFT folks
      - [487314](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487314&view=results) succeeded, target `2d0b7506`.

# Wednesday
`@endgame-champ`:
- [x] Publish website so that in-product release notes are ready
  - [Production 487477](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487477&view=results) succeeded; [release notes live](https://code.visualstudio.com/updates/v1_143).
- [x] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
  - [487478](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487478&view=results) started at 20%, target `2d0b7506`. Configured end: Oct 28, 06:13 UTC.
- [x] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
    - [Candidate 485945](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=485945&view=results) / [sanity log](https://dev.azure.com/monacotools/Monaco/_apis/build/builds/485945/logs/178): **12 passing**, on Insiders; host commit `f82b72f8`.
  - [x] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
    - [488021](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=488021&view=results): production deployment succeeded in all three regions.
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
  - [488023](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=488023&view=results): publish pipeline succeeded for `0.71.0`; [public npm](https://registry.npmjs.org/@vscode%2fchat-lib/0.71.0) still returns 404 (16:35 Zurich).
- [x] Publish socials (ping Cynthia)
  - [Cynthia: published social posts](https://vscodeteam.slack.com/archives/CG14A4G3Z/p1792615182045779).
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
  - N/A: documentation-only diff; no API signature changes. Publication skipped per endgame champ.
- [x] Create an official release
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
    - [Tag 1.143.0](https://github.com/microsoft/vscode/tree/1.143.0) → `2d0b7506`, matching [shipped Stable](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487478&view=results).
  - [x] Push the tag: `git push origin <x.y.z>`
    - [Remote tag ref](https://api.github.com/repos/microsoft/vscode/git/ref/tags/1.143.0) verified.
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
    - [GitHub release 1.143.0](https://github.com/microsoft/vscode/releases/tag/1.143.0) published.
- [x] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [x] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded
  - [487914](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=487914&view=results) passed build/sanity; [public update API](https://update.code.visualstudio.com/api/update/win32-x64-user/insider/087f03b7b82a0c89753986603421c3d24a24cd41) served `c8f3fd17` (Oct 22).


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_343623
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/343623
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/343623
- **SHA256_FINGERPRINT**: `18426cbb8b6205a79d6152b929b14ae7359f837df212c27a17d405b8c5051841`
- **LAST_VERIFIED_UTC**: 2026-10-30T05:00:19.910662+00:00
---

# VS Code Insiders Roadmap: 1.143.1 Endgame
- **Issue Number**: #343623
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/343623

- [x] Create a milestone `1.143.1` **@hediet**
- [x] Bump the version number & run `npm i` to bump `package-lock.json` as well. Ensure there are no other `package-lock.json` changes. **@hediet**
- [x] [🔖candidate issues](https://github.com/issues?q=org%3Amicrosoft%20is%3Aissue%20milestone%3A%221.143.1%22%20label%3Acandidate)
- [x] Assign candidate issues to the recovery milestone **team**
- [x] Review the `candidate` issues, and if they pass the review assign them to the recovery milestone **team**
- [x] All `candidate` fixes are peer reviewed and pushed to `main` and then cherry-picked into the release branch **team**
- [ ] Initiate `insiders` build from `main`
- [ ] Issues are tested in the `insiders` **team**
- [ ] Build and manually release Insider from main branch for vscode.dev (if there were vscode.dev candidates)
  - [ ] Issues are tested in the `insiders` **team**
- [x] Build `stable` for all platforms from release branch **@hediet**
- [x] Issues are verified on `stable` build and the `verified` label is added **@hediet**
- [x] Check `https://github.com/Microsoft/vscode/compare/release/<x.y>` to ensure no other commits have been made in the release branch **@hediet**
- [x] The `insiders` build with all candidate fixes needs to be in the wild for 24 hours before recovery release, unless explicitly approved by @kieferrm
- [x] Update the release notes and include a link to a query for the fixed issues @ntrogh
- [x] Publish website @ntrogh
- [x] Publish stable build **@hediet**
- [ ] (if there were vscode.dev candidates) Trigger the [vscode.dev Deploy pipeline](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) for `release/x.y` for the `prod` deployment target. **@hediet**
  - [ ] Request approval from another team member at the necessary step to deploy the vscode.dev build. **@hediet**
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals) **@hediet**
- [x] Create an official release **@hediet**
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z> release/<x.y>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right `... > Create Release`. Use the correct title and description from our release notes. [Example](https://github.com/microsoft/vscode/releases/tag/1.81.1)
- [x] Close the milestone on [GitHub](https://github.com/microsoft/vscode/milestones) **@hediet**


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_344219
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/344219
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/344219
- **SHA256_FINGERPRINT**: `ccdcd5790e5f58965f428005589e78773fe2fdd5f9c5ca68e61d139fab2d7a17`
- **LAST_VERIFIED_UTC**: 2026-10-29T18:15:13.508000+00:00
---

# VS Code Insiders Roadmap: 1.144.0 Endgame
- **Issue Number**: #344219
- **Category**: `endgame-plan`
- **State**: open
- **Source Issue**: https://github.com/microsoft/vscode/issues/344219

[Endgame guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md)

# Before Monday 6AM Zurich time

`@team`:
- Update endgame availability
- Test plan items created
- Milestone only has TPIs. All other issues need to be closed
- All closed issues in milestone labeled `on-testplan`, `bug`, or `verification-needed`
- Verification steps added to `bug` and `verification-needed` issues

# Monday morning  (Zurich)

`@endgame-champ`:
- [x] Unpin the previous endgame plan from the [VS Code issue tracker](https://github.com/microsoft/vscode/issues) — [#342482](https://github.com/microsoft/vscode/issues/342482) unpinned.
- [x] Pin this endgame plan in the [VS Code issue tracker](https://github.com/microsoft/vscode/issues) — [#344219](https://github.com/microsoft/vscode/issues/344219) pinned.
- [x] Assign TPIs
  - Former assignment gaps [microsoft/vscode-internalbacklog#10404](https://github.com/microsoft/vscode-internalbacklog/issues/10404) and [microsoft/vscode-internalbacklog#10382](https://github.com/microsoft/vscode-internalbacklog/issues/10382) are now closed.
  - [x] Create TPI's for all verification needed bugs. Visit `Testing and Verification` on tools site, and generate groupings, then create TPIs. The TPI section below  will update with all of the generated items.
    - [37 verification TPIs](https://github.com/microsoft/vscode-internalbacklog/issues?q=is%3Aissue%20milestone%3A1.144.0%20%22Verification%20TPI%3A%22%20in%3Atitle) created and assigned.
- [x] Pause automatic releases (this also ensures chat-pre-release isn't released) after 10am. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=383))
  - [489137](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489137): Disable continuous release succeeded.
- [x] Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow

  - PRs opened with auto-merge enabled — ensure they get reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): [#344221](https://github.com/microsoft/vscode/pull/344221) merged.
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): [#344220](https://github.com/microsoft/vscode/pull/344220) merged.

  - [Run 40289809619](https://github.com/microsoft/vscode-engineering/actions/runs/40289809619) succeeded; three release branches created.
  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [x] Monday-morning addition: build Stable from `release/1.144`, validate it, and release internally to Microsoft.
  - [x] Queue the Stable Product build (publish artifacts; do not release publicly).
    - [489126](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489126): Stable build and Publish succeeded at `ff05b50`.
  - [x] Verify Stable build and sanity results.
    - [489126](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489126&view=logs): Sanity Tests stage and all 46 Run Sanity tasks succeeded.
  - [x] Release the validated Stable build internally to Microsoft.
    - [489193](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489193): internal Stable release succeeded at `ff05b50`.
- [ ] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.144.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.144.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [x] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
  - [489425](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489425): Insiders release succeeded at `9559530`.
- [x] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
  - [489330](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489330): Stable build succeeded at `9559530`; [489428](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=489428) subsequently released it internally.

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [x] Generate "Thank you" section of the release notes in the `vnext` branch of the private `vscode-docs-pr` repo.
    - [01f066493](https://github.com/microsoft/vscode-docs-pr/commit/01f0664939c85ba3c954e46cbaa7c3ace04b4c77): 4 issue-tracking credits, 10 contributors, 11 PRs.
    - [x] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [x] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [x] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [x] Build stable from release/<x.y> and release to MSFT folks
  - [ ] Reenable automatic releases
    - A build is scheduled for 7:00 PM Zurich time (`19:00 GMT+2`); make sure automatic releases are reenabled before then so we get an Insiders build from `main` on Tuesday evening.

# Tuesday afternoon/Wednesday morning

- In extreme cases, accept candidate changes
    - [ ] Build stable from `release/<x.y>`. Do *not* bump the VS Code version.
    - [ ] Release stable to MSFT folks

# Wednesday
`@endgame-champ`:
- [x] Publish website so that in-product release notes are ready
- [x] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [x] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [x] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
    - https://dev.azure.com/monacotools/Monaco/_build/results?buildId=490463&view=results
- [x] Publish socials (ping Cynthia)
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [x] Create an official release
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [x] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [x] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_345227
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/345227
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/345227
- **SHA256_FINGERPRINT**: `1be6bfb630e2e87994241b2ed6133c4b6c6eab5649fed6a8c61205cbcfdb4647`
- **LAST_VERIFIED_UTC**: 2026-11-04T19:33:34.300959+00:00
---

# VS Code Insiders Roadmap: 1.145.0 Endgame
- **Issue Number**: #345227
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/345227

[Endgame guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md)

# Before Monday 6AM Zurich time

`@team`:
- Update endgame availability
- Test plan items created
- Milestone only has TPIs. All other issues need to be closed
- All closed issues in milestone labeled `on-testplan`, `bug`, or `verification-needed`
- Verification steps added to `bug` and `verification-needed` issues

# Monday morning  (Zurich)

`@endgame-champ`:
- [x] Unpin the previous endgame plan from the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Pin this endgame plan in the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Assign TPIs
  - [x] Create TPI's for all verification needed bugs. Visit `Testing and Verification` on tools site, and generate groupings, then create TPIs. The TPI section below  will update with all of the generated items.
- [x] Pause automatic releases (this also ensures chat-pre-release isn't released) after 10am. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=383))
- [x] Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow

  - PRs opened with auto-merge enabled — ensure they get reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/345477
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/345476

  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [ ] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.145.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.145.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [x] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
- [x] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [x] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [x] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [x] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [x] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [x] Build stable from release/<x.y> and release to MSFT folks
  - [x] Reenable automatic releases
    - A build is scheduled for 7:00 PM Zurich time (`19:00 GMT+2`); make sure automatic releases are reenabled before then so we get an Insiders build from `main` on Tuesday evening.

# Tuesday afternoon/Wednesday morning

- In extreme cases, accept candidate changes
    - [x] Build stable from `release/<x.y>`. Do *not* bump the VS Code version.
    - [x] Release stable to MSFT folks

# Wednesday
`@endgame-champ`:
- [x] Publish website so that in-product release notes are ready
- [x] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [x] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [x] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
- [x] Publish socials (ping Cynthia)
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [x] Create an official release
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [x] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [x] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_346279
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/346279
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/346279
- **SHA256_FINGERPRINT**: `d65fe3a95fadfef7ee3c70e5ce4c6ae97070908c040573ac130792a56a190e0f`
- **LAST_VERIFIED_UTC**: 2026-11-06T05:48:43.971858+00:00
---

# VS Code Insiders Roadmap: 1.145.1 Endgame
- **Issue Number**: #346279
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/346279

- [x] Create a milestone `1.145.1` **@deepak1556**
- [x] Bump the version number & run `npm i` to bump `package-lock.json` as well. Ensure there are no other `package-lock.json` changes. **@deepak1556**
- [x] [🔖candidate issues](https://github.com/issues?q=org%3Amicrosoft%20is%3Aissue%20milestone%3A%221.145.1%22%20label%3Acandidate)
- [x] Assign candidate issues to the recovery milestone **team**
- [x] Review the `candidate` issues, and if they pass the review assign them to the recovery milestone **team**
- [x] All `candidate` fixes are peer reviewed and pushed to `main` and then cherry-picked into the release branch **team**
- [x] Initiate `insiders` build from `main` — Remaining work confirmed complete by @amunger at recovery closeout; not independently re-exercised here.
- [x] Issues are tested in the `insiders` **team** — Remaining work confirmed complete by @amunger at recovery closeout; not independently re-exercised here.
- [x] Build and manually release Insider from main branch for vscode.dev (if there were vscode.dev candidates) — **Not applicable:** no vscode.dev candidate in this recovery.
  - [x] Issues are tested in the `insiders` **team** — **Not applicable:** conditional vscode.dev step.
- [x] Build `stable` for all platforms from release branch **@deepak1556**
- [x] Issues are verified on `stable` build and the `verified` label is added **@deepak1556**
- [x] Check `https://github.com/Microsoft/vscode/compare/release/<x.y>` to ensure no other commits have been made in the release branch **@deepak1556**
- [x] ~~The `insiders` build with all candidate fixes needs to be in the wild for 24 hours before recovery release, unless explicitly approved by @kieferrm~~ — **Skipped:** @amunger confirmed the recovery proceeded without the 24-hour soak. This records the actual deviation, not an assertion of a named approval.
- [x] Update the release notes and include a link to a query for the fixed issues @ntrogh
- [x] Publish website @ntrogh
- [x] Publish stable build **@deepak1556**
- [x] (if there were vscode.dev candidates) Trigger the [vscode.dev Deploy pipeline](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) for `release/x.y` for the `prod` deployment target. **@deepak1556** — **Not applicable:** no vscode.dev candidate in this recovery.
  - [x] Request approval from another team member at the necessary step to deploy the vscode.dev build. **@deepak1556** — **Not applicable:** no vscode.dev candidate in this recovery.
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `patch`; the release pipeline job requires two approvals) **@deepak1556** — **Not applicable:** no Copilot Chat/library code changes; only `engines.vscode` changed. Patch publication run 493511 was canceled.
- [x] Create an official release **@deepak1556**
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z> release/<x.y>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right `... > Create Release`. Use the correct title and description from our release notes. [Example](https://github.com/microsoft/vscode/releases/tag/1.81.1)
- [x] Close the milestone on [GitHub](https://github.com/microsoft/vscode/milestones) **@deepak1556**

## Recovery evidence

- Version bump: #346285. Approved candidate backports: #346275 and #346280. Both candidate issues (#346286, #346287) are closed and labeled `verified`.
- Stable [493338](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=493338&view=results): build, Publish, and Sanity succeeded at `6bab64e2d12b04d04c0d99c27ff166023efd1dda`. Release branch comparison contains only the version bump and the two candidate backports since 1.145.0.
- Packaged Windows ARM64 verification: edit-survival attribution was exercised with real Copilot edits and Git commits, including an overwrite control. Engine pairing was exercised with 26 controlled checks against the exact packaged router and a no-network capture sink; no native engine snapshots arrived during the live model calls. Live account-switching/subagent and backend-ingestion checks were not performed.
- Internal Stable [493439](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=493439&view=results) succeeded. Superseding rollout [493451](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=493451&view=results) succeeded, targeting the same commit and replacing 1.145.0. Public Windows update API now serves 1.145.1 at that commit.
- Website production [493455](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=493455&view=results) succeeded; [release notes](https://code.visualstudio.com/updates/v1_145) include the 1.145.1 issue query.
- [Official 1.145.1 GitHub release](https://github.com/microsoft/vscode/releases/tag/1.145.1) and tag created at the shipped commit.
- Chat-lib publication was deemed not applicable: Copilot Chat/library code and package version did not change. Only the VS Code engine requirement changed. [493511](https://dev.azure.com/monacotools/Monaco/_build/results?buildId=493511&view=results) is confirmed canceled.
- **Closeout:** @amunger confirmed remaining release work complete and that 1.145.1 is rolling out. The 24-hour soak was explicitly not followed; the checklist records that deviation rather than claiming the wait or a named waiver occurred.

[comment authored by copilot]


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_346427
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/346427
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/346427
- **SHA256_FINGERPRINT**: `7eed945f870c1d4b1ae8867df6056882b837a38fa9bf9f0dcfc1d9adaead9d93`
- **LAST_VERIFIED_UTC**: 2026-11-06T19:05:39.543045+00:00
---

# VS Code Insiders Roadmap: 1.145.2 Endgame
- **Issue Number**: #346427
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/346427

- [x] Create a milestone `1.145.2` **@deepak1556**
- [x] Bump the version number & run `npm i` to bump `package-lock.json` as well. Ensure there are no other `package-lock.json` changes. **@deepak1556**
- [x] [🔖candidate issues](https://github.com/issues?q=org%3Amicrosoft%20is%3Aissue%20milestone%3A%221.145.2%22%20label%3Acandidate)
- [x] Assign candidate issues to the recovery milestone **team**
- [x] Review the `candidate` issues, and if they pass the review assign them to the recovery milestone **team**
- [x] All `candidate` fixes are peer reviewed and pushed to `main` and then cherry-picked into the release branch **team**
- [x] Initiate `insiders` build from `main`
- [x] Issues are tested in the `insiders` **team**
- [ ] Build and manually release Insider from main branch for vscode.dev (if there were vscode.dev candidates)
  - [ ] Issues are tested in the `insiders` **team**
- [x] Build `stable` for all platforms from release branch **@deepak1556**
- [x] Issues are verified on `stable` build and the `verified` label is added **@deepak1556**
- [x] Check `https://github.com/Microsoft/vscode/compare/release/<x.y>` to ensure no other commits have been made in the release branch **@deepak1556**
- [x] The `insiders` build with all candidate fixes needs to be in the wild for 24 hours before recovery release, unless explicitly approved by @kieferrm
- [x] Update the release notes and include a link to a query for the fixed issues @ntrogh
- [x] Publish website @ntrogh
- [x] Publish stable build **@deepak1556**
- [ ] (if there were vscode.dev candidates) Trigger the [vscode.dev Deploy pipeline](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) for `release/x.y` for the `prod` deployment target. **@deepak1556**
  - [ ] Request approval from another team member at the necessary step to deploy the vscode.dev build. **@deepak1556**
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `patch`; the release pipeline job requires two approvals) **@deepak1556**
- [x] Create an official release **@deepak1556**
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z> release/<x.y>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right `... > Create Release`. Use the correct title and description from our release notes. [Example](https://github.com/microsoft/vscode/releases/tag/1.81.1)
- [x] Close the milestone on [GitHub](https://github.com/microsoft/vscode/milestones) **@deepak1556**


---
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_346882
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/346882
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/346882
- **SHA256_FINGERPRINT**: `e077509966ea8f7fc95606e2f6edc04c1f3ec7922a618fd5474930e666e0a06c`
- **LAST_VERIFIED_UTC**: 2026-11-11T19:24:27.293311+00:00
---

# VS Code Insiders Roadmap: 1.146.0 Endgame
- **Issue Number**: #346882
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/346882

[Endgame guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md)

# Before Monday 6AM Zurich time

`@team`:
- Update endgame availability
- Test plan items created
- Milestone only has TPIs. All other issues need to be closed
- All closed issues in milestone labeled `on-testplan`, `bug`, or `verification-needed`
- Verification steps added to `bug` and `verification-needed` issues

# Monday morning  (Zurich)

`@endgame-champ`:
- [x] Unpin the previous endgame plan from the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Pin this endgame plan in the [VS Code issue tracker](https://github.com/microsoft/vscode/issues)
- [x] Assign TPIs
  - [x] Create TPI's for all verification needed bugs. Visit `Testing and Verification` on tools site, and generate groupings, then create TPIs. The TPI section below  will update with all of the generated items.
- [x] Pause automatic releases (this also ensures chat-pre-release isn't released) after 10am. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=383))
- [x] Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow

  - PRs opened with auto-merge enabled — ensure they get reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/346890
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/346889

  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [ ] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.146.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.146.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [x] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
- [x] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [x] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [x] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [x] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [ ] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [ ] Build stable from release/<x.y> and release to MSFT folks
  - [ ] Reenable automatic releases
    - A build is scheduled for 7:00 PM Zurich time (`19:00 GMT+2`); make sure automatic releases are reenabled before then so we get an Insiders build from `main` on Tuesday evening.

# Tuesday afternoon/Wednesday morning

- In extreme cases, accept candidate changes
    - [x] Build stable from `release/<x.y>`. Do *not* bump the VS Code version.
    - [x] Release stable to MSFT folks

# Wednesday
`@endgame-champ`:
- [x] Publish website so that in-product release notes are ready
- [x] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [x] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [x] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [x] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
- [x] Publish socials (ping Cynthia)
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [x] Create an official release
  - [x] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [x] Push the tag: `git push origin <x.y.z>`
  - [x] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [x] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [x] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded


---
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_271045
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/271045
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/271045
- **SHA256_FINGERPRINT**: `c052b7684ca85ac366b4fd1620f565afa70efe0494eeed1a9cac40f9efc62120`
- **LAST_VERIFIED_UTC**: 2026-11-03T19:17:08.634501+00:00
---

# VS Code Insiders Roadmap: Iteration Plan for October 2025
- **Issue Number**: #271045
- **Category**: `iteration-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/271045

This plan captures our work in **October 2025**. This is a 5-week iteration. We will ship in **early November**.

## Endgame
- **November 4, 2025**: Endgame begins
- **November 7, 2025**: Endgame done

The endgame details for this iteration are tracked [here](https://github.com/microsoft/vscode/issues?q=is%3Aissue+label%3Aendgame-plan+milestone%3A%22October+2025%22).

## Plan Items

Below is a summary of the top level plan items.

Legend of annotations:

| Mark                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| :runner:             | work in progress                                  |
| :hand:               | blocked task                                      |
| :muscle:             | stretch goal for this iteration                   |
| :red_circle:         | missing issue reference                           |
| :large_blue_circle:  | more investigation required to remove uncertainty |
| :black_circle:       | under discussion within the team                  |
| :black_large_square: | a large work item, larger than one iteration      |

### Accessibility
- [x] Accessibility issues, see [query](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility+milestone%3A%22October+2025%22) @meganrogge @anthonykim1 **team**

### Workbench
- [x] Support JSON file as a policy backend on Linux [vscode#148945](https://github.com/microsoft/vscode/issues/148945) @pwang347 @joshspicer

### Code Editor
- [x] Allow using LSP in the Monaco Editor [vscode#262872](https://github.com/microsoft/vscode/issues/262872) @hediet

### Notebook Editor / Jupyter Notebooks
- [x] Support next/previous find matches (F3) in notebook [vscode#235762](https://github.com/microsoft/vscode/issues/235762) @dineshc-msft
- [ ] :runner: Inline Chat V2 for notebooks improvement [vscode#259903](https://github.com/microsoft/vscode/issues/259903) @amunger

### Source Control
- [x] SCM: Support single repositories only [vscode#245346](https://github.com/microsoft/vscode/issues/245346) @lszomoru
- [x] SCM: Improve Repositories view [vscode#271097](https://github.com/microsoft/vscode/issues/271097) @lszomoru
- [x] Git: Support deep link to continue working on PR in VS Code [vscode#271101](https://github.com/microsoft/vscode/issues/271101) @alexr00

### Settings
- [x] Configuration: Advanced settings support [vscode#270142](https://github.com/microsoft/vscode/issues/270142) @sandy081

### Languages
#### Python
- [ ] :runner: Roll out Python Environments Extension as bundled by default with the Python Extension [vscode-python-environments#190](https://github.com/microsoft/vscode-python-environments/issues/190) @eleanorjboyd
    - [ ] :runner: Add Support for Python Environments Extension API in the Python Debugger [vscode-python-debugger#835](https://github.com/microsoft/vscode-python-debugger/issues/835) @eleanorjboyd
    - [ ] :hand: :runner: Create setting to toggle using `uv` for venvs and support new `uv` specific environment tag from PET [vscode-python-environments#938](https://github.com/microsoft/vscode-python-environments/issues/938) @eleanorjboyd

### Terminal
- [x] Ship shell-agnostic terminal intellisense by default in stable [vscode#226562](https://github.com/microsoft/vscode/issues/226562) @meganrogge @Tyriar
- [x] Take ownership of terminal-links, terminal-find, terminal-layout, terminal-sticky-scroll, terminal-local-echo, terminal-external [vscode#261683](https://github.com/microsoft/vscode/issues/261683) @anthonykim1
    - [x] Exiting out of alt buffer brings the scroll to the top [vscode#224750](https://github.com/microsoft/vscode/issues/224750) @anthonykim1
    - [x] Unify timeout setting under `terminal.integrated.shellIntegration` to use in runCommand [vscode#270813](https://github.com/microsoft/vscode/issues/270813) @anthonykim1
- [ ] :runner: Ramp up on terminal-process @anthonykim1
    - [ ] :runner: Investigate issues integrating conpty on Windows 25H2 [vscode#243584](https://github.com/microsoft/vscode/issues/243584), [vscode#241978](https://github.com/microsoft/vscode/issues/241978) [vscode#274372](https://github.com/microsoft/vscode/issues/274372) @anthonykim1 @Tyriar
    - [ ] :hand: :runner: Investigate issues around cwd and remotes https://github.com/microsoft/vscode/issues/272892 @anthonykim1 @Tyriar

### API
- [ ] :runner: API proposals: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22October+2025%22+label%3A%22api-proposal%22) @mjbvz @alexr00
- [ ] :runner: API finalization: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22October+2025%22+label%3A%22api-finalization%22) @mjbvz @alexr00

### AI
#### Chat
- [ ] :runner: Support for CoT tokens [vscode#257104](https://github.com/microsoft/vscode/issues/257104) @justschen @karthiknadig @jo-oikawa
- [ ] :runner: Review and address Chat UX feedback from social channels [vscode#26703](https://github.com/microsoft/vscode/issues/260703) @justschen @jo-oikawa @bpasero @isidorn
- [x] Improvements to Auto model selection [vscode#265906](https://github.com/microsoft/vscode/issues/265906) @lramos15
- [x] Model picker models should be cached for reload [vscode#268856](https://github.com/microsoft/vscode/issues/268856) @lramos15
- [ ] :runner: Improve chat empty state with context clearing and active tasks [vscode#270465](https://github.com/microsoft/vscode/issues/270465) @eli-w-king @isidorn @bpasero
- [x] Add context menus for welcome prompts [vscode#266374](https://github.com/microsoft/vscode/issues/266374) @benvillalobos @eli-w-king @eleanorjboyd
- [ ] :runner: Chat: Support contributable chat context resources [vscode#271104](https://github.com/microsoft/vscode/issues/271104) @alexr00
- [ ] :runner: Chat: Improve model management UI [vscode#270143](https://github.com/microsoft/vscode/issues/270143) @sandy081

#### MCP
- [x] Support Client Id Metadata Document auth flow [vscode#270811](https://github.com/microsoft/vscode/issues/270811) @TylerLeonhardt
- [x] Support MCP registry endpoint as org-policy to allow-list MCP [vscode#272247](https://github.com/microsoft/vscode/issues/272247) @sandy081

#### Prompt, Instruction and Mode Files
- [x] Identify and close gaps needed to implement multi-step modes such as TDD [vscode#261542](https://github.com/microsoft/vscode/issues/261542) @digitarald @aeschli @roblourens @jo-oikawa
  - [x] Chat modes can define handoffs to the next mode/prompt [vscode#272211](https://github.com/microsoft/vscode/issues/272211) @digitarald @aeschli @bhavyaus
  - [x] Enable `runSubagent` tool for spawning isolated agent loops by default [vscode#270841](https://github.com/microsoft/vscode/issues/270841) @digitarald @roblourens
  - [x] Built-in Plan Mode [vscode#272211](https://github.com/microsoft/vscode/issues/272211) @digitarald
- [x] Improve `/save` for reusable prompts [vscode#262163](https://github.com/microsoft/vscode/issues/262163) @aeschli

#### Inline Chat
- None.

#### Tools and tools management
- [x] Improve pre-selection of tools [vscode#263272](https://github.com/microsoft/vscode/issues/263272) @connor4312 @yufanhuang-ms
- [x] Improve editing model to correctly reflect file renames [vscode#263275](https://github.com/microsoft/vscode/issues/263275) @connor4312
- [x] Support post-tool call approvals for inspecting incoming context [vscode#270618](https://github.com/microsoft/vscode/issues/270618) @connor4312

#### Terminal/task tools
- [x] Implement tree sitter-based parser for terminal auto approve [vscode#261794](https://github.com/microsoft/vscode/issues/261794) @Tyriar
- [x] Shell-specific instructions [vscode#262386](https://github.com/microsoft/vscode/issues/262386) @Tyriar
- [x] Fix terminal tool hanging when zsh+powerlevel10k is used [vscode#271897](https://github.com/microsoft/vscode/issues/271897) @Tyriar
- [x] Redirection file write detection [vscode#272984](https://github.com/microsoft/vscode/issues/272984) @Tyriar
- [x] Run in terminal: Show terminal inline inside the chat view [vscode#257468](https://github.com/microsoft/vscode/issues/257468) @meganrogge

#### NES / Completions
- [x] Offer completions from the chat extension [vscode#272672](https://github.com/microsoft/vscode/issues/272672) @benibenj @alexdima @dbaeumer @chrmarti
- [x] Trigger NES when switching files [vscode#268115](https://github.com/microsoft/vscode/issues/268115) @ulugbekna
- [x] Explore offering next cursor location predictions [vscode#271269](https://github.com/microsoft/vscode-internalbacklog/issues/6698) @ulugbekna
- [ ] :runner: Explore UX for next cursor location or cross-file next edits [vscode#271133](https://github.com/microsoft/vscode/issues/271133) @benibenj @hediet @mrleemurray
- [x] Create an npm package which contains NES as a library [vscode-copilot-chat#216](https://github.com/microsoft/vscode-copilot-chat/pull/216) @chrmarti
- [ ] :runner: Explore Optimistic Next Edit Suggestions [vscode-copilot-chat#222](https://github.com/microsoft/vscode-copilot-chat/pull/222) @chrmarti
- [ ] :runner: Revive TypeScript context provider experiment [vscode#255373](https://github.com/microsoft/vscode-internalbacklog/issues/10579) @dbaeumer

#### Integrations
- [ ] :runner: Improve GH Coding Agent (aka Padawan) integration [vscode#270856](https://github.com/microsoft/vscode/issues/270856) @osortega @rebornix
- [ ] :runner: Integrate GH Copilot CLI [vscode#270852](https://github.com/microsoft/vscode/issues/270852) @rebornix @DonJayamanne
- [x] Support Agent/Mode/Model picker for new session creation [vscode#270855](https://github.com/microsoft/vscode/issues/270855) @joshspicer
- [ ] :runner: Chat Sessions: Support single view [vscode#270945](https://github.com/microsoft/vscode/issues/270945) @bpasero @osortega
- [ ] :runner: Chat session provider/editor api [vscode#256396](https://github.com/microsoft/vscode/pull/256396) @mjbvz @roblourens

### Electron
- [ ] :runner: Support a better Windows update flow [vscode#249239](https://github.com/microsoft/vscode/issues/249239) @deepak1556
- [x] Deprecate macOS 11.0 [vscode#268375](https://github.com/microsoft/vscode/issues/268375) @deepak1556

### Engineering
- [ ] :runner: Engineering: Restructure project npm dependencies [vscode#252171](https://github.com/microsoft/vscode/issues/252171) @deepak1556
- [ ] :runner: Engineering: ESM restore support for ASAR [vscode#228064](https://github.com/microsoft/vscode/issues/228064) @deepak1556
- [ ] :runner: Explore leveraging Playwright MCP to "record a demo" as part of pull request review [vscode#272529](https://github.com/microsoft/vscode/issues/272529) @TylerLeonhardt

### Documentation
- [x] Add support info to Copilot docs [vscode-docs#895](https://github.com/microsoft/vscode-docs/issues/8953) @ntrogh
- [x] Consolidate built-in chat modes content (agent/edit/ask) [vscode-docs#8952](https://github.com/microsoft/vscode-docs/issues/8952) @ntrogh
- [ ] :runner: Test-driven development user guide [vscode-docs#8951](https://github.com/microsoft/vscode-docs/issues/8951) @ntrogh @digitarald
- [ ] :muscle: Working with large codebases user guide [vscode-docs#8932](https://github.com/microsoft/vscode-docs/pull/8932) @digitarald @ntrogh
- [ ] :muscle: Refresh Source Control overview [vscode-docs#8964](https://github.com/microsoft/vscode-docs/issues/8964) @ntrogh

### Website
- None

---
### Deferred
- [ ] Update Profiles UI to include AI features [vscode#270130](https://github.com/microsoft/vscode/issues/270130) @sandy081 @eli-w-king
- [ ] Support MCP metadata verion updates [vscode#271137](https://github.com/microsoft/vscode/issues/271137) @sandy081
- [ ] Link MCP servers with Marketplace extensions [vscode#271138](https://github.com/microsoft/vscode/issues/271138) @sandy081
- [ ] :red_circle: Unify the intent prompts by reusing the edit mode @jrieken
- [ ] Explore task-oriented workflow for chat/agent sessions [vscode-pr#8076](https://github.com/microsoft/vscode-pull-request-github/issues/8076) @mjbvz
- [ ] :runner: Allow configuring font family, font size and line height via syntactic tokens [vscode#263545](https://github.com/microsoft/vscode/issues/263545) @aiday-mar
- [ ] :hand: Support to approve agent mode confirmations from desktop notifications [vscode#251621](https://github.com/microsoft/vscode/issues/251621) @bpasero
- [ ] :hand: Remove all hard-coded styles with variables [vscode#248725](https://github.com/microsoft/vscode/issues/248725) @mrleemurray
- [ ] Improve rendering of prompt file usage in Chat [vscode#253014](https://github.com/microsoft/vscode/issues/253014) @aeschli @justschen
- [ ] Support Copilot Chat in web [vscode#245860](https://github.com/microsoft/vscode/issues/245860) @bpasero
- [ ] :muscle: Explore anchored quick widget for mouse interactions to attach context [vscode#238095](https://github.com/microsoft/vscode/issues/238095) @TylerLeonhardt
- [ ] Suggest to user to move app to `/Applications` on startup [vscode#213909](https://github.com/microsoft/vscode/issues/213909) @deepak1556
- [ ] :muscle: Opt-in to LLM-based approval [vscode#253267](https://github.com/microsoft/vscode/issues/253267) @Tyriar
- [ ] :muscle: Explore offering inline completions in the chat input box [vscode#255818](https://github.com/microsoft/vscode/issues/255818) @aiday-mar
- [ ] :muscle: Explore rendering unaccepted files in SCM [vscode#254456](https://github.com/microsoft/vscode/issues/254456 ) @aiday-mar @lszomoru
- [ ] STest cache explorer [vscode#255803](https://github.com/microsoft/vscode/issues/255803) @joaomoreno
- [ ] Explore moving notebook tools into core [vscode#260234](https://github.com/microsoft/vscode/issues/260234) @DonJayamanne @amunger
- [ ] :muscle: Improve width of ToC, and overall the width of a docs page that's available [vscode-docs#8485](https://github.com/microsoft/vscode-docs/issues/8485) @hawkticehurst
- [ ] Explore Builtin create pull request tool / integration in Copilot Chat [vscode#255387](https://github.com/microsoft/vscode/issues/255387) @alexr00
- [ ] :muscle: Support generating `copilot-setup-steps.yml` [vscode#260225](https://github.com/microsoft/vscode/issues/260225) @osortega
- [ ] :runner: Terminal tool UX refresh [vscode#257468](https://github.com/microsoft/vscode/issues/257468) @Tyriar @jo-oikawa
- [ ] Improve how the terminal tool deals with multiple terminals [vscode#253263](https://github.com/microsoft/vscode/issues/257468) @Tyriar
- [ ] :muscle: Re-routing of calls to terminal tool to appropriate native tools [vscode#253884](https://github.com/microsoft/vscode/issues/253884) @Tyriar
- [ ] Explore layouts for Chat session + Multi File Diff [vscode#260226](https://github.com/microsoft/vscode/issues/260226) @joshspicer
- [ ] Build "Diagnose with AI" flow for Python Environment Extension [vscode-python-environments#592](https://github.com/microsoft/vscode-python-environments/issues/592) @eleanorjboyd
- [ ] :runner: Support Mermaid diagram rendering in Chat [vscode-copilot-release#7440](https://github.com/microsoft/vscode-copilot-release/issues/7440) @mjbvz


---
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_277757
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/277757
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/277757
- **SHA256_FINGERPRINT**: `01f228c810b1f6d4b96e10c1ef718c4f1d648e9de012ba05213e3d122b0e962e`
- **LAST_VERIFIED_UTC**: 2026-11-03T19:17:08.633751+00:00
---

# VS Code Insiders Roadmap: Iteration Plan for November 2025
- **Issue Number**: #277757
- **Category**: `iteration-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/277757

This plan captures our work in **November 2025**. This is a 4-week iteration. We will ship in **early December**.

## Endgame
- **December 1, 2025**: Endgame begins
- **December 5, 2025**: Endgame done

The endgame details for this iteration are tracked [here](https://github.com/microsoft/vscode/issues?q=is%3Aissue+label%3Aendgame-plan+milestone%3A%22November+2025%22).

## Plan Items

Below is a summary of the top level plan items.

Legend of annotations:

| Mark                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| :runner:             | work in progress                                  |
| :hand:               | blocked task                                      |
| :muscle:             | stretch goal for this iteration                   |
| :red_circle:         | missing issue reference                           |
| :large_blue_circle:  | more investigation required to remove uncertainty |
| :black_circle:       | under discussion within the team                  |
| :black_large_square: | a large work item, larger than one iteration      |

### Accessibility
- [x] Accessibility issues, see [query](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility+milestone%3A%22November+2025%22) @meganrogge **team**

### Workbench
- [ ] :runner: Glob matching should be case insensitive [vscode#10633](https://github.com/microsoft/vscode/issues/10633) @dmitrivMS
- [ ] :runner: Investigate improvements for simple browser [vscode#277298](https://github.com/microsoft/vscode/issues/277298) @kycutler @jruales
- [ ] :runner: Support in-context Quick Pick interactions [vscode#238095](https://github.com/microsoft/vscode/issues/238095) @lszomoru @joaomoreno

### Code Editor
- [ ] :runner: Allow configuring font family, font size and line height via syntactic tokens [vscode#263545](https://github.com/microsoft/vscode/issues/263545) @aiday-mar

### Languages
#### Python
- [ ] :runner: Roll out Python Environments Extension as bundled by default with the Python Extension [vscode-python-environments#190](https://github.com/microsoft/vscode-python-environments/issues/190) @eleanorjboyd
    - [x] Create setting to toggle using `uv` for venvs and support new `uv` specific environment tag from PET [vscode-python-environments#938](https://github.com/microsoft/vscode-python-environments/issues/938) @eleanorjboyd

### Terminal
- [ ] :runner: Ramp up on terminal-process @anthonykim1
    - [ ] :hand: :runner: Investigate issues integrating conpty on Windows 25H2 [vscode#243584](https://github.com/microsoft/vscode/issues/243584), [vscode#241978](https://github.com/microsoft/vscode/issues/241978) [vscode#274372](https://github.com/microsoft/vscode/issues/274372) @anthonykim1 @Tyriar
    - [ ] :runner: Investigate issues around cwd and remotes [vscode#272892](https://github.com/microsoft/vscode/issues/272892) @anthonykim1 @Tyriar
- [x] Bugs in terminal links: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue%20state%3Aopen%20assignee%3Aanthonykim1%20milestone%3A%22November%202025%22%20label%3Aterminal-links) @anthonykim1

### API
- [x] API proposals: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22November+2025%22+label%3A%22api-proposal%22) @mjbvz @alexr00
- [x] API finalization: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22November+2025%22+label%3A%22api-finalization%22) @mjbvz @alexr00

### AI
#### Chat
- [ ] :runner: Chat: Support contributable chat context resources [vscode#271104](https://github.com/microsoft/vscode/issues/271104) @alexr00
- [ ] :runner: Chat: Improve model management UI [vscode#270143](https://github.com/microsoft/vscode/issues/270143) @sandy081
- [x] Linkification improvements: improve file path links with precise line anchors [vscode#276767](https://github.com/microsoft/vscode/issues/276767) @vijayupadya
- [x] Redesign prompt area responsive layout to reduce clutter [vscode#272502](https://github.com/microsoft/vscode/issues/272502) @unthinkmedia
- [ ] :runner: Polish thinking token rendering [vscode#257104](https://github.com/microsoft/vscode/issues/257104) @justschen @karthiknadig @jo-oikawa
- [ ] :runner: Explore minimal presentation of tools [vscode#273444](https://github.com/microsoft/vscode/issues/273444) @jo-oikawa @tyriar @meganrogge @justschen
- [x] Support Entra to authenticate to Azure models [vscode#270234](https://github.com/microsoft/vscode/issues/270234) @eleanorjboyd
- [x] Improve life cycle management [vscode#277318](https://github.com/microsoft/vscode/issues/277318) @roblourens @connor4312
- [ ] :runner: Show terminal inside chat view [vscode#257468](https://github.com/microsoft/vscode/issues/257468) @meganrogge
- [ ] :muscle: Revisit terminal tool running background terminals UX [vscode#274550](https://github.com/microsoft/vscode/issues/274550) @Tyriar

#### MCP
- [x] Adding directory support for MCP resources [vscode#262368](https://github.com/microsoft/vscode/issues/262368) @dileepyavan
- [x] Enable support for Http/Https based MCP resources [vscode#259253](https://github.com/microsoft/vscode/issues/259253) @dileepyavan

#### Prompt, Instruction and Mode Files
- [x] Align tool names with GitHub custom agents [vscode#272734](https://github.com/microsoft/vscode/issues/272734) @pwang347 @aeschli
- [x] Adopt GitHub API to discover Enterprise/Organization custom agent modes [vscode#274341](https://github.com/microsoft/vscode/issues/274341) @pwang347 @aeschli
- [ ] :hand: Support GitHub's organization custom instructions [vscode#276636](https://github.com/microsoft/vscode/issues/276636) @pwang347 @aeschli
- [x] ⁠Explore support for infer property [vscode#277431](https://github.com/microsoft/vscode/issues/277431) @aeschli @pwang347
- [ ] :muscle: Investigate for code-execution (see Claude skills) [vscode#277433](https://github.com/microsoft/vscode/issues/277433) @aeschli @pwang347

#### Inline Chat
- [ ] :runner: Inline Chat V2 for notebooks improvement [vscode#259903](https://github.com/microsoft/vscode/issues/259903) @amunger
- [ ] :runner: Allow connecting the new UI with the older backend [vscode#278054](https://github.com/microsoft/vscode/issues/278054) @jrieken
- [ ] :runner: Improve inline chat editing [vscode#278057](https://github.com/microsoft/vscode/issues/278057) @jrieken

#### NES / Completions
- [x] NES at distance in the same file [vscode#277816](https://github.com/microsoft/vscode/issues/277816) @benibenj @hediet @mrleemurray
- [x] Explore rendering cross-file next edits [vscode#271133](https://github.com/microsoft/vscode/issues/271133) @benibenj @hediet @mrleemurray
- [x] Render NES / Completions model information in the status bar [vscode#277826](https://github.com/microsoft/vscode/issues/277826) @hediet
- [x] Explore invoking semantic rename with NES [vscode#277818](https://github.com/microsoft/vscode/issues/277818) @dbaeumer
- [x] Revive TypeScript context provider experiment [vscode#255373](https://github.com/microsoft/vscode-internalbacklog/issues/10579) @dbaeumer
- [x] Include diagnostics in NES prompts [vscode#277809](https://github.com/microsoft/vscode/issues/277809) @benibenj @ulugbekna
- [x] Register a single `InlineCompletionItemProvider` [vscode#277831](https://github.com/microsoft/vscode/issues/277831) @hediet @benibenj @chrmarti
- [ ] :muscle: Allow running simulation tests that include the completions model [vscode#280344](https://github.com/microsoft/vscode/issues/280344) @ulugbekna @benibenj

#### Agents
- [x] Chat Sessions: Support single view [vscode#270945](https://github.com/microsoft/vscode/issues/270945) @bpasero @osortega @eli-w-king
- [x] Agent Sessions UX/UI Improvements [vscode#277524](https://github.com/microsoft/vscode/issues/277524) @eli-w-king @bpasero @jo-oikawa @mrleemurray @hawkticehurst
- [x] Improve delegation between foreground/background/cloud agents [vscode#277313](https://github.com/microsoft/vscode/issues/277313) @joshspicer
- [x] Delegating plan mode to background [vscode#278484](https://github.com/microsoft/vscode/issues/278484#issuecomment-3560845119) @joshspicer @unthinkmedia
- [ ] :runner: GH Coding Agent (aka Padawan) integration improvements [vscode#278921](https://github.com/microsoft/vscode/issues/278921) @osortega
- [x] GH Copilot CLI sdk upgrade and improvements [vscode#277312](https://github.com/microsoft/vscode/issues/277312) @DonJayamanne @rebornix
- [x] Support running CLI agent sessions in background [vscode#278922](https://github.com/microsoft/vscode/issues/278922) @DonJayamanne @osortega
- [x] Chat session provider/editor api [vscode#256396](https://github.com/microsoft/vscode/pull/256396) @mjbvz @roblourens
- [ ] :runner: Sandboxing terminal while running commands through agent [vscode#277286](https://github.com/microsoft/vscode/issues/277286) @dileepyavan
- [x] Explore git worktree support for agents [vscode#268219](https://github.com/microsoft/vscode/issues/268219) @lszomoru

#### Code Review
- [x] Investigate why local copilot code review is slow [vscode#276974](https://github.com/microsoft/vscode/issues/276974) @benvillalobos

### Electron
- [x] Support a better Windows update flow [vscode#249239](https://github.com/microsoft/vscode/issues/249239) @deepak1556

### Engineering
- [ ] :runner: Engineering: ESM restore support for ASAR [vscode#228064](https://github.com/microsoft/vscode/issues/228064) @deepak1556
- [x] Explore leveraging Playwright MCP to "record a demo" as part of pull request review [vscode#272529](https://github.com/microsoft/vscode/issues/272529) @TylerLeonhardt

### Documentation
- [ ] :runner: Test-driven development user guide [vscode-docs#8951](https://github.com/microsoft/vscode-docs/issues/8951) @ntrogh @digitarald
- [ ] :muscle: Working with large codebases user guide [vscode-docs#8932](https://github.com/microsoft/vscode-docs/pull/8932) @digitarald @ntrogh
- [x] Refresh Source Control overview [vscode-docs#8964](https://github.com/microsoft/vscode-docs/issues/8964) @ntrogh
- [x] Investigate automatically generating Insiders release notes using AI based on PRs [vscode-docs#9071](https://github.com/microsoft/vscode-docs/issues/9071) @ntrogh

---
### Deferred
- [ ] Link MCP servers with Marketplace extensions [vscode#271138](https://github.com/microsoft/vscode/issues/271138) @sandy081
- [ ] Improve open editor handoff for Plan agent [vscode#277432](https://github.com/microsoft/vscode/issues/277432) @aeschli @pwang347
- [ ] Improve the speed for import NES suggestions [vscode#277811](https://github.com/microsoft/vscode/issues/277811) @benibenj @dbaeumer
- [ ] Port the Completions model prompt to use `@vscode/prompt-tsx` [vscode#277829](https://github.com/microsoft/vscode/issues/277829) @dbaeumer
- [ ] Adopt `ICompletionsFetchService` for completions [vscode#277830](https://github.com/microsoft/vscode/issues/277830) @chrmarti @ulugbekna
- [ ] Explore task-oriented workflow for chat/agent sessions [vscode-pr#8076](https://github.com/microsoft/vscode-pull-request-github/issues/8076) @mjbvz
- [ ] Upgrade tree sitter wasm to latest tree sitter version [vscode#274547](https://github.com/microsoft/vscode/issues/274547) @alexr00
- [ ] Explore layouts for Chat session + Multi File Diff [vscode#260226](https://github.com/microsoft/vscode/issues/260226) @joshspicer
- [ ] Update Profiles UI to include AI features [vscode#270130](https://github.com/microsoft/vscode/issues/270130) @eli-w-king
- [ ] :runner: Explore Optimistic Next Edit Suggestions [vscode-copilot-chat#222](https://github.com/microsoft/vscode-copilot-chat/pull/222) @chrmarti


---
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_284547
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/284547
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/284547
- **SHA256_FINGERPRINT**: `d51977322fde3358c921842fce157c2c4c60d192a29cda289769c9afa565a792`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.162395+00:00
---

# VS Code Insiders Roadmap: Release Schedule 12/19/2025 - 01/05/2026
- **Issue Number**: #284547
- **Category**: `iteration-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/284547

Thank you for a great 2025!

We don't plan to release Insider or Stable builds between December 19, 2025  and January 5, 2026. We will monitor incoming issues and reconsider if needed.


---
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_286040
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/286040
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/286040
- **SHA256_FINGERPRINT**: `0a18aeb6ef4e5740b1fd3a103b9c86e50866c9aa48589dd496d35d9de56550d9`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.162395+00:00
---

# VS Code Insiders Roadmap: Iteration Plan for January 2026
- **Issue Number**: #286040
- **Category**: `iteration-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/286040

This plan captures our work in **January 2026**. This is a 4-week iteration. We will ship in **early February**.

## Endgame
- **January 26, 2026**: Endgame begins
- **January 30, 2026**: Endgame done

The endgame details for this iteration are tracked [here](https://github.com/microsoft/vscode/issues?q=is%3Aissue+label%3Aendgame-plan+milestone%3A%22January+2026%22).

## Plan Items

Below is a summary of the top level plan items.

Legend of annotations:

| Mark                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| :runner:             | work in progress                                  |
| :hand:               | blocked task                                      |
| :muscle:             | stretch goal for this iteration                   |
| :red_circle:         | missing issue reference                           |
| :large_blue_circle:  | more investigation required to remove uncertainty |
| :black_circle:       | under discussion within the team                  |
| :black_large_square: | a large work item, larger than one iteration      |

### Accessibility
- [x] Accessibility issues, see [query](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility+milestone%3A%22January+2026%22) @meganrogge **team**

### Workbench
- [x] Glob matching should be case insensitive [vscode#10633](https://github.com/microsoft/vscode/issues/10633) @dmitrivMS
- [x] Investigate improvements for Simple Browser [vscode#277298](https://github.com/microsoft/vscode/issues/277298) @kycutler @jruales @unthinkmedia
- [x] Integrated Browser V1 [vscode#286579](https://github.com/microsoft/vscode/issues/286579) @kycutler @jruales @unthinkmedia
- [x] Rollout Windows 11 Explorer context menu item to Stable [vscode#204696](https://github.com/microsoft/vscode/issues/204696) @deepak1556
- [x] Rollout improved Windows update flow to Stable [vscode#281963](https://github.com/microsoft/vscode/issues/281963) @deepak1556
- [ ] :runner: Support in-context Quick Pick interactions [vscode#238095](https://github.com/microsoft/vscode/issues/238095) @lszomoru @tylerleonhardt
- [ ] :runner: Portable mode improvements @dmitrivMS
- [ ] :runner: Metered network connections support @dmitrivMS
- [ ] :runner: Update UI improvements @dmitrivMS

### Code Editor
- [x] Hover on keyboard modifier should trigger instantly [vscode#276558](https://github.com/microsoft/vscode/issues/276558) @benvillalobos
- [x] Fix important self host issues with experimental GPU acceleration [project](https://github.com/orgs/microsoft/projects/1367/views/1) @tyriar
- [ ] :runner: Allow configuring font family, font size and line height via syntactic tokens [vscode#263545](https://github.com/microsoft/vscode/issues/263545) @aiday-mar

### Languages
#### Python
- [x] Use environment extension api when executing Python code and file [vscode-python#25687](https://github.com/microsoft/vscode-python/issues/25687) @anthonykim1
    - [x] Create terminal api does not return activated terminal for command type [vscode-python-environments#1078](https://github.com/microsoft/vscode-python-environments/issues/1078) @anthonykim1
    - [x] Ctrl+c immeditately issued upon run, execution cancelled by activation command [vscode-python-environments#640](https://github.com/microsoft/vscode-python-environments/issues/640) @anthonykim1
- [ ] :runner: Various bug fixes for Python Environments Extension [vscode-python-environments-query](https://github.com/microsoft/vscode-python-environments/issues?q=is%3Aissue%20state%3Aopen%20label%3Abug%20label%3Aimportant) @eleanorjboyd

### Terminal
- [x] Remove winpty support [node-pty#842](https://github.com/microsoft/node-pty/issues/842) [vscode#284519](https://github.com/microsoft/vscode/issues/284519) @anthonykim1
- [x] Implement kitty keyboard protocol [vscode#286809](https://github.com/microsoft/vscode/issues/286809) @tyriar
- [x] Implement win32 input mode [vscode#286896](https://github.com/microsoft/vscode/issues/286896) @tyriar
- [ ] :hand: :runner: Conpty issues @anthonykim1
    - [ ] Ship newer version of conpty [vscode#224488](https://github.com/microsoft/vscode/issues/224488) @anthonykim1 @Tyriar
    - [ ] Issues from conpty on Windows 25H2 [vscode#243584](https://github.com/microsoft/vscode/issues/243584), [vscode#241978](https://github.com/microsoft/vscode/issues/241978) [vscode#274372](https://github.com/microsoft/vscode/issues/274372) @anthonykim1 @Tyriar
- [ ] :runner: Implement kitty graphics protocol [vscode#286141](https://github.com/microsoft/vscode/issues/286141) @anthonykim1

### API
- [x] API proposals: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22January+2026%22+label%3A%22api-proposal%22) @mjbvz @alexr00
- [x] API finalization: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22January+2026%22+label%3A%22api-finalization%22) @mjbvz @alexr00

### Source Control
- [ ] :runner: Git: Support setup steps for new worktrees [vscode#276834](https://github.com/microsoft/vscode/issues/276834) @lszomoru

### AI
#### Chat
- [x] Allow creating new sessions from chat input [vscode#284091](https://github.com/microsoft/vscode/issues/284091) @benibenj
- [x] Chat: Improve model management UI [vscode#270143](https://github.com/microsoft/vscode/issues/270143) @sandy081
- [x] Address chat performance problems for longer chats [vscode#286610](https://github.com/microsoft/vscode/issues/286610) @roblourens @connor4312
- [x] Render progress as tool calls stream in [vscode#278640](https://github.com/microsoft/vscode/pull/278640) @lramos15
- [x] Enable mermaid support by default [vscode#271372](https://github.com/microsoft/vscode/issues/271372) @mjbvz
- [x] Improve terminal inside chat view [vscode#257468](https://github.com/microsoft/vscode/issues/257468) @meganrogge
- [x] Unify changes in the 'working set' area across agent session types [vscode#278654](https://github.com/microsoft/vscode/issues/278654) @connor4312 @lostintangent
- [x] Support tool approval in a hover [vscode#280617](https://github.com/microsoft/vscode/issues/280617) @connor4312
- [ ] :runner: Polish Agent Sessions UI [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue%20state%3Aopen%20assignee%3Abpasero%20label%3Achat-agents-view) @bpasero @lostintangent
- [ ] :runner: Chat: Support contributable chat context resources [vscode#271104](https://github.com/microsoft/vscode/issues/271104) @alexr00
- [ ] :runner: Improve chat response rendering [query](https://github.com/microsoft/vscode/issues/275215) @justschen @jo-oikawa @hawkticehurst
- [ ] :runner: Chat Sessions Controller API @mjbvz [vscode#276243](https://github.com/microsoft/vscode/issues/276243)
- [ ] :runner: Revisit terminal tool running background terminals UX [vscode#274550](https://github.com/microsoft/vscode/issues/274550) @Tyriar

#### MCP
- [x] Support MCP registry url property [vscode#278398](https://github.com/microsoft/vscode/issues/278398) @sandy081
- [x] Explore supporting MCP apps [vscode#260218](https://github.com/microsoft/vscode/issues/260218) @connor4312

#### Inline Chat
- [x] Make inline chat more discoverable [vscode#287105](https://github.com/microsoft/vscode/issues/287105) @jrieken

#### NES / Completions
- [x] Improve the speed for import NES suggestions [vscode#277811](https://github.com/microsoft/vscode/issues/277811) @benibenj @dbaeumer
- [x] Improve rendering of inline completions in small edits scenarios (single characters, punctuation) [vscode#284517](https://github.com/microsoft/vscode/issues/284517) @benibenj
- [x] Prefer NES/completions over word suggestions [vscode#284076](https://github.com/microsoft/vscode/issues/284076) @benibenj
- [x] Add support for diagnostics to the inline completion prompt [vscode#277829](https://github.com/microsoft/vscode/issues/277829) @dbaeumer
- [x] Suggest semantic renames when editing an identifier [vscode#289124](https://github.com/microsoft/vscode/issues/289124)@dbaeumer
- [x] Add support for patch-based model response format [vscode#287115](https://github.com/microsoft/vscode/issues/287115) @ulugbekna @vkrd
- [x] Adopt `ICompletionsFetchService` for completions [vscode#277830](https://github.com/microsoft/vscode/issues/277830) @ulugbekna
- [ ] :muscle: Allow running simulation tests that include the completions model [vscode#280344](https://github.com/microsoft/vscode/issues/280344) @ulugbekna @benibenj

#### Agents
- [x] Suggest to install GHPRI from Cloud agent sessions [vscode#286168](https://github.com/microsoft/vscode/issues/286168) @alexr00
- [x] Support model-specific tools and tool descriptions [vscode#277472](https://github.com/microsoft/vscode/issues/277472) @connor4312 @bhavyaus
- [x] Support model / 3rd party agents in Cloud Agents [vscode#286170](https://github.com/microsoft/vscode/issues/286170) @joshspicer
- [x] Polish background agent session UX [vscode#287043](https://github.com/microsoft/vscode/issues/287043) @lszomoru @rebornix **team**
- [x] Sandboxing terminal while running commands through agent [vscode#277286](https://github.com/microsoft/vscode/issues/277286) @dileepyavan
- [ ] :runner: Support for Claude Agent [vscode#266962](https://github.com/microsoft/vscode/issues/266962) @TylerLeonhardt
- [ ] :runner: Support repo picker for cloud agents and polish empty workspace experience [vscode#286020](https://github.com/microsoft/vscode/issues/286020) @osortega @rebornix
- [ ] :runner: CLI integration improvements (custom-agent/model/tools) [vscode#286028](https://github.com/microsoft/vscode/issues/286028) @DonJayamanne

#### Prompt/Instruction Files and Custom Agents
- [x] Allow parallel subagent execution [vscode#274630](https://github.com/microsoft/vscode/issues/274630) @roblourens
- [x] Improve custom agents [vscode#286237](https://github.com/microsoft/vscode/issues/286237) @aeschli @pwang347 @digitarald
- [x] Improve skill lookup [vscode#286238](https://github.com/microsoft/vscode/issues/286238) @aeschli @pwang347
- [x] Provide skill lookup debugging [vscode#286239](https://github.com/microsoft/vscode/issues/286239) @aeschli @pwang347
- [x] Support GitHub's organization custom instructions [vscode#276636](https://github.com/microsoft/vscode/issues/276636) @pwang347 @aeschli
- [ ] :muscle: Improve open editor handoff for Plan agent [vscode#277432](https://github.com/microsoft/vscode/issues/277432) @aeschli @pwang347

#### Code Review
- [ ] :muscle: Notify user when CCR no-ops [vscode#277286](https://github.com/microsoft/vscode/issues/276240) @benvillalobos
- [ ] :muscle: Add `Chat: Code Review` command [vscode#276977](https://github.com/microsoft/vscode/issues/276977) @benvillalobos

### Engineering
- [x] Consume codicons from npm [vscode#283823](https://github.com/microsoft/vscode/issues/283823) @alexr00
- [x] Explore distributing .dmg for macOS arm64 [vscode#265849](https://github.com/microsoft/vscode/issues/265849) @deepak1556

### Documentation
- [x] Test-driven development user guide [vscode-docs#8951](https://github.com/microsoft/vscode-docs/issues/8951) @ntrogh @digitarald
- [x] Refactor Enterprise article into separate articles [vscode-docs#9132]([url](https://github.com/microsoft/vscode-docs/issues/9132)) @ntrogh @joshspicer
- [ ] :muscle: Working with large codebases user guide [vscode-docs#8932](https://github.com/microsoft/vscode-docs/pull/8932) @digitarald @ntrogh

---
### Deferred
- [ ] Register a single inline completions provider to vscode's API [vscode#287116](https://github.com/microsoft/vscode/issues/287116) @ulugbekna
- [ ] Archive handling for background/cloud sessions [vscode#286171](https://github.com/microsoft/vscode/issues/286171) @joshspicer
- [ ] Explore layouts for Chat session + Multi File Diff [vscode#260226](https://github.com/microsoft/vscode/issues/260226) @joshspicer
- [ ] Update Profiles UI to include AI features [vscode#270130](https://github.com/microsoft/vscode/issues/270130) @eli-w-king
- [ ] Engineering: ESM restore support for ASAR [vscode#228064](https://github.com/microsoft/vscode/issues/228064) @deepak1556
- [ ] Explore task-oriented workflow for chat/agent sessions [vscode-pr#8076](https://github.com/microsoft/vscode-pull-request-github/issues/8076) @mjbvz
- [ ] Exploration: Support runtime experimentation [vscode#286162](https://github.com/microsoft/vscode/issues/286162) @deepak1556
- [ ] Refine chat motion rendering [vscode#287175](https://github.com/microsoft/vscode/issues/287175) @hawkticehurst @justchen @roblourens


---
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_293855
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/293855
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/293855
- **SHA256_FINGERPRINT**: `fb5520d1b9a0127f5c4c11d1b43d2226400a5b5618a9f23af13f7b31a0d854fc`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.159456+00:00
---

# VS Code Insiders Roadmap: Iteration Plan for February 2026
- **Issue Number**: #293855
- **Category**: `iteration-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/293855

This plan captures our work in **February 2026**. This is a 4-week iteration. We will ship in **early March**.

## Endgame
- **February 23, 2026**: Endgame begins
- **February 27, 2026**: Endgame done

The endgame details for this iteration are tracked [here](https://github.com/microsoft/vscode/issues?q=is%3Aissue+label%3Aendgame-plan+milestone%3A%22February+2026%22).

## Plan Items

Below is a summary of the top level plan items.

> [!IMPORTANT]
> We're experimenting with changing the structure of the plan. This is work in progress. What you see below is a fragment of the plan.

Legend of annotations:

| Mark                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| :runner:             | work in progress                                  |
| :hand:               | blocked task                                      |
| :muscle:             | stretch goal for this iteration                   |
| :red_circle:         | missing issue reference                           |

### Accessibility
- [x] Accessibility issues, see [query](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility+milestone%3A%22February+2026%22) @meganrogge **team**

### Workbench
- [x] Support in-context Quick Pick interactions [vscode#238095](https://github.com/microsoft/vscode/issues/238095) @lszomoru @tylerleonhardt
- [x] Metered network connections support [vscode#103451](https://github.com/microsoft/vscode/issues/103451) @dmitrivMS
- [x] Update UI improvements [vscode#277330](https://github.com/microsoft/vscode/issues/277330) @dmitrivMS
- [x] Update progress indicator on Windows [vscode#293872](https://github.com/microsoft/vscode/issues/293872) @dmitrivMS
- [x] Fix double update issue on Windows [vscode#268531](https://github.com/microsoft/vscode/issues/268531) @dmitrivMS
- [ ] :muscle: Title bar update UI [vscode#293891](https://github.com/microsoft/vscode/issues/293891) @dmitrivMS

### Code Editor
- [ ] :runner: Allow configuring font family, font size and line height via syntactic tokens [vscode#263545](https://github.com/microsoft/vscode/issues/263545) @aiday-mar

### Languages
#### Python
- [ ] :runner: Ship Python Environments Extension to 100% of users and handle various bug fixes [vscode-python-environments-query](https://github.com/microsoft/vscode-python-environments/issues?q=is%3Aissue%20state%3Aopen%20label%3Abug%20label%3Aimportant) @eleanorjboyd

### Terminal
| Theme | Description | Owners |
|-------|-------------|--------|
| 🖥️ Terminal Profiles | Elevate AI CLI Terminal Profiles | @meganrogge |
| 🖼️ Terminal Image Support | Kitty graphics protocol MVP | @anthonykim1 |
| 🪟 Terminal Windows Experience | Ship newer conpty and fix Windows 25H2 issues | @anthonykim1 @Tyriar |
| 🖥️ External Terminal Experience | Enhance multi-root external terminal experience, Ghostty compatibility | @anthonykim1

    - [ ] :runner: :hand: Conpty issues @anthonykim1
    - [ ] Ship newer version of conpty [vscode#224488](https://github.com/microsoft/vscode/issues/224488) @anthonykim1 @Tyriar
    - [ ] Issues from conpty on Windows 25H2 [vscode#243584](https://github.com/microsoft/vscode/issues/243584), [vscode#241978](https://github.com/microsoft/vscode/issues/241978) [vscode#274372](https://github.com/microsoft/vscode/issues/274372) @anthonykim1 @Tyriar
    - [ ] :runner: :muscle: Implement kitty graphics protocol [vscode#286141](https://github.com/microsoft/vscode/issues/286141) @anthonykim1

### API
- [x] API proposals: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22February+2026%22+label%3A%22api-proposal%22) @mjbvz @alexr00
- [x] API finalization: [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen+milestone%3A%22February+2026%22+label%3A%22api-finalization%22) @mjbvz @alexr00

### Source Control
- [ ] :runner: Git: Support setup steps for new worktrees [vscode#276834](https://github.com/microsoft/vscode/issues/276834) @lszomoru

### AI
#### Chat
- [ ] :runner: Polish Agent Sessions UI [query](https://github.com/microsoft/vscode/issues?q=is%3Aissue%20state%3Aopen%20assignee%3Abpasero%20label%3Achat-agents-view) @bpasero @lostintangent
- [ ] :runner: Chat: Support contributable chat context resources [vscode#271104](https://github.com/microsoft/vscode/issues/271104) @alexr00
- [ ] :runner: Improve chat response rendering [query](https://github.com/microsoft/vscode/issues/275215) @justschen @jo-oikawa @hawkticehurst
- [ ] :runner: Chat Sessions Controller API @mjbvz [vscode#276243](https://github.com/microsoft/vscode/issues/276243)
- [ ] :runner: Revisit terminal tool running background terminals UX [vscode#274550](https://github.com/microsoft/vscode/issues/274550) @Tyriar
- [ ] Tips Feature @meganrogge @sbatten

    - [ ] Make tips contextual [vscode#290019](https://github.com/microsoft/vscode/issues/290019) @meganrogge
    - [ ] Enable devs to easily add tips via a showcase label and pipeline [vscode-engineering#1777](https://github.com/microsoft/vscode-engineering/issues/1777) @meganrogge
    - [ ] Add context menu actions like dismiss and don't show again [vscode#293507](https://github.com/microsoft/vscode/issues/293507) @meganrogge
    - [ ] Experiment with location [vscode-internalbacklog#6646](https://github.com/microsoft/vscode-internalbacklog/issues/6646) @meganrogge
    - [ ] Consider using tips for new model announcements [vscode#293526](https://github.com/microsoft/vscode/issues/293526) @meganrogge

- [ ] Model picker improvements [vscode#6754](https://github.com/microsoft/vscode/issues/293875) @sandy081

#### MCP
- None.

#### Inline Chat
- None.

#### NES / Completions
- None.

#### Agents
- [ ] :runner: Support for Claude Agent [vscode#266962](https://github.com/microsoft/vscode/issues/266962) @TylerLeonhardt

#### Prompt/Instruction Files and Custom Agents
- [ ] :muscle: Improve open editor handoff for Plan agent [vscode#277432](https://github.com/microsoft/vscode/issues/277432) @aeschli @pwang347

#### Code Review
- [ ] :muscle: Notify user when CCR no-ops [vscode#277286](https://github.com/microsoft/vscode/issues/276240) @benvillalobos
- [ ] :muscle: Add `Chat: Code Review` command [vscode#276977](https://github.com/microsoft/vscode/issues/276977) @benvillalobos

### Documentation
- [ ] :muscle: Working with large codebases user guide [vscode-docs#8932](https://github.com/microsoft/vscode-docs/pull/8932) @digitarald @ntrogh
- [x] Best practices for working with agents in VS Code [vscode-docs#8581](https://github.com/microsoft/vscode-docs/issues/8581) @ntrogh
- [x] Refresh AI customization docs [vscode-docs#9344](https://github.com/microsoft/vscode-docs/issues/9344) @ntrogh
- [ ] :runner: Add guide for developer-adjacent roles to leverage AI features [vscode-docs#9345](https://github.com/microsoft/vscode-docs/issues/9345) @ntrogh @digitarald

### Engineering
- [x] Use esbuild to transpile and bundle VS Code @jrieken

---
### Deferred
- [ ] Explore layouts for Chat session + Multi File Diff [vscode#260226](https://github.com/microsoft/vscode/issues/260226) @joshspicer
- [ ] Update Profiles UI to include AI features [vscode#270130](https://github.com/microsoft/vscode/issues/270130) @eli-w-king
- [ ] Refine chat motion rendering [vscode#287175](https://github.com/microsoft/vscode/issues/287175) @hawkticehurst @justchen @roblourens


---
# DOCUMENT_SOURCE: web::github_changelog_copilot_rss
- **CANONICAL_URL**: https://github.blog/changelog/label/copilot/feed/
- **RAW_SOURCE_URL**: https://github.blog/changelog/label/copilot/feed/
- **SHA256_FINGERPRINT**: `f6c5c6fbfe671c55890651aa310a9f540bc6b4c129c894aa824e8f918c8d7fba`
- **LAST_VERIFIED_UTC**: 2026-11-11T05:27:03.215713+00:00
---

# GitHub Copilot Official Changelog Feed

## GitHub App support for Enterprise Copilot seat management
- **Date**: Wed, 11 Nov 2026 00:10:31 +0000
- **URL**: https://github.blog/changelog/2026-11-10-github-app-support-for-enterprise-copilot-seat-management

Enterprise GitHub Apps can now call the enterprise-level Copilot seat management APIs to control which users and enterprise teams are assigned Copilot seats. The Copilot seat management APIs are accessible...
The post GitHub App support for Enterprise Copilot seat management appeared first on The GitHub Blog .

## Gemini 4 Carbon in GitHub Copilot
- **Date**: Tue, 10 Nov 2026 19:26:51 +0000
- **URL**: https://github.blog/changelog/2026-11-10-gemini-4-carbon-in-github-copilot

Gemini 4 Carbon, Google’s latest model, is now generally available in GitHub Copilot. It is designed for complex coding, agentic, and reasoning tasks, with a focus on secure code generation...
The post Gemini 4 Carbon in GitHub Copilot appeared first on The GitHub Blog .

## C++ language server now auto-configures MSBuild builds
- **Date**: Tue, 10 Nov 2026 17:04:10 +0000
- **URL**: https://github.blog/changelog/2026-11-10-c-language-server-now-auto-configures-msbuild-builds

The Microsoft C++ Language Server for GitHub Copilot CLI now bundles its MSBuild compile commands extractor and invokes it automatically. An agent no longer needs to discover and run a...
The post C++ language server now auto-configures MSBuild builds appeared first on The GitHub Blog .

## Claude Fable 5.2 in GitHub Copilot
- **Date**: Mon, 09 Nov 2026 16:46:43 +0000
- **URL**: https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot

Claude Fable 5.2, Anthropic’s newest Fable model, is now generally available in GitHub Copilot. You can use it for complex, multistep coding tasks across large codebases. In early testing, Fable...
The post Claude Fable 5.2 in GitHub Copilot appeared first on The GitHub Blog .

## Copilot code review: API management and review overview updates
- **Date**: Sat, 07 Nov 2026 00:27:19 +0000
- **URL**: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates

You can now manage GitHub Copilot code review settings through the REST and GraphQL APIs, from enterprise policy down to individual repositories. Copilot’s review overview comment is now more compact,...
The post Copilot code review: API management and review overview updates appeared first on The GitHub Blog .

## Copilot impact dashboard adds chat and VS Code agent usage
- **Date**: Fri, 06 Nov 2026 22:17:28 +0000
- **URL**: https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage

The Agent adoption chart in the Copilot impact dashboard now includes Copilot Chat and the VS Code Agents window, so you can see engagement across nine Copilot experiences. The adoption...
The post Copilot impact dashboard adds chat and VS Code agent usage appeared first on The GitHub Blog .

## GitHub Copilot weekly releases — November 2
- **Date**: Fri, 06 Nov 2026 21:00:26 +0000
- **URL**: https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2

This week, Copilot comes to JetBrains Air and Xcode’s coding assistant, with updates to help you manage pull requests, settings, and agent sessions. GitHub Copilot app Set up Agent Merge...
The post GitHub Copilot weekly releases — November 2 appeared first on The GitHub Blog .

## @GitHub in Slack and Teams is generally available and more
- **Date**: Fri, 06 Nov 2026 20:31:08 +0000
- **URL**: https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available

Turn conversations into code with @GitHub in Slack and Teams! Investigate bugs, create issues, implement changes, and open pull requests—all without leaving your conversation. What’s new Build and review together...
The post @GitHub in Slack and Teams is generally available and more appeared first on The GitHub Blog .

## Usage metrics API adds code review details and addressed rate
- **Date**: Fri, 06 Nov 2026 00:19:07 +0000
- **URL**: https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate

The enterprise and organization repository-level Copilot usage metrics reports now show what happens to Copilot code review feedback. A new copilot_code_review object on each repos-1-day row reports how many Copilot-reviewed...
The post Usage metrics API adds code review details and addressed rate appeared first on The GitHub Blog .

## Usage metrics API flags telemetry and version gaps
- **Date**: Fri, 06 Nov 2026 00:08:31 +0000
- **URL**: https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps

The Copilot usage metrics API now shows which users are missing client telemetry or are running IDE or extension versions below the usage metrics minimums. New per-user fields appear in...
The post Usage metrics API flags telemetry and version gaps appeared first on The GitHub Blog .
