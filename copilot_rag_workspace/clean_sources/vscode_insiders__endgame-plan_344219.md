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
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
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
