# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-10-29T05:00:59.699127+00:00
- **Total Palabras**: 19,424 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_143.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_143
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_143.md
- **SHA256_FINGERPRINT**: `5fde412cfe9148bf34b8f8ca45496feabf91b8990906f1295b841bcc73454408`
- **LAST_VERIFIED_UTC**: 2026-10-26T18:29:23.900825+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.143

# Visual Studio Code 1.143

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

Welcome to the 1.143  release of Visual Studio Code.

**Update 1.143.1**: The update addresses these [issues](https://github.com/microsoft/vscode/pulls?q=is%3Apr+milestone%3A1.143.1+is%3Aclosed+label%3Acandidate).

## Release highlights

This release makes the Copilot harness the default for new sessions and adds tools to compare models, reclaim storage, run models locally, and navigate file changes.

* [Copilot harness by default](#copilot-harness-as-the-default): The default for new sessions, built on the Copilot SDK, lets you switch between editor and Agents window.

* [Compare models (Preview)](#compare-model-results-preview): Run the same task with multiple models in the Agents window, then compare and combine their solutions.

* [Reclaim worktree storage (Experimental)](#reclaim-storage-from-inactive-worktrees-experimental): Free disk space by reviewing and removing inactive agent session worktrees.

* [On-device models (Experimental)](#run-copilot-models-on-your-device-experimental): Run MAI Code 1.1 Flash locally on your device for your agent tasks.

* [Multi-diff file list (Experimental)](#multi-file-diff-editor-file-list-experimental): Keep an overview of and jump between changed files in the multi-file diff editor.

## Agents

### Copilot harness as the default

**The Copilot harness is now the default for new sessions in VS Code.** It's our latest harness, built on the Copilot SDK, a shared foundation that helps align behavior, capabilities, and improvements across Copilot products.

When you start a new session, **Copilot** in the harness picker indicates that the session uses the Copilot harness:

![Screenshot showing Copilot selected in the harness picker with a hover description of its Copilot SDK and Agent Host integration.](images/1_143/harness-copilot-description.webp)

In VS Code, you can keep Copilot harness sessions running in the background and access them from both the VS Code editor window and the Agents window. These sessions run through the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host).

Thank you so much to everyone who has shared valuable feedback. This release includes more improvements shaped directly by your feedback.

We're continuing to improve performance and reduce latency based on the scenarios and setups you share. For example, [reports of long waits before chat responses](https://github.com/microsoft/vscode/issues/341543#issuecomment-6202370962) helped us reduce delays caused by MCP servers that don't finish loading their tools.

We're also continuing to make our documentation clearer based on the feedback and questions you've shared. Learn how to [work with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses), or explore the architecture and workflows in the [agent host blog post](https://code.visualstudio.com/blogs/2026/08/26/agent-host-architecture).

Please continue [filing issues](https://github.com/microsoft/vscode/issues) to let us know how the Copilot harness is working for you. Your feedback is a huge help and directly shapes the harness experience.

#### Initial file-level working set support (Experimental)

**Setting:** ``chat.editor.workingSet.enabled``

You gave us feedback that when using the Copilot harness, approving or rejecting agent edits in the editor was challenging. As of this release, we are introducing _initial_ file-level working set support to help you manage and review changes more effectively.

Copilot harness sessions in the editor window now support file-level **Keep** in the experimental working set above the chat input. Enable ``chat.editor.workingSet.enabled`` to try it.

Select **Keep** on a file, or in the heading for all files, to mark changes as reviewed and remove them from the working set. The edits stay on disk, and files return if the agent changes them again.

<video src="images/1_143/file-level-keep.mp4" title="Video showing file-level and bulk Keep actions in the working set above the chat input." autoplay loop controls muted></video>

**What's next:** We plan to add file-level **Undo** to the working set and bring **Keep** and **Undo** back into the editor for individual changes. These are planned for later releases, landing in [Insiders](https://code.visualstudio.com/insiders/) first, then Stable.

### Discard changes from more changesets in the Agents window

The **Changes** view in the Agents window lets you see all the modifications made by the agent. Until now, discarding pending changes was only available in the **Uncommitted Changes** changeset.

![Screenshot showing the Discard Changes option in the Uncommitted Changes changeset.](images/1_143/discard-branch-changes.webp)

In this release, the **Branch Changes**, **Session Changes**, and **Last Turn Changes** changesets also offer the possibility to discard changes. Select **Discard Changes** on a file in the **Changes** view or in the multi-file diff editor. What VS Code discards depends on the changeset:

* **Branch Changes**: restores the file to its version where the branch diverged from its base branch, and deletes files that the branch added.
* **Session Changes**: reverts the session's edits to the file and keeps changes made outside the session, such as your own edits.
* **Last Turn Changes**: reverts only the latest turn's edits to the file and keeps all other changes to it.

### Compare model results (Preview)

**Setting**: ``sessions.chat.compareAgents.enabled`` (Agents window only)

Compare how different models and harnesses approach the same coding task. Run attempts in parallel, review their results, and combine ideas into one solution.

<video src="images/1_143/bake-off.mp4" title="Video showing the Agent bake off model comparison workflow." autoplay loop controls muted></video>

To get started, enable ``sessions.chat.compareAgents.enabled`` in the Agents window, then select **Compare Models** in the model picker.

* **Choose the approaches to compare:** Select two or more models to attempt your task independently. You can mix Copilot, Claude, and Codex harnesses and configure different reasoning levels.

    ![Screenshot showing four models with different reasoning levels selected for an Agent bake off.](images/1_143/bake-off-picker.webp)

* **Run the attempts:** Enter one prompt and start all selected attempts together.

    ![Screenshot showing a prompt ready to run with four Agent bake off attempts.](images/1_143/bake-off-multiple-attempts.webp)

* **Follow progress side by side:** Each attempt runs in its own session, so you can compare its approach and open the worktree or changes at any time.

    ![Screenshot showing four Agent bake off attempts running side by side in a grid.](images/1_143/bake-off-grid.webp)

* **Evaluate and combine the results:** Optionally select a Judge model to evaluate the attempts and recommend a solution. Its scorecard shows time and token usage, with expandable rationale, validation evidence, and links to each attempt. You can then select **Synthesize** to build on the recommended attempt with ideas from the others. Synthesis starts only when you request it.

    ![Screenshot showing Agent bake off results with the recommended attempt, scorecard, and Synthesize action.](images/1_143/bake-off-results.webp)

### Tab shortcuts in an empty side pane

When you closed every tab in the [Agents window](https://code.visualstudio.com/docs/agents/run/agents-window) side pane, the editor area was left blank, and you had to find the **Add Tab (+)** menu to get back to your session's changes or files.

The empty editor area now lists the tabs you can add, such as **Changes**, **Files**, **Browser**, and **Search**, each with its icon and keyboard shortcut. Select an entry to open that tab. If you have a canvas extension installed, a **Canvas** entry lists the available canvases. When you switch to a session whose editor area is empty, VS Code shows this list instead of reopening the **Changes** and **Files** tabs automatically.

<video src="images/1_143/empty-editor-add-tab.mp4" title="Video showing the list of tabs to add in an empty side pane editor in the Agents window." autoplay loop controls muted></video>

### Session Activity Bar (Experimental)

**Sessions**: ``sessions.showSessionActivityBar``, ``sessions.sessionActivityBar.showLayoutActions``

The Session Activity Bar brings a session's **Changes**, **Files**, **Browser**, and available canvases next to the side pane, keeping these editors and artifacts visually connected to where they open. You can still open session artifacts from the pills at the top of the session.

The Session Activity Bar is a slim vertical strip of icons at the right edge of the active chat. Select an icon to open that tab in the side pane. If the side pane is closed, it opens with that tab active. If the tab is already open, VS Code focuses it instead of opening a second copy. If you have a canvas extension installed, a **Canvas** entry opens a submenu of the available canvases.

<video src="images/1_143/session-activity-bar.mp4" title="Video showing the Session Activity Bar opening the Changes, Files, and Browser tabs beside the active chat in the Agents window." autoplay loop controls muted></video>

You can drag the Session Activity Bar up or down by its grip to move it out of your way, and double-click the grip to reset its position. When you split the chat area, only the focused group shows the Activity Bar.

To keep session-related layout actions together, right-click the Activity Bar and select **Show Layout Actions**. This moves the **Toggle Side Panel** and **Toggle Panel** actions from the title bar into the Activity Bar.

The Session Activity Bar is off by default in Stable. Select **View** > **Appearance** > **Session Activity Bar** to turn it on. To hide it again, right-click the Activity Bar and select **Hide Session Activity Bar**.

You can also configure these options with ``sessions.showSessionActivityBar`` and ``sessions.sessionActivityBar.showLayoutActions``. If you previously set `sessions.showSessionToolbar`, VS Code carries your value over to ``sessions.showSessionActivityBar``.

### Find and create files from the empty Files tab (Experimental)

**Setting**: ``sessions.experimental.emptyFileEditorActions``

In the Agents window, the **Files** tab was blank when no file was open, so you had to switch to the Files view to find or create a file in your session's folder.

When you enable ``sessions.experimental.emptyFileEditorActions``, the empty **Files** tab shows a search box and a **New File** action. The search works like [Quick Open](https://code.visualstudio.com/docs/editing/getting-started/tips-and-tricks#_quick-open) (``Shortcut: workbench.action.quickOpen``), with the same ranking, highlights, and file icons, and it only finds files in the folders of the current session. Select a result to open it in the editor, or select **New File** to create a file in the session's folder. When you close the file, the search box returns.

<video src="images/1_143/empty-files-tab-search.mp4" title="Video showing a file search and the New File action in the empty Files tab of the Agents window." autoplay loop controls muted></video>

### Improved performance when opening large chats

Opening a long [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host) chat in the Agents window used to freeze the window for up to half a minute while the chat's history was restored. In this release, history is restored in small slices instead of one long blocking task, so the window stays responsive. Opening, switching back to, and reloading large chats is significantly faster.

| Scenario | Chat | Time to open: 1.142 → 1.143 | Window unresponsive: 1.142 → 1.143 |
|---|---|---|---|
| Cold open | Chat A (~1,150 requests, ~530 MB history) | 35.6 s → 9.0 s | 28.3 s → 0.6 s |
| Cold open | Chat B (~1,450 requests, ~200 MB history) | 20.3 s → 3.0 s | 20.3 s → 0.4 s |
| Re-open | Chat A | 26.7 s → 0.6 s | 26.8 s → 0.3 s |
| Re-open | Chat B | 16.4 s → 0.4 s | 16.4 s → 0.2 s |
| Reload window | Chat A | 26.7 s → 2.9 s | 25.3 s → 0.9 s |
| Reload window | Chat B | 22.3 s → 2.2 s | 20.8 s → 0.4 s |

_Median of three runs on macOS, with real chats from day-to-day development. "Cold open" means opening a chat for the first time after the window starts. "Re-open" means switching to another chat and back. "Window unresponsive" is the longest time the window could not respond to input during the open._

### Reclaim storage from inactive worktrees (Experimental)

**Setting**: ``chat.agentSessions.sessionStorageCleanupSuggestion.enabled`` (Agents window only)

Worktrees are very useful for letting agents work on multiple features simultaneously without interfering with each other's changes. Over time, inactive worktrees can accumulate and consume significant disk space.

Run **Chat: Open Worktree Cleanup** from the Command Palette to see how much disk space inactive agent session worktrees use and remove the ones you no longer need. Filter sessions by how long they have been inactive, review each worktree's size, and select the worktrees to clean up.

Cleaning up marks the selected sessions as done and deletes their worktrees. You can restore a session later to recreate its worktree. Active, running, needs-input, and pinned sessions are protected from cleanup.

The cleanup editor lets you configure automatic cleanup for sessions with merged pull requests and control whether VS Code suggests cleanup when session storage grows large.

![Screenshot showing the worktree cleanup editor with cleanup settings and inactive session worktrees.](images/1_143/worktree-cleanup-editor.webp)

When ``chat.agentSessions.sessionStorageCleanupSuggestion.enabled`` is enabled, the Agents window notifies you when inactive worktrees accumulate or they use enough disk space to make cleanup worthwhile.

![Screenshot showing a worktree cleanup suggestion in the Agents window.](images/1_141/worktree-cleanup.webp)

## Models

### Run Copilot models on your device (Experimental)

Laptops such as the new [Surface Laptop Ultra](https://www.microsoft.com/en-us/surface/devices/surface-laptop-ultra), powered by NVIDIA RTX Spark with up to 128 GB of unified memory, have enough GPU memory to run a capable coding model locally. On-device models let you use that hardware with Copilot: download MAI Code 1.1 Flash from the new **On This Device** tab in the model picker and chat with it in Copilot harness sessions, with model processing on your device.

VS Code downloads and manages the model for you. Responses that run on your device are labeled **On-device** and don't use AI credits. To let Auto route suitable requests to the on-device model with cloud fallback, turn on **Use in Auto** on the model's details page.

<video src="images/1_143/on-device-models.mp4" title="Video showing MAI Code 1.1 Flash downloaded from the On This Device tab in the model picker, loaded, and answering a chat prompt on the device." autoplay loop controls muted></video>

To get started:

* Install a [llama.cpp build](https://github.com/ggml-org/llama.cpp/releases) that supports the model
* Set ``chat.copilot.localModel.llamaServerPath`` to its `llama-server` executable
* Enable ``chat.copilot.localModel.enabled``

On-device models require GitHub sign-in and an NVIDIA GPU with 96 GB or more of GPU memory.

Learn more about [on-device models](https://code.visualstudio.com/docs/agent-customization/language-models#_use-on-device-models-experimental).

### Bring your own OpenAI model to Voice Mode (Preview)

**Settings**: ``agents.voice.enabled``, ``agents.voice.useBYOKVoiceModel``

Use your own OpenAI API key and live model for voice-driven coding conversations instead of the hosted Voice Mode backend. Add your OpenAI key in the Language Models editor, enable ``agents.voice.enabled``, and set ``agents.voice.useBYOKVoiceModel`` to a live model ID, like `gpt-live-1` that your key can access.

## Sandboxing

### Manage sandbox certificate trust

Sandbox certificate trust management is available for agent hosts running Windows or macOS.

The sandbox credential proxy lets tools authenticate to approved services without exposing real authentication tokens to sandboxed processes. It gives tools placeholder credentials, then substitutes the real credentials when forwarding requests to approved destinations. For HTTPS requests, this requires the proxy to present its own TLS certificates, which the tools must trust.

Copilot supplies a certificate bundle for tools that support it. Some tools instead rely on the operating system's certificate trust store and can encounter certificate errors when the proxy's certificate authority (CA) isn't trusted. Installing the CA improves compatibility with these tools. **Domain filtering alone does not require CA installation:** the built-in local proxy can check destinations and tunnel HTTPS traffic without decrypting it.

VS Code shows a dismissible **Sandbox trusted CA is not installed** notice with an **Install** option when trust is missing and installation is supported. Installation adds the locally generated CA's public certificate to the Windows machine-wide trust store or the macOS user's login Keychain and can require operating system authorization.

<video src="images/1_143/sandbox-ca-install.mp4" title="Video showing installation of the sandbox trusted certificate authority in VS Code." autoplay loop controls muted></video>

You can also run **Sandbox: Manage Trusted CA** from the Command Palette to install, rotate, or remove trust for the last-focused chat's agent host, whether local or remote. Each operation asks for confirmation and identifies the target host. **Remove** removes operating system trust but keeps the stored certificate and private key. Running tools might need to restart after a certificate change.

Installation is optional. Missing trust doesn't block chat startup or sending messages, and opening a chat never changes certificate trust.

For more details, see [Trust the sandbox CA certificate on Windows and macOS](https://code.visualstudio.com/docs/agents/run/agent-sandboxing#_trust-the-sandbox-ca-certificate-on-windows-and-macos).

### Change session sandboxing when policy permits

If your organization's managed policy permits sandbox bypass, you can turn [sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) off for an individual Copilot harness session without changing your global settings. Use the **Sandboxing for terminal** toggle in the session permissions menu in either the editor or the Agents window. Administrators can continue to require sandboxing by disallowing bypass, which keeps the toggle on and locked.

Changes remain subject to approval by the agent runtime. If a change is rejected, VS Code shows an error and restores the last applied sandbox state. The collapsed permissions control and the reopened menu reflect that state.

## Chat

### Open canvases from the chat menu (Preview)

**Setting**: ``chat.canvases.enabled``

VS Code 1.142 introduced canvases (Preview), which are shared, interactive surfaces for collaborating with agents.

In this release, you can now open available canvases from **New Chat (+)** > **Canvas** in the editor window, without asking Copilot to open them.

![Screenshot showing the Canvas submenu in the editor window's New Chat menu, listing Cache Stats, Chess, Diagram Explorer, and Token Pac-Man.](images/1_143/editor-canvas-menu.webp)

When canvas support is enabled and you have canvas extensions installed, the submenu appears _after your first message_ in a Copilot harness session. You can also open canvases from the `+` menu in the Agents window.

Learn about [installing, creating, and using canvases with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses#_use-canvases-with-the-copilot-harness).

### See output from detached background shells

In [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses) sessions, the agent can start commands that need to continue running after it responds in a detached background shell. A dev server or a file watcher are common examples of such commands.

Previously, you couldn't view the output of detached background shells, for example to check whether a dev server started successfully. Detached shells now stream their output like attached shells. Select the **Background Shells** pill, and then select a detached shell to watch its output as the command runs. The shell's terminal output in the chat response also keeps updating after the agent finishes its response. When the command exits, the shell leaves the list, and the chat response keeps the command's output and exit status.

![Screenshot showing a detached background shell's output streaming in its details, next to the Background Shells list where the shell is marked Detached.](images/1_143/background-shell-detached.webp)

You can now also stop detached shells, which was previously [only available for attached shells](https://code.visualstudio.com/updates/v1_142#_stop-background-shells). When you no longer need a dev server or watcher, select **Stop Shell** in the shell's details.

## Editor Experience

### Diagnostic highlight limits

To improve diagnostic visibility in files with many reported problems, the editor highlight limit has increased from 500 to 5,000 diagnostics per file.

A warning in the editor's language status indicator indicates when diagnostics or their highlights are limited for performance reasons:

* **Diagnostic source limit:** Each extension diagnostic collection can provide up to 1,000 diagnostics per file. If a collection exceeds this limit, the warning indicates that some diagnostics are not shown.

* **Editor highlight limit:** The editor highlights up to 5,000 diagnostics per file across all sources. If this limit is exceeded, the warning indicates that only 5,000 diagnostics are highlighted.

If both limits are reached, the warning reports both conditions. Hover over the language status indicator in the Status Bar to view the details.

![Screenshot showing the language status bar diagnostic highlights addition](images/1_143/diagnostic-highlights.webp)

## Source Control

### Multi-file diff editor file list (Experimental)

**Setting**: ``multiDiffEditor.experimental.fileList``

Navigate changes from commits, stashes, and agent sessions with a file list beside the multi-file diff view. Enable ``multiDiffEditor.experimental.fileList`` to try it.

Each file in the list has a status letter: A (added), M (modified), D (deleted), or R (renamed). As you scroll, the list highlights the file you're viewing. Select a file in the list to jump to its diff. Open **Files View & Position** in the editor toolbar's **More Actions** (**...**) menu to choose **View as List** or **View as Tree**, and to place the files **On the Left** or **On the Right** of the diffs.

![Screenshot showing the multi-file diff editor file list with status letters for each changed file.](images/1_143/multi-file-diff-editor-file-list.webp)

## Enterprise

### Dynamic headers for managed OpenTelemetry

Administrators can generate and refresh HTTP headers for OpenTelemetry (OTel) exports with the new `telemetry.headersProvider` managed setting. For example, use a helper to supply short-lived authentication tokens for your collector, without asking developers to update headers manually or opt in through personal OTel settings.

This setting applies **only to Copilot Agent Host sessions**. Configure it in [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started), not user settings:

```json
{
    "telemetry": {
        "enabled": true,
        "endpoint": "https://<collector-host>:4318",
        "protocol": "http",
        "headersProvider": {
            "path": "<absolute-path-to-header-helper>",
            "args": [],
            "refreshIntervalMs": 5000
        }
    }
}
```

The helper writes a JSON object of header names and string values to standard output.

See [Configure dynamic headers](https://code.visualstudio.com/docs/agents/guides/monitoring-agents#_configure-dynamic-headers) for helper requirements and further details.

### Managed model defaults

New Copilot harness chats use your organization's managed defaults, even when you configure ``chat.defaultModel`` to another preference. The model picker and setting now explain which defaults apply. You can still change models and supported options per chat.

![Screenshot showing the model picker identifying the organization default and explaining that you can choose another model for the chat.](images/1_143/managed-model-default-picker.webp)

For example, the following configuration defaults new chats to Auto with the Intelligence tier in [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started):

```json
{
    "model": "auto",
    "autoTier": "intelligence"
}
```

### Why Local is disabled

When enterprise policy requires the [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses), the Local harness now stays visible but is disabled in the harness picker, with a [**Learn why**](https://aka.ms/vscode-copilot-harness-policy) link explaining the restriction.

![Screenshot showing Local disabled by policy in the harness picker, with a Learn why link explaining that the organization requires Copilot.](images/1_143/local-harness-disabled-by-policy.webp)

Copilot is required to enforce nonempty managed `permissions.deny` rules or `sandbox.enabled: true`, unless the temporary override below applies. Other `permissions.*` settings and an empty deny list do not trigger this requirement.

Administrators can prohibit Local with these enterprise-managed settings, not user settings:

```json
{
    "vscode": {
        "temporaryAllowLocalHarness": false,
        "temporaryDefaultToLocalHarness": false
    }
}
```

| Setting | Description |
| --- | --- |
| `vscode.temporaryAllowLocalHarness` | `false` prohibits Local, Claude, and Codex harnesses, overriding the temporary default below. `true` does not override other policies. |
| `vscode.temporaryDefaultToLocalHarness` | `true` keeps Local available and suppresses automatic Copilot routing, including deny-list and sandbox requirements. Explicit and remembered choices are preserved. |

When Copilot is required, opening unarchived Local chats moves them to Copilot. Editor inline chat and other Claude and Codex restrictions are unchanged.

> **Note**: These controls are temporary while Local is retired. Local cannot enforce runtime-only permission and sandbox controls. Do not enable the temporary Local override if you require those controls. If Copilot fails in your enterprise environment, [report an issue](https://github.com/microsoft/vscode/issues).

### Fewer interruptions while organization settings load

Copilot harness sessions and model changes now wait for slow organization settings to load, with progress and a retry option on failure. You can still select **Stop** while you're waiting. Organization restrictions apply before requests run.

### Fewer approval prompts for managed tools

[Assisted permissions](https://code.visualstudio.com/updates/v1_142#_manage-copilot-permission-modes-independently) no longer prompt again for eligible managed tool requests they approve. One-time limits, managed denials, and sandbox restrictions still apply.

### Managed plugins install automatically

Copilot harness sessions now install or update the [agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins) that your organization requires before using them.

For example, require a plugin in [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started):

```json
{
    "enabledPlugins": {
        "my-plugin@my-marketplace": true
    }
}
```

Plugins enabled by a trusted repository's settings, and plugins your organization assigns to your team, install in the background without blocking chat.

* Managed settings take precedence, followed by trusted repository settings and then your own choices.
* Team assignments apply only when no other choice exists.
* Automatically installed plugins are enabled only for the session and aren't added to your user settings.

### Claude and Codex sessions

When policy requires the Copilot harness, existing Claude and Codex sessions remain visible in the sessions list, so you still can continue them with the Copilot harness. Creating new Claude or Codex sessions remains disabled in this scenario.

## VS Code setup

### Install GitHub Copilot CLI with VS Code

We now make it easier for you to get started with the [GitHub Copilot CLI](https://github.com/features/copilot/cli) by letting you install it with the VS Code installer.

**Note:** Organizations can choose to disable this option via the [Managed AI Settings](https://code.visualstudio.com/docs/enterprise/manage-ai-settings#_enable-or-disable-the-copilot-command).

* Windows

    The VS Code installer on Windows now includes an option to install GitHub Copilot CLI. If you already have it installed, this option is not presented. Find more details in [Set up the copilot command on Windows](https://code.visualstudio.com/docs/setup/windows#_setup-the-copilot-command).

    ![install-copilot-in-windows-installer](images/1_143/windows-installer-copilot.webp)

* Linux

    The VS Code Linux installers add a `copilot` executable into the user path.

    If you run the `copilot` command in the terminal, it will either prompt you to install GitHub Copilot CLI if it's not installed, or run GitHub Copilot CLI if it is already installed.

* macOS

    On macOS, you are prompted to install GitHub Copilot CLI when you add VS Code to the `$PATH` environment variable via the Command Palette in VS Code.

    ![command-to-add-code-to-path](images/1_143/macos_install_copilot.webp)

## Deprecated features and settings

None

## Thank you

Contributions to `vscode`:

* [@bstee615 (Benjamin Steenhoek)](https://github.com/bstee615): nes: Add prompt template which enables only low/medium eagerness modes [PR #340404](https://github.com/microsoft/vscode/pull/340404)
* [@davidfowl (David Fowler)](https://github.com/davidfowl): Fix incomplete Mission Control sandbox session discovery [PR #341823](https://github.com/microsoft/vscode/pull/341823)
* [@denizguney (Deniz Güney Yıldırım)](https://github.com/denizguney): Add version validation check to getContextProviderAPI method [PR #339523](https://github.com/microsoft/vscode/pull/339523)
* [@KRRT7 (Kevin Turcios)](https://github.com/KRRT7): Skip serializing bulk edits when debug logging is off [PR #341765](https://github.com/microsoft/vscode/pull/341765)
* [@matt-sorenson (Matt Sorenson)](https://github.com/matt-sorenson): Mark variables in zsh integration functions as local [PR #290298](https://github.com/microsoft/vscode/pull/290298)
* [@mcumming (Michael Cummings (MSFT))](https://github.com/mcumming)
  * Private Marketplace extension blocking: add gallery and install enforcement [PR #333859](https://github.com/microsoft/vscode/pull/333859)
  * Reject non-manifest 200 responses as extension gallery service index [PR #331804](https://github.com/microsoft/vscode/pull/331804)
  * Fix lost race leaving a signed-out user on an Available marketplace [PR #331800](https://github.com/microsoft/vscode/pull/331800)
* [@na2co3-ftw (na2co3)](https://github.com/na2co3-ftw): Modern UI: fix frosted glass menu background corners [PR #339456](https://github.com/microsoft/vscode/pull/339456)
* [@pwang347 (Paul)](https://github.com/pwang347)
  * Allow retrying pending Copilot connectors [PR #341081](https://github.com/microsoft/vscode/pull/341081)
  * agentHost: enable SDK skill installation [PR #340762](https://github.com/microsoft/vscode/pull/340762)
  * Fix customization marketplace sign-in [PR #341648](https://github.com/microsoft/vscode/pull/341648)
* [@rahadbhuiya (Rahad)](https://github.com/rahadbhuiya): cli: respect VSCODE_PORTABLE and make Quality parsing case-insensitive [PR #341565](https://github.com/microsoft/vscode/pull/341565)
* [@rksharma-owg (RKS)](https://github.com/rksharma-owg): sessions: Stabilize approval row height during sticky scrolling [PR #338210](https://github.com/microsoft/vscode/pull/338210)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * fix: memory leak in timeline providers [PR #340881](https://github.com/microsoft/vscode/pull/340881)
  * fix: memory leak in chat debug providers [PR #340880](https://github.com/microsoft/vscode/pull/340880)
  * fix: memory leak in language model removal notifications [PR #340577](https://github.com/microsoft/vscode/pull/340577)
  * fix: memory leak in canceled tree drag transfers [PR #340845](https://github.com/microsoft/vscode/pull/340845)
  * fix: memory leak in pending quick pick items [PR #340846](https://github.com/microsoft/vscode/pull/340846)
  * fix: guard notebook diff input lifecycle [PR #339389](https://github.com/microsoft/vscode/pull/339389)
  * fix: memory leak in terminal process startup [PR #340582](https://github.com/microsoft/vscode/pull/340582)
  * fix: memory leak in suggest enabled input [PR #340913](https://github.com/microsoft/vscode/pull/340913)
* [@sw23 (Spencer Williams)](https://github.com/sw23): Scope content exclusion path rules to their repository [PR #339415](https://github.com/microsoft/vscode/pull/339415)
* [@VirajMishra1 (Viraj Mishra)](https://github.com/VirajMishra1): fix: path, URI, JSON edit utility bugs [PR #334259](https://github.com/microsoft/vscode/pull/334259)
* [@vscodebot-pr (VS Code PR Bot)](https://github.com/vscodebot-pr)
  * fix: tolerate post-close debug adapter messages (fixes #340511) [PR #340519](https://github.com/microsoft/vscode/pull/340519)
  * fix: guard webview find against disposed frame subtree (fixes #339314) [PR #339331](https://github.com/microsoft/vscode/pull/339331)
  * fix: guard Auto routing stream pushes against cancelled turns (fixes #341067) [PR #341077](https://github.com/microsoft/vscode/pull/341077)
* [@wycats (Yehuda Katz)](https://github.com/wycats): chat: preserve conversation ID for Agent Host BYOK requests [PR #341450](https://github.com/microsoft/vscode/pull/341450)
* [@yuki-nakano-520 (yuki nakano)](https://github.com/yuki-nakano-520): fix: sort terminal type-ahead latencies numerically [PR #341303](https://github.com/microsoft/vscode/pull/341303)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_144.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_144
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_144.md
- **SHA256_FINGERPRINT**: `bc09923fe097ce1745ab20ff60974a15abdeb1e114eac0608ed25f9010c9fd93`
- **LAST_VERIFIED_UTC**: 2026-10-28T18:07:38.440161+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.144

# Visual Studio Code 1.144

## Release recap

The road to GitHub Universe ([join us virtually!](https://githubuniverse.com/)) is paved with lots of pull requests! So, let's take a step back and look at what we've shipped recently.

* Remember when agent sessions would stop as soon as you closed your client? We built the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host), a separate process that keeps your agents running, on your local machine or remotely.

* With language servers in mind, we designed the [Agent Host Protocol (AHP)](https://microsoft.github.io/agent-host-protocol/) to allow any client to interact with agent sessions. All of sudden, session continuity across VS Code, Copilot CLI, GitHub Copilot App, and github.com lets you pick up right where you left off.

* The Agents window lets you manage your agents across workspaces and environments from a single interface, whether you kick off things yourself or use [automations](https://code.visualstudio.com/docs/agents/run/automations) to handle repetitive tasks.

* By default, agents are now powered by the [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses), the same harness used in Copilot Code Review, the Copilot CLI, the Copilot App, and Copilot Cloud sessions. Write agent customizations once and use them consistently across all these experiences.

* If you prefer [Anthropic's Claude Code harness or the one from OpenAI Codex](https://code.visualstudio.com/docs/agents/run/agent-harnesses?id=requirements-and-setup), just use those instead with your Copilot subscription and enjoy the familiar VS Code developer experience.

* As we continue to offer new models from different providers, how do you decide which one is best suited for your task? With [model comparisons](https://code.visualstudio.com/docs/agents/run/compare-models) (aka Agent Bake-Off), run the same prompt against multiple models and harnesses to see which performs best. Prefer a hands-off approach? Use [Copilot Fusion](https://code.visualstudio.com/docs/agents/concepts/language-models#_copilot-fusion) to choose the best model and orchestrate multiple models to work together for your task.

* We've had vision capabilities for a while, but you kept asking for more. The wait is over, and now you can also prompt the agent to [generate images](https://code.visualstudio.com/docs/chat/chat-overview#_generate-and-edit-images-experimental) directly in chat.

* Chat is not always the best interface for every task. With [canvas support](https://code.visualstudio.com/docs/agents/run/canvases), you can create rich, interactive UI to interact with your agents and visualize their outputs.

* Coding with agents can be more than just writing code. Let agents interact with the browser to validate their results, or let them [drive apps on your computer](https://code.visualstudio.com/docs/agents/run/tools#_control-desktop-applications-experimental) for automation and task execution.

* If you need it, build it! So, we created a beautiful new [Markdown editor](https://code.visualstudio.com/docs/languages/markdown#_markdown-editor). Instead of editing the raw Markdown, you can edit the rendered Markdown directly. And, of course, you can still edit the source if you prefer.

* And if you didn't notice, we also [refreshed the overall look and feel of VS Code](https://code.visualstudio.com/blogs/2026/10/15/modern-ui), so it looks fresh and beautiful in light and dark themes.

Read all about this, and more, in our [VS Code Wrapped blog post](https://code.visualstudio.com/blogs/2026/10/28/vscode-wrapped).

## Release highlights

This release helps you keep agent work moving across environments, find the right models for each task, and stay in control of changes and tool calls.

* [Session continuity](#session-continuity): Manage remotes in one place and keep sessions and automations running even when your computer is off.

* [Copilot Fusion and model comparisons](#models): Let Copilot choose and orchestrate models, or compare models side by side.

* [Image generation (Preview)](#image-generation-in-copilot-preview): Create and edit images directly in chat.

* [Computer use (Experimental)](#let-agents-use-desktop-apps-with-computer-use): Let agents use desktop apps on your computer.

* [Working set (Experimental)](#review-copilot-file-edits-with-the-working-set-experimental): Keep or undo agent file edits in the editor.

* [Assisted permissions](#assisted-permissions-are-generally-available): Reduce interruptions with automatic approval for tool calls that pass a risk check.

* [Customization marketplace](#discover-marketplace-customizations-preview) and [Copilot connectors](#connect-services-with-copilot-connectors-preview) (Preview): Discover skills and plugins for your workflow, and bring context from Slack, Notion, and other services into your agent sessions.

## Session continuity

### Run and continue Copilot tasks in the cloud

Cloud sessions let you run Copilot tasks from VS Code without keeping your development machine online. Your repository and tools run in a managed environment on GitHub's infrastructure.

From the **Chat view** in the editor window or the **Agents window**, you can:

* Select **Cloud** and choose a GitHub repository to start a task.
* Send follow-up instructions, respond to approval requests, and review the agent's changes.
* Reopen an existing cloud session from the sessions list to continue the same conversation.

Your cloud sessions are also accessible from other Copilot clients. For example, you can check progress on GitHub.com or in the **GitHub Mobile app**, then return to VS Code to continue working.

<video src="images/1_144/cloud-continuity.mp4" title="Video showing cloud continuity in Copilot tasks." autoplay loop controls muted></video>

Cloud sessions use a separate workspace. Local uncommitted changes aren't automatically copied. The new cloud experience requires a paid Copilot plan and is subject to organization policies.

### Manage remote environments

VS Code lets you run agents and perform development tasks across different (remote) environments. To make it easier to manage these environments, we're introducing the **Remote Environments** dialog, which brings your GitHub Environments, Dev Tunnels, WSL distributions, and SSH hosts together in one place.

Select **Manage Remote Environments** at the bottom of the Environment picker to see the status of each remote, connect or disconnect, and choose which remotes should be visible in the pickers.

![Screenshot showing the Remote Environments dialog with GitHub Environments, Dev Tunnels, WSL, and SSH groups, each remote's status, and inline actions for a connected tunnel.](images/1_144/remote-environments.webp)

Learn more about [remote agent sessions](https://code.visualstudio.com/docs/agents/run/remote-agent-sessions).

### Cloud Automations (Preview)

**Setting:** ``chat.automations.cloud.enabled``

Create and manage Copilot cloud automations directly in the Agents window. Enabled by default, they run on GitHub infrastructure on a schedule or in response to repository events, even when your computer is off.

To create a cloud automation, you can ask an agent to set one up for you, or use the **Create Automation** button in the Automations view in the Agents window.

With cloud automations, you can:

* **Set up automations that run in response to issue or pull request events**: Act automatically when activity happens in your repository. For example, automatically triaging issues as they get assigned to you.
* **Build shared workflows in the cloud with your team**: Create automations that are visible to everyone with access to the repository and act as Copilot.
* **Control exactly when your agent runs and what it can do**: Limit allowed tools and add filters for precise control over your automations. For example, trigger an automation when you are assigned an issue with a specific label.

![Screenshot showing the create cloud automation interface.](images/1_144/cloud-automations.webp)

To learn more, see [Create and manage agent automations](https://code.visualstudio.com/docs/agents/run/automations) in the Visual Studio Code docs.

### Agent Host Protocol v1.0

We've published the first version of the [Agent Host Protocol](https://microsoft.github.io/agent-host-protocol/), the protocol that VS Code uses to communicate with its agents locally and on remote machines, including for [cloud automations](#cloud-automations-preview). It's an open, extensible protocol designed to be an easy way to build custom UI's for your agents, or build agent platforms that plug into any UI that speaks it.

You can add a websocket-based agent host to your VS Code instance via the command **Agents: Add Remote Agent Host...** in the Agents window, and run `code agent endpoints` to get the endpoints for your editor's running agent host. We publish libraries in six languages and have found agents are good at making clients and hosts using them.

You can read more about the protocol and find additional resources on the [Agent Host Protocol website](https://microsoft.github.io/agent-host-protocol/).

## Models

### Route and orchestrate models with GitHub Copilot Fusion

Instead of picking a model for each task, select **Copilot Fusion** in the model picker and let Copilot intelligently route requests and orchestrate models for you. Copilot Fusion brings together [Project HydraFusion](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/)'s multi-model orchestration and [Copilot auto model selection](https://docs.github.com/copilot/concepts/models/auto-model-selection)'s task-aware model selection to balance performance and cost efficiency.

For each request, Copilot Fusion chooses the models, reasoning effort, and execution pattern for your task. For example, one model completes a simple task, while for harder tasks one model drafts a solution and other models review or critique it. Hover over the effort level below a response to see which models were used.

Choose an effort level to balance quality and cost: **Standard** for everyday coding work, **High** for more demanding tasks, and **Max** for the most complex tasks.

<video src="images/1_144/copilot-fusion.mp4" title="Video showing the model picker in Copilot Chat." autoplay loop controls muted></video>

You're billed for each model that Copilot Fusion uses at its standard rate. Through November 30, 2026, paid Copilot plans receive a 30% discount when using Copilot Fusion.

GitHub Copilot Fusion is now generally available, with Copilot Fusion High and Max offered on Copilot Pro+, Max, Business, and Enterprise plans. To learn more, see our documentation on [GitHub Copilot Fusion](https://aka.ms/vscode-copilot-fusion).

### Compare models and harnesses by default and in more projects

**Setting**: ``sessions.chat.compareAgents.enabled``

[Model comparisons](https://code.visualstudio.com/docs/agents/run/compare-models) run the same prompt across models for side-by-side review. They are enabled by default for eligible new sessions in the Agents window, unless overridden by user settings or experiments.

![Screenshot showing the Compare Models picker with four models selected and Done and Configure Judge buttons.](images/1_144/compare-models-picker.webp)

In this release, we expanded model comparison to more scenarios:

* **Explore ideas without a project:** Run independent attempts from a folderless **Chat**, without a Git repository, judge, or synthesizer.
* **Start with a local or empty repository:** A Git remote and an initial commit are no longer required. For repositories without commits, each isolated attempt starts from a snapshot of non-ignored working files without changing your source branch or index.

To open comparison setup from the keyboard, press ``Shortcut: sessions.compareModels`` from an eligible chat input or model picker.

Within setup, navigation buttons name their destination, such as **Configure Judge**, **Configure Attempts**, and **Configure Synthesis**, instead of using generic next and previous labels.

> **Note**: Model comparisons are not supported in Dev Containers.

### Image generation in Copilot (Preview)

**Setting:** ``chat.copilot.imageGeneration.model``, ``chat.copilot.imageGeneration.watermark``.

Agents can generate images from your prompts with GPT Image 2.5 Flare. Ask the agent to create an image for your website, a chat background, a new icon, or a website wireframe. You can also add an existing image as chat context and ask the agent to modify it or generate variations.

The default image model is GPT Image 2.5 Flare. To disable image generation, set ``chat.copilot.imageGeneration.model`` to `off`. Image generation requires access to the selected model and uses AI credits in addition to those used by the conversation model.

Additionally, set ``chat.copilot.imageGeneration.watermark`` to `true` to add a perceptible `Made with AI` watermark to your image.

<video src="images/1_144/image-gen.mp4" title="Video showing an image of a cat in a cafe being generated in the Agents Window." autoplay loop controls muted></video>

## Agent integration

### Let agents use desktop apps with computer use

**Setting**: ``chat.agentHost.computerUse.enabled``

Some tasks happen in desktop apps rather than in your code or the terminal. With Computer Use, the agent can see and control apps on your computer. Computer Use works in [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses) sessions that run on your own macOS or Windows machine.

When a task needs Computer Use, the agent asks you to allow turning it on, or you can run `/computer on`. Computer Use stays on for Copilot until you run `/computer off`.

Learn more about [Computer Use](https://code.visualstudio.com/docs/agents/run/tools#_control-desktop-applications-experimental) in the documentation.

### Canvases (Preview)

**Setting**: ``chat.canvases.enabled``

Previously introduced in VS Code 1.142, [Canvases](https://code.visualstudio.com/docs/agents/run/agent-harnesses#_use-canvases-with-the-copilot-harness) are shared, interactive surfaces where you and the agent can inspect and update the same artifact. This release makes canvases easier to find, manage, and open.

#### Manage canvases in the Agent Customizations editor

The Agent Customizations editor's **Canvases** section lists the canvases available to the active Copilot session and groups their contributing canvas extensions by source. To see it, open a Copilot session with at least one message in it, and open the Agent Customizations editor from there.

![Screenshot showing canvases from two workspace extensions in the Agent Customizations editor.](images/1_144/agent-customizations-canvases.webp)

Under the **Browse** section, select **Canvases** to find plugins whose metadata indicates that they provide canvases. Some canvas-capable plugins might not have that metadata and would appear under **Plugins** instead. Learn how to [manage canvas extensions](https://code.visualstudio.com/docs/agent-customization/overview#_manage-canvas-extensions).

![Screenshot showing the Agent Customizations Browse page filtered by @type:canvas, with canvas plugins available to install.](images/1_144/canvas-marketplace-filter.webp)

#### Open canvases from the Add Context menu

In chats in the editor or Agents window, select **Add Context (+)** > **Canvas...** to open or refocus an available canvas.

![Screenshot showing Canvas selected in the chat's Add Context menu.](images/1_144/canvas-add-context-menu.webp)

This adds another entry point alongside **New Chat (+)** > **Canvas** in the editor window and **Add Tab (+)** > **Canvas** in the Agents window.

## Agents

### Assisted permissions are generally available

Agents can make many tool calls to accomplish a task. Approving every tool call ensures that each action is explicitly authorized, but it can become cumbersome for frequent or low-risk calls. Giving the agent full autonomy might be risky and result in unintended actions or security issues.

With assisted permissions (now generally available for Copilot sessions), the agent performs an LLM-based risk assessment for each tool call and automatically approves low-risk calls. When a call is deemed higher risk or if the risk cannot be determined, the tool call still requires explicit user approval. This approach gives you a balance between convenience and security.

Select **Assisted permissions** in the permissions picker to have an LLM assess tool-call risk. Calls it approves run without prompting, while other calls still require your confirmation. Assisted permissions require Folder isolation and might be restricted by your organization. Read the [GitHub announcement of assisted permissions general availability](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available/).

### Session composer controls (Experimental)

Starting a new agent session is something you do often, so we've grouped the key settings at the top and added shortcuts for quick access.

#### Choose the environment first

With session continuity, where you run an agent session and where you access it from is completely up to you. So, when you create a new session in the Agents window, selecting the environment where the session runs is likely the first thing you do. Use the environment picker to choose from **This Computer**, **Cloud**, an eligible remote host, or a supported Dev Container.

The other configuration options will change based on the selected environment. For example, creating a session locally will let you specify the branch and worktree code isolation options.

To hide the Environment picker, disable ``sessions.chat.experimental.environmentPicker``.

![Screenshot showing the Environment picker in the new-session composer with This Computer, Cloud, GitHub Environments, Dev Tunnels, and SSH options.](images/1_144/session-composer-environment-picker.webp)

#### Chat without a project

**Setting**: ``sessions.chat.experimental.workspaceOptOut``

Sometimes you just want to start an agent conversation that is not associated with a specific workspace or folder (workspace-less chat). Rather than scrolling through the workspace picker, you can dismiss the current selection by hovering over (or on keyboard focus) the picker and selecting `X`.

Enable ``sessions.chat.experimental.workspaceOptOut`` to enable dismissing the selected workspace.

If you dismiss the selected workspace for an ongoing session, your prompt and attachments are preserved. The action is available only for harnesses and environments that support workspace-less chat.

<video src="images/1_144/new-session-composer.mp4" title="Video showing how to remove the workspace folder from the new-session composer to start a chat without a project." autoplay loop controls muted></video>

#### Reduce clutter

To reduce visual clutter, you can reduce each of the key configuration options to only show their icon. Right-click the UI control and select **Collapse to Icon**. Each picker retains its tooltip and accessible name, and your choices persist across reloads and Settings Sync.

#### Use the keyboard

From the focused new-session chat input, use ``Shortcut: sessions.focusNewSessionEnvironmentPicker``, ``Shortcut: sessions.focusNewSessionBranchPicker``, ``Shortcut: sessions.focusNewSessionWorktreePicker``, or ``Shortcut: sessions.focusSessionSyncAction`` to reach available controls. Collapsed session options expand as needed. The Sync shortcut only moves focus. Press Enter to synchronize.

### Copilot harness as the default

The Copilot harness continues to be the default for new sessions in VS Code. It's our latest harness, built on the Copilot SDK, a shared foundation that helps align behavior, capabilities, and improvements across Copilot products.

When you start a new session, **Copilot** in the harness picker indicates that the session uses the Copilot harness:

![Screenshot showing Copilot selected in the harness picker with a hover description of its Copilot SDK and Agent Host integration.](images/1_143/harness-copilot-description.webp)

In VS Code, you can keep Copilot harness sessions running in the background and access them from both the VS Code editor window and the Agents window. These sessions run through the [Agent Host](https://code.visualstudio.com/docs/agents/concepts/agent-host).

#### Review Copilot file edits with the working set (Experimental)

**Setting:** ``chat.editor.workingSet.enabled``

The Copilot harness records edits made through agent tools in a working set, so you can review and decide which changes to keep or undo, just like in the Local harness. Use the inline **Keep** and **Undo** controls in the editor for individual changes, or manage files and all pending changes from the working set above the chat input.

Keep and undo are enabled by default in the editor window and remain experimental. Set ``chat.editor.workingSet.enabled`` to `false` to show the Changes pill instead. Changes made through terminal commands do not appear in the working set. In the Agents window, use the **Changes** view to discard files.

Thank you so much to everyone who has shared valuable feedback. This release includes more improvements shaped directly by your feedback. Please continue [filing issues](https://github.com/microsoft/vscode/issues) to let us know how the Copilot harness is working for you. Your feedback is a huge help and directly shapes the harness experience.

Learn how to [work with the Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses), or explore the architecture and workflows in the [agent host blog post](https://code.visualstudio.com/blogs/2026/08/26/agent-host-architecture).

### Copilot Memory in the Copilot harness

Copilot harness sessions can now use [Copilot Memory](https://docs.github.com/copilot/concepts/agents/copilot-memory), the same cloud memory service that other Copilot surfaces like Copilot CLI, Copilot cloud agent, and Copilot code review also use.

Agents recall relevant repository facts and your preferences when a session starts, and store new learnings as you work, so you don't have to repeat the same context in every new conversation.

Memories are stored as repository facts, which are shared with others who have access to the repository, or as user preferences, which apply across your repositories. Ask the agent to remember a convention or preference, and state the scope when it matters:

```prompt
Across all my repositories, remember that I prefer concise commit message subjects.
```

Copilot Memory is enabled by default and respects your [Copilot Memory settings on GitHub](https://github.com/settings/copilot/memory) and your organization's policies. You can review and delete your memories on GitHub at any time.

Learn more about [using memory with agents](https://code.visualstudio.com/docs/agents/run/memory).

### Manage worktree storage (Experimental)

**Setting**: ``chat.agentSessions.sessionStorageCleanupSuggestion.enabled``

Last release, we introduced worktree storage cleanup for agent sessions to help you reclaim disk space used by worktrees. This release adds more ways to find the worktrees you want to remove:

* **See all past worktrees**: The **Any time** option is selected by default, to let you review recent worktrees as well as older ones.
* **Find worktrees by workspace**: Each row shows its workspace, and a workspace filter narrows the results. Changing the workspace filter clears the selection.

![Screenshot showing the workspace filter in Worktree Cleanup, with All workspaces selected and workspace names in each row.](images/1_144/worktree-cleanup-workspace-filter.webp)

When cleanup suggestions are enabled and a local worktree's disk has less than 5 GB available, the Agents window provides a suggestion below the sessions list to run worktree cleanup, regardless of worktree age or count. The suggestion opens cleanup with **Any time** selected.

![Screenshot showing the disk-almost-full notification with Open Worktree Cleanup and Don't Show Again actions.](images/1_144/diskspace-full.webp)

### Enable extensions in agents window

Extensions can run and be enabled or disabled directly from the Agents window. This requires ``extensions.experimental.agentsWindowManagement`` to be set to `true`.

![Extensions in Agents window](images/1_144/extensions-in-agents-window.webp)

## Agent customizations

### Connect services with Copilot connectors (Preview)

Bring the Slack discussion behind a change, project context from Notion, or API documentation from Microsoft Learn into your agent sessions. [Copilot connectors](https://code.visualstudio.com/docs/agent-customization/copilot-connectors) are GitHub-managed MCP servers that connect your agent to these services without local server setup or MCP configuration.

[Open Browse](vscode://chat-customizations/open?page=discover), choose **Copilot Connectors** in the source menu, and select **Connect** on a service. Authorize access in your browser. Connect once and reuse the connection across supported Copilot clients signed in with the same account.

![Screenshot showing the Copilot Connectors source in Browse, listing Port, Postman, Sentry, Slack, Statsig, and Work IQ with Connect and Disconnect buttons.](images/1_144/copilot-connectors.webp)

Connectors are enabled by default on all Copilot plans and work only with the Copilot harness. For Business and Enterprise, an administrator must enable **Editor preview features**. Your organization's MCP restrictions apply, and some services require administrator approval.

### Discover marketplace customizations (Preview)

Add skills, tools, and entire workflows to your agent without building them from scratch. [**Browse**](https://code.visualstudio.com/docs/agent-customization/overview#_discover-marketplace-customizations-preview), the new home page for Customizations, brings together **GitHub Feed** and plugins from [marketplaces configured by you or your enterprise](https://code.visualstudio.com/docs/agent-customization/agent-plugins#_configure-plugin-marketplaces).

Explore **Editor's picks**, **Plan, build, and ship**, and **Connect your work**, or search and filter by source or type. [Open Browse](vscode://chat-customizations/open?page=discover) or run **Chat: Open Customizations** to start.

![Screenshot showing the Browse page in Customizations with Editor's picks and Plan, build, and ship sections, and the source menu open to list GitHub Feed, Copilot Connectors, and plugin marketplaces.](images/1_144/customization-marketplace.webp)

Link to Browse from a README or team guide, optionally with a search. For example, [Browse filtered to MCP servers](vscode://chat-customizations/open?page=discover&search=%40type%3Amcp).

GitHub Feed requires a supported harness and isn't available in Local sessions. For Copilot Business and Enterprise, an administrator must enable **Editor preview features**.

### Richer editing for GitHub Copilot custom agents

When you customize agents for the GitHub Copilot harness, completions, hovers, and validation help you choose available models, tools, and skills and catch configuration errors before you run the agent.

* **Models**: The `model` attribute offers Copilot model IDs as a single value or an ordered list of preferences.
* **Tools**: The `tools` attribute offers Copilot tool aliases, such as `read`, `edit`, and `execute`, alongside qualified client and extension tools.
* **Skills**: The `skills` attribute offers available skills, with descriptions and source information in completions and hovers.
* **Configuration validation**: Copilot-specific attributes and nested structures, including hooks and agent-scoped MCP servers, have completions, hovers, and validation. Unknown models, tools, and skills are only flagged after discovery has finished, so valid values aren't marked as errors while inventories are still loading.
* **Body features**: In GitHub Copilot agent files, placeholders such as `{{cwd}}` and `{{shellToolName}}` are recognized and show hovers. Unknown placeholders and Local-only `#tool:` and `#file:` references are flagged.

<video src="images/1_144/copilot-agent-editing.mp4" title="Video showing model, tool, and skill completions in a GitHub Copilot custom agent file, followed by an unavailable-model diagnostic and hover." autoplay loop controls muted></video>

### Harness-aware defaults for custom agent editing

When your `.agent.md` file has no `target` attribute, the editor now uses the active customization harness to provide matching completions, hovers, and diagnostics. Switching harnesses refreshes this guidance without reopening the file. An explicit `target: vscode` or `target: github-copilot` continues to override the default.

### Share links to plugins and customizations

You can share deep links in a README or team guide to help others add an [agent plugin marketplace](https://code.visualstudio.com/docs/agent-customization/agent-plugins), install a specific plugin, or open a page in the customization dialog.

| Action | Example link |
|--------|--------------|
| Add a marketplace | `vscode://chat-plugin/add-marketplace?ref=owner/repo` |
| Add a marketplace and install a named plugin | `vscode://chat-plugin/install?source=owner/repo&plugin=plugin-name` |
| Open the Plugins page with a search filter | `vscode://chat-customizations/open?page=plugins&search=github` |

Replace `owner/repo` with the marketplace's GitHub repository and `plugin-name` with the plugin's name in that marketplace. VS Code asks for confirmation before adding a marketplace or installing a plugin. These actions use a Copilot harness session; if none is available, VS Code asks before creating one. Only proceed if you trust the source, because plugins can run code on your machine.

Use these links for **Install in VS Code** buttons in your plugin's README, as shown in the [Session timeline plugin's getting started section](https://github.com/microsoft/vscode-team-kit/tree/main/session-timeline#getting-started).

Customization links also support pages such as `agents`, `skills`, `instructions`, `hooks`, `mcp-servers`, `tools`, and `migrations`. Omit `search` to open the page without a filter. Use `vscode-insiders://` instead of `vscode://` to open VS Code Insiders.

### Manage Copilot customizations with slash commands

You can manage plugins, MCP servers, and skills without leaving the Chat view in a Copilot harness session. Type `/plugin`, `/mcp`, or `/skills` followed by a space to see the available subcommands.

* **Plugins**: List, install, update, enable, disable, or uninstall [agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins). Use `/plugin marketplace` to manage marketplaces, or `/plugin install` to choose a plugin to install.
* **MCP servers**: Use `/mcp show`, `/mcp enable`, or `/mcp disable` with a server name to inspect or manage your [MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
* **Skills**: Use `/skills info` with a skill name to inspect an available [agent skill](https://code.visualstudio.com/docs/agent-customization/agent-skills).

Completions suggest supported subcommands and relevant plugin, marketplace, server, or skill names. Available commands depend on the Copilot runtime, and results appear directly in chat.

The following video shows browsing the `vscode-team-kit` marketplace and installing the Session timeline plugin with `/plugin install`.

<video src="images/1_144/copilot-plugin-install.mp4" title="Video showing browsing a plugin marketplace and installing Session timeline with slash commands in Copilot Chat." autoplay loop controls muted></video>

## Session management

### Move chats between sessions (Preview)

**Setting**: ``chat.agentHost.moveChats.enabled``

The [Agents window](https://code.visualstudio.com/docs/agents/run/agents-window) lets you organize related conversations into sessions. Rearrange those conversations as your work evolves without starting over or losing their history.

* Drag a nested chat into another session, or drop it between that session's nested chats to choose its position.
* Right-click a nested chat and select **Promote to Session** to give it its own session. You can also drag it onto empty space in the sessions list.
* Drag a single-chat session onto another session to nest it there.
* Reorder nested chats by dragging them, or use **Move Up** and **Move Down** from their context menu. With focus in the sessions list, use ``Shortcut: sessionsViewPane.moveChatUp`` and ``Shortcut: sessionsViewPane.moveChatDown``.

Moves preserve the chat's working folder, including an existing worktree or a temporary folder for a chat without a workspace. A shared worktree remains available while another session still uses it. Moves between sessions require the same agent and provider, and a destination that supports multiple chats. Subagent conversations move with their parent chat rather than independently.

The sessions list shows move progress and provides **Undo** after a move. Enable the setting to try this feature in Stable; it is on by default in Insiders.

Learn more about [organizing sessions in the Agents window](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions#_organize-sessions).

### Choose a workspace for nested sessions

Previously, nested sessions inherited the workspace of their parent session. Now, you can choose a separate workspace for each nested session. This lets you work across repositories while keeping related conversations together in one session. For example, a frontend chat and a backend chat can work in different folders without splitting the task across separate sessions.

Select **New Nested Session** in the Agents window to open a composer with a folder picker that defaults to the parent session's folder. Choose a recent folder, browse to another folder, or select **No Workspace** for a chat with its own temporary folder.

For a Git repository, choose **New Worktree** and a branch to isolate the nested chat's file changes. The nested chat uses its parent session's agent and host. Agents that do not support multiple working directories offer only the parent session's folder.

### Nested sessions in quick chats

Follow up on a quick chat without mixing separate questions into one conversation or losing track of related discussions. For example, explore two approaches in separate nested sessions under the same quick chat, without opening a project folder.

Quick chats in the Agents window support nested sessions: select **+** on a quick chat or use **New Nested Session** from its context menu.

Each nested session starts with **No Workspace** selected and gets its own temporary folder, separate from the parent quick chat. The quick chat stays in the **Chats** section, keeping its related conversations together.

### Custom icons and colors for session groups

Make workspace groups, environment groups (including remote hosts), and custom groups easier to recognize with custom icons and theme-aware colors. In the Agents window, open a group's context menu and select **Change Icon...** or **Change Color...**. Your choices persist across reloads and host reconnections, and **Reset to default** restores the icon or color independently. _[#343576](https://github.com/microsoft/vscode/pull/343576)_

<video src="images/1_144/session-group-appearance.mp4" title="Video showing a group context menu, searchable icon picker, and color picker used to customize a session group." autoplay loop controls muted></video>

## Chat

### Voice conversations with session context (Experimental)

[Voice Mode](https://code.visualstudio.com/docs/configure/accessibility/voice) (``agents.voice.enabled``) lets you discuss tasks aloud while the coding agent works. Use an OpenAI live model with your own API key (``agents.voice.useBYOKVoiceModel``) to ask questions such as 'Where were we?' or 'Which session needs input?' without starting a coding request.

![Screenshot showing the blue Voice Mode indicator and its hover identifying OpenAI GPT Live as the real-time voice provider.](images/1_144/voice-mode-connection-hover.webp)

The enabled-by-default ``agents.voice.sessionAwareness`` shares a bounded briefing of tracked sessions and recent active-chat context with OpenAI BYOK Voice Mode. It includes session titles, response summaries, pending prompt details, the selected model, and attachment names, but not attachment contents.

Voice Mode's animation uses a single color for a more conversational feel: you can jump in and speak at any time.

<video src="images/1_144/voice-mode-session-awareness.mp4" title="Video showing a user asking where they left off in the current chat and receiving a summary from Voice Mode." autoplay loop controls muted></video>

GPT Live conversations also handle follow-ups and ongoing work more predictably:

* Ask questions while the agent works and hear the answers, with other updates queued and read aloud afterward.
* Single-question forms read the full question, and multi-question forms collect one numbered answer at a time.
* New spoken coding instructions during ongoing work are sent as steering rather than queued until the task finishes. Steering applies at the next opportunity supported by the provider and does not guarantee immediate interruption. Voice-only exchanges during ongoing work are not retained for later requests.

### Localized voice approvals and clearer connection status (Experimental)

Approve or reject GPT Live tool requests in your selected voice language (``agents.voice.language``), with support for 25 languages and English as a fallback. Answer questions with displayed choice labels, numbers, or free text where allowed. Ambiguous approvals still require an explicit answer or chat controls.

The voice language setting does not translate agent-provided questions or choices. Commands such as 'skip' and 'other' remain English-only.

## Editor Experience

### Issue Reporter

**Settings**: ``issueReporter.wizard.enabled``, ``issueReporter.wizard.openLocation``, ``issueReporter.additionalRepositories``

Issues with clear steps, screenshots, and logs are faster for us to reproduce and fix. The [new issue reporter](https://code.visualstudio.com/updates/v1_122#_improved-issue-reporting-flow), which you turn on with ``issueReporter.wizard.enabled``, makes it easier for you to create high quality issues. You can capture screenshots and screen recordings without leaving VS Code, from the capture bar or with `Shortcut: workbench.action.issueReporter.captureScreenshot` and `Shortcut: workbench.action.issueReporter.toggleRecording`.

This release makes these changes to the new issue reporter:

* The form fits on a single page instead of three steps.
* Attach other files that help us debug your issue, such as log files or zip archives. You can also paste or drop images and videos into the form.
* The reporter opens in its own window. To open it in an editor tab instead, set ``issueReporter.wizard.openLocation`` to `editor`.
* To file issues in other GitHub repositories, for example your team's own tracker, add them to ``issueReporter.additionalRepositories`` in `owner/repo` format. Then pick the repository in the form.

<video src="images/1_144/issue-reporter-update.mp4" title="Video showing the issue reporter opening in its own window, capturing a screenshot and a screen recording, attaching a file, and previewing the report on GitHub." autoplay loop controls muted></video>

## Terminal

### Dialogs from terminal commands open in front of VS Code on Windows

**Setting**: ``terminal.integrated.windowsReparentConsoleWindow``

On Windows, some command-line tools open dialogs that could appear behind VS Code when run from the terminal. For example, the Azure PowerShell `Connect-AzAccount` sign-in picker opened behind the VS Code window, so the command looked stuck until you moved or minimized VS Code.

VS Code now makes the window that shows each local terminal the owner of that terminal's hidden console window, as Windows Terminal does. Dialogs that tools attach to their console window now open in front of the VS Code window the terminal is in.

This requires ``terminal.integrated.windowsUseConptyDll``, which is enabled by default. To turn off this behavior, set ``terminal.integrated.windowsReparentConsoleWindow`` to `false`.

## Enterprise

### Clearer permission restrictions

Assisted and Allow All remain visible but disabled when restricted by your organization, with an explanation instead of disappearing.

Example Copilot managed settings:

```json
{
  "permissions": {
    "disableAssistedPermissionsMode": true,
    "disableBypassPermissionsMode": "disable"
  }
}
```

![Screenshot showing Assisted permissions and Allow All disabled by organization policy.](images/1_144/managed-permission-modes.webp)

### Organization-managed session defaults

New chats in the Editor and Agents windows respect your organization's default model, [Copilot Fusion](#route-and-orchestrate-models-with-github-copilot-fusion) tier, and permission level, taking precedence over remembered selections. You can change these defaults within a session where policy allows; unavailable permission modes fall back to Manual.

Example Copilot managed settings, for organizations with Fusion Max available:

```json
{
  "model": "fusion",
  "fusionTier": "max",
  "permissions": {
    "defaultMode": "assisted"
  }
}
```

![Screenshot showing chat configured with Copilot Fusion Max and Assisted permissions.](images/1_144/managed-session-defaults.webp)

### Managed settings loading progress

When organization settings load slowly, progress appears inline in the waiting chat instead of stacking notification toasts. Background loading no longer interrupts you.

![Screenshot showing organization-managed settings loading progress in chat.](images/1_144/managed-settings-loading.webp)

## Contributions to extensions

### GitHub Pull Requests

There has been more progress on the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension, which enables you to work on, create, and manage pull requests and issues. New features include:

- The "Update stack" action now uses the GitHub API to update a stacked pull request when possible, so you no longer need to have a pull request from the stack checked out.
- The pull request overview shows a banner offering to create a stack when the pull request's branches line up with other open pull requests that aren't stacked yet.
![PR can be stacked](./images/1_144/pull-can-stack-banner.webp)

Review the [changelog for the 0.174.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01740) release of the extension to learn about everything in the release.

## Extension Authoring

### Publish extensions with OIDC and Trusted Publishing

You can now publish extensions to the Visual Studio Marketplace from GitHub Actions without storing a Personal Access Token (PAT) as a repository secret. The `vsce publish --oidc` command requests a short-lived OpenID Connect (OIDC) token from GitHub Actions and exchanges it for a temporary Marketplace credential that is valid for up to 15 minutes. If the token exchange fails, `vsce` doesn't fall back to a PAT.

To get started, create a Trusted Publishing policy for your repository and workflow in the Visual Studio Marketplace publisher management page, grant the publishing job the `id-token: write` permission, and run `vsce publish --oidc` in your workflow. Use a version of `@vscode/vsce` that supports OIDC, such as `4.0.2` or later.

Trusted Publishing is currently supported for GitHub Actions only. For Azure Pipelines, continue to use Microsoft Entra ID with a service connection. As global PATs in Azure DevOps are retired on December 1, 2026, we recommend that you move your extension publishing to one of these secure methods.

Learn more about [publishing extensions with vsce](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#publish-with-github-actions-and-trusted-publishing).

Learn more about [Trusted Publishing in the Visual Studio Marketplace blog post](https://aka.ms/vsm/trustedpublishing/blogpost).

## Deprecated features and settings

None

## Thank you

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

### Pull requests

Contributions to `vscode`:

* [@aguashui (Noah Webber)](https://github.com/aguashui): Kitchen sink changes [PR #334932](https://github.com/microsoft/vscode/pull/334932)
* [@bluerose73 (Shengjie Ma)](https://github.com/bluerose73): Add configurable xtab reasoning effort and completion token limits [PR #342204](https://github.com/microsoft/vscode/pull/342204)
* [@cipheraxat (Akshat Anand)](https://github.com/cipheraxat): fix: keep paused debug location range valid in chat [PR #342379](https://github.com/microsoft/vscode/pull/342379)
* [@dhairyajangir (dhairya)](https://github.com/dhairyajangir): Fix UTF-8 encoding of MCP resource URI template values [PR #339846](https://github.com/microsoft/vscode/pull/339846)
* [@HectorHZZZ](https://github.com/HectorHZZZ): NES: add applied-then-undone rejected-edit memory mode [PR #341436](https://github.com/microsoft/vscode/pull/341436)
* [@mcumming (Michael Cummings (MSFT))](https://github.com/mcumming): Authenticate Entra ID marketplace API requests via RFC 9728 PRM negotiation [PR #325804](https://github.com/microsoft/vscode/pull/325804)
* [@r3na7 (renat)](https://github.com/r3na7): Preserve Explorer rename input when the window loses focus [PR #338126](https://github.com/microsoft/vscode/pull/338126)
* [@rfeltis (Ralph Feltis)](https://github.com/rfeltis): Chat: onboarding spotlight tour for the Copilot harness chat input [PR #337814](https://github.com/microsoft/vscode/pull/337814)
* [@SahinurDEV (Sahinur)](https://github.com/SahinurDEV): Debug Extension Host: enable inspector on running extension host instead of requiring restart [PR #343437](https://github.com/microsoft/vscode/pull/343437)
* [@timrogers (Tim Rogers)](https://github.com/timrogers)
  * Default new cloud automations to no allowed tools [PR #342481](https://github.com/microsoft/vscode/pull/342481)
  * Align `require_actor_write_permission` cloud automation option naming with GitHub.com and ensure compliance with repository policies [PR #344444](https://github.com/microsoft/vscode/pull/344444)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_145.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_145
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_145.md
- **SHA256_FINGERPRINT**: `779bcb031dac085f1bdc07445bdcc33e738348b34ceb2f86daebec0857240a25`
- **LAST_VERIFIED_UTC**: 2026-10-28T18:07:38.397223+00:00
---

**MetaDescription**: Learn what is new in Visual Studio Code 1.145 (Insiders).

# Visual Studio Code 1.145

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: October 28, 2026_

Welcome to the 1.145  release of Visual Studio Code.

Happy Coding!

---

## October 28, 2026

* Track bulk worktree cleanup progress, keep completed results visible, and retry failed cleanups in the Agents window. _[microsoft/vscode#344588: Improve bulk worktree cleanup progress and recovery](https://github.com/microsoft/vscode/issues/344588)_

## October 27, 2026

* Preview web apps running on remote agent hosts in the Agents window's integrated browser (Experimental). _[microsoft/vscode#331926: Integrated browser remote proxy should support remote AHP hosts in Agents window](https://github.com/microsoft/vscode/issues/331926)_

* Fix keyboard access to MCP authentication prompts in screen reader mode. _[microsoft/vscode#343890: MCP authentication inline hint is not keyboard accessible in screen reader mode](https://github.com/microsoft/vscode/issues/343890)_

* Move the default **Agent** picker into **Add Context** in editor-window chat with the experimental ``sessions.chat.experimental.agentsPickerInAttachContextMenu`` setting. _[microsoft/vscode#344606: Apply the Agent picker Add Context setting to editor-window chat](https://github.com/microsoft/vscode/issues/344606)_

* Add support for breadcrumbs in unsaved files when the language provides symbols. _[microsoft/vscode#84746: Enable breadcrumbs for unsaved files](https://github.com/microsoft/vscode/issues/84746)_

* Run saved automations with **Chat: Run Automation...** in the Agents window **Command Palette**. _[microsoft/vscode#344445: Add a "Chat: Run Automation..." action](https://github.com/microsoft/vscode/issues/344445)_

## October 26, 2026

* Open sessions in an editor instead of the **Chat** view by enabling the experimental ``chat.agentSessions.openInEditor`` setting. _[microsoft/vscode#336136: Allow configuring the default click action for Chat Sessions](https://github.com/microsoft/vscode/issues/336136)_

* Show size estimates faster for unchanged idle sessions when reopening or refreshing **Worktree Cleanup** in the Agents window. _[microsoft/vscode#344370: Persist session worktree sizes for Worktree Cleanup](https://github.com/microsoft/vscode/issues/344370)_

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
- **SHA256_FINGERPRINT**: `0db38d2f8adffce4c1154c147c4435581b3c5a8c2f5ae81113980c08c71a0971`
- **LAST_VERIFIED_UTC**: 2026-10-23T04:01:53.027709+00:00
---

# VS Code Insiders Roadmap: 1.143.1 Endgame
- **Issue Number**: #343623
- **Category**: `endgame-plan`
- **State**: open
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
- **SHA256_FINGERPRINT**: `62e7e4778317cd876fdd0f20ea1f00ad01b6346fb9e86730860ae998ac471d2a`
- **LAST_VERIFIED_UTC**: 2026-10-29T05:00:59.509065+00:00
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
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
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
# DOCUMENT_SOURCE: vscode_insiders::iteration-plan_271045
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/271045
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/271045
- **SHA256_FINGERPRINT**: `bbdddf50563f89ff6fe83c256dd8fc3fed39f9c052d47a2307e7330078484e8c`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.166362+00:00
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
- [ ] :runner: Revive TypeScript context provider experiment [vscode#255373](https://github.com/microsoft/vscode/issues/255373) @dbaeumer

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
- **SHA256_FINGERPRINT**: `30a907360593dc7ddc58c4e9cdb47fe6977124644bb2cf1554c85ae860ebc2f7`
- **LAST_VERIFIED_UTC**: 2026-10-21T19:55:00.164423+00:00
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
- [x] Revive TypeScript context provider experiment [vscode#255373](https://github.com/microsoft/vscode/issues/255373) @dbaeumer
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
- **SHA256_FINGERPRINT**: `3e6345707becbb6fd42eafe9c6f0fb4e0dad79c0cc24db3eb941683469595c53`
- **LAST_VERIFIED_UTC**: 2026-10-29T05:00:57.653947+00:00
---

# GitHub Copilot Official Changelog Feed

## Route and orchestrate models with GitHub Copilot Fusion
- **Date**: Wed, 28 Oct 2026 16:00:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion

GitHub Copilot Fusion is generally available. Instead of picking a model for each task, choose Copilot Fusion and let Copilot intelligently route and orchestrate which models it uses for you....
The post Route and orchestrate models with GitHub Copilot Fusion appeared first on The GitHub Blog .

## GitHub Copilot app, Universe releases
- **Date**: Wed, 28 Oct 2026 15:55:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases

Work doesn’t always fit in a single repository or session. A feature can span several repositories. A launch plan can pull in specs, designs, and assets without touching a repository...
The post GitHub Copilot app, Universe releases appeared first on The GitHub Blog .

## GitHub Enterprise now includes access to GitHub Copilot
- **Date**: Wed, 28 Oct 2026 15:50:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot

Enterprises working with a GitHub or Microsoft account team can now get Copilot included with GitHub Enterprise for every licensed user. Previously, you had to manage two things: how many...
The post GitHub Enterprise now includes access to GitHub Copilot appeared first on The GitHub Blog .

## Security extension for the GitHub Copilot app
- **Date**: Wed, 28 Oct 2026 15:45:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app

You can now work through your repository’s GitHub code scanning alerts without leaving the GitHub Copilot app. The new GitHub security extension, now in public preview, lets you find the...
The post Security extension for the GitHub Copilot app appeared first on The GitHub Blog .

## GitHub intelligence puts your code, context, and history to work
- **Date**: Wed, 28 Oct 2026 15:40:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work

Agents should understand more than your codebase—they should understand how your team works. Your preferences, repository conventions, skills, and custom instructions guide how changes should be made, while code in...
The post GitHub intelligence puts your code, context, and history to work appeared first on The GitHub Blog .

## Build shared workflows for your team with Copilot Automations
- **Date**: Wed, 28 Oct 2026 15:35:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations

Shared Copilot Automations are rolling out, enabling teams to build and maintain AI-powered workflows together. With Copilot Automations, you can combine prompts, triggers, and tools to design workflows around the...
The post Build shared workflows for your team with Copilot Automations appeared first on The GitHub Blog .

## GitHub Copilot in VS Code, Universe releases
- **Date**: Wed, 28 Oct 2026 15:33:00 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases

This year, we focused on giving you more choice in how you work with GitHub Copilot in Visual Studio Code: which models you use, where your agents run, and how...
The post GitHub Copilot in VS Code, Universe releases appeared first on The GitHub Blog .

## Generate and edit images directly in Copilot
- **Date**: Wed, 28 Oct 2026 15:30:55 +0000
- **URL**: https://github.blog/changelog/2026-10-28-generate-and-edit-images-directly-in-copilot

You can now generate and edit images using natural language in GitHub Copilot. When you ask for an image, your selected reasoning model calls a dedicated image-generation tool powered by...
The post Generate and edit images directly in Copilot appeared first on The GitHub Blog .

## GitHub Copilot Fusion now supports selection of local models
- **Date**: Wed, 28 Oct 2026 15:30:42 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-copilot-fusion-now-supports-selection-of-local-models

Today we are shipping intelligent routing for local models into experimental preview. GitHub Copilot Fusion can now choose between supported on-device models and cloud models, enabling intelligent local model routing...
The post GitHub Copilot Fusion now supports selection of local models appeared first on The GitHub Blog .

## GitHub Agentic Workflows generally available
- **Date**: Wed, 28 Oct 2026 15:30:15 +0000
- **URL**: https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available

GitHub Agentic Workflows, an open source project from GitHub Next, is now generally available. With agentic workflows, you can automate reasoning-based tasks like issue triage, CI failure analysis, documentation updates,...
The post GitHub Agentic Workflows generally available appeared first on The GitHub Blog .
