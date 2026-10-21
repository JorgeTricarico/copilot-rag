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
