**MetaDescription**: Learn what is new in the latest Visual Studio Code Insiders build, including agent session management and editor tab improvements.

# Visual Studio Code 1.148

Follow us on [LinkedIn](https://www.linkedin.com/showcase/vs-code), [X](https://go.microsoft.com/fwlink/?LinkID=533687), [Bluesky](https://bsky.app/profile/vscode.dev), [Instagram](https://www.instagram.com/vscode)

---

_Last updated: November 23, 2026_

Welcome to the 1.148  release of Visual Studio Code.

Happy Coding!

---

## November 21, 2026

* Sign in to sites that use HTTP Basic authentication directly in the integrated browser. _[#300149: Integrated browser: Enable Http Basic Authentication](https://github.com/microsoft/vscode/issues/300149)_

* Enter text in `window.prompt()` dialogs in the integrated browser. _[#347876: Integrated browser: support window.prompt()](https://github.com/microsoft/vscode/issues/347876)_

## November 20, 2026

* In screen-reader mode, the Agents window opens Markdown files and diffs in the text editor by default (Experimental). _[#349533: Make Agents window Markdown editor defaults screen-reader-aware](https://github.com/microsoft/vscode/issues/349533)_

* In experimental **Inbox Mode**, set ``sessions.list.inboxAutoAdvance`` to `newSession` to focus the **New Session** chat input after replying. _[#349317: Inbox: Add an option to focus the New Session chat input after replying](https://github.com/microsoft/vscode/issues/349317)_

## November 19, 2026

* Use ``sessions.keepAwakeWhileWorking`` to prevent idle sleep while an agent works on a supported host (Preview). _[#348891: Agents window: keep the computer awake while a local agent is working](https://github.com/microsoft/vscode/issues/348891)_

* The first time experimental **Inbox Mode** advances after a reply, it highlights the session you replied to so you can return to it. _[#349307: Spotlight the replied-to session when Inbox automatically advances](https://github.com/microsoft/vscode/issues/349307)_

## November 17, 2026

* Stay in the current session after replying in experimental **Inbox Mode** by setting ``sessions.list.inboxAutoAdvance`` to `off`. _[#348715: Inbox: when I replied to a message in a session, the jump to the next session was jarring](https://github.com/microsoft/vscode/issues/348715)_

## November 16, 2026

* Experimental **Inbox Mode** shows session counts beside category labels and lets you collapse **Inbox**. _[#348711: Inbox headers need more intuitive state differences and move the location of count](https://github.com/microsoft/vscode/issues/348711)_

* Experimental **Inbox Mode** uses stronger headings and visible collapse arrows to distinguish session categories from conversations. _[#348709: It's hard to differentiate between headers (Working, on hold) with sessions](https://github.com/microsoft/vscode/issues/348709)_

* Experimental **Send Later** shows relative send times, such as 'Sends in 5 minutes', for scheduled messages and **Drafts** entries in the Agents window. _[#348622: Send Later: Show relative time until scheduled messages are sent](https://github.com/microsoft/vscode/issues/348622)_

* In the Agents window, the **Send** dropdown opens the scheduling time picker directly when experimental **Send Later** is the only secondary action. _[#348482: Single-entry menu: Send Later...](https://github.com/microsoft/vscode/issues/348482)_

* The experimental new tab (+) button opens tabs at the end of the group and highlights your last-used action in the menu. _[#348560: New tab button: open at the end, recent entry as default](https://github.com/microsoft/vscode/issues/348560)_

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>
