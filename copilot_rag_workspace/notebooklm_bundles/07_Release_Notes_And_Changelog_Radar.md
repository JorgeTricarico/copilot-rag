# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-10-27T17:44:22.515752+00:00
- **Total Palabras**: 16,408 / 500,000 máx.
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
- **SHA256_FINGERPRINT**: `82c1dfcc4ecf9fdb4401cb43247324253cd990c963098789222e0a91e68b2dc1`
- **LAST_VERIFIED_UTC**: 2026-10-26T18:29:23.901813+00:00
---

**MetaDescription**: Learn what is new in Visual Studio Code 1.144 (Insiders)

# Visual Studio Code 1.144

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: October 21, 2026_

Welcome to the 1.144  release of Visual Studio Code.

Happy Coding!

---

## October 21, 2026

* UI updates for Voice Mode. _[#343323: Simplify Voice Mode connection visuals and show GPT Live usage](https://github.com/microsoft/vscode/issues/343323)_

* When session storage cleanup suggestions are enabled, the Agents window warns when a local worktree's disk has less than 5 GB available and offers cleanup of recent worktrees. _[#343230: add workspace almost full notification](https://github.com/microsoft/vscode/issues/343230)_

* UI updates for embedded editors in the rich Markdown editor. _[#343191: Update rich Markdown editor package to 0.0.2-136](https://github.com/microsoft/vscode/issues/343191)_

* In Voice Mode, the microphone button reflects its muted or active state. _[#337053: Reverse the mute and unmute microphone icons in voice mode](https://github.com/microsoft/vscode/issues/337053)_

* When you paste a web link into Quick Open, choose from its available handlers, with the default listed first, or open the target to the side. _[#342544: Show available link handlers in a Quick Pick](https://github.com/microsoft/vscode/issues/342544)_

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
- **SHA256_FINGERPRINT**: `578217163f604325c095347efe5c78bda3d2a4050130abf3a68a943db857edc0`
- **LAST_VERIFIED_UTC**: 2026-10-27T17:44:22.506356+00:00
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
- [ ] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [ ] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [ ] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
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
- [ ] Publish website so that in-product release notes are ready
- [ ] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [ ] Deploy vscode.dev
  - [ ] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [ ] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
- [ ] Publish socials (ping Cynthia)
- [ ] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [ ] Create an official release
  - [ ] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [ ] Push the tag: `git push origin <x.y.z>`
  - [ ] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [ ] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [ ] Move all remaining issues to "On Deck"
- [ ] Ensure that the latest Insiders release from main has succeeded


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
- **SHA256_FINGERPRINT**: `92848f03ff083a1f63b4b7fc8d59f13d52bd412fc44036fe51384c0b7804598d`
- **LAST_VERIFIED_UTC**: 2026-10-27T04:20:52.756820+00:00
---

# GitHub Copilot Official Changelog Feed

## GitHub Copilot assisted permissions generally available
- **Date**: Mon, 26 Oct 2026 22:31:30 +0000
- **URL**: https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available

Assisted permissions are now generally available in GitHub Copilot CLI, GitHub Copilot app, and Visual Studio Code. When Copilot requests permission to run a command, access a file system path,...
The post GitHub Copilot assisted permissions generally available appeared first on The GitHub Blog .

## GPT-6.1 Terra in GitHub Copilot
- **Date**: Mon, 26 Oct 2026 19:15:53 +0000
- **URL**: https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot

GPT-6.1 Terra, OpenAI’s newest model, is now generally available in GitHub Copilot. It is designed for everyday agentic coding and terminal work at a lower cost than GPT-6.1 Sol. In...
The post GPT-6.1 Terra in GitHub Copilot appeared first on The GitHub Blog .

## Usage metrics API adds usage from tools like OpenCode
- **Date**: Fri, 23 Oct 2026 23:42:03 +0000
- **URL**: https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode

The Copilot usage metrics API now reports model usage from more of the tools your developers use with Copilot, including tools like OpenCode that weren’t previously captured in your reports....
The post Usage metrics API adds usage from tools like OpenCode appeared first on The GitHub Blog .

## Turn notifications into code with GitHub Copilot in Teams
- **Date**: Fri, 23 Oct 2026 21:29:58 +0000
- **URL**: https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams

The new GitHub app in Teams brings notifications and Copilot together, helping teams turn issues into fixes and ship code faster without leaving the conversation. Get notified in channels, group...
The post Turn notifications into code with GitHub Copilot in Teams appeared first on The GitHub Blog .

## GitHub Copilot in Visual Studio — September update
- **Date**: Fri, 23 Oct 2026 00:17:51 +0000
- **URL**: https://github.blog/changelog/2026-10-22-github-copilot-in-visual-studio-september-update-2

September 2026 brought deeper visibility into your work: explore pull requests without leaving chat, bring the AI model your team trusts, and fix vulnerable packages the moment Visual Studio flags...
The post GitHub Copilot in Visual Studio — September update appeared first on The GitHub Blog .

## Custom skills, agents, and MCP servers in usage metrics API
- **Date**: Thu, 22 Oct 2026 22:19:17 +0000
- **URL**: https://github.blog/changelog/2026-10-22-custom-skills-agents-and-mcp-servers-in-usage-metrics-api

Copilot usage metrics now show the names of the skills, custom agents, Model Context Protocol (MCP) servers, slash commands, and plugins that your organization creates, instead of grouping them under...
The post Custom skills, agents, and MCP servers in usage metrics API appeared first on The GitHub Blog .

## Global default for Copilot features generally available
- **Date**: Thu, 22 Oct 2026 20:44:28 +0000
- **URL**: https://github.blog/changelog/2026-10-22-global-default-for-copilot-features-generally-available

In September, we announced a global default policy for generally available GitHub Copilot features and supported client capabilities on Copilot Business and Copilot Enterprise plans. Starting today, we’re gradually rolling...
The post Global default for Copilot features generally available appeared first on The GitHub Blog .

## Industry comparisons in the Copilot impact dashboard
- **Date**: Thu, 22 Oct 2026 16:28:24 +0000
- **URL**: https://github.blog/changelog/2026-10-22-industry-comparisons-in-the-copilot-impact-dashboard

The Copilot impact dashboard now includes an “Industry comparison” section. Enterprises, and organizations that aren’t owned by an enterprise, can compare their Copilot agentic adoption and leverage with aggregated benchmarks...
The post Industry comparisons in the Copilot impact dashboard appeared first on The GitHub Blog .

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
