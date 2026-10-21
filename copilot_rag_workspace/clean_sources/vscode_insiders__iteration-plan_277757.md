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
