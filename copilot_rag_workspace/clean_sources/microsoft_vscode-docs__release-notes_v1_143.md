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
