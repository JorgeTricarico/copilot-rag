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
- [ ] Publish website so that in-product release notes are ready
- [ ] Start Stable rollout to everyone (start percentage: `20%`, end time UTC: `6AM next Wednesday`)
- [ ] Deploy vscode.dev
  - [x] Verify the [release candidate](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) `release/x.y` passed the sanity tests in the last step
  - [ ] [Kick off deploy](https://dev.azure.com/monacotools/Monaco/_build?definitionId=276) (Branch `release/x.y`, Deployment Target `prod`, needs peer approval)
- [ ] [Publish @vscode/chat-lib](https://dev.azure.com/monacotools/Monaco/_build?definitionId=683) (Branch `release/x.y`, Release Version `auto`; the release pipeline job requires two approvals)
- [ ] Publish socials (ping Cynthia)
- [x] [Publish @types/vscode](https://github.com/microsoft/vscode/wiki/Publish-vscode-types) if you find type diffs after running the steps
- [ ] Create an official release
  - [ ] Create a tag (make sure you pull the release branch first): `git tag <x.y.z>`
  - [ ] Push the tag: `git push origin <x.y.z>`
  - [ ] Create a GitHub release: [Open the GitHub tags](https://github.com/microsoft/vscode/tags), and click far right ... > Create Release. Use the version as title <x.y.z> and use the release link `https://code.visualstudio.com/updates/v<x_y>` for the description
- [ ] Close milestone (**do not** delete it): https://github.com/microsoft/vscode/milestones
- [ ] Move all remaining issues to "On Deck"
- [x] Ensure that the latest Insiders release from main has succeeded
