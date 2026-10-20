# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-10-20T22:05:40.003090+00:00
- **Total Palabras**: 8,351 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_141.md
- **CANONICAL_URL**: https://code.visualstudio.com/release-notes/v1_141
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_141.md
- **SHA256_FINGERPRINT**: `18237e23206356d71f5afb2099e74dcd215f19f4689560e115c6a031bf8163d3`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:32.031016+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.141

# Visual Studio Code 1.141

**Update 1.141.1**: The update addresses these [security issues](https://github.com/microsoft/vscode/issues?q=is%3Aissue+milestone%3A1.141.1).

**Update 1.141.2**: The update addresses these [issues](https://github.com/microsoft/vscode/pulls?q=is%3Apr+milestone%3A1.141.2+is%3Aclosed+label%3Acandidate).

## Release highlights

This release makes it easier to manage agent sessions, protect agent workflows, edit columnar text, and work across GitHub Enterprise instances.

* [Clean up worktree storage](#reclaim-storage-from-inactive-worktrees): Reclaim disk space from inactive agent session worktrees, on demand or automatically.

* [Cross-platform sandboxing](#sandboxing-in-the-copilot-agent-host): Limit agent access to files and network resources on Windows, macOS, and Linux with terminal sandboxing.

* [Arrange sessions](#arrange-sessions-in-a-grid): Compare and monitor multiple agent sessions side by side in a grid layout.

* [Continue external sessions](#continue-local-external-copilot-sessions-without-reloading): Pick up local external Copilot and Codex conversations in VS Code without losing context.

* [Block pasting](#spreading-block-pasting): Paste block rows across successive lines from a single cursor.

* [Multiple GitHub Enterprise instances](#sign-in-to-multiple-github-enterprise-instances): Sign in to GHE.com and GitHub Enterprise Server accounts from the same VS Code window.

## Agent loop

### Copilot harness

The Copilot harness adds exciting new agent functionality to VS Code. It's powered by the Copilot SDK, so its behavior and capabilities are consistent with other Copilot products, including the standalone GitHub Copilot app and the Copilot CLI.

To start using the Copilot harness, select it from the harness picker in the chat input. In this release, it might already be the default selection for you. You can continue working as you normally do.

![Screenshot showing the Copilot harness selected in the harness picker.](images/1_141/Harness-Copilot.webp)

The harness runs in a dedicated [agent host](https://code.visualstudio.com/docs/agents/concepts/agent-host) process based on the Agent Host Protocol (AHP), so you can connect to the same agent session from multiple VS Code windows.

Learn how to [work with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses#copilot), or explore the architecture and workflows in the [agent host blog post](https://code.visualstudio.com/blogs/2026/08/26/agent-host-architecture). If you have feedback or requests, [please file an issue](https://github.com/microsoft/vscode/issues).

### Reclaim storage from inactive worktrees

Run **Chat: Open Worktree Cleanup** to see how much disk space inactive agent session worktrees use and remove the ones you no longer need. Filter sessions by how long they have been inactive, review each worktree's size, and select the worktrees to clean up.

The cleanup editor also lets you configure automatic cleanup for sessions with merged pull requests and control whether VS Code suggests cleanup when session storage grows large.

![Screenshot showing the worktree cleanup editor with cleanup settings and inactive session worktrees.](images/1_141/worktree-cleanup-editor.webp)

When ``chat.agentSessions.sessionStorageCleanupSuggestion.enabled`` is enabled, the Agents window notifies you when enough inactive worktrees accumulate or they use enough disk space to make cleanup worthwhile.

![Screenshot showing a worktree cleanup suggestion in the Agents window.](images/1_141/worktree-cleanup.webp)

Cleaning up marks the selected sessions as done and deletes their worktrees. You can restore a session later to recreate its worktree. Active, running, needs-input, and pinned sessions are protected from cleanup.

### Keep track of background shells

When the agent runs a command in the background, it keeps working on other steps while the command runs. In [Copilot harness](#copilot-harness) sessions, a **Background Shells** pill above the chat input lists the shells that are still running, in both the Agents window and the editor window.

Select the pill to see each shell's command and how long it has been running, and select a shell to watch its output stream as the command runs, if output is available. A shell leaves the list when its command finishes.

![Screenshot showing the Background Shells pill with a running shell's output streaming in its details.](images/1_141/background-shell-streaming.webp)

### More control for agent-triggered messages

When agents delegate work across conversations, they can adjust the delegated task as requirements change instead of waiting for the other session to finish. The `send_message` tool supports these actions between sessions and nested sessions on the same agent host:

* Steer an active conversation with a correction.
* Queue a follow-up as a separate turn.
* Replace a queued message while preserving its place in the queue.
* Cancel a queued message before processing begins.

Queued messages run in order. After a message starts processing, it can no longer be replaced or cancelled.

## Agent UX

### Arrange sessions in a grid

Compare results, monitor long-running tasks, or work across related conversations without repeatedly switching between sessions. Like in the editor window, the two-dimensional session grid in the Agents window lets you drag sessions into horizontal or vertical splits and resize the panes.

Maximize a session when you need to focus, then return to the grid to continue working across conversations.

<video src="images/1_141/sessions-grid.mp4" title="Video showing multiple agent sessions arranged in a grid in the Agents window." autoplay loop controls muted></video>

### Compact layout density

**Setting**: ``window.density.layout``

Fit more content in the Agents window with the Compact layout density. Compact density uses a shorter title bar, removes the gaps between workbench parts, and reduces pane spacing.

By default, the Agents window follows the user-level ``window.density.layout`` setting, which also applies to editor windows. To set a different density for the Agents window only, open it and choose **View > Layout Density**. The density of editor windows remains unchanged.

<video src="images/1_141/agents-compact-mode.mp4" title="Video showing the Agents window in compact layout density." autoplay loop controls muted></video>

### Additional session-filtering options

Focus your sessions list on the work you care about. Open **Filter Sessions** to filter independently by:

* **Environment**: Where the session runs, such as locally, in the cloud, or on a remote host.
* **Harness**: Which agent harness the session uses.
* **Created In**: Which application created the session, such as VS Code, Copilot CLI, or the Copilot app.

The menu also brings together ordering, grouping, **Show Done**, and **Created Externally** controls.

![Screenshot showing the Filter Sessions menu with environment, application, harness, and external-session filters.](images/1_141/sessions-filter-menu.webp)

### Track activity across nested sessions

[Nested sessions](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions#_run-multiple-chats-in-a-session) let you split related work across separate conversations. In the Agents window, each nested session shows its unread status and last-modified time, helping you find recent activity and conversations that need your attention without opening them individually.

![Screenshot showing the nested sessions tree in the Agents window, with one nested session highlighted to show its blue unread indicator, repository, and last-modified time.](images/1_141/nested-session-details.webp)

Status is tracked independently for each conversation:

* Opening a nested session marks only that conversation as read. An unread nested session does not make the main session appear unread.
* The last-modified time reflects activity in that conversation, not activity in the main session or another nested session.

Read status and last-modified times persist when you reload the window or restart VS Code.

To clear unread status for an entire session tree, right-click the main session and select **Mark as Read**. Unrelated sessions are not affected.

### Simplified new-session controls (Experimental)

**Settings**: ``sessions.chat.experimental.newSessionComposerLayout``, ``sessions.chat.unifiedWorkspacePicker.enabled`` (Agents window only)

The experimental new-session composer keeps your prompt at the center while making session choices easier to review. Workspace, repository, and harness controls now appear in a collapsible **Session Options** tray above the chat input.

<video src="images/1_141/new-session-composer-options.mp4" title="Video showing the new-session composer expanding and collapsing workspace, worktree, branch, and harness controls." autoplay loop controls muted></video>

Getting-started tips now appear in a rounded notice below the chat input, so they no longer separate the session controls from your prompt.

![Screenshot showing a getting-started tip below the new-session chat input.](images/1_141/new-session-composer-tip-below-input.webp)

Collapse the tray to reduce visual clutter without changing your selections. The composer remembers your choice, adapts labels as the window narrows, and keeps the options expanded when screen reader optimized mode is active. When you use a custom chat background, the tray has an opaque surface to keep its controls readable.

### Improved context picker positioning

The **Add Context** picker now opens next to the button that invoked it and closes when you select the button again. This keeps the picker visually connected to the chat input in the editor and Agents windows.

![Screenshot showing the Add Context picker anchored beside the chat input button.](images/1_141/add-context-picker-anchored.webp)

### Move agent picker in context control (Experimental)

**Setting**: ``sessions.chat.experimental.agentsPickerInAttachContextMenu`` (Agents window only)

If you prefer to have the **Agent** picker initially hidden from the chat input to reduce the number of controls, you can configure this setting to move it into the **Add Context** menu. After you select an agent, the picker returns to the chat input.

<video src="images/1_141/agent-picker-in-add-context.mp4" title="Video showing the Agent picker moving from Add Context to the chat toolbar after an agent is selected." autoplay loop controls muted></video>

### Customize new-session welcome messages (Experimental)

**Settings**: ``sessions.chat.experimental.welcomePhrases``, ``sessions.chat.experimental.welcomeMessages`` (Agents window only)

New-session welcome messages add personality to the Agents window. In this release, you can add your own phrases to the defaults or replace the default phrases. Use the `{name}` placeholder to position your welcome name anywhere in a phrase.

<video src="images/1_141/customize-welcome-phrases.mp4" title="Video showing a personalized new-session welcome phrase and the welcome name editor." autoplay loop controls muted></video>

Select **Customize Welcome Message** beside the heading to change your name or open the phrase setting. You can also right-click the heading and select **Hide Welcome Message** to turn welcome phrases off.

## Agent environments

### Continue local external Copilot sessions without reloading

New conversations from the Copilot CLI and GitHub Copilot app are now picked up automatically as external sessions as soon as you send the first request, even when the Agents window is already open. You can open and continue these conversations directly from the Agents window.

<video src="images/1_141/copilot-sessions-live.mp4" title="Video showing a new Copilot conversation appearing as an external session in the Agents window without reloading." autoplay loop controls muted></video>

Use the **Created In** and **Created Externally** filters to choose which conversations appear in the sessions list.

### Codex chat handoff between apps

Pick up a Codex chat started in the ChatGPT app or Codex CLI and continue it in VS Code's Agents window on the same machine, with your conversation history intact. You can switch back to the ChatGPT app or Codex CLI later and continue the same chat.

To use your GitHub Copilot subscription in VS Code, choose a Copilot model in the model picker. For example, you can keep working with Copilot after reaching your ChatGPT usage limit.

With [Codex enabled](https://code.visualstudio.com/docs/agents/run/agent-harnesses#codex) and **Created Externally** sessions visible, chats created or updated in ChatGPT or Codex CLI appear within a few seconds without reloading VS Code.

Only one application can send messages to the chat at a time. If ChatGPT or Codex CLI still has the chat open, a **This chat is open in another app** banner in VS Code explains why sending is unavailable. Fully quit ChatGPT or exit the Codex CLI session, then select **Retry**. Your draft and attachments stay in place, and **Retry** checks access without sending your message.

<video src="images/1_141/chatgpt-codex-handoff.mp4" title="Video showing a Codex chat started in ChatGPT continuing in VS Code with a GitHub Copilot subscription, including the lock banner and Retry action." autoplay loop controls muted></video>

### Download remote files from the editor

Save an open remote file locally, without having to navigate for it in the Files panel. In the Agents window, open the editor's **More Actions** menu and select **Download...** to download the file to a local destination.

### Dev Container samples (Experimental)

**Setting**: ``chat.agentHost.devContainer.samples.enabled`` (Agents window only)

Try an agent with a ready-to-use development environment without first cloning a repository or installing its language tools locally. The Agents window now offers Dev Container samples for Go, .NET, Node.js, PHP, Python, and Rust.

![Screenshot showing the Dev Container Sample submenu in the Agents window with samples for Go, .NET, Node.js, PHP, Python, and Rust.](images/1_141/dev-container-samples.webp)

[Install and start Docker](https://code.visualstudio.com/docs/devcontainers/containers#installation), and then enable the setting. Open a new session in the desktop Agents window, select **Dev Container Sample** from the workspace picker, and send a prompt.

This also requires ``chat.agentHost.devContainer.enabled`` and ``chat.remoteAgentHostsEnabled`` to be enabled.

## Agent security

### Sandboxing in the Copilot agent host

**Settings**: ``chat.agent.sandbox.enabled``

Sandboxing gives you more control over what Copilot can access while working on a task. It limits how supported agent operations access files and network resources, and helps to reduce the impact of model mistakes, prompt injection, untrusted dependencies, and locally launched tool servers.

Depending on the operation and platform, these restrictions use operating-system protections or checks within the agent host process. Sandboxing adds a layer of protection, but does not replace endpoint security or provide a standalone security boundary.

Sandboxing is available on **Windows, macOS, and Linux**. On Windows, required operating-system updates must be installed. Refer to [Check platform availability](https://code.visualstudio.com/docs/agents/run/agent-sandboxing#_check-platform-availability) for more details.

To configure sandboxing for all your sessions, enable the ``chat.agent.sandbox.enabled`` setting. You can also control sandboxing at the session level with the **Sandboxing for terminal** toggle in the **Permissions** menu.

![Screenshot showing the Sandboxing for terminal toggle in the Permissions menu.](images/1_141/sandbox-toggle.webp)

You can further customize filesystem permissions and network access via their respective settings in VS Code.

Sandboxing works with both local and connected remote sessions. For local sessions, restrictions are enforced on your machine. For remote sessions, they are enforced on the remote host where Copilot runs tools and commands. Filesystem permissions refer to paths on the machine running the agent.

Locally launched MCP and language servers are sandboxed by default when sandboxing is enabled.

## Chat experience

### Persistent progress in chat

**Settings**: ``chat.experimental.persistentProgress``, ``chat.experimental.persistentProgressVerbosity``

Persistent progress is rolling out to all users. It keeps in-progress responses visible and lets you control how much progress detail appears. Use ``chat.experimental.persistentProgress`` to choose among three icon variants, including a monochrome icon or no icon.

### Meet Blobby

The `/vscode-pet` has a name: Blobby. Type `/vscode-pet` in any chat in the editor or Agents window to meet Blobby.

Type `/blobby` to customize Blobby. More customization options become available as you explore chat and unlock achievements.

![Animation showing the VS Code Pet sleeping in both insiders and stable colors.](images/1_141/sleep-wake-pr330399.png)

Learn more about [Blobby and chat pets](https://code.visualstudio.com/docs/agents/reference/chat-pet).

## MCP

### See discovered MCP servers in Customizations editor (Preview)

Find MCP servers supplied by plugins, extensions, and built-in integrations alongside your configured servers in the **MCP Servers** section of the Agent Customizations editor. Servers discovered outside your workspace's `mcp.json` are visible in the UI, so you don't have to use **MCP: List Servers** to find them.

Run **Chat: Open Customizations** from the Command Palette and select **MCP Servers** to inspect the available integrations. Learn more about [adding and managing MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers).

## Editor experience

### Frosted glass overlays and menus

**Settings**: ``workbench.modernUIFrostedGlass``, ``workbench.modernUIFrostedGlassOpacity``

Menus, the Command Palette, and other pop-ups now use softly blurred, frosted glass backgrounds in the desktop Agents window. Frosted glass is also available in editor windows when the modernized UI is enabled with ``workbench.experimental.modernUI``.

Use ``workbench.modernUIFrostedGlassOpacity`` to control how much of the blurred content shows through. Lower values make the background more transparent, while higher values make it more solid.

Frosted glass respects reduced-transparency preferences in VS Code and your operating system, and uses solid backgrounds with high contrast themes or when the effect isn't supported. Disable ``workbench.modernUIFrostedGlass`` if you notice display or performance issues.

<video src="images/1_141/frosted-glass.mp4" title="Video showing the frosted glass effect in the editor with the modernized UI enabled." autoplay loop controls muted></video>

### Choose your tab style (Experimental)

**Setting**: ``workbench.experimental.modernUIEditorTabStyle``

When the modernized UI is enabled (``workbench.experimental.modernUI``), you can choose between two tab styles:

* `connected`: visually connect the active tab to its content.
* `pill`: display tabs as separate rounded pills.

<video src="images/1_141/connected-pill-tabs.mp4" title="Video showing the connected and pill editor tab styles." autoplay loop controls muted></video>

### Spreading block pasting

**Setting**: ``editor.multiCursorPaste``

Paste a copied block at a single cursor to distribute its rows across successive destination lines. This behavior is enabled by default when ``editor.multiCursorPaste`` is set to `spread`. Set it to `full` to paste the complete block instead.

<video src="images/1_141/block-pasting.mp4" title="Video showing the new behavior of block pasting." autoplay loop controls muted></video>

## Authentication

### Sign in to multiple GitHub Enterprise instances

**Setting**: ``github-enterprise.uris``

Many organizations use GitHub Copilot through a GHE.com account but keep their code on GitHub Enterprise Server (GHES). The `github-enterprise.uri` setting held a single instance, so you couldn't be signed in to both at once. For example, you couldn't use Copilot with your GHE.com account and review pull requests on GHES in the same VS Code window.

The new ``github-enterprise.uris`` setting takes a list of GHE.com and GHES instances:

```json
"github-enterprise.uris": [
  "https://octocat.ghe.com",
  "https://github.contoso.com"
]
```

The GitHub Enterprise authentication provider holds accounts from every instance in the list. Each account is labeled with its host, such as `monalisa - octocat.ghe.com`, so you can tell them apart in the Accounts menu. When more than one instance is configured, signing in asks which instance to use. The order of the entries doesn't select a default instance.

To check or change which account an extension uses, select **Manage Extension Account Preferences...** in the Accounts menu, or run **Accounts: Manage Extension Account Preferences...** from the Command Palette.

These extensions support multiple instances:

* **GitHub Copilot** works with GHE.com instances. When you sign in with **Continue with GHE.com**, you can enter an instance name, such as `octocat`, or its full URL. VS Code adds the instance to ``github-enterprise.uris`` without removing your other instances, and if an existing entry isn't a valid URL, it offers to fix that entry.
* **GitHub Pull Requests** offers to add the host to ``github-enterprise.uris`` when you open a repository from an enterprise instance that isn't configured yet. It uses one GitHub Enterprise account at a time, so repositories on your other instances are available after you switch accounts. Using several enterprise instances at the same time is tracked in [microsoft/vscode-pull-request-github#9004](https://github.com/microsoft/vscode-pull-request-github/issues/9004).
* **GitHub Repositories** opens repositories from several GHE.com instances side by side. It doesn't support GHES repositories.

If you already use `github-enterprise.uri`, you stay signed in. The first time you launch this release, VS Code moves your stored credentials to work with the new setting. `github-enterprise.uri` is deprecated. When both settings are set, ``github-enterprise.uris`` takes precedence, and an empty list (`[]`) turns off GitHub Enterprise sign-in.

## Enterprise

### Migration of legacy VS Code policies to Agent Host managed settings

The Copilot harness, powered by the Copilot SDK and running in VS Code's Agent Host, is gradually becoming the default for enterprise users who have VS Code experiments enabled. To preserve existing enterprise controls during this transition, VS Code translates supported legacy policies into unified managed settings at runtime when possible. This translation applies to sessions on the same machine and does not change your policy configuration.

Enterprises should still migrate to [unified managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started) where applicable for consistent policy management across VS Code, the GitHub Copilot app, and Copilot CLI.

### Use managed settings to require sandboxing (Preview)

To require sandboxing in Copilot Agent Host and prevent bypass, use these [unified managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started):

```json
{
    "sandbox": {
        "enabled": true,
        "allowBypass": false
    }
}
```

Legacy VS Code sandbox settings and device policies are deprecated. `ChatAgentSandboxEnabled` now supplies an overridable default rather than a mandatory requirement in Agent Host. Local behavior is unchanged.

### Attribute Agent Host sessions to users and machines

Administrators can more easily attribute Agent Host sessions to users and machines by including operating system usernames and hostnames in VS Code's Agent Host telemetry. Merge this example into your [unified managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started), alongside your existing telemetry exporter configuration:

```json
{
    "telemetry": {
        "enabled": true,
        "capture": {
            "identity": true
        }
    }
}
```

For example, captured identity attributes can include (illustrative values):

```json
{
    "user.name": "octokit",
    "process.user.name": "devuser",
    "host.name": "dev-workstation"
}
```

The OS username (`process.user.name`) and hostname (`host.name`) are resource attributes. The signed-in GitHub username (`user.name`) appears on runtime spans when supported by the bundled Copilot runtime.

Identity capture is off by default, and the managed value overrides personal preferences. It is independent of content capture. VS Code's host-side control does not govern a runtime's direct exports.

### Keep your selected agent through policy checks

When your enterprise requires a fresh policy check with [`forceRemoteSettingsRefresh`](https://github.com/github/docs/blob/main/content/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md#supported-keys), chat preserves your selected agent during policy checks instead of switching to **Ask** or **Edit**. Routine background refreshes also keep the last accepted policy active while loading. Startup, account changes, and failed refreshes continue to block submissions until policy checks succeed. Newly accepted restrictions continue to apply.

## Contributions to extensions

### GitHub Pull Requests

There has been more progress on the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension, which enables you to work on, create, and manage pull requests and issues. New features include:

* Create, view, and merge stacked pull requests by setting `githubPullRequests.experimental.stacks` to `true`.
* Support for configuring and selecting between multiple GitHub Enterprise instances.

Review the [changelog for the 0.168.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01680) release of the extension to learn about everything in the release.

## Deprecated features and settings

### GitHub Enterprise URI setting

The `github-enterprise.uri` setting is deprecated in favor of ``github-enterprise.uris``, which accepts multiple GHE.com and GitHub Enterprise Server instances. VS Code still reads `github-enterprise.uri` when ``github-enterprise.uris`` isn't configured.

### Legacy VS Code sandbox settings and device policies

Legacy VS Code sandbox settings and device policies are deprecated. `ChatAgentSandboxEnabled` now supplies an overridable default rather than a mandatory requirement in Agent Host. Local behavior is unchanged.

## Thank you

Contributions to `vscode`:

* [@dzamoshchin (Daniel Zamoshchin)](https://github.com/dzamoshchin): Mark virtual tool groups as used when they are activated [PR #338812](https://github.com/microsoft/vscode/pull/338812)
* [@jimmylewis (Jimmy Lewis)](https://github.com/jimmylewis): extensions: keep update checks on polling cadence [PR #339365](https://github.com/microsoft/vscode/pull/339365)
* [@na2co3-ftw (na2co3)](https://github.com/na2co3-ftw): Modern UI: Fix redundant tab action fading in connected editor tabs [PR #336871](https://github.com/microsoft/vscode/pull/336871)
* [@rohit489 (Rohit Agrawal - MSFT)](https://github.com/rohit489): Record CAPI X-GitHub-Copilot-Request-Te on GitHub telemetry events [PR #339087](https://github.com/microsoft/vscode/pull/339087)
* [@shoemoney (Jeremy Schoemaker)](https://github.com/shoemoney): fix(markdown): preserve non-line fragments in preview links [PR #332661](https://github.com/microsoft/vscode/pull/332661)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * fix: memory leak in terminal replay [PR #338252](https://github.com/microsoft/vscode/pull/338252)
  * fix: memory leak in semantic tokens [PR #336024](https://github.com/microsoft/vscode/pull/336024)
  * fix: memory leak in search editor [PR #331014](https://github.com/microsoft/vscode/pull/331014)
  * terminal: cancel unnecessary telemetry timeout on disposal [PR #333963](https://github.com/microsoft/vscode/pull/333963)
  * fix: memory leak in animation frame window disposal [PR #338263](https://github.com/microsoft/vscode/pull/338263)
  * fix: memory leak in chat participant disposal [PR #338230](https://github.com/microsoft/vscode/pull/338230)
  * fix: memory leak in custom document disposal [PR #338250](https://github.com/microsoft/vscode/pull/338250)
  * fix: memory leak in mapped edit provider disposal [PR #338245](https://github.com/microsoft/vscode/pull/338245)
  * fix: memory leak in extension host telemetry [PR #334096](https://github.com/microsoft/vscode/pull/334096)
  * fix: memory leak in auxiliary window font measurements [PR #338255](https://github.com/microsoft/vscode/pull/338255)
  * fix: memory leak in SCM artifact commands [PR #338251](https://github.com/microsoft/vscode/pull/338251)
  * fix: memory leak in pixel ratio window disposal [PR #338257](https://github.com/microsoft/vscode/pull/338257)
  * fix: memory leak in integrated browser element handles [PR #338247](https://github.com/microsoft/vscode/pull/338247)
  * fix: memory leak in terminal horizontal scrollbars [PR #338241](https://github.com/microsoft/vscode/pull/338241)
  * fix: memory leak in extension host tree view disposal [PR #338235](https://github.com/microsoft/vscode/pull/338235)
  * fix: memory leak in composite drag and drop registrations [PR #338215](https://github.com/microsoft/vscode/pull/338215)
  * fix: memory leak in integrated browser inspector sessions [PR #338228](https://github.com/microsoft/vscode/pull/338228)
  * fix: memory leak in chatInputPart [PR #327157](https://github.com/microsoft/vscode/pull/327157)
  * fix: memory leak in terminal shell execution streams [PR #338243](https://github.com/microsoft/vscode/pull/338243)
  * fix: memory leak in notebook cell status bar commands [PR #336028](https://github.com/microsoft/vscode/pull/336028)
  * fix: memory leak in issueReporterModel [PR #335098](https://github.com/microsoft/vscode/pull/335098)
  * fix: memory leak in image carousel editor [PR #333981](https://github.com/microsoft/vscode/pull/333981)
  * fix: memory leak in notebook serializer disposal [PR #338212](https://github.com/microsoft/vscode/pull/338212)
  * fix: memory leak in MainThreadShare [PR #334110](https://github.com/microsoft/vscode/pull/334110)
  * fix: memory leak in multi diff editor tabs [PR #333186](https://github.com/microsoft/vscode/pull/333186)
  * fix: memory leak in test observer disposal [PR #338213](https://github.com/microsoft/vscode/pull/338213)
  * fix: memory leak in modalEditorPart [PR #326885](https://github.com/microsoft/vscode/pull/326885)
  * fix: memory leak in comment thread disposal [PR #338216](https://github.com/microsoft/vscode/pull/338216)
  * fix: memory leak in line data event addon [PR #332139](https://github.com/microsoft/vscode/pull/332139)
  * fix: memory leak in notebook kernel source menus [PR #338218](https://github.com/microsoft/vscode/pull/338218)
* [@soreavis](https://github.com/soreavis): JSON - support ${workspaceFolder} in json.schemas fileMatch patterns [PR #326706](https://github.com/microsoft/vscode/pull/326706)
* [@yuezhang030](https://github.com/yuezhang030): Add vscModelF prompt [PR #338809](https://github.com/microsoft/vscode/pull/338809)

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_142.md
- **CANONICAL_URL**: https://code.visualstudio.com/release-notes/v1_142
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_142.md
- **SHA256_FINGERPRINT**: `5978f7b095056c2c8a5b9b32a7caa43249e7d0521cf71a90a8f75950b54879cd`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.980751+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.142

# Visual Studio Code 1.142

## Release highlights

This release adds shared canvases for agent workflows, lets you move chats without losing context, expands the Markdown editor, and gives administrators more control over agent permissions.

* [Canvases (Preview)](#canvases-preview): Collaborate with agents beyond chat using visual and interactive canvases.

* [Move chats](#move-chats-between-folders-and-worktrees): Continue a chat in another folder or a new Git worktree without losing conversation history.

* [Markdown editor](#markdown-editor): Work on Markdown files more efficiently with features like pasting images, renaming file links, or breadcrumb navigation.

* [Enterprise management](#enterprise): Enforce agent sandboxing and permission policies while controlling which permission modes developers can use.

* [Redesigned model picker](#redesigned-model-picker): Quickly switch between Copilot and BYOK contributed models, and manage effort levels and context windows more intuitively.

## Agents

### Copilot harness

The Copilot harness is powered by the Copilot SDK, a shared foundation that helps align behavior, capabilities, and improvements across Copilot products. In VS Code, the Copilot harness runs sessions through the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host), which lets sessions continue in the background and be accessed from both the VS Code editor window and the Agents window.

The Copilot harness has been available from the harness picker in the chat input. Based on overwhelmingly positive and valuable feedback, we're progressively rolling it out as the default harness for new sessions in VS Code. When you start a new session, **Copilot** in the harness picker indicates that the session will use the Copilot harness.

![Screenshot showing the harness picker with hover descriptions for the Local and Copilot harnesses.](images/1_142/harness-hover.webp)

Thank you to everyone who has shared feedback. We're actively using it to shape the experience. One example is reintroducing **Ask** as a built-in agent in the Copilot harness. Your feedback showed that a dedicated read-only experience remains valuable. Select **Ask** from the agent picker to use it.

Learn how to [work with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses#use-the-copilot-harness), or explore the architecture and workflows in the [agent host blog post](https://code.visualstudio.com/blogs/2026/08/26/agent-host-architecture). If you have feedback or requests, [please file an issue](https://github.com/microsoft/vscode/issues).

### Canvases (Preview)

**Setting**: ``chat.canvases.enabled``

Canvases are interactive interfaces to collaborate with an agent. A canvas opens beside the chat, where you and the agent can inspect and update the same artifact instead of coordinating solely through prompts.

For example, use a Kanban canvas to plan and track implementation work. You can create and move cards directly, while the agent can break a feature into tasks, update their status, or add newly discovered work. Canvases work in both the VS Code editor window and the Agents window, and canvas extensions are also supported in the [GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-canvas-extensions).

![Screenshot of a kanban canvas showing tasks and columns in the editor.](images/1_142/kanban-canvas.webp)

Canvases are available in Preview in the VS Code desktop app for local sessions that use the Copilot harness. Enable ``chat.canvases.enabled``, and then start a new session with the Copilot harness.

Every canvas is provided by a canvas extension. To get started, you have two options:

* **Create a canvas extension**: Enter `/create-canvas` in the chat input and describe the user interface you want for your project. The skill then creates a canvas extension in your workspace and opens its canvas.

* **Install a chat plugin**: For now, install a [chat plugin that includes a canvas extension](https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-canvas-extensions) through the GitHub Copilot app. Then switch to VS Code and ask the agent to list the available canvases and have it open one.

After you install a canvas extension, you can also open an available canvas in the Agents window from **Add Tab (+)** > **Canvas**.

Explore and install [sample canvas extensions from the community](https://awesome-copilot.github.com/extensions/).

Learn more about [canvas support](https://code.visualstudio.com/docs/agents/run/agent-harnesses#_use-canvases-with-the-copilot-harness) in the VS Code documentation.

<video src="images/1_142/canvases.mp4" title="Video showing a canvas being used in VS Code." autoplay loop controls muted></video>

### Move chats between folders and worktrees

Previously, if you started investigating a task in one folder and then wanted to implement it in a Git worktree, or continue in a different repository, you had to start a new chat and rebuild the context.

In the [Agents window](https://code.visualstudio.com/docs/agents/run/agents-window), you can now ask the agent to move the current chat to another folder or into a new Git worktree, and it keeps the conversation history intact. Changing the workspace also works for chats that already have a workspace, and the agent can isolate work in a new worktree.

Ask the agent with a natural-language prompt, for example:

```prompt
Continue this task in a new Git worktree of the current repository before implementing it.
```

The agent finishes the current turn, moves the chat, and shows a notice when the workspace changes. Then it continues the task automatically in the new location. Edits and commands run in the new location while your original checkout stays unchanged.

<video src="images/1_142/move-chat-worktree.mp4" title="Video showing a chat started in the VS Code repository moving to a new Git worktree, continuing with edits, and showing the worktree in the Files explorer." autoplay loop controls muted></video>

The move is available for agent sessions that use the Codex harness or Codex in Interactive mode, and that contain one chat and one local folder. For prerequisites and details about which files are available in the new location, see [Move a chat to another folder or worktree](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions#move-a-chat-to-another-folder-or-worktree).

### Session-scoped layout in the Agents window (Experimental)

**Setting**: ``sessions.experimental.layoutScope`` (Agents window only)

Previously, when you switched between sessions in the Agents window, VS Code shared layout settings such as editor visibility, details, and panel visibility across sessions. If you're used to VS Code remembering the layout for each workspace, sharing the layout across sessions can be disruptive.

With the new experimental ``sessions.experimental.layoutScope`` setting, you can choose how much of the layout each session remembers. Reload the window after you change the setting. It supports the following values:

* `session-shared` (default): The current behavior. A session and its nested sessions share the same editors and selected panel views. Editor, details, and bottom panel visibility are shared across existing workspace sessions.

* `chat-shared`: A session and each of its nested sessions keep their own editors and selected panel views, while editor, details, and bottom panel visibility stay shared across existing workspace sessions.

* `chat`: A session and each of its nested sessions also keep their own editor and details composition and bottom panel visibility.

Window geometry, pane sizes, and the sidebar currently remain shared across the window.

### Customize the Agents window panel layout

You can now choose how the bottom panel is aligned in the Agents window. Right-click a panel tab, select **Align Panel**, and choose one of the following layouts:

* `Center` aligns the panel beneath the chat area, leaving more room for the side pane.

* `Justify` extends the panel across the full width of the window.

Your selection is saved per profile and preserved when maximizing or restoring the panel.

<video src="images/1_142/agents-window-bottom-panel-layout.mp4" title="Video showing the bottom panel alignment options in the Agents window." autoplay loop controls muted></video>

## Chat

### Quickly identify the active harness

Chat titles show the active harness name, such as **Copilot** or **Codex**, so you can identify it without opening the harness picker or hovering over the session list.

![Screenshot showing two chat sessions in editor windows, with the Codex and Copilot harness names displayed before each chat title.](images/1_142/harness-title.webp)

### Stop background shells

In [Copilot harness](#copilot-harness) sessions, the [background shells pill](https://code.visualstudio.com/updates/v1_141#_keep-track-of-background-shells) above the chat input lists the commands that the agent is still running in the background. When one of those commands is no longer useful, for example a test run that you want to restart or a command that runs longer than expected, you can stop it instead of waiting for it to finish.

Select the **Background Shells** pill, select a shell to open its details, and then select **Stop Shell** next to its command. Only that command ends, and the shell leaves the list. You can reach **Stop Shell** with the keyboard, and screen readers announce when the shell stops.

<video src="images/1_142/background-shell-stop.mp4" title="Video showing a background shell's output streaming in its details, then selecting Stop Shell, which removes the shell from the Background Shells list." autoplay loop controls muted></video>

Stopping a shell is only available for **attached shells**, which the agent runs as part of its current request. Detached shells run independently of the agent and can't be stopped from this interface.

Shell details also show each shell's full description above its command, even when the list truncates it. Long output is no longer cut off, and you can scroll back through earlier output, both in the shell's details and in the terminal output in the chat response.

### Stateful responses for BYOK custom endpoints

If your bring-your-own-key (BYOK) model uses a stateless Responses API, set `"statefulResponses": false` on its model entry in `chatLanguageModels.json` to send full conversation history with each request.

See [Custom Endpoint configuration](https://code.visualstudio.com/docs/agent-customization/language-models#stateful-responses-api-endpoints) for details.

### Windows sandboxing for Local harness is no longer supported

Windows sandboxing for terminal commands in Local agent sessions has been deprecated. For sandboxed command execution on Windows, use an Agent Host session. See the [Agent Host sandboxing documentation](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) for details.

### Redesigned model picker

Copilot and bring-your-own-key (BYOK) providers offer many models, each with strengths for different tasks. The redesigned model picker makes it easier to choose and switch models as your work changes.

The model picker uses a tabbed interface to separate Copilot and BYOK models.

![Screenshot showing the redesigned model picker with the Copilot tab selected and a list of models, where the selected model shows its thinking level and context size.](images/1_142/model-picker-list.webp)

When you hover over a model in the list, you can further configure its thinking level and context window size.

![Screenshot showing the model details view in the model picker, with options to select the thinking level and context size.](images/1_142/model-picker-reasoning-effort.webp)

## Markdown editor

### Editing mode closer to the Markdown source

When you edit Markdown, each source line appears on a separate visual line, making the document structure easier to follow. Read-only mode continues to render Markdown as before.

### Paste images

To add an image, for example a screenshot, to your Markdown document, simply paste it directly into the Markdown editor, like you could already do in the text editor. This makes it easier to include visual content without having to save and insert files manually.

<video src="images/1_142/markdown-pasting-images.mp4" title="Video showing an image pasted from the clipboard into the Markdown editor." autoplay loop controls muted></video>

### Rename file links

The Markdown editor now supports **Rename Symbol** (``Shortcut: editor.action.rename``), so you can rename file links in place and have the changes reflected throughout your document.

<video src="images/1_142/markdown-rename.mp4" title="Video showing a file link renamed in the Markdown editor." autoplay loop controls muted></video>

### Outline and breadcrumbs

The Markdown editor integrates with the Outline view and breadcrumbs, making it easier to inspect the heading structure and jump to a section.

<video src="images/1_142/markdown-outline-breadcrumbs.mp4" title="Video showing navigation through a Markdown document with the Outline view and breadcrumbs." autoplay loop controls muted></video>

### Copy code blocks

Like the Markdown preview, code blocks in the Markdown editor display a copy button on hover. This makes it easy to copy multiline code fragments without accidentally editing the content.

<video src="images/1_142/markdown-copy.mp4" title="Video showing the Copy button copying code from a Markdown code block." autoplay loop controls muted></video>

## Editor experience

### Merging document highlights from different providers

**Setting**: ``editor.occurrencesHighlightFromAllProviders``

Enable ``editor.occurrencesHighlightFromAllProviders`` to merge document highlights from all providers. By default, VS Code uses highlights only from the highest-priority provider.

## Languages

### Python

This release includes fixes for environment discovery, interpreter selection, and terminal activation in the Python Environments Extension.

* **Environment discovery:** Python installations managed by `uv` now appear under **Global**. Selecting an interpreter by path adds its virtual environment to the environment list, and deleting a virtual environment outside VS Code updates the selection.

* **Project-specific environments:** Automatic selection now prefers a project's own virtual environment over nested environments. Conda environment selection and Poetry package operations respect project scope, and background refreshes no longer overwrite newer interpreter selections.

* **Interpreter configuration:** Fixed resolution of `${workspaceFolder}`, relative paths, and commands such as `python3` in `python.defaultInterpreterPath`. The project-view environment selector now includes **Enter Interpreter Path**.

* **Terminal activation:** Shell-startup activation now updates when the global interpreter changes and is preserved when environment files change. Environment-file notifications include **Enable for Workspace** or **Enable for Folder** actions.

* **Python installation:** When `uv` is required but missing, setup offers to install it and continues to Python version selection without requiring a PATH refresh.

## Enterprise

### Automatically move policy-managed chats to Copilot Agent Host

Enterprise managed settings let administrators govern agent permissions and sandboxing. When your organization configures a nonempty `permissions` object or sets `sandbox.enabled` to `true`, VS Code now requires the [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses) in Agent Host for full chat sessions, to be able to enforce these policies.

Opening an existing, unarchived **Local** chat automatically moves it to **Copilot**, preserving the transcript and unsent draft, including attachments. Nothing is sent automatically. The new chat uses its normal model and permission defaults under current organization policy.

VS Code archives the original chat only after the new chat opens successfully. If you switch away while the move is in progress, the original stays unchanged and the unopened destination is removed.

While these policies apply, Claude, Codex, and terminal chat are unavailable. Editor inline chat remains available for limited read and edit tasks. An empty `permissions` object or legacy policy alone does not trigger this migration. Administrators can [temporarily opt out of automatic migration](#temporarily-keep-the-local-harness).

### Temporarily keep the Local harness

Administrators who need more time to transition to Copilot Agent Host can set `vscode.temporaryDefaultToLocalHarness` to `true` in their [unified managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started):

```json
{
    "vscode": {
        "temporaryDefaultToLocalHarness": true
    }
}
```

This keeps the **Local** harness available and stops automatic switching to **Copilot**, while preserving explicit, remembered, and current harness choices. Set the managed value to `false` or remove it to restore normal routing.

> **Note:** This temporary opt-out also overrides routing required by managed sandbox and permission settings. Local does not enforce those runtime-only rules. Enforcement in Copilot Agent Host sessions is unchanged.

### Manage Copilot permission modes independently

Administrators can permit **Assisted** while blocking **Allow All**, giving developers assisted approvals without bypassing permission checks. The Copilot permission picker reflects the modes permitted by your organization's managed settings.

For example, merge this configuration into your [unified managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started):

```json
{
    "permissions": {
        "disableBypassPermissionsMode": "disable",
        "disableAssistedPermissionsMode": false
    }
}
```

![Screenshot showing the Copilot permission picker with Manual and Assisted permissions available and Allow All absent.](images/1_142/managed-permission-modes.webp)

Use `permissions.disableAssistedPermissionsMode` to restrict **Assisted** independently. `permissions.defaultMode` supplies a starting default, not a restriction on the modes users can select.

The legacy `ChatToolsAutoApprove: false` policy still blocks both **Allow All** and **Assisted** unless you configure explicit managed mode restrictions. Setting only `permissions.defaultMode` does not replace that legacy restriction.

> **Note:** Assisted Permissions is not currently compatible with `permissions.{allow,ask,deny}`.
> If you are using any of `permissions.allow`, `permissions.ask`, `permissions.deny`, please set `"disableAssistedPermissionsMode": true`.
> In the next release, both will be supported alongside one another.

### Windows numeric policies support DWORD values

On Windows, policies that accept numeric values support DWORDs and QWORDs.

## Contributions to extensions

### GitHub Pull Requests

There has been more progress on the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension, which enables you to work on, create, and manage pull requests and issues. New features include:

* Stacked pull request support is enabled by default.

    ![Screenshot showing a stacked pull request.](images/1_142/pull-request-stack.webp)

* Conflict-free, locally checked-out pull requests can be updated.

Review the [changelog for the 0.170.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01700) release of the extension to learn about everything in the release.

## Deprecated features and settings

### New deprecations in this release

* [Windows sandboxing for Local harness is no longer supported](#windows-sandboxing-for-local-harness-is-no-longer-supported)

## Thank you

Contributions to `vscode`:

* [@bluerose73 (Shengjie Ma)](https://github.com/bluerose73): Copilot NES: add ExP toggle to omit max_tokens [PR #340327](https://github.com/microsoft/vscode/pull/340327)
* [@codelovingcat (Ürem Sancaktutan)](https://github.com/codelovingcat): Fix/issue 337524 multidiff order [PR #337565](https://github.com/microsoft/vscode/pull/337565)
* [@denizguney (Deniz Güney Yıldırım)](https://github.com/denizguney): Fix duration calculation for agent stop command [PR #338278](https://github.com/microsoft/vscode/pull/338278)
* [@na2co3-ftw (na2co3)](https://github.com/na2co3-ftw): Modern UI: Prevent vertical scrolling when dragging connected tabs (revised) [PR #338180](https://github.com/microsoft/vscode/pull/338180)
* [@rksharma-owg (RKS)](https://github.com/rksharma-owg): Preserve newer debugger stop details during continued cleanup [PR #339530](https://github.com/microsoft/vscode/pull/339530)
* [@sgent-epic](https://github.com/sgent-epic): agentHost: preserve BYOK state through tool continuations [PR #331749](https://github.com/microsoft/vscode/pull/331749)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * fix: memory leak in document paste edits [PR #338233](https://github.com/microsoft/vscode/pull/338233)
  * fix: memory leak in native context menu dismissal [PR #338214](https://github.com/microsoft/vscode/pull/338214)
  * fix: memory leak in output channel disposal listeners [PR #338240](https://github.com/microsoft/vscode/pull/338240)
  * fix: memory leak in debug adapter descriptor factory [PR #334103](https://github.com/microsoft/vscode/pull/334103)
  * fix: release terminal command history when clearing the normal buffer [PR #326931](https://github.com/microsoft/vscode/pull/326931)
  * perf: reduce number of strings by 1200 [PR #327689](https://github.com/microsoft/vscode/pull/327689)
  * fix: memory leak in MainThreadDebugService [PR #334102](https://github.com/microsoft/vscode/pull/334102)
  * fix: memory leak in extHostTimeline [PR #334098](https://github.com/microsoft/vscode/pull/334098)
  * fix: memory leak in debug visualization registrations [PR #340046](https://github.com/microsoft/vscode/pull/340046)
  * fix: memory leak in hidden status bar command arguments [PR #338238](https://github.com/microsoft/vscode/pull/338238)
  * fix: memory leak in extension host language model providers [PR #340579](https://github.com/microsoft/vscode/pull/340579)
  * fix: memory leak in terminal disposal subscriptions [PR #340037](https://github.com/microsoft/vscode/pull/340037)
* [@Tabisharaza (TABISH AYUB RAZA)](https://github.com/Tabisharaza): mcp: read migrated local servers from workspace configuration [PR #340034](https://github.com/microsoft/vscode/pull/340034)
* [@tuanvtdeptre199](https://github.com/tuanvtdeptre199): Disable Step Out action when the active thread has only one stack frame [PR #336125](https://github.com/microsoft/vscode/pull/336125)
* [@tyrielv (Tyrie Vella)](https://github.com/tyrielv): Avoid unnecessary --numstat diff for incoming changes decorations [PR #339008](https://github.com/microsoft/vscode/pull/339008)
* [@yuezhang030](https://github.com/yuezhang030): Update VSC model F prompt [PR #340187](https://github.com/microsoft/vscode/pull/340187)

Contributions to `vscode-pull-request-github`:

* [@L4XB (Lukas )](https://github.com/L4XB): Don't open two browser tabs when clicking the pull request number [PR #8962](https://github.com/microsoft/vscode-pull-request-github/pull/8962)
* [@strawberry-little-bear](https://github.com/strawberry-little-bear): Fix malformed issue links in overview HTML [PR #9025](https://github.com/microsoft/vscode-pull-request-github/pull/9025)
* [@vsharha (Viktor Sharha)](https://github.com/vsharha): Fix mergeability polling in pull request overview [PR #8954](https://github.com/microsoft/vscode-pull-request-github/pull/8954)

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

> If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_143.md
- **CANONICAL_URL**: https://code.visualstudio.com/release-notes/v1_143
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_143.md
- **SHA256_FINGERPRINT**: `009f4acdd647fbd8c0d114aea3c6c82309696c660f1ad0add8943b854a1d8eea`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.857819+00:00
---

**MetaDescription**: Learn what is new in Visual Studio Code Insiders, including the latest features and improvements.

# Visual Studio Code 1.143

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode.ig)

---

_Last updated: October 19, 2026_

Welcome to the 1.143  release of Visual Studio Code.

Happy Coding!

---

## October 19, 2026

* Add experimental support for administrator-configured authentication headers when exporting Copilot Agent Host OpenTelemetry data to Microsoft Entra ID-protected endpoints. _[#304505: GitHub Copilot Entra Id auth header support for Open Telemetry ingestion](https://github.com/microsoft/vscode/issues/304505)_

* Increase the editor's diagnostic highlight limit to 5,000 per file and show a language status warning when diagnostics or highlights are limited. _[#200206: Only 500 diagnostics are underlined, but there's no indication about the limit](https://github.com/microsoft/vscode/issues/200206)_

## October 18, 2026

* Manage sandbox certificate trust with **Sandbox: Manage Trusted CA**, including optional CA installation, rotation, and trust removal. _[#341946: Agent Host: provide optional sandbox trusted CA setup and management](https://github.com/microsoft/vscode/issues/341946)_

* View live output from detached background shells in Agent Host Copilot chats after the response completes. _[#341645: Show live output for detached background shells in Agent Host chats](https://github.com/microsoft/vscode/issues/341645)_

* Add support for `/fork <title>` and `/fork prompt <prompt>` to name forks or start them with a prompt and attachments in Agent Host chats. _[#341229: Support `/fork <title>` and `/fork prompt <prompt>` in Agent Host chats](https://github.com/microsoft/vscode/issues/341229)_

## October 16, 2026

* In the experimental Markdown editor, Git commit links with `?path=...` repository hints show commit subjects and change counts and open in multi-diff. _[#342125: Open path-hinted Git commit links in multi-diff with rich metadata](https://github.com/microsoft/vscode/issues/342125)_

* After sending a message, choose **Copy Link** from an Agent Host chat editor tab's context menu to revisit the session or peer chat. _[#342121: Add Copy Link for Agent Host chat editor tabs](https://github.com/microsoft/vscode/issues/342121)_

* Open supported links directly from Quick Open. _[#342051: Support opening links directly from Quick Open (Ctrl+P)](https://github.com/microsoft/vscode/issues/342051)_

* Add a **Stop Shell** action for attached background shells in Agent Host chats without stopping the session. _[#324824: Provide way to stop running command in agent host copilot](https://github.com/microsoft/vscode/issues/324824)_

## October 15, 2026

* Add GPT-Live support with your OpenAI API key in experimental Voice Mode (``agents.voice.enabled`` and ``agents.voice.useBYOKVoiceModel``), where client BYOK is allowed. _[#338708: Support OpenAI GPT-Live BYOK in Voice Mode](https://github.com/microsoft/vscode/issues/338708)_

* Add support for deleting multiple local history entries together and comparing two selected revisions in the Timeline view. _[#145202: Timeline: support multi select commands](https://github.com/microsoft/vscode/issues/145202)_

* Add a **Canvas** submenu to **New Chat** for initialized Copilot sessions with ``chat.canvases.enabled`` enabled. _[#341660: Canvases: open registered canvases from the Editor Window New Chat menu](https://github.com/microsoft/vscode/issues/341660)_

## October 14, 2026

* In portable mode, CLI state and cache files are stored under the portable data directory instead of the user's home directory. _[#184646: .vscode\\cli\\ ignores portable mode](https://github.com/microsoft/vscode/issues/184646)_

## October 13, 2026

* Add a **Stop Shell** action for detached background shells in Agent Host chats. _[#341329: Offer Stop for detached background shells in Agent Host chats](https://github.com/microsoft/vscode/issues/341329)_

* Workspace-root `.mcp.json` files support `${VAR}` and `${VAR:-default}` environment variable expansion for MCP server configuration values. _[#340348: Support Env Var expansion in VS Code mcp.json](https://github.com/microsoft/vscode/issues/340348)_

## October 12, 2026

* Extensions can contribute Explorer title actions through `view/title` by using `view == workbench.explorer.fileView`. _[#108271: Add an explorer/title menu contribution point](https://github.com/microsoft/vscode/issues/108271)_

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: web::github_changelog_copilot_rss
- **CANONICAL_URL**: https://github.blog/changelog/label/copilot/feed/
- **RAW_SOURCE_URL**: https://github.blog/changelog/label/copilot/feed/
- **SHA256_FINGERPRINT**: `fbfc1e9842c7fa75972040ff02bde01c46bcfca0f55ec688bcce6c9e719db075`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:35.801198+00:00
---

# GitHub Copilot Official Changelog Feed

## Copilot model policy API for enterprise, orgs, and teams
- **Date**: Mon, 19 Oct 2026 21:32:18 +0000
- **URL**: https://github.blog/changelog/2026-10-19-copilot-model-policy-api-for-enterprise-orgs-and-teams

You can now use the REST API to retrieve and update Copilot model policies for enterprises, enterprise teams, agent apps, and organizations. What’s new GET and PATCH endpoints are now...
The post Copilot model policy API for enterprise, orgs, and teams appeared first on The GitHub Blog .

## GitHub Copilot models deprecated on October 19, 2026
- **Date**: Mon, 19 Oct 2026 21:27:10 +0000
- **URL**: https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026

As of today, October 19, 2026, we have deprecated the following models across most GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions). These...
The post GitHub Copilot models deprecated on October 19, 2026 appeared first on The GitHub Blog .

## Multi-repository support and other improvements for GitHub in Slack and Teams
- **Date**: Fri, 16 Oct 2026 02:16:35 +0000
- **URL**: https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates

@GitHub in Slack and Teams now supports working across multiple repositories in a single conversation. Whether you’re creating issues, opening pull requests, or investigating bugs, you can work across repositories...
The post Multi-repository support and other improvements for GitHub in Slack and Teams appeared first on The GitHub Blog .

## Upcoming deprecation of selected GitHub Copilot models in mid-November
- **Date**: Thu, 15 Oct 2026 19:35:13 +0000
- **URL**: https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november

We will deprecate the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on November 16th, 2026: Model Deprecation date...
The post Upcoming deprecation of selected GitHub Copilot models in mid-November appeared first on The GitHub Blog .

## Agentic autofix for code scanning alerts general availability
- **Date**: Thu, 15 Oct 2026 13:49:20 +0000
- **URL**: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability

Agentic autofix for code scanning alerts is now generally available. It remediates alerts by working across your codebase the way a developer would: it explores relevant files, proposes a fix,...
The post Agentic autofix for code scanning alerts general availability appeared first on The GitHub Blog .

## HydraFusion updates and new Max option
- **Date**: Wed, 14 Oct 2026 20:01:35 +0000
- **URL**: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option

HydraFusion has an updated model pool, improved orchestration workflows, and introduces HydraFusion Max. Both HydraFusion and HydraFusion Max are available across VS Code, the GitHub Copilot app, and GitHub Copilot...
The post HydraFusion updates and new Max option appeared first on The GitHub Blog .

## Gemini 4 Argon in GitHub Copilot
- **Date**: Tue, 13 Oct 2026 18:39:56 +0000
- **URL**: https://github.blog/changelog/2026-10-13-gemini-4-argon-in-github-copilot

Gemini 4 Argon, Google’s newest frontier model, is now generally available in GitHub Copilot. It is designed for complex coding, agentic, and reasoning tasks. In early testing, Gemini 4 Argon...
The post Gemini 4 Argon in GitHub Copilot appeared first on The GitHub Blog .

## Enterprise managed settings enforcement updates
- **Date**: Tue, 13 Oct 2026 15:20:10 +0000
- **URL**: https://github.blog/changelog/2026-10-13-enterprise-managed-settings-enforcement-updates

Enterprise administrators can now require supported GitHub Copilot clients to retrieve current server-managed settings at startup instead of relying on a cached policy. We are also adding minimum client version...
The post Enterprise managed settings enforcement updates appeared first on The GitHub Blog .

## Client telemetry user attribution and configurable capture
- **Date**: Mon, 12 Oct 2026 22:38:00 +0000
- **URL**: https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture

Enterprise administrators can now use telemetry in managed settings to attribute GitHub Copilot activity to a user without collecting their prompts, responses, or tool content. The telemetry.capture.identity setting adds three...
The post Client telemetry user attribution and configurable capture appeared first on The GitHub Blog .

## New controls and chat improvements in Copilot for JetBrains
- **Date**: Sat, 10 Oct 2026 18:53:39 +0000
- **URL**: https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains

This update brings more control over default models and MCP server in GitHub Copilot for JetBrains. It also makes diagnostics easier to address, improves chat navigation and account controls, and...
The post New controls and chat improvements in Copilot for JetBrains appeared first on The GitHub Blog .
