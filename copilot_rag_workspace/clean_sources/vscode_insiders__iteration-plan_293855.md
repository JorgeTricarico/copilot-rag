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
