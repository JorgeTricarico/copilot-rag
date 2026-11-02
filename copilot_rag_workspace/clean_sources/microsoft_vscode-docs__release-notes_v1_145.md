**MetaDescription**: Learn what is new in Visual Studio Code 1.145 (Insiders).

# Visual Studio Code 1.145

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: November 2, 2026_

Welcome to the 1.145  release of Visual Studio Code.

Happy Coding!

---

## November 2, 2026

* Add support for nesting Claude and Codex chats under a Copilot session in the Agents window. _[microsoft/vscode#343910: Why can't I nest a Claude/Codex session under a Copilot session?](https://github.com/microsoft/vscode/issues/343910)_

## October 31, 2026

* Keep sessions visible in the Agents window's **Worktree Cleanup** list after opening them for review with the default **Any time** filter. _[microsoft/vscode#342637: [Worktree Cleanup] Clicking on a session removed it from the list](https://github.com/microsoft/vscode/issues/342637)_

## October 30, 2026

* Add stable API support for extensions to contribute file, folder, and workspace history to the **Timeline** view. _[microsoft/vscode#84297: API support for Timeline view](https://github.com/microsoft/vscode/issues/84297)_

* Add support for `!`-prefixed exception patterns in ``files.exclude`` and ``search.exclude`` to restore excluded files and folders in the **Explorer** and built-in search. _[microsoft/vscode#869: Exclude all files except for...](https://github.com/microsoft/vscode/issues/869)_

* Round keyboard focus outlines on the **Dictation** and **Voice Mode** buttons (Experimental) in editor chat and the Agents window. _[microsoft/vscode#330524: Add corner rounding to dictation and voice mode buttons focus outline](https://github.com/microsoft/vscode/issues/330524)_

* Use Agents window without GitHub sign-in or an opt-in setting. Individual agents and models can still require credentials or setup. _[microsoft/vscode#345254: Agents window is usable without GitHub sign-in by default](https://github.com/microsoft/vscode/issues/345254)_

## October 29, 2026

* Add support for disabling Copilot's `Co-authored-by` commit trailer in new or resumed agent-host sessions with ``chat.agentHost.copilot.includeCoAuthoredBy`` set to `false`. _[microsoft/vscode#342213: Allow disabling Copilot's Co-authored-by trailer in agent-host sessions](https://github.com/microsoft/vscode/issues/342213)_

## October 28, 2026

* Track bulk worktree cleanup progress, keep completed results visible until the editor closes, and retry eligible failed cleanups in the Agents window. _[microsoft/vscode#344588: Improve bulk worktree cleanup progress and recovery](https://github.com/microsoft/vscode/issues/344588)_

* Hide space and tab indicators by default in the rich Markdown editor (``markdown.editor.renderWhitespace``). _[microsoft/vscode#344703: Markdown editor: hide whitespace indicators by default (markdown.editor.renderWhitespace)](https://github.com/microsoft/vscode/issues/344703)_

* Add support for calling tools provided by MCP Apps in Copilot agent-host sessions in the editor and Agents windows. _[microsoft/vscode#338336: MCP Apps: App-provided tools registered via App.registerTool() are not exposed to Copilot agent](https://github.com/microsoft/vscode/issues/338336)_

* Add setting to show breadcrumbs in untitled files. _[microsoft/vscode#344755: Add a setting to show breadcrumbs for untitled files, off by default](https://github.com/microsoft/vscode/issues/344755)_

* Add support for recording WebM demos of web pages with the experimental `/record-video` skill in Copilot CLI sessions. _[microsoft/vscode#344781: Add a built-in skill to record demo videos of web pages](https://github.com/microsoft/vscode/issues/344781)_

* Add support for cleaning up managed worktrees without a listed session in the Agents window's **Worktree Cleanup** editor. _[microsoft/vscode#344779: Allow Worktree Cleanup to manage worktrees without a listed session](https://github.com/microsoft/vscode/issues/344779)_

## October 27, 2026

* Preview web apps running on remote agent hosts in the Agents window's integrated browser (Experimental). _[microsoft/vscode#331926: Integrated browser remote proxy should support remote AHP hosts in Agents window](https://github.com/microsoft/vscode/issues/331926)_

* Fix keyboard access to MCP authentication prompts in agent-host sessions when screen reader mode is enabled. _[microsoft/vscode#343890: MCP authentication inline hint is not keyboard accessible in screen reader mode](https://github.com/microsoft/vscode/issues/343890)_

* Move the default **Agent** picker into **Add Context** in editor-window chat with the experimental ``sessions.chat.experimental.agentsPickerInAttachContextMenu`` setting. _[microsoft/vscode#344606: Apply the Agent picker Add Context setting to editor-window chat](https://github.com/microsoft/vscode/issues/344606)_

* Add support for breadcrumbs in untitled files when ``breadcrumbs.showInUntitledFiles`` is enabled and the language provides symbols. _[microsoft/vscode#84746: Enable breadcrumbs for unsaved files](https://github.com/microsoft/vscode/issues/84746)_

* Run saved automations with **Chat: Run Automation...** in the Agents window **Command Palette**. _[microsoft/vscode#344445: Add a "Chat: Run Automation..." action](https://github.com/microsoft/vscode/issues/344445)_

## October 26, 2026

* Open sessions in an editor instead of the **Chat** view by enabling the experimental ``chat.agentSessions.openInEditor`` setting. _[microsoft/vscode#336136: Allow configuring the default click action for Chat Sessions](https://github.com/microsoft/vscode/issues/336136)_

* Show size estimates faster for unchanged idle sessions when reopening or refreshing **Worktree Cleanup** in the Agents window. _[microsoft/vscode#344370: Persist session worktree sizes for Worktree Cleanup](https://github.com/microsoft/vscode/issues/344370)_

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>
