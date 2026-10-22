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
