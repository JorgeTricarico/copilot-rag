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
