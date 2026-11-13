**MetaDescription**: Learn what is new in Visual Studio Code Insiders, including agent session management, chat resources, and Markdown editing.

# Visual Studio Code 1.147

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: November 13, 2026_

Welcome to the 1.147  release of Visual Studio Code.

Happy Coding!

---

## November 12, 2026

* Add an editor tab bar **+** menu for creating text files, Markdown documents, chats, and integrated browser tabs. _[#347849: Experimental new tab (+) button in the editor tab bar](https://github.com/microsoft/vscode/issues/347849)_
* Add actions for generating code, starting a chat, choosing a language, or reopening an untitled file in another editor. _[#347848: Experiment: show a list of actions in the hint of new untitled files](https://github.com/microsoft/vscode/issues/347848)_
* Name images pasted into chat after their source file when available. _[#347828: Chat: name pasted images after their source file](https://github.com/microsoft/vscode/issues/347828)_
* Start the Agents window's **Open Folder** dialog at the parent of the selected local folder to reduce navigation between sibling projects. _[#335652: Choose Folder: Make parent folder of current folder the starting point](https://github.com/microsoft/vscode/issues/335652)_
* Use toolbar menus to filter and sort worktrees in the Agents window's cleanup editor. _[#347138: Controls area for worktree cleanup could use some design love](https://github.com/microsoft/vscode/issues/347138)_
* Show minimap section headers for single-line `#region` comments in HTML and CSS files. _[#210637: Minimap section headers are not shown for regions in HTML and CSS](https://github.com/microsoft/vscode/issues/210637)_
* Add the proposed `contribTitleBar` API for contributing buttons to editor and Agents window title bars during [local extension development](https://code.visualstudio.com/api/advanced-topics/using-proposed-api). _[#347839: Proposed API: let extensions contribute buttons to the title bar of the editor and Agents windows](https://github.com/microsoft/vscode/issues/347839)_
* Remove the experimental **AI Usage Statistics** Status Bar widget. _[#340001: Remove the AI Usage Statistics widget](https://github.com/microsoft/vscode/issues/340001)_

## November 11, 2026

* Share agent sessions between the Agents window and WSL, Remote - SSH, or Dev Container editor windows when both windows use the same agent host. _[#346859: Share agent host sessions between the Agents Window and WSL, SSH and Dev Container editor windows](https://github.com/microsoft/vscode/issues/346859)_
* Drag sessions between compatible inbox categories to pin, hold, clear, archive, or resume them (Experimental). _[#346934: Inbox mode: Sessions cannot be dragged between groups](https://github.com/microsoft/vscode/issues/346934)_
* Enable opening all web links in the integrated browser. _[#316528: Option to open all links in Integrated Browser](https://github.com/microsoft/vscode/issues/316528)_

## November 10, 2026

* Add an inline **Merge Pull Request** action for eligible sessions in inbox mode (Experimental). _[#346936: Inbox mode: Ready to Merge sessions have no inline Merge action](https://github.com/microsoft/vscode/issues/346936)_
* Hide empty categories in inbox mode (Experimental), while keeping **Inbox** visible. _[#346938: Inbox mode: Empty sections take up too much vertical space](https://github.com/microsoft/vscode/issues/346938)_
* Hover over a Compare Models (Preview) parent chat in the Agents window to see its original settings. _[#347109: Model compare: show original settings on hover of the parent chat](https://github.com/microsoft/vscode/issues/347109)_
* Shorten worktree cleanup confirmations while retaining the session restoration reminder. _[#347134: Worktree cleanup confirmation is unncessarily wordy](https://github.com/microsoft/vscode/issues/347134)_
* Add support for collapsible `` sections in the Markdown editor (Experimental). _[#347433: Markdown editor: render ``/`<summary>` as collapsible sections](https://github.com/microsoft/vscode/issues/347433)_
* Add support for viewing pinned chat files above the chat input (Experimental). _[#345427: Let extensions dock views above the chat input](https://github.com/microsoft/vscode/issues/345427)_
* Add context menu option to hide VS Code pet (Experimental). _[#346510: Remove option for vscode-pet](https://github.com/microsoft/vscode/issues/346510)_
* Filter inbox sessions by workspace and execution environment (Experimental). _[#347488: Add workspace and environment scope pickers to Inbox](https://github.com/microsoft/vscode/issues/347488)_

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>
