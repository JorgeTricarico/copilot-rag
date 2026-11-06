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
