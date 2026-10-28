**MetaDescription**: Compare agent harnesses and built-in agents in Visual Studio Code, select one for a session, and review provider requirements.

# Choose an agent harness

VS Code supports multiple agent harnesses, each with its own tools, customizations, and workflows. An agent harness coordinates the language model, context, and tools that an agent uses to complete your task.

Use this guide to compare the available options, identify which harness your session uses, select a harness or the Cloud execution target, and review its setup requirements.

For a deeper explanation of how harnesses work and differ from models and hosts, [learn about agent harness concepts](/docs/agents/concepts/agent-harnesses.md).

## Compare agent harnesses

Start with the Copilot harness for day-to-day coding and agent tasks. Choose another harness or the Cloud target when you need different tools, customizations, or execution workflows.

| Harness | What runs | What this means for your work |
|----------------|-----------|-------------------------------|
| **Copilot** | Run tasks using the [copilot.copilot_sdk_short], which provides the shared agent experience across GitHub Copilot products. The agent works in the [Agent Host](/docs/agents/concepts/agent-host.md#session-lifetime-and-client-dependencies). | Sessions run independently of the editor window and can continue in the background after you close it, while the Agent Host stays running. You can also continue sessions across supported interfaces. See [Copilot requirements and limitations](#copilot). |
| **Local** | Run tasks within VS Code's built-in agent harness. The agent works in VS Code's [extension host](/docs/agents/concepts/agent-host.md#local-and-existing-extension-host-sessions). | The agent iterates via chat and works interactively to implement changes in your current workspace. The session is tied to the editor window: closing that window stops the agent's ongoing work. See [Local requirements](#local). |
| **Claude** | The [product.prodname_anthropic_claude] Agent SDK is integrated into VS Code. | Sessions use Claude project configuration and provider workflows in your current workspace or an isolated worktree. See [Claude requirements](#claude). |
| **Codex** | [product.prodname_openai_codex] runs through the [product.prodname_openai_codex] extension or the experimental Agent Host integration. | Sessions support interactive or background coding. Available interfaces depend on the integration. See [Codex requirements](#codex). |
| **Cloud** | The Copilot harness runs in a managed cloud environment. Cloud is an execution target, not a separate harness. | Use an interactive [cloud session](/docs/agents/run/cloud-sandbox-sessions.md) `feature(cloud-sessions)` and reconnect to continue work without keeping your own machine online. Cloud work uses a separate workspace rather than your local editor state. See [Cloud target requirements](#cloud-target). |

For Agent Host sessions managed by desktop VS Code on your machine, keep the application running. Closing an editor window is different from quitting the application. Tools provided by a window also require that window to stay connected.

Changing the model or agent role does not change the harness. For example, selecting a Claude model in a Copilot harness session still uses the Copilot harness. Opening the same session in another supported interface also keeps its harness.

**Local** is a harness name, not a synonym for running on your machine. The Copilot, Claude, and Codex harnesses can also run on your machine.

Available models depend on the harness and how you [access models](/docs/agent-customization/language-models.md#choose-how-to-access-models), such as through a GitHub Copilot subscription, another supported account, or your own API key. Harness-specific customizations, including [hooks](/docs/agent-customization/hooks.md#choose-the-hook-implementation-for-your-session), follow the selected harness.

> [!NOTE]
> Claude and Codex harnesses are disabled when [Copilot enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), including managed permission or sandbox settings. Contact the IT team that deployed the settings to discuss access. If you don't know the owner, ask your IT help desk to find the responsible administrator.

## Select a harness

Select a harness before you submit the first prompt for a session:

1. [Open the Chat view](/docs/agents/run/chat-view.md) or [open the Agents window](/docs/agents/run/agents-window.md).

1. Select **New Chat** (`+`) in the Chat view, or select **New** in the Agents window.

1. In the Agents window, select the folder or GitHub repository for the session.

1. Open the **Session Target** UI control and select an available harness or the Cloud target.

    ![Screenshot showing the Session Target UI control in the Agents window.](../images/agent-harnesses/agents-window-session-target-2.png)

The control only lists targets whose [requirements](#requirements-and-setup) are met in the current window.

### Choose a built-in agent

After selecting a harness, choose an available built-in agent from the agent picker. The available built-in agents depend on the harness:

| Harness | Built-in agents |
|---------|----------------|
| **Copilot** | <ul><li>**Ask** answers questions and researches your codebase without making changes. It only uses read-only tools and can't edit files or run state-changing commands.</li><li>**Agent** implements changes and validates the result.</li><li>**[Plan](/docs/agents/run/planning.md)** researches a task and creates an implementation plan for you to review. Invoke it with `/plan`.</li></ul> |
| **Local** | <ul><li>**Ask** answers questions without changing your code.</li><li>**Agent** implements changes and validates the result.</li><li>**Plan** researches a task and creates an implementation plan for you to review.</li></ul> |

Switching agents doesn't change the harness. You can also select [custom agents](/docs/agent-customization/custom-agents.md) from the same picker. In the Copilot harness, [Autopilot](/docs/agents/run/approvals.md#how-autopilot-works) is a mode with its own workflow, not an additional built-in agent.

Your harness choice is separate from where the session changes code. In the Agents window, you can also [choose between a folder and a worktree](/docs/agents/run/agents-window.md#choose-where-an-agent-makes-changes) or [run a session in a Dev Container](/docs/agents/run/agents-window.md#run-a-session-in-a-dev-container).

### Identify your current harness

To identify the current harness for a chat session, use one of the following methods:

* In the editor window, the active harness is shown as a prefix in the chat title.

* In the Agents window, the chat input box shows the active harness as the watermark.

* In the Agents window, hover over the session entry in the sessions list to see a tooltip showing the harness.

## Requirements and setup

Check the accounts, extensions, and settings needed for your chosen harness or the Cloud target. If a choice does not appear in the **Session Target** UI control, start with its requirements below.

Your harness and model access are separate choices. Using a provider's model through Copilot is different from using that provider's own credentials. The access option you select determines which account's usage limits and billing apply.

If you're starting with an existing account or key:

* **GitHub Copilot access**: Start with the [Copilot harness](#copilot). The [[product.prodname_anthropic_claude]](#claude) and [[product.prodname_openai_codex]](#codex) integrations also offer Copilot-routed models, subject to their requirements.
* **[product.prodname_anthropic_claude] credentials**: Follow the [authentication options](#claude).
* **ChatGPT account**: Follow the [Codex setup](#codex) for your chosen integration.
* **Another model API key or local model**: [Configure a model provider](/docs/agent-customization/language-models.md#bring-your-own-language-model-key) for Local sessions or supported Experimental Copilot harness workflows.

For access through a provider's own credentials, that provider's usage limits, billing, and data-handling terms apply. Organization policies can restrict the available routes, even when you have separate credentials.

### Copilot

To use models through GitHub Copilot, follow the [Copilot setup guide](/docs/setup/copilot.md). Copilot harness sessions use the same GitHub authentication context as chat in VS Code, including your GitHub Enterprise account when configured.

To use supported models through your own credentials, follow the [Experimental Agent Host BYOK setup](/docs/agent-customization/language-models.md#bring-your-own-language-model-key). This is separate from configuring provider-native authentication for the [product.prodname_anthropic_claude] or [product.prodname_openai_codex] harness.

For managed user accounts on GHE.com, complete the setup in [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).

Before reusing a Local harness session's configuration, check [tool availability](/docs/agents/run/tools.md#manage-tool-availability-for-the-copilot-harness) and [MCP configuration compatibility](/docs/agents/reference/mcp-configuration.md#configuration-file). Copilot harness sessions don't have access to every built-in or extension-provided tool. The shared SDK runtime also does not imply identical tools, models, permissions, or customizations across products, or that all sessions and personal settings synchronize.

For enterprise SDK Policy Hooks requirements, see [enterprise hook configuration](/docs/enterprise/manage-ai-settings.md#enable-or-disable-hooks).

To let a local Copilot session interact with desktop applications on macOS or Windows, see [Computer Use (Experimental)](/docs/agents/run/tools.md#control-desktop-applications-experimental).

### Claude

Claude support is enabled by default unless [enterprise-managed settings disable the harness](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability). When organization policy permits it, turn support on or off with ``chat.agentHost.claudeAgent.enabled`` (Experimental).

To use Claude, configure one of these authentication and billing options:

* **GitHub Copilot subscription**: sign in to GitHub to use Copilot-routed models. Usage is billed through your Copilot subscription.
* **Bring your own key (BYOK)**: use a Claude API key or another supported Claude BYOK option. Usage is billed by your configured provider.

When both options are available, the model picker groups models by **Anthropic** and **Copilot**. The model you select determines the provider and billing method for the next turn. You can switch between BYOK-backed and Copilot-routed models in an existing Claude harness session.

<a id="use-claude-without-github-sign-in" name="use-claude-without-github-sign-in"></a>

To use Claude without signing in to GitHub _(Experimental)_, configure a Claude API key or another supported Claude BYOK option. For an Anthropic API key, set `ANTHROPIC_API_KEY` in your environment or in the `env` object in `~/.claude/settings.json`. Learn more about [Claude Code authentication](https://code.claude.com/docs/en/authentication).

Enable ``chat.agentHost.allowSignedOutWhenUsable`` to open the Agents window while signed out of GitHub. The model picker only shows models from your Claude BYOK configuration until you sign in. After you sign in to GitHub, Copilot-routed models are also available.

See [Claude permission modes](/docs/agents/run/approvals.md#claude-permission-modes) for approval behavior and related cautions.

### Codex

Codex is not listed by default. Choose one of the following integrations. You don't need both.

#### Extension-based integration

To use Codex in the Chat view, install and enable the [OpenAI Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt). Follow the extension's documentation for authentication and permissions.

#### Agent Host integration (Experimental)

> [!NOTE]
> The Codex Agent Host integration is disabled when [enterprise-managed settings apply](/docs/enterprise/manage-ai-settings.md#claude-and-codex-availability), even with a ChatGPT account or the integration's user setting set to `true`. Contact the IT team that deployed the settings to discuss access.

Enable ``chat.agentHost.codexAgent.enabled`` to make Codex available in the Agents window without the [product.prodname_openai_codex] extension.

To also use this integration in the Chat view, enable ``chat.editor.codex.preferAgentHost`` and restart VS Code when prompted. Only one Codex implementation appears in each window. In the **Session Target** UI control, this setting replaces the **Codex** choice contributed by the OpenAI extension.

Choose one of these access options for the Agent Host integration:

* **GitHub Copilot subscription**: sign in to GitHub to use Copilot-backed models. This option requires [copilot.copilot_pro_plus_short].
* **ChatGPT account**: open the account menu and select **Sign in to ChatGPT**. A free ChatGPT account is sufficient.

When both accounts are signed in, the model picker groups models by **Copilot** and **ChatGPT**. Your selection determines which account provides model access, and VS Code saves that provider with the session.

To use Codex without signing in to GitHub _(Experimental)_, sign in to ChatGPT and enable ``chat.agentHost.allowSignedOutWhenUsable``. The Agents window then shows ChatGPT-backed models while signed out. Copilot-backed models prompt you to sign in to GitHub, and the browser-based Agents window still requires GitHub sign-in.

See [Codex approval presets](/docs/agents/run/approvals.md#codex-approval-presets) for approval behavior and related cautions.

### Local

Local harness sessions use the models configured in VS Code. [Set up GitHub Copilot](/docs/setup/copilot.md) to use Copilot-provided models, or [configure your own model credentials](/docs/agent-customization/language-models.md#bring-your-own-language-model-key) for a supported model.

Select **Local** in the Chat view and keep the editor window open while the agent works. Local harness sessions use different [customization settings](/docs/agent-customization/custom-instructions.md) from Copilot harness sessions.

SDK Policy Hooks are not loaded in Local harness sessions. Check [hook compatibility](/docs/agent-customization/hooks.md#migrate-hooks-between-harnesses) before reusing hooks from another harness.

### Cloud target

Use a cloud session to work interactively with an agent on managed compute and return to the same session later, without keeping your own machine online. Cloud is an execution target, separate from your choice of language model.

#### Cloud sessions

`feature(cloud-sessions)`

With ``chat.agentHost.cloudSandbox.enabled`` on, new **Cloud** sessions use a managed environment running the Copilot runtime. In the Agents window, this replaces the Copilot cloud agent workflow on [product.prodname_github] Actions for new **Cloud** sessions. You can send follow-ups and reconnect to the session without keeping your own machine online. Connections require ``chat.remoteAgentHostsEnabled`` and service access for your account.

The cloud environment has its own workspace and tools. Choosing another model doesn't change the harness. Enabling cloud sessions doesn't move a local conversation or local files into the cloud.

To get started, follow [Run cloud sessions](/docs/agents/run/cloud-sandbox-sessions.md) for creation, continuation, and lifecycle guidance. The **Cloud** creation experience depends on your settings and account availability.

## Continue with a different harness

A handoff continues an ongoing task with a different harness or execution environment and carries the conversation history and context with it. The tools, permissions, and models might change because the new configuration provides different capabilities.

### Hand off from a Local harness session

From a Local harness session, you can select another supported harness after work starts. Sessions that use the Copilot or Claude harness, and sessions that use the [experimental Codex integration](#codex), can receive these handoffs but can't hand off to another harness or to a cloud session.

To hand off a Local harness session:

1. Open the session.

1. In the chat input, open the **Session Target** dropdown.

1. Select Copilot, Claude, or Codex to continue the work.

VS Code carries the conversation history and context to the destination session. To implement a plan or continue it with another supported session, see [planning with agents](/docs/agents/run/planning.md).

> [!NOTE]
> Enterprise-managed sandbox or permission settings might automatically move a Local session to the Copilot harness so the Agent Host can enforce the policy. This policy-driven move preserves the conversation history and unsent input without submitting a prompt, and archives the original Local session as read-only. It is different from a user-initiated handoff. Learn more about [Agent Host policy enforcement](/docs/enterprise/manage-ai-settings.md#enforce-runtime-policies-with-copilot-agent-host).

Changing a harness is different from starting another conversation or opening the same session in another interface. Learn more about [sessions, forks, and handoffs](/docs/agents/concepts/sessions.md).

## Use canvases with the Copilot harness

`feature(canvases)`

Canvases are interactive visual surfaces shared by you and the agent in supported local Copilot sessions. For prerequisites and steps to find, open, and manage canvases, see [Use canvases with agents](/docs/agents/run/canvases.md).

## Frequently asked questions

### What is the difference between Local and Copilot?

Both harnesses can run on your machine. **Local** uses VS Code's built-in proprietary agent harness and works in VS Code's extension host. **Copilot** uses the [copilot.copilot_sdk], which is the agent experience shared consistently across GitHub Copilot products.

Both harnesses support tools, model selection, and agent customizations, but the available capabilities and configuration differ.

The Copilot harness provides these benefits:

* **A shared runtime across Copilot products**: core capabilities and behavior are more consistent across VS Code, GitHub Copilot CLI, and the GitHub Copilot app.

* **Continuity between interfaces and machines**: you can continue the same live session in the Chat view, the Agents window, and other GitHub Copilot interfaces. You can also [connect remotely from another machine](/docs/agents/run/remote-agent-sessions.md) while the session continues to run on its host. Local sessions are available only in the editor's Chat view.

* **Work independent of an editor window**: ongoing work can continue after you close the editor window, while the Agent Host remains running. Closing a Local harness session's editor window stops its ongoing work.

### Which harness should I choose?

Start with **Copilot** for day-to-day coding and agent tasks, especially when you want to continue work between the Chat view and Agents window, or keep work running after closing an editor window.

If your workflow depends on specific tools or customizations that aren't supported by the Copilot harness, please [let us know](https://github.com/microsoft/vscode/issues). Before moving an existing workflow, check [tool availability](/docs/agents/run/tools.md#manage-tool-availability-for-the-copilot-harness), [MCP configuration compatibility](/docs/agents/reference/mcp-configuration.md#configuration-file), and [hook compatibility](/docs/agent-customization/hooks.md#migrate-hooks-between-harnesses).

### Can I keep Local available while migrating?

Yes. Local remains an editor harness option while you adapt integrations that depend on it. Start a new session in the editor's Chat view and select **Local** from **Session Target**. Local is not available in the Agents window.

For an unmanaged editor, the following experimental settings make Local visible and turn off automatic Copilot preference:

```json
{
    "chat.editor.localAgent.enabled": true,
    "chat.defaultToCopilotHarness": false,
    "chat.editor.preferCopilotHarness": false
}
```

An organization policy can override user settings. Starting with version 1.142, administrators can set `vscode.temporaryDefaultToLocalHarness` to `true` in [enterprise-managed settings](/docs/enterprise/manage-ai-settings.md#keep-local-harness-as-default). This temporary control keeps Local available and suppresses automatic Copilot routing, including routing triggered by managed sandbox and permission settings. It preserves explicit, remembered, and current harness choices.

> [!WARNING]
> Local does not enforce runtime-only sandbox and permission rules. Administrators must review the security impact before using the temporary Local default. Copilot harness sessions continue to enforce those rules.

For customization-specific blockers and next steps, see the [migration FAQ](/docs/agent-customization/migrate-customizations.md#frequently-asked-questions).

### Does running locally mean the language model runs on my machine?

No. The harness coordinates the session and its tools, but the language model can run elsewhere. A session that edits files and runs commands on your machine can still send model requests to a hosted service. The **Local** harness name does not mean that the model runs locally or that the session works offline. Learn how [harnesses differ from models and execution environments](/docs/agents/concepts/agent-harnesses.md#how-a-harness-differs-from-other-agent-concepts).

### Does selecting a different model change the harness?

No. Selecting a model changes the model used within the current harness. For example, selecting a Claude model in a Copilot session does not switch to the Claude harness. Changing the agent role, such as Ask or Agent, also does not change the harness. To check which harness you are using, see [Identify your current harness](#identify-your-current-harness).

### Can I continue an existing Local session with Copilot?

Yes. In the Local session's chat input, open the **Session Target** dropdown and select **Copilot**. The handoff carries the conversation history and context to the destination session, but the available tools, permissions, and models might change. See [Hand off from a Local harness session](#hand-off-from-a-local-harness-session).

## Related resources

* [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md), including [continuing in the terminal](/docs/agents/run/sessions/manage-sessions.md#use-copilot-cli-from-the-terminal).
* [Remote agent access through GitHub Environments, SSH, or dev tunnels](/docs/agents/run/remote-agent-sessions.md#choose-how-to-connect)
* [Approvals and permissions](/docs/agents/run/approvals.md)
