# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-10-21T03:47:16.551644+00:00
- **Total Palabras**: 8,497 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


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
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_143
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_143.md
- **SHA256_FINGERPRINT**: `f2011c32f61a5652440b7ab548c8c5e6d783cf80a66cf4b856c1ab8b4f29ee61`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:56.281656+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.143

# Visual Studio Code 1.143

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode.ig)

---

_Last updated: October 19, 2026_

Welcome to the 1.143  release of Visual Studio Code.

## Release highlights

This release makes the Copilot harness the default for new sessions and adds tools to compare models, reclaim storage, run models locally, and navigate file changes.

* [Copilot harness by default](#copilot-harness-as-the-default): The default for new sessions, lets you switch between editor and Agents window, and keeps sessions running in the background.

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
- **SHA256_FINGERPRINT**: `551a52158895e1377505407b2323627d2c5681245e362c48c33cf6226938f521`
- **LAST_VERIFIED_UTC**: 2026-10-21T03:44:56.348753+00:00
---

**MetaDescription**: Learn what is new in Visual Studio Code 1.144 (Insiders)

# Visual Studio Code 1.144

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode.ig)

---

_Last updated: October 21, 2026_

Welcome to the 1.144  release of Visual Studio Code.

Happy Coding!

---

## October 20, 2026

* In the experimental new session composer, clear the selected workspace to start without a project or choose another workspace. _[#342930: Agents window: clear the selected workspace from the new session composer](https://github.com/microsoft/vscode/issues/342930)_

* Resize Mermaid diagrams, expand them to the editor width, or open them in full view in the rich Markdown editor. _[#342880: Support presentation controls for Mermaid in the rich Markdown editor](https://github.com/microsoft/vscode/issues/342880)_

* Keep OAuth tokens separate for each MCP server. _[#293533: MCP: Cannot authenticate to multiple Atlassian sites simultaneously - OAuth credentials shared across MCP server configurations](https://github.com/microsoft/vscode/issues/293533)_

## October 19, 2026

* Add experimental support for comparing multiple models without opening a folder. _[#342578: Bake off feedback](https://github.com/microsoft/vscode/issues/342578)_

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
