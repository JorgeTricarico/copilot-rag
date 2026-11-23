# COMPENDIO RAG NOTEBOOKLM: 07_Release_Notes_And_Changelog_Radar
- **Generado (UTC)**: 2026-11-23T23:37:12.607569+00:00
- **Total Palabras**: 21,780 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_146.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_146
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_146.md
- **SHA256_FINGERPRINT**: `f4a0f4575cfa355f2fea25e3bfb4e605c5fdf565904eebdb3c6756243d07c231`
- **LAST_VERIFIED_UTC**: 2026-11-21T18:53:47.570173+00:00
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

VS Code supports virtual workspaces, allowing you to do things like [view a GitHub repository without having to clone it](https://code.visualstudio.com/docs/sourcecontrol/github#_github-repositories-extension).

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
- **SHA256_FINGERPRINT**: `98817e26b28ec56e52ffefa61bb09d044cf0324a9e299dd2992d63628d38cc08`
- **LAST_VERIFIED_UTC**: 2026-11-21T18:53:47.562044+00:00
---

**MetaDescription**: Learn what's new in Visual Studio Code 1.147

# Visual Studio Code 1.147

## Release highlights

Have a task in mind but not ready to send it? This week, save requests as drafts or schedule them for later. When you're ready, let a model router match the task to your preferred model. And when a result is easier to show than explain, ask for a chart or mockup.

* [Send later (Experimental)](#send-later-for-chat-requests-experimental): Schedule local agent requests and follow-ups for later in the Agents window.

* [Browser integration (Preview)](#browser-integration): Let agents control your default browser, and preview remote HTML files without copying them to your machine.

* [Draft requests (Experimental)](#save-and-resume-drafts-experimental): Keep multiple unsent requests with their context and configuration in the Agents window, ready to send when you are.

* [Customize assisted permissions](#more-context-for-assisted-permissions): Tell the permission reviewer which actions you consider safe and which should need your approval.

* [Visual chat responses](#html-previews-and-native-visuals-in-agent-responses): Review reports, mockups, and charts inline in the Agents window with HTML previews and experimental native visuals.

* [Model routers (Experimental)](#decision-model-based-model-routers-experimental): Let a model router choose from your preferred models for different tasks.

<br/>
Happy coding!

## Agent sessions

### Send Later for chat requests (Experimental)

**Setting**: ``sessions.sendLater.enabled`` (Agents window only)

Sometimes you want an agent to run a request after some time has passed. You might want to check a build after it finishes, or follow up on a review in the morning. With the Send Later feature, you can postpone sending a chat request until a specific time.

You can schedule a chat request by using the **Send Later** menu on the send button in chat.

![Screenshot showing the Send Later menu with preset times.](images/1_147/send-later-menu.webp)

For a specific time, select **Choose Date and Time**, pick a day in the calendar and a time from the dropdown, and select **Schedule**.

![Screenshot showing the Send Later date and time picker with a calendar, a time dropdown, and a Schedule button.](images/1_147/send-later-date-time.webp)

Where the request waits depends on where you scheduled it:

* **New session**: In the **Drafts** section of the sessions list.
* **Existing chat**: In that chat's **Scheduled** area, with its send time. If the agent is still busy at the scheduled time, the request waits its turn instead of interrupting.

![Screenshot showing a scheduled message in a chat, labeled with the date and time it will be sent.](images/1_147/send-later-scheduled-message.webp)

Alternatively, you can ask the agent to schedule a request for you by using plain language in the chat prompt, for example: `"Check the build in 10 minutes."`

The agent schedules a one-time, text-only request in the current chat and confirms when it will be sent. The request appears in the chat's **Scheduled** area, like one you scheduled from the menu.

![Screenshot showing an agent confirming a request to check the build in 10 minutes, with the follow-up listed in the chat's Scheduled area.](images/1_147/send-later-ask-agent.webp)

The local agent host must be running at the scheduled time. Scheduling doesn't wake a sleeping computer. A missed request is processed once the host is available again.

To manage your scheduled requests (edit, send immediately, reschedule, or cancel), use the options available when you hover over them in the chat or session list. To find sessions with pending requests, look for the clock indicator in the session list, or select **Scheduled Only** in the sessions filter menu.

Learn more about scheduling requests in the [Send Later documentation](https://code.visualstudio.com/docs/agents/run/agents-window#_send-a-request-later).

> **Note**: Scheduled requests work only for sessions on **This Computer** and require automations to be enabled (``chat.automations.enabled``).

### Save and resume drafts (Experimental)

**Setting**: ``sessions.drafts.enabled``

Previously, the new-session input held a single unsent request at a time. With drafts, you can keep several unsent requests side by side, each with its own workspace, agent, and configuration, and come back to any of them later.

When you leave a new session that has content, VS Code saves it to the **Drafts** section of the sessions list. Nothing is sent, and no agent session starts. To jump right back, select **Open Draft** in the notification.

![Screenshot showing the Drafts section in the sessions list with two saved drafts.](images/1_147/sessions-drafts.webp)

Each draft keeps everything you set up: text, attachments, inline references, workspace, agent, model, and other configuration. Drafts survive reloads and restarts.

From the Drafts list, you can preview, open, or delete a draft. When you send a draft, it's removed only after the request is accepted, so a failed send doesn't lose your work.

Turning off the setting hides the Drafts section but keeps your saved drafts.

### Share remote environments as GitHub Environments

Share a remote as a GitHub Environment to pick up its agent sessions from another device or supported Copilot app, using your GitHub account.

To share a connected SSH host, WSL distribution, or Dev Tunnel, open the Remote Environments editor in the Agents window and select **Share as GitHub Environment** (GitHub icon) on the remote's row.

A shared remote stays in its group and shows a GitHub icon after its name. Select the action again to stop sharing.

![Screenshot showing the Remote Environments editor with the Share Build Server as GitHub Environment action on a connected SSH host, and a Dev Tunnel that is already shared.](images/1_147/remote-environments-share-github-environment.webp)

Learn more about [remote agent sessions](https://code.visualstudio.com/docs/agents/run/remote-agent-sessions).

### Keep chat sessions across Dev Container rebuilds (Experimental)

**Settings**: ``dev.containers.stateVolume.enabled``, ``chat.agentHost.devContainer.stateVolume.enabled``

Rebuilding a Dev Container used to remove the Copilot chat sessions stored inside it. When you enable these settings, VS Code stores the user and agent state of a new Dev Container on a Docker volume, preserving your chat sessions across rebuilds.

> **Important**: A container gets the volume only when it's created with the setting enabled, so rebuild once to start keeping your sessions.

### Inbox mode improvements (Experimental)

**Setting**: ``sessions.list.inboxEnabled``

Inbox mode groups your Agents window sessions by what needs your attention. You can switch to Inbox mode at any time with **Grouping > Inbox Mode** in the sessions list. The ``sessions.list.inboxEnabled`` setting makes it the default grouping.

This release builds on your feedback to make Inbox mode more useful and manageable:

* **Acknowledge sessions you've handled**

    If a session doesn't need your attention but isn't finished, you can mark it as acknowledged (eye icon). Acknowledging a session moves it out of the Inbox and into the **Acknowledged** section. The session isn't marked as read or done, archived, or closed.

    When there is new activity in the session, it returns to the Inbox. You can acknowledge several selected sessions at once.

* **Focus on one workspace or environment**

    Use the workspace and environment pickers at the top of the sessions list to see only the sessions you care about right now. The filter applies to every section, including pinned and archived sessions, and is remembered across reloads.

    ![Screenshot showing Inbox mode with workspace and environment pickers above the Pinned and Inbox sections.](images/1_147/sessions-inbox-scope.webp)

## Agent experience

### Decision model-based model routers (Experimental)

**Setting**: `chat.copilot.modelRouter.enabled`

With a model router, you describe which model you want for which kind of work. A decision model, `gpt-6-luna-decisions`, then matches your request to one of your routes, and VS Code runs the chat on that route's model. A router is a YAML file in `~/.agents/model-routers/` that appears in the model picker in [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses#_copilot) sessions.

Model routers are at an early stage, and your feedback will help shape them. Tell us what works and what doesn't by [filing an issue](https://github.com/microsoft/vscode/issues).

```yaml
version: 1
description: Opus to build, GPT-6 Luna for quick questions.
routes:
  - model: opus
    when: Building or changing code over many steps, such as a feature, a bug fix, or a refactor.
  - model: gpt-6-luna
    when: Quick answers and small chores, such as where something is or what a setting does.
```

To try model routers, add `"chat.copilot.modelRouter.enabled": true` to your user [`settings.json`](https://code.visualstudio.com/docs/configure/settings#_settings-json-file) file.

To author a router, type `/model-router` in a Copilot harness chat and describe how you want your requests routed. Then select the router in the model picker.

### Model comparison improvements (Preview)

[Model comparison](https://code.visualstudio.com/docs/agents/run/compare-models) lets you run the same prompt across models in the Agents window, so you can review, judge, and combine their results. This release makes comparisons easier to find and understand:

* **Comparisons stay with their chat**: When you [ask an agent to run a comparison](https://code.visualstudio.com/docs/agents/run/compare-models#_ask-an-agent-to-run-a-comparison), it appears beneath that chat in the sessions list. The agent's response includes an **Open Comparison** action to go straight to the results.

* **See how a comparison was set up**: Hover over a comparison in the sessions list to see its original settings: repository, isolation, base branch, each attempt's model and effort level, judge, and synthesizer. You no longer need to open each attempt to check.

    ![Screenshot showing the Original comparison settings hover over a comparison in the sessions list, listing the repository, isolation, base branch, four attempts, judge, and synthesizer.](images/1_147/compare-models-settings-hover.webp)

### HTML previews and native visuals in agent responses

**Settings**: ``chat.htmlPreview.enabled``, ``chat.nativeComponents.enabled`` (Agents window only)

Some agent responses are easier to review as a visual or a chart than as text, such as a comparison of approaches, a mockup, or build times before and after a change. In the [Agents window](https://code.visualstudio.com/docs/agents/run/agents-window), agents can show these inline in the response in two ways. Each has its own setting, which is off by default.

* **HTML previews**: For free-form layouts, such as reports, diagrams, and mockups. Previews display HTML, CSS, tables, inline SVG, and expandable sections. Scripts, forms, external links, and external resources aren't supported. Enable ``chat.htmlPreview.enabled`` and use the built-in `/html-preview` [skill](https://code.visualstudio.com/docs/agent-customization/agent-skills) in your request, for example `/html-preview compare the two caching approaches`.

* **Native visuals (Experimental)**: For data, such as key numbers and comparisons. Agents can show metrics, badges, tables, bar charts, and expandable details that VS Code renders itself, so they match your theme, including high-contrast themes. Enable ``chat.nativeComponents.enabled`` and use the built-in `/vscode-ui` skill in your request, for example `/vscode-ui compare the full and incremental build times`.

<video src="images/1_147/html-preview-native-visuals.mp4" title="Video showing agent responses in the Agents window: an inline HTML preview with three mockups, native visuals with metrics, a bar chart, and a table, and an HTML preview of a chart with hover details." autoplay loop controls muted></video>

Both appear as part of the response, without a title bar or permanent buttons. Right-click a preview or visual and select **Show Source** to see its markup. For an HTML preview, you can also select **Open Preview** for a larger view or **Save HTML** to export a self-contained HTML file.

### Automations

Automations allow you to define tasks that run automatically based on specific triggers and conditions. You can create, manage, and monitor automations from the Automations view in the Agents window. This release adds guided setup, end dates, and filters for automation runs:

* **Agent-guided automation creation**

    Creating an automation with an agent is now a more guided experience. The agent helps you define what a successful result looks like, decide when the automation runs, and choose where it runs. To start, ask an agent to create an automation. You can also select **Create with Agent** in the Automations view to continue in chat.

    If you prefer configuring everything yourself, open the dropdown next to **Create with Agent** and select **Create Manually**.

* **Set an end date for automations**

    Automations can stop automatically after a specified duration. Set an end date when creating an automation with an agent, or choose **Days**, **Weeks**, or **Months** under **Advanced Settings** in the manual configuration form. Select **Never** to remove an existing end date.

* **Filter automation runs in session lists**

    Automation runs are hidden from session lists by default. Use the **Automations** filter to include or exclude them in the Agents window and the editor Chat sessions list.

### More context for assisted permissions

**Setting**: ``chat.permissions.assisted.instructions``

With [assisted permissions](https://code.visualstudio.com/docs/agents/run/approvals#_permission-levels), an LLM reviewer assesses each tool call in Copilot harness sessions and approves low-risk calls for you. Previously, the reviewer relied only on its default guidance, so it couldn't account for what you consider safe or risky in your own work.

Use ``chat.permissions.assisted.instructions`` to give the LLM reviewer your own instructions, for example:

```text
Always ask before installing packages or pushing to a remote.
Running tests and read-only Git commands doesn't need my approval.
```

Your instructions take precedence over the reviewer's default guidance. Changes to the setting apply to sessions that are already open. They can't override permission rules, organization policy, or the sandbox, and they aren't sent to the agent.

The reviewer also takes into account who asked for the work:

* **Automations and other agents**: Requests that an [automation](https://code.visualstudio.com/docs/agents/run/automations) starts or that another agent sends are no longer treated as if you wrote them. In these sessions, tool calls might ask for approval where they previously didn't.

* **Your answers**: Your answers to an agent's questions and plan reviews count, including when you decline. An approval can cover later work that your answer describes, and a refusal can block an action that was approved before.

### Arrange the Details panel around the editor (Experimental)

**Settings**: ``sessions.experimental.detailsPosition``, ``sessions.experimental.floatingDetails`` (Agents window only)

In the Agents window, you can position Files, Changes, and other Details views around the editor to make better use of the available space. Open **View > Appearance > Details Position** and choose **Left**, **Right**, **Above Editor**, **Below Editor**, or **Floating**. **Right** is the default.

Floating Details overlays the editor instead of reserving space. Hover over or focus the widget to preview its contents, then select the pin control to keep it open. You can also drag and resize it.

<video src="images/1_147/details-position.mp4" title="Video showing floating and docked Details views in the Agents window." autoplay loop controls muted></video>

### View extension info

The Extensions section of Customizations shows the same detailed information about each installed extension, including its version, publisher, and available commands, as you can find in the Extensions view in the editor window.

![Screenshot of the GitHub Pull Requests extension in the Extensions section of Customizations.](images/1_147/customizations-extensions.webp)

## Chat

### Attach screenshots of other apps (Experimental)

**Setting**: ``chat.appWindowScreenshots.enabled``

Give the agent a view of the app you're building, even when it runs in another application. Select **Add Context** > **Screenshot App Window** and choose a window, such as a browser or simulator.

You can also press ``Shortcut: workbench.action.chat.attachAppWindowScreenshot`` while another app is in the foreground to capture its window and attach it to the chat. From VS Code, the shortcut captures the app window you just left. You can mark up the image before sending.

<video src="images/1_147/app-screenshots-demo.mp4" title="Video showing screenshots from other apps being added to chat." autoplay loop controls muted></video>

### Capture and mark up images in chat

Select **Mark Up** on any image attachment in the chat input to crop it, draw arrows or shapes, or add text before sending. This works with screenshots, pasted images, and images attached from files, so you can point out a layout problem or highlight the part you want changed.

### Inline chat attachment pills (Experimental)

**Setting**: ``chat.inlineAttachments.enabled``

[Inline chat attachments](https://code.visualstudio.com/updates/v1_145#_inline-chat-attachments-experimental) show files, images, and other context as pills at the position where you added them in your prompt, so references stay next to the instructions they belong to. Recent updates make the pills more useful in the chat input and in sent requests:

* **Preview and open GitHub references**: Hover over or focus a GitHub issue or pull request pill to see its title, status, and description. Select the pill to open the issue or pull request. In sent requests, where selecting a pill previously did nothing, this also works when inline attachments are off.

* **Rearrange pills by dragging**: Drag a pill to a new position in the same chat input, rather than removing the context and attaching it again.

* **Clearer sent requests**: Sent requests show attached images as thumbnails above the text, in addition to the inline pills. Pills and slash commands line up with the surrounding text. Image and GitHub pills are restored after you reload the window, instead of appearing as plain links.

![Screenshot showing an image pill and two file pills inline with the prompt text in the chat input, each next to the instruction it belongs to.](images/1_147/chat-inline-attachments.webp)

Inline attachments are enabled by default in Insiders and off by default in Stable.

## MCP

### Skills over MCP

[Skills over MCP](https://github.com/modelcontextprotocol/ext-skills) (SEP-2640) is now enabled by default, allowing MCP servers to automatically provide skills to the model.

The first time you connect to an MCP server that provides skills, you are asked to allow them into your model context. Afterwards, the model can interact with these skills and you can see them on the **Skills** tab of the Agent Customizations editor.

You can opt out of skills over MCP by disabling the ``chat.agentHost.mcpSkills.enabled`` setting.

## Browser integration

### Let agents use your browser with browser use (Preview)

**Setting**: ``chat.agentHost.browserUse.enabled``

Browser Use lets agents interact directly with your default browser (Google Chrome or Microsoft Edge). This complements VS Code's integrated browser, for example by allowing agents to reuse existing authenticated sessions and interact with web pages outside of VS Code.

Browser Use requires the [GitHub Copilot browser extension](https://chromewebstore.google.com/detail/github-copilot/hblomdgalaelcilcdepgohfcogjiijhe), a [Copilot harness](https://code.visualstudio.com/docs/agents/run/agent-harnesses) session that runs on your own machine, and Node.js 22 or later on your `PATH`.

To get started with Browser Use:

1. Enable the ``chat.agentHost.browserUse.enabled`` setting and restart VS Code.
1. Open a local Copilot session and enter `/plugin enable browser-use` to enable the browser-use plugin.
1. Ask Copilot to perform a browser task, for example: `Open my app at localhost:3000, check the navigation, and capture a screenshot.`
1. Approve site access when prompted; complete sign-in and sensitive steps yourself.
1. Run `/browser-use:doctor` and follow its guidance to check your setup in case of any issues.

### Preview remote HTML files in the integrated browser (Preview)

**Setting**: ``workbench.browser.enableRemoteProxy``

You can now open HTML files from a remote workspace, such as SSH, WSL, or a Dev Container, in the [integrated browser](https://code.visualstudio.com/docs/debugtest/integrated-browser), just like [local HTML files](https://code.visualstudio.com/updates/v1_134#_open-html-files-in-the-integrated-browser-by-default). In the Explorer, right-click an HTML file and select **Open in Integrated Browser**. The page keeps its `file://` address, and the file and the resources it references, such as scripts, styles, images, and fonts, load from the remote workspace. Remote files only load from folders you trust.

This also works in the Agents window for sessions on a [remote agent host](https://code.visualstudio.com/docs/agents/run/remote-agent-sessions), so you and the agent can preview a page the agent wrote without copying it to your machine.

Enable ``workbench.browser.enableRemoteProxy`` to try it out, and file any issues you encounter in the [VS Code repository](https://github.com/microsoft/vscode/issues).

### Open non-localhost links in the integrated browser

**Setting**: ``workbench.externalUriOpeners``

Localhost links could already open in the integrated browser with ``workbench.browser.openLocalhostLinks``. The integrated browser is now listed as an opener in the ``workbench.externalUriOpeners`` setting, so you can choose it for other links instead of using the default browser. For example, to open links to your company's sites in the integrated browser:

```json
"workbench.externalUriOpeners": {
  "*.contoso.com": "workbench.integratedBrowser"
}
```

Use `*` as the pattern to open every link there instead.

### Turn off dimming in the integrated browser

**Setting**: ``workbench.browser.dimOnOverlay``

When something overlaps the integrated browser, such as a tab hover or a tooltip, the page pauses and dims. As hovers come and go, the page repeatedly darkens and returns to normal, which might appear as flicker and be uncomfortable for users who are sensitive to it.

You can now disable ``workbench.browser.dimOnOverlay`` to keep the page undimmed while it's paused. Notifications still dim the page.

## Sandboxing

### Retry with updated permissions inside the sandbox

If a terminal command fails because it can't access a file or folder, you can grant access at the session, workspace, or user level. With [sandbox bypass](https://code.visualstudio.com/docs/agents/run/agent-sandboxing#_control-approval-and-fallback-behavior) enabled, Copilot can use that permission to retry the command inside the sandbox instead of asking to run it outside.

<video src="images/1_147/sandboxing.mp4" title="Video showing file access approval and a command retry inside the sandbox." autoplay loop controls muted></video>

Use the approval dropdown to choose where the permission applies:

* **Allow for This Session** (default): Applies to all chats in this session, even after you resume it.
* **Allow for This Workspace** (when available): Applies to sessions with the same workspace folders on the same Agent Host. The host saves the permission without changing your workspace settings.
* **Allow for This User**: Saves the permission in your User settings so it applies across sessions and workspaces.

The command retries inside the sandbox. None of these options grants permission to run outside it.

## Accessibility

### Clearer focus and session attention

In high-contrast themes, Agents window controls now use a dashed outline for pointer hover and a solid outline for keyboard focus and open or expanded states. This makes it easier to follow your focus when navigating.

Sessions that need input are also easier to spot: light themes use a clearer amber indicator, and high-contrast themes show a marker at the left edge of the session row. You can customize the color with `agentSessionNeedsInput.foreground` in ``workbench.colorCustomizations``.

![Screenshot showing needs-input markers on session rows in high-contrast dark and light themes.](images/1_147/session-needs-input-high-contrast.webp)

## Editor Experience

### Customize panel corners and spacing

**Setting**: ``workbench.sizeCustomizations``

Customize panel corners and spacing in the editor window and in Agents windows with the Modern UI enabled. Set corner radii in whole pixels from 0 to 8 and spacing from 0 to 16. For example, you can use square panel corners, add space between panels, and give agent chat panels their own corners:

```json
{
  "workbench.sizeCustomizations": {
    "panels.cornerRadius": 0,
    "panels.spacing": 12,
    "agentsWindow.chatPanels.cornerRadius": 4
  }
}
```

<video src="images/1_147/size-customizations.mp4" title="Video showing size customizations in the Editor window." autoplay loop controls muted></video>

Compact layouts remain gapless, and the setting doesn't change controls, individual tabs, or native window corners.

### Connected panel tabs (Experimental)

With the Modern UI enabled, the connected tab style now extends from editor tabs to horizontal panel and side bar tabs. Selected views visually connect to their content, including when the Activity Bar is at the top or bottom. Choose `connected` (the default) or `pill` with ``workbench.experimental.modernUIEditorTabStyle``. The default vertical Activity Bar is unchanged.

![Screenshot showing connected tabs extending from editor tabs to horizontal panel and side bar tabs.](images/1_147/connected-panel-tabs.webp)

### Edit Markdown tables cell by cell

Editing a Markdown table in the source means keeping pipes and separator rows intact by hand. In the Markdown editor, tables stay rendered while you edit them, and you edit one cell at a time.

![Screenshot of a Markdown table in the Markdown editor, with the cursor in a cell that shows its bold syntax while you edit it.](images/1_147/markdown-editor-table-editing.webp)

### Collapsible details sections in the Markdown editor

Long documents often hide optional content in `` sections. The Markdown editor now renders `` and `<summary>` as collapsible sections, like GitHub does. Sections with the `open` attribute start expanded, and other sections start collapsed.

![Screenshot of the Markdown editor showing an expanded details section with its source tags and pin, and a collapsed section below it.](images/1_147/markdown-editor-details-sections.webp)

## Enterprise

### Permit Claude and Codex alongside managed settings

Previously, any Copilot [enterprise-managed setting](https://code.visualstudio.com/docs/enterprise/manage-ai-settings) disabled the Claude and Codex [harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses), because they don't enforce those settings. An organization couldn't govern Copilot and still offer Claude or Codex to its developers.

Administrators can now permit one or both harnesses by listing them in `vscode.allowedHarnesses`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "vscode": {
    "allowedHarnesses": ["claude", "codex"]
  }
}
```

![Screenshot showing a managed settings file that lists claude and codex in allowedHarnesses, next to the harness picker offering Claude and Codex below Copilot and Local.](images/1_147/allowed-harnesses.webp)

* The list permits the harnesses it names and blocks the others, so an empty list blocks both. Without the setting, managed settings disable both harnesses, as before.
* Valid entries are `claude` and `codex`, in lowercase. Other entries are ignored.
* Permitting a harness only lifts this restriction. Other controls still apply, such as `vscode.temporaryAllowLocalHarness: false`.
* Set it in file-based or MDM-managed settings. Server-managed settings don't support it yet.

> **Note:** Permitting a harness doesn't make it enforce your managed settings. Claude and Codex sessions run without Copilot's managed permission, sandbox, MCP, and plugin controls.

### Regular expressions in managed shell permission rules

Previously, managed shell permission rules matched only exact text or `*` wildcards, so a single rule couldn't cover alternatives or word boundaries. In Copilot harness sessions, `Shell(...)`, `Bash(...)`, and `PowerShell(...)` rules in [enterprise-managed settings](https://code.visualstudio.com/docs/enterprise/manage-ai-settings) accept a JavaScript regular expression written as `/pattern/flags` in `permissions.deny`, `permissions.ask`, and `permissions.allow`.

For example, require approval for commands that start with `git push` or `git pull`:

```json
{
  "permissions": {
    "ask": ["Shell(/^git\\s+(push|pull)\\b/)"]
  }
}
```

## Contributions to extensions

### GitHub Pull Requests

There has been more progress on the [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension, which enables you to work on, create, and manage pull requests and issues. New features include:

* When GitHub Actions workflows are waiting for a maintainer's approval, such as for a pull request from a first-time contributor, the checks section of the pull request overview has an **Approve workflows to run** button.

* Comments and other timeline items in the pull request overview use the full width once they're below the sidebar, and the overview switches to a single column below 1000px wide instead of 768px.

* In the Agents window, the pull request overview can be split into **Timeline**, **Checks/Merge**, and **Metadata** tabs with the experimental setting `"githubPullRequests.experimental.agentsOverviewTabs"`. The Timeline tab shows the number of unresolved conversations, and the Checks/Merge tab shows whether the pull request is ready to merge.

Review the [changelog for the 0.180.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01800) release of the extension to learn about everything in the release.

## Deprecated features and settings

### New deprecations in this release

* VS Code desktop on **macOS Ventura** and **macOS Sonoma** is deprecated. For details, see the [VS Code FAQ](https://code.visualstudio.com/docs/supporting/faq#_can-i-run-vs-code-on-old-macos-versions).

* VS Code desktop on **32-bit ARM Linux** is deprecated. For details, see the [VS Code FAQ](https://code.visualstudio.com/docs/supporting/faq#_can-i-run-vs-code-on-32-bit-arm-linux).

* The experimental AI usage statistics in the Status Bar (`editor.aiStats.enabled`) are removed because of low usage.

### Upcoming deprecations

* [The Local harness is deprecated](https://code.visualstudio.com/updates/v1_146#_copilot-harness-and-deprecation-of-the-local-harness) and will be removed in February 2027.

## Thank you

### Issue tracking

Contributions to our issue tracking:

* [@gjsjohnmurray (John Murray)](https://github.com/gjsjohnmurray)
* [@RedCMD (RedCMD)](https://github.com/RedCMD)
* [@IllusionMH (Andrii Dieiev)](https://github.com/IllusionMH)
* [@albertosantini (Alberto Santini)](https://github.com/albertosantini)

### Pull requests

Contributions to `vscode`:

* [@AAAkater](https://github.com/AAAkater): agentHost: fix incorrect model attribution in Codex subagent responses [PR #340470](https://github.com/microsoft/vscode/pull/340470)
* [@Aryan9891 (Aryan Sachin)](https://github.com/Aryan9891): fix(terminal): support multiple action view items for create terminal dropdown (#346848) [PR #346854](https://github.com/microsoft/vscode/pull/346854)
* [@Boulea7 (Langning Zhang)](https://github.com/Boulea7): Fix PWA manifest start URL for server base paths [PR #330360](https://github.com/microsoft/vscode/pull/330360)
* [@DivyaRaval1909 (Divya Raval)](https://github.com/DivyaRaval1909): Hide action list item icon and submenu indicator from screen readers [PR #339952](https://github.com/microsoft/vscode/pull/339952)
* [@Iyanuoluwa007 (Oke Iyanuoluwa Enoch)](https://github.com/Iyanuoluwa007): Report problems of pending lines when a task problem collector is done [PR #346122](https://github.com/microsoft/vscode/pull/346122)
* [@mcumming (Michael Cummings (MSFT))](https://github.com/mcumming): Never send Entra sign-in tokens to the marketplace [PR #343689](https://github.com/microsoft/vscode/pull/343689)
* [@NeoMetric](https://github.com/NeoMetric): agentHost: stream BYOK model output as it is produced [PR #341851](https://github.com/microsoft/vscode/pull/341851)
* [@rudy-07 (Rudransh Shekhar)](https://github.com/rudy-07): terminal-suggest: fix root directory check in npm and yarn package.json lookup [PR #347265](https://github.com/microsoft/vscode/pull/347265)
* [@sameerihs (Sameer)](https://github.com/sameerihs)
  * Reset notebook controller language restrictions [PR #347068](https://github.com/microsoft/vscode/pull/347068)
  * Clean up obsolete webview resource caches [PR #346867](https://github.com/microsoft/vscode/pull/346867)
  * Use pending URLs when restoring browser tabs [PR #346996](https://github.com/microsoft/vscode/pull/346996)
  * Invalidate cached TS responses after document reopen [PR #347028](https://github.com/microsoft/vscode/pull/347028)
  * Keep the latest debugger source refresh [PR #347124](https://github.com/microsoft/vscode/pull/347124)
  * Track forwarded tunnel connections by socket [PR #347033](https://github.com/microsoft/vscode/pull/347033)
  * Keep task problem markers scoped to each terminal [PR #346994](https://github.com/microsoft/vscode/pull/346994)
  * Isolate copied notebook output items [PR #347117](https://github.com/microsoft/vscode/pull/347117)
  * Cancel stale format-on-type requests [PR #347115](https://github.com/microsoft/vscode/pull/347115)
  * Keep configuration retries on their original file [PR #347074](https://github.com/microsoft/vscode/pull/347074)
  * Keep in-memory working copy backups distinct [PR #347066](https://github.com/microsoft/vscode/pull/347066)
  * Serialize rapid virtual document refreshes [PR #346986](https://github.com/microsoft/vscode/pull/346986)
  * Clear buffered results before a new Quick Search [PR #347031](https://github.com/microsoft/vscode/pull/347031)
* [@ShakilUrRehman21 (SHAKIL UR REHMAN)](https://github.com/ShakilUrRehman21): map: preserve custom toKey and re-key on ResourceMap copy [PR #347344](https://github.com/microsoft/vscode/pull/347344)
* [@shoutoutuoadi325 (Zhiqi Zhang)](https://github.com/shoutoutuoadi325): Fix UTF-16 column counts in TextLength [PR #345715](https://github.com/microsoft/vscode/pull/345715)
* [@SimonSiefke (Simon Siefke)](https://github.com/SimonSiefke)
  * fix: memory leak in word highlighter [PR #346673](https://github.com/microsoft/vscode/pull/346673)
  * fix: memory leak in task providers [PR #338231](https://github.com/microsoft/vscode/pull/338231)
  * fix: memory leak in untitled editor resolution [PR #346674](https://github.com/microsoft/vscode/pull/346674)
  * perf: avoid rescanning test children in Test Explorer [PR #347176](https://github.com/microsoft/vscode/pull/347176)
  * perf: batch Test Explorer test run updates [PR #346656](https://github.com/microsoft/vscode/pull/346656)
  * fix: memory leak in test results terminal [PR #347183](https://github.com/microsoft/vscode/pull/347183)
  * feature: reduce idle CPU usage by up to 75% [PR #338767](https://github.com/microsoft/vscode/pull/338767)
  * fix: race condition in notebook kernel picker [PR #341483](https://github.com/microsoft/vscode/pull/341483)
  * fix: memory leak in SCM repository context keys [PR #346683](https://github.com/microsoft/vscode/pull/346683)
  * fix: memory leak in emitter warning names [PR #347966](https://github.com/microsoft/vscode/pull/347966)
  * perf: reduce memory usage by 44 kB [PR #342392](https://github.com/microsoft/vscode/pull/342392)
  * fix: memory leak in markersView [PR #348007](https://github.com/microsoft/vscode/pull/348007)
* [@trivikr (Trivikram Kamat)](https://github.com/trivikr): Add --hidden-window to run extension tests without showing a window [PR #344174](https://github.com/microsoft/vscode/pull/344174)
* [@wasim-builds (MOHAMMED WASIM KHAN)](https://github.com/wasim-builds): fix: prevent DisposableStore leak per tree node in ExtHostTreeView (#346620) [PR #346727](https://github.com/microsoft/vscode/pull/346727)
* [@wozhenbang2004 (Kayokoi)](https://github.com/wozhenbang2004): Fix authentication provider cleanup when an extension host stops [PR #345127](https://github.com/microsoft/vscode/pull/345127)
* [@wynnsimon (wynn)](https://github.com/wynnsimon): fix: Fix findWithArgs ignoring empty search strings (#151311) [PR #334803](https://github.com/microsoft/vscode/pull/334803)
* [@YOSHII-Hiroto (吉井 啓人(YOSHII, Hiroto))](https://github.com/YOSHII-Hiroto): Fix element picker with mobile emulation [PR #332183](https://github.com/microsoft/vscode/pull/332183)

Contributions to `vscode-pull-request-github`:

* [@hungud (Uong Dong Hung)](https://github.com/hungud): fix: handle null review comment commit in parseGraphQLComment (fixes #9159) [PR #9168](https://github.com/microsoft/vscode-pull-request-github/pull/9168)

---

We really appreciate people trying our new features as soon as they are ready, so check back here often and learn what's new.

>If you'd like to read release notes for previous VS Code versions, go to [Updates](https://code.visualstudio.com/updates) on [code.visualstudio.com](https://code.visualstudio.com).

<a id="scroll-to-top" role="button" title="Scroll to top" aria-label="scroll to top" href="#"><span class="icon"></span></a>
<link rel="stylesheet" type="text/css" href="css/inproduct_releasenotes.css"/>


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::release-notes/v1_148.md
- **CANONICAL_URL**: https://code.visualstudio.com/updates/v1_148
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_148.md
- **SHA256_FINGERPRINT**: `73caa09149dbf845835be68440e0bf6e9bef8f0ef730659036357e07e89611c0`
- **LAST_VERIFIED_UTC**: 2026-11-23T23:37:07.009112+00:00
---

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
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_348483
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/348483
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/348483
- **SHA256_FINGERPRINT**: `6155adabb15d02aa0bcbf4a9612b44b7acb202c76ad87acd77034fe946b5db2b`
- **LAST_VERIFIED_UTC**: 2026-11-23T23:37:12.473169+00:00
---

# VS Code Insiders Roadmap: 1.147.0 Endgame
- **Issue Number**: #348483
- **Category**: `endgame-plan`
- **State**: closed
- **Source Issue**: https://github.com/microsoft/vscode/issues/348483

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
    - [x] Version bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/348492
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): https://github.com/microsoft/vscode/pull/348491

  - If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).
- [x] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.147.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.147.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
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
- [x] If this is not Patch Tuesday only:
  - [x] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [x] Build stable from release/<x.y> and release to MSFT folks
  - [x] Reenable automatic releases
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
# DOCUMENT_SOURCE: vscode_insiders::endgame-plan_349753
- **CANONICAL_URL**: https://github.com/microsoft/vscode/issues/349753
- **RAW_SOURCE_URL**: https://github.com/microsoft/vscode/issues/349753
- **SHA256_FINGERPRINT**: `033ae8708f7619b53b9f08c80995e7fd4953bf739a94badc35aa13c7f93a9ffd`
- **LAST_VERIFIED_UTC**: 2026-11-23T23:37:12.472584+00:00
---

# VS Code Insiders Roadmap: 1.148.0 Endgame
- **Issue Number**: #349753
- **Category**: `endgame-plan`
- **State**: open
- **Source Issue**: https://github.com/microsoft/vscode/issues/349753

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
- [x] Run the [Start Endgame](https://dev.azure.com/monacotools/Monaco/_build?definitionId=730) pipeline. It replaces the workflow below, which can no longer sign in to Azure. It pushes the version bump and endgame notebook branches but doesn't open their PRs: open them from the links it adds under this task, enable auto-merge, and get them approved.

  - Open these PRs, enable auto-merge, and get them reviewed and merged Monday morning so Insiders picks up the next milestone version:
    - [x] Version bump (`microsoft/vscode`): [open the PR](https://github.com/microsoft/vscode/compare/main...automation/bump-version-1.149.0?quick_pull=1&title=Bump%20version%20to%201.149.0&body=Automated%20version%20bump%20after%20release%20branch%20creation.%0A%0A1.148.0%20%E2%86%92%201.149.0%20(copilot%200.76.0%20%E2%86%92%200.77.0)%0A%0A**How%20this%20bump%20was%20generated%3A**%0A-%20The%20edits%20of%20%60scripts%2Fvscode-version-bump%2Fbump-version-fields.ts%60%20in%20microsoft%2Fvscode-engineering%2C%20which%20only%20change%20the%20version%20values%0A%0ATriggered%20by%20%5Bpipeline%20run%5D(https%3A%2F%2Fdev.azure.com%2Fmonacotools%2FMonaco%2F_build%2Fresults%3FbuildId%3D502599))
    - [x] Endgame notebook milestone bump (`microsoft/vscode`): [open the PR](https://github.com/microsoft/vscode/compare/main...automation/update-endgame-notebooks-1.148?quick_pull=1&title=Update%20endgame%20notebook%20milestones%20to%201.148.0&body=Automated%20milestone%20update%20for%20endgame%20notebooks.%0A%0AUpdated%20milestone%20to%201.148.0%20in%3A%0A-%20%60.vscode%2Fnotebooks%2Fendgame.github-issues%60%0A-%20%60.vscode%2Fnotebooks%2Fmy-endgame.github-issues%60%0A%0ATriggered%20by%20%5Bpipeline%20run%5D(https%3A%2F%2Fdev.azure.com%2Fmonacotools%2FMonaco%2F_build%2Fresults%3FbuildId%3D502599))

- [ ] ~~Run the [Start Endgame](https://github.com/microsoft/vscode-engineering/actions/workflows/start-endgame.yml) workflow~~
  - ~~If you need to run these steps manually, see the [Branching guide](https://github.com/microsoft/vscode-internalbacklog/blob/main/guidelines/endgame-guide.md#branching).~~
- [x] In absence of the tech writer, follow the steps in the [website endgame issue](https://github.com/microsoft/vscode-website/wiki#performing-a-weekly-release)

# Monday morning (Redmond and Zurich)

`@team`:
- [Test plan items](https://github.com/issues?q=org%3Amicrosoft%20milestone%3A%221.148.0%22%20is%3Aissue%20is%3Aopen%20label%3Atestplan-item). All TPIs must be finished by noon. This includes verification TPIs.
- Make sure your TPIs are being tested and ping folks if to confirm they will finish by noon.

# Monday afternoon (Redmond and Zurich)

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

# Monday EOD Redmond time

`@team`:
- All issues including late fixes, are verified ([query](https://github.com/issues?q=org%3Amicrosoft+milestone%3A%221.148.0%22+is%3Aissue+is%3Aclosed+reason%3Acompleted++label%3Abug+-label%3Averified+-label%3Aon-testplan+-label%3A*duplicate+-label%3Aduplicate+-label%3Ainvalid+-label%3A*as-designed+-label%3Aerror-telemetry+-label%3Averification-steps-needed+-label%3Az-author-verified+-label%3Aunreleased+-label%3A*not-reproducible+-label%3A*out-of-scope+sort%3Aupdated-asc))
- Release notes written

`@endgame-champ`:
- [ ] Build and release Insiders from `release/<x.y>` branch so we can finish verification. ([Pipeline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))
- [ ] Build stable from `release/<x.y>` branch (do not release) so that the Zurich team would have a build to release given no candidates. ([Pipline Link](https://dev.azure.com/monacotools/Monaco/_build?definitionId=111))

# Tuesday by noon CET

`@team`:
- Fix essential issues. Default to pushing to next iteration
- Release notes

`@endgame-champ`:
- [ ] Generate "Thank you" section of the release notes in the `vnext` branch of the `vscode-docs` repo.
    - [ ] [Acknowledge third-party pull requests](https://tools.code.visualstudio.com/acknowledgement) in release notes.
    - [ ] Acknowledge [issue trackers](https://github.com/microsoft/vscode-internalbacklog/wiki/Community-Triage---Credits#community-triage---role-based) from the community (do the copy-paste variant) -
- [ ] If this is not Patch Tuesday only:
  - [ ] Build and release insiders from release/<x.y> (if there have been newer changes since last release)
  - [ ] Build stable from release/<x.y> and release to MSFT folks
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
- **SHA256_FINGERPRINT**: `92be5b3b64c24928c4b5570d787980d0f8e152fbab24bba88543b0f2dfb65ac2`
- **LAST_VERIFIED_UTC**: 2026-11-19T06:41:21.910391+00:00
---

# GitHub Copilot Official Changelog Feed

## Connect Supabase, Box, Calendly, and more to Copilot
- **Date**: Wed, 18 Nov 2026 22:04:50 +0000
- **URL**: https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot

You can now connect eight more services to Copilot using GitHub-verified MCP servers, or connectors, available in public preview. They join more than 25 services you can already connect, like...
The post Connect Supabase, Box, Calendly, and more to Copilot appeared first on The GitHub Blog .

## Gemini 4 Neon in GitHub Copilot
- **Date**: Wed, 18 Nov 2026 21:49:21 +0000
- **URL**: https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot

Gemini 4 Neon is now generally available in GitHub Copilot. It is designed for agentic coding, multistep tool use, and knowledge work. According to Google, Gemini 4 Neon delivers quality...
The post Gemini 4 Neon in GitHub Copilot appeared first on The GitHub Blog .

## Customize GitHub Copilot for your team
- **Date**: Wed, 18 Nov 2026 16:00:13 +0000
- **URL**: https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team

You can now share the GitHub Copilot plugins your team relies on without asking every member to repeat the same setup. Team customizations are generally available for organization teams. Team...
The post Customize GitHub Copilot for your team appeared first on The GitHub Blog .

## OpenAI’s GPT-6.2 Astra and GPT-6.2 Sol now available
- **Date**: Tue, 17 Nov 2026 20:20:29 +0000
- **URL**: https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available

OpenAI’s GPT-6.2 Astra and GPT-6.2 Sol are now generally available in GitHub Copilot. Both models are designed for agentic coding and code review, with stronger coding judgment than earlier GPT-6...
The post OpenAI’s GPT-6.2 Astra and GPT-6.2 Sol now available appeared first on The GitHub Blog .

## GitHub Copilot Fusion updates: more availability, benchmarks, and models
- **Date**: Tue, 17 Nov 2026 18:04:48 +0000
- **URL**: https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models

Today, we’re expanding GitHub Copilot Fusion with new models, available on more Copilot surfaces, and results on two public Terminal-Bench leaderboards, giving you more ways to use Fusion and compare...
The post GitHub Copilot Fusion updates: more availability, benchmarks, and models appeared first on The GitHub Blog .

## GitHub Copilot app, Microsoft Ignite releases
- **Date**: Tue, 17 Nov 2026 18:03:42 +0000
- **URL**: https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases

Copilot is most useful when it can work where you do. The GitHub Copilot app now supports your Azure DevOps repositories, your GitHub Enterprise Server instance, and the browser you’re...
The post GitHub Copilot app, Microsoft Ignite releases appeared first on The GitHub Blog .

## Copilot code review: Adaptive effort, secret detection, and more
- **Date**: Tue, 17 Nov 2026 18:02:05 +0000
- **URL**: https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more

GitHub Copilot code review now helps you catch more issues earlier, with less effort. Adaptive matches review depth to each pull request, so routine changes get a quick pass and...
The post Copilot code review: Adaptive effort, secret detection, and more appeared first on The GitHub Blog .

## MAI Code 2 and MAI Code 2 Flash in GitHub Copilot
- **Date**: Tue, 17 Nov 2026 18:01:45 +0000
- **URL**: https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot

The next generation of Microsoft AI (MAI) coding models has arrived in GitHub Copilot. Introducing MAI Code 2 and MAI Code 2 Flash, two new models that represent a major...
The post MAI Code 2 and MAI Code 2 Flash in GitHub Copilot appeared first on The GitHub Blog .

## GitHub Copilot in JetBrains, Ignite releases
- **Date**: Tue, 17 Nov 2026 18:00:59 +0000
- **URL**: https://github.blog/changelog/2026-11-17-github-copilot-in-jetbrains-ignite-releases

This update brings remote access, on-device voice dictation, and browser use controls to GitHub Copilot for JetBrains. Copilot users in JetBrains IDEs also get context usage shortcuts, historical diffs, simpler...
The post GitHub Copilot in JetBrains, Ignite releases appeared first on The GitHub Blog .

## Monitor GitHub Copilot activity through Microsoft Agent 365
- **Date**: Tue, 17 Nov 2026 18:00:59 +0000
- **URL**: https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365

Enterprises can now stream GitHub Copilot agent activity directly into Microsoft Agent 365. This lets you bring audit data from across GitHub Copilot clients into Microsoft’s agent control plane, where...
The post Monitor GitHub Copilot activity through Microsoft Agent 365 appeared first on The GitHub Blog .
