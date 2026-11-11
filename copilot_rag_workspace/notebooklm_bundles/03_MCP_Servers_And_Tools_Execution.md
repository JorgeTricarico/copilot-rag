# COMPENDIO RAG NOTEBOOKLM: 03_MCP_Servers_And_Tools_Execution
- **Generado (UTC)**: 2026-11-11T05:27:05.015512+00:00
- **Total Palabras**: 8,770 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/mcp-servers.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/mcp-servers
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/mcp-servers.md
- **SHA256_FINGERPRINT**: `5432af25cf1b47d03759f4cfe219f4b4e4ad137645ae798f87962ce7b5e0103b`
- **LAST_VERIFIED_UTC**: 2026-11-11T05:26:57.973709+00:00
---

**MetaDescription**: Add MCP servers to Copilot in VS Code and use their tools.

# Add and use MCP servers in VS Code

Add an MCP server when Copilot needs tools or data that aren't already available, such as querying a database or searching a documentation service. [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) connects agents to these tools and data sources.

Choose how to add the capability you need:

* **Connect a supported service:** use a [Copilot connector](/docs/agent-customization/copilot-connectors.md) `feature(copilot-connectors)`. [product.prodname_github] manages configuration and authentication without local server setup.
* **Find a published integration:** [browse servers](#find-and-install-a-server) or [install an agent plugin](/docs/agent-customization/agent-plugins.md#discover-and-install-plugins) that bundles MCP tools.
* **Add a server directly:** [use a publisher's URL or launch command](#add-a-server-by-url-or-command).

## Before you start

* [Enable AI features](/docs/getstarted/overview.md#enable-ai-features) and open a local project folder in VS Code.
* Select **Copilot** in the **Session Target** dropdown. The connection example below uses a personal configuration.

> [!CAUTION]
> Local MCP servers can run code on your machine, and tools can access services using your permissions. Review the publisher, command or endpoint, and requested access before installing or starting a server. Learn about [MCP server trust](/docs/agents/run/manage-mcp-servers.md#mcp-server-trust).

## Find and install a server

### Discover servers in the Customization Marketplace (Preview)

Use the [Customization Marketplace](/docs/agent-customization/overview.md#discover-and-install-existing-customizations-preview) to find existing server integrations:

1. Run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``) and select **Browse**.

1. Select **GitHub Feed** from the source menu and search by name or with `@type:mcp`.

1. Review the publisher, server capabilities, and setup requirements, then select **Install** when available.

1. Complete the publisher's setup and [use the server's tools](#use-your-servers-tools).

GitHub Feed is Experimental and requires a harness that provides marketplace search. Availability also depends on organization policy. If discovery or automatic installation isn't available, [add the publisher's URL or command](#add-a-server-by-url-or-command) instead.

You can also select a plugin marketplace and [install a plugin that bundles MCP servers](/docs/agent-customization/agent-plugins.md#install-a-plugin-from-a-marketplace). Adding a marketplace makes its plugins available to browse but doesn't install them.

**Other discovery and installation options**

* Run **MCP: Browse MCP Servers** to open server discovery.
* To import configuration from another application, run **MCP: Add Server** and choose **Add from another application**. See [supported discovery sources](/docs/agents/reference/mcp-configuration.md#automatic-mcp-server-discovery).
* If you have a package or image name, run **MCP: Add Server** and choose **NPM Package**, **Pip Package**, or **Docker Image** when available. Model assistance generates a configuration. Review its command, publisher, and credential requirements before accepting it, and install the required runtime.

## Add a server by URL or command

Provide the publisher's URL or launch command so Copilot knows how to access an existing MCP server. Use a URL for a remote server or a command to start a local server process.

If you already installed a server or connected a connector, continue to [use its tools](#use-your-servers-tools).

For a first server, try the [Microsoft Learn MCP server](https://learn.microsoft.com/en-us/training/support/mcp). It searches official Microsoft documentation and requires no authentication or local runtime.

1. With **Copilot** selected, run **Chat: Open Customizations** and select **MCP Servers**. Select **Add Server** (**+**) in the **User** group.

1. Choose **HTTP (HTTP or Server-Sent Events)** and enter the server endpoint. For the Microsoft Learn MCP server, use `https://learn.microsoft.com/api/mcp`.

1. Enter a unique server ID, such as `microsoftLearn`.

1. Select **Global**, then **Copilot Global**. This personal configuration is shared across your workspaces and compatible Copilot experiences on the same host, including Copilot CLI. For sharing within a workspace, see [Choose a configuration destination](#choose-a-configuration-destination).

    If **Copilot Global** isn't available, check the [Copilot harness requirements](/docs/agents/run/agent-harnesses.md#copilot).

1. Review any server trust requests before accepting them.

For another HTTP server, substitute the publisher's endpoint and follow its authentication instructions. Don't paste credentials into chat or put them in shared configuration. For API keys or configuration copied from another client, check the [authentication and compatibility guidance](/docs/agents/reference/mcp-configuration.md#authentication-and-secrets).

**Add a server with a launch command (stdio)**

For a server that runs as a local process, choose **Command (stdio)** instead of HTTP and enter the publisher's launch command. Install its runtime where the server runs.

For example, the [Playwright MCP server](https://github.com/microsoft/playwright-mcp) requires Node.js 18 or newer with `npx` available:

```bash
npx -y @playwright/mcp@latest
```

Use `playwright` as the server ID and follow the remaining connection steps. For browser tasks that don't require an MCP server, consider the [built-in browser tools](/docs/agents/run/browser-tools.md).

As an alternative to the Agent Customizations editor, run **MCP: Add Server** from the Command Palette to start the guided flow.

## Use your server's tools

Ask Copilot for a task that needs the connected service, such as finding official documentation for an API. Copilot selects relevant tools, so you don't need to name the server in every request. Naming it explicitly can help when testing a connection or directing a request to a specific service.

Review startup, sign-in, or tool approval requests as they appear. Approve only actions you understand. Depending on the server, you might also encounter:

* **Input requests:** the server asks for missing information, such as a filter or date range. Don't enter passwords or API keys in these forms. Learn about [server input requests](/api/extension-guides/ai/mcp.md#elicitation).
* **Interactive results (Experimental):** [MCP Apps](/api/extension-guides/ai/mcp.md#mcp-apps) display forms, visualizations, or other controls alongside a tool result.

### Verify the first tool call

To check your setup, name the server and a low-impact task. For Microsoft Learn:

```prompt
Use the Microsoft Learn MCP tools to find the official documentation for the Kusto Query Language where operator. Summarize its syntax and link to the documentation. Do not change files.
```

Expand the tool call in the conversation. Confirm that it used Microsoft Learn and returned documentation for the Kusto `where` operator, not a similarly named operator in another language. The answer should reflect that result. A plausible answer without a tool call doesn't verify the connection.

For another server, choose a low-impact task supported by its tools and inspect the result in the same way.

## If the server does not work

| What you observe | Next step |
|------------------|-----------|
| The server doesn't appear or cannot start. | Check its configuration scope, runtime requirements, and [server output](/docs/agents/run/manage-mcp-servers.md#view-server-output). |
| Sign-in or a connection fails. | Check the publisher's authentication instructions and your organization's access restrictions. See [MCP troubleshooting](/docs/agents/run/manage-mcp-servers.md#troubleshoot-mcp-servers). |
| The server runs, but no tool from it is called. | Check [tool availability and invocation](/docs/agents/agent-troubleshooting/chat-debug-view.md#an-mcp-tool-is-not-being-invoked). |

After correcting the problem, repeat the request and inspect the tool output again.

## Choose a configuration destination

The connection example uses a personal configuration. Choose a different destination when you need to share a server:

| Your goal | Destination |
|-----------|-------------|
| Use a server across your workspaces and compatible Copilot experiences, including Copilot CLI. | **Global** > **Copilot Global** on the same host. |
| Share server configuration with teammates working in the same workspace. | Workspace-root `.mcp.json`, when offered in the guided flow. Share the file with the workspace, for example through source control. |

**Copilot Global** applies to clients that read the same personal Copilot configuration. It doesn't synchronize configuration across machines or guarantee shared authentication credentials.

See the [configuration reference](/docs/agents/reference/mcp-configuration.md#configuration-file) for workspace setup availability, file locations, supported fields, and authentication. For remote hosts or containers, follow the [remote setup guidance](/docs/agents/run/manage-mcp-servers.md#remote-workspaces-and-dev-containers).

For existing Local harness `feature(local-harness)` configurations, use the [compatibility reference](/docs/agents/reference/mcp-configuration.md#editor-managed-configuration-for-local-harness-compatibility) instead of copying their settings into a new configuration.

## Manage an existing server

Open **Chat: Open Customizations** > **MCP Servers** to manage your servers. If you only wanted to try a server, use its ellipsis (**...**) menu to **Disable** or **Uninstall** it. Stopping a server only ends its current run, and a later request can start it again.

For connectors, [disconnect the service](/docs/agent-customization/copilot-connectors.md#disconnect-a-service) instead. If **Uninstall** isn't available for another server, follow the [removal instructions for its configuration source](/docs/agents/run/manage-mcp-servers.md#control-or-remove-a-server).

For editing connections, server output, and sharing configuration, see [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md). To control which tools the agent can use, see [Manage available tools](/docs/agents/run/tools.md#manage-available-tools).

## Related resources

* [Use tools with agents](/docs/agents/run/tools.md)
* [MCP configuration reference](/docs/agents/reference/mcp-configuration.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/reference/mcp-configuration.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/reference/mcp-configuration
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/reference/mcp-configuration.md
- **SHA256_FINGERPRINT**: `f0ed8e4fa70a71268863137646e1db849c0b7fab37bbbacbfebe7c696c39ccc8`
- **LAST_VERIFIED_UTC**: 2026-11-11T05:26:59.031267+00:00
---

**MetaDescription**: Configure MCP servers for the Copilot harness with portable files, authentication, and tool controls.

# MCP configuration reference

Configure MCP servers for the Copilot harness with the portable `mcpServers` format. This reference covers configuration locations, fields, authentication, and relevant controls.

* **Connect a server to Copilot:** [choose a configuration destination](#configure-mcp-for-copilot), then use the [portable examples and fields](#portable-configuration).
* **Reuse an existing editor configuration:** check [forwarding and migration](#editor-forwarding-to-copilot).
* **Maintain a deprecated Local configuration:** use the separate [Local compatibility reference](#editor-managed-configuration-for-local-harness-compatibility).

For a complete first-time walkthrough, see [Add MCP servers](/docs/agent-customization/mcp-servers.md). To operate an existing server, see [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md).

Configuration compatibility is separate from protocol support. For tools, prompts, resources, roots, sampling, elicitation, and MCP Apps, see [MCP support and limitations](/api/extension-guides/ai/mcp.md#mcp-support-in-copilot).

## Configure MCP for Copilot

Use the Agent Customizations editor to add a server to the intended Copilot session:

1. Select the **Copilot** harness in a chat session, then run **Chat: Open Customizations** and select **MCP Servers**.

1. Select **Add Server**, provide the publisher's command or endpoint, and choose a destination below. For personal configuration, select **Global** > **Copilot Global**.

1. Complete any authentication prompts and [verify a tool call](/docs/agent-customization/mcp-servers.md#verify-the-first-tool-call). Adding a configuration alone doesn't confirm that the session can use the server.

### Configuration file

Choose a native Copilot destination. Both files use a top-level `mcpServers` object, and the harness reads them directly.

| Your goal | Configuration file | Guided setup destination |
|-----------|--------------------|--------------------------|
| Use a server across your workspaces | `$COPILOT_HOME/mcp-config.json`, or `~/.copilot/mcp-config.json` when `COPILOT_HOME` is unset | **Global** > **Copilot Global** |
| Share server definitions with your team | `.mcp.json` at the workspace root | Workspace-root `.mcp.json`, offered when the Experimental ``chat.mcp.workspaceRootConfig.enabled`` setting is on |

As an alternative to guided setup, edit the native file using the [portable configuration examples](#portable-configuration). Existing workspace-root `.mcp.json` files remain available when the guided-setup setting is off.

> [!IMPORTANT]
> For new Copilot configurations, use these native destinations, not `.vscode/mcp.json` or profile `mcp.json`. Those files use the deprecated Local harness's `feature(local-harness)` editor-managed `servers` format. Eligible existing definitions can be [forwarded](#editor-forwarding-to-copilot), but the harness doesn't read those files directly.

[Plugin-provided servers](/docs/agents/reference/agent-plugin-reference.md#mcp-servers-in-plugins) travel with their plugin. Installing a plugin is different from copying its server definitions into a personal or workspace configuration.

For remote and Dev Container sessions, native user configuration refers to the home directory where the harness runs. The connected client's `$COPILOT_HOME/mcp-config.json` (or `~/.copilot/mcp-config.json`) isn't forwarded to another host or harness. Configure the server in the execution environment or use an eligible forwarded configuration instead. See [remote session customization sources](/docs/agent-customization/overview.md#manage-customizations-for-remote-sessions).

For other providers, use the provider's MCP configuration documentation. Their configuration locations and schemas can differ.

The guided setup and configuration form support a subset of the native file's options. Both native destinations have a configuration form in the Agent Customizations editor:

| Destination | Transports offered in the form | Working-directory field |
|-------------|--------------------------------|-------------------------|
| Copilot user `mcp-config.json` | stdio, HTTP, and legacy SSE | Yes |
| Workspace-root `.mcp.json` | stdio and HTTP | No |

The configuration form preserves properties that it doesn't display. Select **Other Properties** in the form to open the complete server entry in JSON.

### Portable configuration

Use a top-level `mcpServers` object in workspace-root `.mcp.json` or Copilot user `mcp-config.json`. This example configures one local Playwright server:

```json
{
    "mcpServers": {
        "playwright": {
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"],
            "tools": ["*"]
        }
    }
}
```

Install the publisher's runtime prerequisites before starting the server. The [Playwright setup requirements](https://github.com/microsoft/playwright-mcp#requirements) include Node.js 18 or newer.

For an HTTP server, replace the server entry with the publisher's endpoint:

```json
{
    "mcpServers": {
        "context7": {
            "type": "http",
            "url": "https://mcp.context7.com/mcp",
            "tools": ["*"]
        }
    }
}
```

Follow the [Context7 setup instructions](https://context7.com/docs/resources/all-clients) for authentication and service limits. An endpoint alone doesn't grant access to a service.

These are common fields in a portable server entry:

| Field | Applies to | Purpose |
|-------|------------|---------|
| `type` | All servers | `stdio` for a command, `http` for Streamable HTTP, or `sse` for a legacy SSE endpoint. Prefer HTTP when the server supports it. |
| `command`, `args` | stdio | Executable and its arguments. Install the runtime where the harness runs. |
| `env` | stdio | Environment-variable values or references. Use strings for values. |
| `cwd` | stdio | Working directory. The Copilot user configuration form supports this field; the workspace-root form does not. |
| `url`, `headers` | HTTP and SSE | Endpoint and optional request headers. Don't store literal credentials in shared files. |
| `tools` | All servers | Tool names to make available. `["*"]` makes all server tools available; use specific names to limit the selection. This doesn't bypass tool approvals. |
| `oauthClientId` | HTTP and SSE | Client ID for a server that requires a pre-registered OAuth client. This is a flat field, not the editor format's nested `oauth` object. |

For additional runtime-specific options, see the [Copilot CLI MCP configuration guidance](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers). Don't copy editor-only fields such as `inputs`, `envFile`, `dev`, or `sandboxEnabled` into a portable file.

### Environment-variable references

Portable configurations support environment variables independently of VS Code input prompts. Use `${NAME}` to reference a value, or `${NAME:-default}` for a non-secret default. Stdio servers can use references in `command`, `args`, and `env` values. HTTP servers can use them in header values.

Provide variables in the environment of the host that runs or connects to the server. For remote sessions, that is the remote host or container. Use the braced `${NAME}` form for compatibility across the Copilot runtime and the VS Code MCP client, which treats bare `$NAME` as literal text.

You can edit environment variables and HTTP headers in the Copilot user [MCP configuration form](/docs/agents/run/manage-mcp-servers.md#edit-an-mcp-server-configuration). Enter references rather than literal credentials. The workspace-root form rejects `${...}` expressions, so use **Other Properties** to edit references in the source `.mcp.json` instead. A form restriction does not mean that the Copilot runtime cannot read the reference.

Support for environment variables does not include `envFile`, input prompting, or a bridge to VS Code `SecretStorage`. For a worked example, see [Replace input prompts with environment variables](/docs/agent-customization/migrate-customizations.md#replace-input-prompts-with-environment-variables).

### Authentication and secrets

Authentication grants access to an external service. It is separate from trusting a server to start and approving individual tool calls.

| Server requirement | Copilot guidance |
|--------------------|------------------|
| Browser sign-in or OAuth | Follow the publisher's instructions and complete authorization when prompted. Use **Authenticate** in the session's server actions when offered. The editor coordinates authentication for Copilot sessions in VS Code; don't assume another client shares its saved credentials. |
| A pre-registered OAuth client | Use supported flat Copilot fields such as `oauthClientId`, not the editor format's nested `oauth` object. See the [Copilot CLI guidance](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers). |
| An API key or fixed token | Use [environment-variable references](#environment-variable-references) if they meet your requirements. Provide credentials in the environment of the host that runs or connects to the server. |
| VS Code input prompts or an environment file | These are editor-managed options, not native Copilot configuration. Review the [migration limitations](/docs/agent-customization/migrate-customizations.md#check-mcp-values-before-migration). |

Do not commit tokens, passwords, or populated authentication headers. A personal configuration file is not a secret store.

The Copilot harness has no built-in MCP configuration option to forward a `${input:...}` secret or read an existing VS Code `SecretStorage` value into an HTTP authentication header. OAuth can be an alternative when the server supports it, but it does not substitute a prompted API key. If your integration requires a static bearer token without environment variables or credentials in files, see the [migration FAQ](/docs/agent-customization/migrate-customizations.md#can-copilot-pass-a-prompted-secret-to-an-http-mcp-server-without-an-environment-variable-or-a-file).

### Server naming conventions

Use a descriptive, unique name for each server you use together, such as `github` or `database`. Avoid whitespace and special characters. For multi-word names, use camelCase, such as `uiTesting` or `githubIntegration`.

### Commands

Use these commands for Copilot setup and management from the Command Palette (``Shortcut: workbench.action.showCommands``).

| Command | Copilot workflow |
|---------|------------------|
| **Chat: Open Customizations** | Open **MCP Servers** in the intended session's context to add, edit, or manage servers. |
| **MCP: Add Server** | Start guided setup. Choose **Copilot Global** for native user configuration or workspace-root `.mcp.json` when offered. |
| **MCP: Browse MCP Servers** | Open [MCP discovery](/docs/agent-customization/mcp-servers.md#find-and-install-a-server). With marketplace discovery enabled, continue in the Agent Customizations editor. |
| **MCP: Install Server from Manifest** | Install from an MCP manifest. Review the destination rather than assuming it uses native Copilot configuration. |
| **MCP: List Servers** | Open available server controls. Use the intended session's context because Copilot runtime and editor-managed connections have different actions. |

Commands that open profile `mcp.json` or `.vscode/mcp.json`, and `code --add-mcp`, target [editor-managed configuration](#editor-managed-commands), not the portable Copilot files.

### Settings

These settings are relevant to Copilot setup or its connected editor. They don't replace the server entries in the native configuration file.

| Setting | Copilot workflow |
|---------|------------------|
| ``chat.mcp.access`` | Manage which MCP servers can be used in VS Code. |
| ``chat.mcp.workspaceRootConfig.enabled`` | (Experimental) Offer workspace-root `.mcp.json` in **MCP: Add Server**. Existing `.mcp.json` files remain available when this setting is off. |
| ``chat.mcp.apps.enabled`` `feature(mcp-apps)` | Control whether the connected editor displays MCP Apps, which provide interactive tool UI. |
| ``chat.agent.sandbox.mcpServers`` | Configure MCP server inclusion in the [Copilot harness sandbox](/docs/agents/run/agent-sandboxing.md). Review the required session sandbox settings; this is separate from Local per-server sandboxing. |
| ``accessibility.verbosity.mcpServerConfiguration`` | Control whether the MCP configuration form announces information about opening Accessibility Help. |

Copilot reads its native configuration independently of the editor's discovery setting. The editor's autostart and sampling-model settings also don't control the native runtime. Use [server enablement](/docs/agents/run/manage-mcp-servers.md#enable-or-disable-mcp-servers) to prevent a server from starting, and review the [Copilot sampling approval flow](/api/extension-guides/ai/mcp.md#sampling) for model requests.

For the full settings list, see the [AI Settings Reference](/docs/agents/reference/ai-settings.md). Settings for the deprecated Local path are listed under [editor-managed settings](#editor-managed-settings).

## Editor forwarding to Copilot

Editor forwarding reuses an eligible server definition in a Copilot session. It does not move the original file or turn an editor-managed server connection into the runtime's connection. Prefer [native configuration](#portable-configuration) for integrations that must work without the editor.

* Workspace `.vscode/mcp.json`, profile configurations, and eligible extension-provided definitions can be forwarded. Extension discovery and definition resolution require the contributing extension and editor.
* Configurations requiring `${input:...}` or `${command:...}` are rejected before variable resolution. Resolving or caching the value in Local first does not make the configuration eligible.
* Editor development mode, per-server sandbox rules, and `envFile` behavior do not transfer. Review authentication options and working-directory paths in the destination environment.
* Copilot user configuration is read on the host where the harness runs, not forwarded from a different host. Plugin servers are delivered with their plugin rather than duplicated as standalone definitions.

Forwarding is not [automatic migration](/docs/agent-customization/migrate-customizations.md#migrate-mcp-servers). Migration writes native files and can remove successfully migrated source entries; forwarding leaves the source configuration in place.

When reusing an existing configuration, check these differences:

| Capability | Portable Copilot configuration | Editor-managed configuration |
|------------|--------------------------------|------------------------------|
| Top-level server object | `mcpServers` | `servers` |
| Copilot delivery | Read by the runtime | Eligible definitions forwarded by the editor |
| Environment-variable references | `${NAME}` or `${NAME:-default}` | `${env:NAME}` |
| Environment file and input prompts | Not supported | `envFile` and `${input:...}` |
| Development mode and per-server sandboxing | Not supported in this format | `dev`, `sandboxEnabled`, and `sandbox` |

## Editor-managed configuration for Local harness compatibility

`feature(local-harness)`

The Local harness is deprecated. Use this section only to maintain an existing editor-managed configuration, not to set up a new native Copilot server.

The following schemas and examples apply to the `servers` format in workspace `.vscode/mcp.json` or [user-profile](/docs/configure/profiles.md) `mcp.json`. These files appear as read-only JSON in the Agent Customizations editor; edit their source file instead. A server using this format might be [eligible for forwarding](#editor-forwarding-to-copilot), but editor-specific behavior does not automatically carry over.

### Configuration structure

The following structure applies to the VS Code format. The portable Copilot format uses a separate schema with a top-level `mcpServers` object.

The configuration file has three main sections:

* **`"servers": {}`**: an object that maps server names to their configurations. Each key is the server name, and the value is the server configuration object. Depending on the server type, different fields are required.

* **`"inputs": []`**: an optional array of input variable definitions for sensitive information like API keys.

* **`"sandbox": {}`**: an optional object that defines file system and network access rules for sandboxed servers. See [Sandbox configuration](#sandbox-configuration). Only applies on macOS and Linux.

You can use [predefined variables](/docs/reference/variables-reference.md) in the server configuration, for example to refer to the workspace folder (`${workspaceFolder}`).

### Standard I/O (stdio) servers

Use this editor-managed configuration for servers that communicate through standard input and output streams.

| Field | Required | Description | Examples |
|-------|----------|-------------|----------|
| `type` | Yes | Server connection type | `"stdio"` |
| `command` | Yes | Command to start the server executable. Must be available on your system path or contain its full path. | `"npx"`, `"node"`, `"python"`, `"docker"` |
| `args` | No | Array of arguments passed to the command | `["server.py", "--port", "3000"]` |
| `cwd` | No | Working directory for the server command. Defaults to the workspace folder when run in a workspace. | `"${workspaceFolder}"` |
| `env` | No | Environment variables for the server. Values can be strings, numbers, or null. | `{"API_KEY": "${input:api-key}"}` |
| `envFile` | No | Path to an environment file to load more variables | `"${workspaceFolder}/.env"` |
| `dev` | No | Development mode settings to watch for file changes and debug the server. See [Development mode](#development-mode). | `{"watch": "src/**/*.ts"}` |
| `sandboxEnabled` | No | Run the server in a sandboxed environment. Only supported on macOS and Linux. | `true` |
| `sandbox` | No | File system and network permissions for this server. Root-level sandbox deny rules also apply. | `{"filesystem": {"allowWrite": ["${workspaceFolder}"]}}` |

> [!NOTE]
> When using Docker with stdio servers, don't use the detach option (`-d`). The server must run in the foreground to communicate with VS Code.

**Example local server configuration**

This example configures the same Playwright server in the VS Code format:

```json
{
    "servers": {
        "playwright": {
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
        }
    }
}
```

### Sandbox configuration

Editor-managed sandboxing restricts file system and network access for stdio MCP servers on macOS and Linux. It does not configure the [Copilot harness sandbox](/docs/agents/run/agent-sandboxing.md) and its ``chat.agent.sandbox.mcpServers`` setting.

To enable sandboxing for a server, set `"sandboxEnabled": true` in its configuration. Add a `sandbox` object to the server to define its file system and network permissions. You can also add a top-level `sandbox` object as a sibling of `servers` and `inputs` to define deny rules that apply to all sandboxed servers in the file.

Allow rules are supported only in a server's `sandbox` object. Top-level `allowWrite` and `allowedDomains` rules are ignored.

> [!NOTE]
> In Local harness `feature(local-harness)` sessions, editor-sandboxed MCP tools are auto-approved. This does not describe the Copilot harness's approval behavior.

The server-level and top-level `sandbox` objects support the following properties:

| Property | Type | Supported scope | Description |
|----------|------|-----------------|-------------|
| `filesystem.allowWrite` | string[] | Server only | File paths that the server is allowed to write to. |
| `filesystem.denyRead` | string[] | Server and top level | File paths that the server is not allowed to read. |
| `filesystem.denyWrite` | string[] | Server and top level | File paths that the server is not allowed to write to. |
| `network.allowedDomains` | string[] | Server only | Domains that the server is allowed to access. Wildcards are supported, for example `*.example.com`. |
| `network.deniedDomains` | string[] | Server and top level | Domains that the server is not allowed to access. |

You can use [predefined variables](/docs/reference/variables-reference.md), such as `${workspaceFolder}`, in file system path values.

**Example sandbox configuration**

This example grants one server write access to the workspace and network access to specific domains. The top-level rule denies all sandboxed servers in the file access to the `.ssh` directory:

```json
{
    "servers": {
        "myServer": {
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@example/mcp-server"],
            "sandboxEnabled": true,
            "sandbox": {
                "filesystem": {
                    "allowWrite": ["${workspaceFolder}"]
                },
                "network": {
                    "allowedDomains": ["api.example.com", "*.cdn.example.com"]
                }
            }
        }
    },
    "sandbox": {
        "filesystem": {
            "denyRead": ["${userHome}/.ssh"]
        }
    }
}
```

### HTTP and Server-Sent Events (SSE) servers

Use this editor-managed configuration for servers that communicate over HTTP. The editor's MCP client first tries the Streamable HTTP transport and falls back to SSE if HTTP is not supported.

| Field | Required | Description | Examples |
|-------|----------|-------------|----------|
| `type` | Yes | Server connection type | `"http"`, `"sse"` |
| `url` | Yes | URL of the server | `"http://localhost:3000"`, `"https://api.example.com/mcp"` |
| `headers` | No | HTTP headers for authentication or configuration | `{"Authorization": "Bearer ${input:api-token}"}` |
| `oauth` | No | OAuth configuration for authenticating with the server | `{"clientId": "example-client-id"}` |

In addition to servers available over the network, VS Code can connect to MCP servers listening for HTTP traffic on Unix sockets or Windows named pipes by specifying the socket or pipe path in the form `unix:///path/to/server.sock` or `pipe:///pipe/named-pipe` on Windows. You can specify subpaths by using a URL fragment, such as `unix:///tmp/server.sock#/mcp/subpath`.

The `oauth` object supports the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientId` | string | Yes | The OAuth client ID to use when authenticating with the server. |

> [!NOTE]
> When `oauth` is configured, VS Code handles the OAuth flow automatically. A browser window opens for authorization on the first connection to the server.

> [!NOTE]
> A client secret is not part of `mcp.json`. If the server's OAuth client is confidential, select the **Set Client Secret** CodeLens that appears above `oauth.clientId` in `mcp.json`. VS Code keeps the secret in its secret storage. To change it later, select **Replace Client Secret**.

**Example remote server configuration**

This example specifies a remote MCP endpoint. Follow the publisher's authentication instructions before using it:

```json
{
    "servers": {
        "context7": {
            "type": "http",
            "url": "https://mcp.context7.com/mcp"
        }
    }
}
```

**Example HTTP server with OAuth**

This example shows the configuration for an MCP server that uses OAuth for authentication. On first use, VS Code opens a browser window to complete the OAuth flow.

```json
{
    "servers": {
        "slack": {
            "type": "http",
            "url": "https://mcp.slack.com/mcp",
            "oauth": {
                "clientId": "example-client-id"
            }
        }
    }
}
```

### Input variables for sensitive data

Input variables in the VS Code format let you define placeholders for values such as API keys or passwords. They aren't supported in portable configuration files, and servers that require them aren't forwarded to Copilot harness sessions.

Forwarding rejects input and command variables before resolving them. Entering or caching the secret in a Local session `feature(local-harness)` first does not make the server available to Copilot. Keep the original configuration until a supported authentication method works in the destination harness.

When you reference an input variable using `${input:variable-id}`, VS Code prompts you for the value when the server starts for the first time. The value is then securely stored for subsequent use. Learn more about [input variables](/docs/reference/variables-reference.md#input-variables) in VS Code.

Each input variable has a `type` that determines how VS Code prompts for the value. The following input types are supported:

* `promptString`: opens an input box to ask the user for a free-text value.
* `pickString`: shows a list of options for the user to choose from.
* `command`: runs a command and uses its result as the input value.

**Common properties:**

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `type` | Yes | Type of input prompt: `promptString`, `pickString`, or `command` | `"promptString"` |
| `id` | Yes | Unique identifier to reference in server config | `"api-key"`, `"database-url"` |

**`promptString` properties:**

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `description` | Yes | User-friendly prompt text | `"GitHub Personal Access Token"` |
| `default` | No | Default value for the input | `"https://localhost"` |
| `password` | No | Hide typed input (default: false) | `true` for API keys and passwords |

**`pickString` properties:**

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `description` | Yes | User-friendly prompt text | `"Select an environment"` |
| `options` | Yes | Array of options to choose from. Each option is a string, or an object with `label` and `value` properties. | `["dev", "prod"]` |
| `default` | No | Default value for the input | `"dev"` |

**`command` properties:**

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `command` | Yes | Command ID to run to obtain the input value | `"myExtension.getApiKey"` |
| `args` | No | Arguments passed to the command. Can be a string, array, or object. | `{ "scope": "global" }` |

**Example server configuration with input variables**

This example configures a local server that requires an API key:

```json
{
    "inputs": [
        {
            "type": "promptString",
            "id": "perplexity-key",
            "description": "Perplexity API Key",
            "password": true
        }
    ],
    "servers": {
        "perplexity": {
            "type": "stdio",
            "command": "npx",
            "args": [
                "-y",
                "server-perplexity-ask"
            ],
            "env": {
                "PERPLEXITY_API_KEY": "${input:perplexity-key}"
            }
        }
    }
}
```

### Development mode

For editor-managed servers, add a `dev` key to the server configuration to use _development mode_. This does not configure a server started independently by the Copilot runtime. The object has two properties:

* `watch`: A glob pattern, or an array of glob patterns, to watch for file changes that restart the MCP server. Available for all server types.
* `debug`: Enables you to set up a debugger with the MCP server. Currently, VS Code supports debugging Node.js and Python MCP servers. Available for stdio servers only.

Learn more about [MCP development mode](/api/extension-guides/ai/mcp.md#mcp-development-mode-in-vs-code) in the MCP integration reference.

### Automatic MCP server discovery

The editor can automatically detect and reuse MCP server configurations from supported applications. Use ``chat.mcp.discovery.enabled`` to select these discovery sources. This is separate from native Copilot discovery and [plugin-provided servers](/docs/agents/reference/agent-plugin-reference.md#mcp-servers-in-plugins).

| Source | Setting property | Configuration location |
|--------|------------------|------------------------|
| Claude Desktop | `claude-desktop` | Windows: `%APPDATA%\Claude\claude_desktop_config.json`<br/>macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`<br/>Linux: `$XDG_CONFIG_HOME/Claude/claude_desktop_config.json`, or `~/.config/Claude/claude_desktop_config.json` if `XDG_CONFIG_HOME` is not set |
| GitHub Copilot CLI | `copilot` | `<COPILOT_HOME>/mcp-config.json`, or `~/.copilot/mcp-config.json` if `COPILOT_HOME` is not set |
| Cursor (global) | `cursor-global` | `~/.cursor/mcp.json` |
| Cursor (workspace) | `cursor-workspace` | `<workspace>/.cursor/mcp.json` |
| Windsurf | `windsurf` | `~/.codeium/windsurf/mcp_config.json` |

GitHub Copilot CLI discovery is on by default. All other discovery sources are off by default. In a remote window, VS Code resolves configuration locations and environment variables in the remote environment.

For GitHub Copilot CLI, setting `COPILOT_HOME` replaces the default `~/.copilot` location. VS Code does not check both locations.

> [!NOTE]
> Copilot harness sessions read the GitHub Copilot CLI MCP configuration independently, whether you use the Chat view or Agents window. The discovery setting does not change how these sessions receive MCP servers. See [configuration formats and forwarding](#configuration-file).

### Editor-managed commands

These commands operate on editor-managed configuration or connections. They aren't the native Copilot configuration workflow.

| Command | Scope and purpose |
|---------|-------------------|
| **MCP: Browse Resources** | Browse resources from editor-managed server connections. This is not a list of every native Copilot server's resources. |
| **MCP: Open Remote User Configuration** | Open the editor-managed remote `mcp.json`, not the Copilot user file. |
| **MCP: Open User Configuration** | Open the editor-managed profile `mcp.json`, not the Copilot user file. |
| **MCP: Open Workspace Folder MCP Configuration** | Open the editor-managed `.vscode/mcp.json`, not workspace-root `.mcp.json`. |
| **MCP: Reset Cached Tools** | Clear the editor's cached tool lists. This doesn't reset a Copilot runtime connection. |
| **MCP: Reset Trust** | Reset separate editor MCP trust decisions for non-workspace sources, not Workspace Trust or runtime tool approvals. |
| **MCP: Show Installed Servers** | Show installed servers in the editor's Extensions view. |

### Command-line installation

Use `code --add-mcp` with a JSON object containing a unique `name` and the server configuration. The command adds a server to the VS Code user-profile configuration.

For example, from a Bash shell:

```bash
code --add-mcp '{"name":"playwright","type":"stdio","command":"npx","args":["-y","@playwright/mcp@latest"]}'
```

This uses the VS Code format, not the portable Copilot user file. To choose a portable destination, use the [guided connection flow](/docs/agent-customization/mcp-servers.md#add-a-server-by-url-or-command). After installation, [verify a tool call](/docs/agent-customization/mcp-servers.md#verify-the-first-tool-call).

### Editor-managed settings

These settings control the editor's MCP client, which the deprecated Local harness uses. They don't configure native Copilot discovery, startup, or sampling.

| Setting | Description |
|---------|-------------|
| ``chat.mcp.discovery.enabled`` | Configure automatic discovery of MCP server configuration from other applications. |
| ``chat.mcp.autostart`` `feature(mcp-autostart)` | Control which MCP servers VS Code starts automatically when you submit a chat message. This setting doesn't prevent a Copilot harness session from starting servers it manages independently. See [MCP autostart behavior](/docs/agents/run/manage-mcp-servers.md#automatically-start-mcp-servers). |
| ``chat.mcp.serverSampling`` | Configure model access for editor-managed sampling. Copilot runtime sampling has a separate [approval flow](/api/extension-guides/ai/mcp.md#sampling). |

## Related resources

* [Add MCP servers](/docs/agent-customization/mcp-servers.md)
* [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md)
* [MCP tool extensibility overview](/api/extension-guides/ai/ai-extensibility-overview.md#mcp-tool)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/run/tools.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/run/tools
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/run/tools.md
- **SHA256_FINGERPRINT**: `1e0c80b7fa4eefc167b8523d1c473f88046ff5acb2f8a9b91239a0eccc5ad3a5`
- **LAST_VERIFIED_UTC**: 2026-11-11T05:26:59.608392+00:00
---

**MetaDescription**: Use agent tools in VS Code to inspect code, run commands, control desktop apps, and manage approvals.

# Use tools with agents

Tools let an agent inspect your project and check results instead of only suggesting code or commands for you to apply. For example, it can read the implementation behind a failing test, make a change, and run the test to check whether the change works.

Start with the tools already available in your session. Visual Studio Code supports built-in tools, Model Context Protocol (MCP) tools, and extension tools. When the task needs a capability these tools don't provide, connect a supported service to the Copilot harness with [Copilot connectors](/docs/agent-customization/copilot-connectors.md) `feature(copilot-connectors)`, [add an MCP server](/docs/agent-customization/mcp-servers.md), [install an agent plugin](/docs/agent-customization/agent-plugins.md#discover-and-install-plugins) that bundles MCP servers, or install an extension that contributes tools.

For background on tool types and how tools work in the agent loop, see [Tools concepts](/docs/agents/concepts/tools.md).

This article shows how to complete a request with tools, direct the agent to specific tools, control which tools are available, and review tool calls.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Try tools in action">
Launch a chat prompt that uses the web tool to summarize the latest VS Code updates.

* [Open in VS Code](vscode://GitHub.Copilot-Chat/chat?agent=agent%26prompt=Summarize%20the%20latest%20VS%20Code%20updates%20%23web)

</div>

## Use tools in a request

By default, the agent chooses from the enabled tools based on your request and the current context. You don't need to name or select each tool before you start.

To complete a request with tools:

1. In the chat input, select **Agent** from the agent picker.

1. Enter a prompt that describes your goal and how the agent should verify its work. For example:

    ```prompt
    Find the cause of the failing tests in this project, fix it, and run the relevant tests to verify the change.
    ```

1. Review each tool call as the agent works. If an approval prompt appears, expand the tool details to review its inputs, and then select the one-time approval option, such as **Allow Once**, to run it.

1. Expand a tool summary in the conversation to inspect the call and its output. When the task is complete, review the agent's response, code changes, and validation results.

To control which calls require approval and how much autonomy the agent has, see [Manage approvals and permissions](/docs/agents/run/approvals.md).

**Change how tool calls are grouped in chat**

By default, tool call details are collapsed in the chat conversation. Use ``chat.agent.thinking.collapsedTools`` (experimental) to change the grouping behavior. Use `off` to keep tool calls separate, `withThinking` to group tools with thinking when available, or `always` to always group tools. When ``chat.agent.thinkingStyle`` is set to `collapsed`, reasoning and grouped tool calls can appear in separate collapsible sections.

## Reference a tool explicitly

Type `#` in the chat input to reference an available tool. Use an explicit reference when you want to direct the agent to a particular capability instead of letting it choose. Tool names depend on the harness.

For example, use the `#web/fetch` tool to retrieve a specific web page:

```prompt
Summarize the latest release notes at code.visualstudio.com/updates with #web/fetch.
```

The `#` menu also contains context items, such as files, folders, and editor selections. Context items provide information for the request, while tools give the agent capabilities to gather information or take actions. Learn more about [adding context to chat prompts](/docs/chat/chat-overview.md#add-context-to-your-prompts).

> [!NOTE]
> User-defined tool sets are deprecated and are not supported in the Copilot harness. For a reusable tool selection, configure a custom agent. See [Replace tool sets](/docs/agent-customization/migrate-customizations.md#replace-tool-sets).

## Manage available tools

For Copilot harness sessions, manage client-tool availability from the Agent Customizations editor. Your selection persists for the selected harness across windows and [user profiles](/docs/configure/profiles.md), rather than applying to only one request. For remote sessions, selections are stored separately for each remote host and harness.

To change the selection:

1. Select the intended session and confirm its workspace and execution environment. In the chat input, select the **Copilot** harness.

1. Open the Agent Customizations editor:

    * In the Chat view, select **Open Customizations** in the title bar, or run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).
    * In the Agents window, select **Customizations** in the sidebar.

1. Select the **Tools** tab.

1. Select or deselect tools to control which ones are available to the agent.

The selected session supplies the editor's context, but changing a client-tool selection can affect other sessions using that harness and host. It isn't a session-only override. See [what customization changes affect](/docs/agent-customization/overview.md#understand-what-a-change-affects).

Limit the selection to tools that are relevant to your request. Add MCP tools by connecting supported services with [Copilot connectors](/docs/agent-customization/copilot-connectors.md) `feature(copilot-connectors)`, [adding MCP servers](/docs/agent-customization/mcp-servers.md), or [installing agent plugins](/docs/agent-customization/agent-plugins.md#discover-and-install-plugins) that bundle MCP servers. [Extensions](/docs/configure/extensions/extensions.md) can also contribute tools.

To define a reusable tool selection for a workflow, specify tools in a [custom agent](/docs/agent-customization/custom-agents.md). For other harnesses, check their [setup requirements and configuration options](/docs/agents/run/agent-harnesses.md#requirements-and-setup).

### Manage tool availability for the Copilot harness

All client-side tools are available to the Copilot harness by default. In the **Tools** tab, tools are organized into collapsible groups. You can:

* Enter text in the search box to filter tool groups and individual tools.
* Select a tool group checkbox to enable or disable every tool in the group.
* Expand a group and select individual tools. The group checkbox shows a mixed state when only some tools are enabled.
* Review the enabled and total tool counts shown for each group.

The count beside **Tools** in the customization navigation includes enabled client-side tools and excludes the read-only tools built into the Copilot harness.

The **Copilot** group lists the harness's built-in tools. These tools run in the Copilot runtime and are read-only in the **Tools** tab. Other tools run in the VS Code client and are available to the agent only while the client is connected.

Tool availability is separate from tool approval. Enabling a tool makes it available to the agent, but doesn't bypass the configured [approval and permission controls](/docs/agents/run/approvals.md).

### Add extension tools for the Copilot harness

In the main VS Code window, you can find extensions that contribute language model tools:

1. Open the **Tools** tab and select **Browse Marketplace**.

1. Search for an extension and select it to view its details and contributed tools.

1. Install the extension. Its tools then appear in the tool list, where you can manage their availability.

The Agents window shows the tool availability list but doesn't include Marketplace browsing.

To remove an extension from the tool list, right-click its tool group and select **Uninstall Extension**.

> [!CAUTION]
> Uninstalling a tool extension removes the entire extension, including contributions that aren't tools.

**Select tools for a Local harness request**

For Local harness sessions `feature(local-harness)`, select tools for an individual request from the Chat view:

1. In the chat input, select the **Local** harness `feature(local-harness)` and then select **Agent** from the agent picker.

1. Select **Configure Tools**.

    ![Screenshot showing the Chat view, highlighting the Configure Tools button in the chat input.](../images/chat-tools/agent-mode-select-tools.png)

1. Select or deselect tools to control which ones are available for the current request. Use the search box to filter the list.

You can also specify tools in a [prompt file](/docs/agent-customization/prompt-files.md) or [custom agent](/docs/agent-customization/custom-agents.md). Learn more about the [tool list priority order](/docs/agents/reference/custom-agent-file-reference.md#tool-list-priority).

## Edit tool parameters

For a tool call that requires approval, expand the confirmation dialog to review its input parameters. Generic and terminal tool confirmations are read-only. If a call needs different parameters, reject it and tell the agent what to change.

**Edit parameters in Local harness and extension tool confirmations**

Confirmations from the Local harness `feature(local-harness)` and extension-contributed tools can support parameter editing. When the confirmation provides editable fields:

1. When the tool confirmation dialog appears, select the chevron next to the tool name to expand its details.

1. Edit any tool input parameters as needed.

1. Select **Allow** to run the tool with the modified parameters.

## Common built-in tool workflows

### Coordinate work across sessions

In sessions using the Copilot or [product.prodname_anthropic_claude_short] harness, agents can use built-in session-management tools to coordinate related work. These tools are also available with the [experimental [product.prodname_openai_codex_short] integration](/docs/agents/run/agent-harnesses.md#codex).

An agent can:

* List sessions and inspect their status, workspace, and file changes.
* Create sessions or nested sessions.
* Read another conversation's recent context.
* Send messages to start or steer follow-up work.

State both the relationship between tasks and where the new work should run:

* **Related work**: Request a nested session that reuses the current workspace and checkout for research or planning that can share files.
* **Independent work**: Request a separate session. Omit the workspace for work that doesn't need repository files, or choose a trusted folder. Request a new worktree when code changes must be isolated.

For related, read-only work:

```prompt
Create a nested session under this session that reuses the current workspace and checkout to review the authentication flow. Do not modify files.
```

For unrelated work without repository files:

```prompt
Create an independent session with no workspace to research licensing options for a separate project.
```

For isolated implementation in a known project:

```prompt
Create an independent session in the vscode workspace with a new worktree to implement and test the authentication change.
```

The tools use `currentSession` for nested work and `independent` for separate sessions. A project name can identify the workspace instead of an absolute path or URI. If names are ambiguous, the agent reports matching projects rather than choosing one. Remote workspace URIs and multi-root project working directories are also supported.

When a tool creates or targets a session, an **Open Session** pill lets you jump to it. To monitor and finish the work yourself, see [Manage agent sessions](/docs/agents/run/sessions/manage-sessions.md).

Keep these constraints in mind:

* Sending a message to another session always requires confirmation.
* Agents can't send messages to the chat they are currently running in.
* Creation and messaging limits guard against unbounded fan-out.
* Archived sessions are excluded from listings unless explicitly requested.

The experimental ``chat.agentHost.agentOrchestrationLimits`` setting defaults to `on`. It limits how many sessions and chats each source session creates and how many messages it sends within a sliding one-hour window, as well as recursive session creation depth. A busy session doesn't consume another session's allowance, and capacity returns as earlier actions leave the window.

Setting it to `off` removes these limits without changing confirmation requirements or input validation. Changes apply without restarting the Agent Host. Reaching a limit doesn't interrupt work already running.

### Use browser tools

Browser tools give agents an interactive way to validate web applications. Instead of inspecting only the source code, an agent can run your app, open it in the integrated browser, exercise a user flow, inspect page content and console errors, and fix problems it discovers.

Browser tools are built into VS Code and don't require an external MCP server. Use them when a task has an observable result in a web interface, such as verifying a form, reproducing a visual bug, checking responsive behavior, or testing a complete user journey.

```prompt
Start the app, open it in the browser, and test the password reset flow.
Fix any issues you find and repeat the flow to verify the fix.
```

Learn how to [use browser tools with agents](/docs/agents/run/browser-tools.md), including browser sessions, page sharing, privacy controls, and effective prompting patterns.

### Run terminal commands

Of all the built-in tools, the terminal tool is one of the most frequently used. The agent uses it to run commands as part of its workflow, for example to install dependencies, run a build, or execute tests. Because terminal commands can change your environment, VS Code provides additional controls for reviewing, running, and monitoring them, building on the [approval](/docs/agents/run/approvals.md) behavior described earlier.

Copilot harness sessions use the built-in shell tool by default. Workspace commands run in the session's environment, and you review the results in chat. To load your shell profile before each command, see [Configure shell initialization](#configure-shell-initialization). The integrated-terminal controls below apply to Local harness sessions `feature(local-harness)` and configurations that use the integrated terminal tool.

**Integrated-terminal controls**

When the agent decides to run a command, it uses the built-in terminal tool to execute it in an integrated terminal within VS Code.

In the chat conversation, the agent displays the commands it ran. You can view the output of the command inline in chat by selecting **Show Output** (`>`) next to the command. You can also view the full output in the integrated terminal by selecting **Show Terminal**.

![Screenshot showing terminal command output in chat.](../images/chat-tools/terminal-command-output.png)

**Change where terminal output appears**

Use ``chat.tools.terminal.outputLocation`` (experimental) to show terminal command output inline in chat or directly in the integrated terminal.

Terminal output previews reflow to fit the available chat width by default. Turn off ``chat.tools.terminal.outputReflow`` to preserve the terminal's column width and use horizontal scrolling for long lines. This setting changes only the preview in chat, not the terminal that runs the command.

#### Continue terminal commands in background

When the agent runs a long-running terminal command, such as starting a development server or running a build in watch mode, you can push the command to the background. This allows the agent to continue with other tasks without waiting for the command to finish.

While a command is running, a **Continue in Background** button appears next to the terminal command in the chat conversation. Select this button to move the command to the background. The command continues running, and the agent can check its output later or use the terminal for other tasks.

The agent can also specify a timeout when running terminal commands. When the timeout is reached, the agent stops waiting for the command and returns the output collected so far. Use the ``chat.tools.terminal.enforceTimeoutFromModel`` setting to control whether to enforce the timeout value that the agent specifies.

The agent can also choose to run commands directly in the background, without user interaction. Background terminals that you have not revealed are automatically cleaned up when their command finishes, which prevents stale terminals from accumulating over a long session. To reveal a background terminal and keep it open after the command completes, select the **Show** link in the chat tool invocation header. The terminal output remains visible in the chat conversation even after a terminal is cleaned up.

> [!TIP]
> To automatically approve terminal commands or restrict file system and network access for agent commands, see [Manage approvals and permissions](/docs/agents/run/approvals.md).

#### Configure shell initialization

`feature(agent-host-shell-initialization)`

Keep agent shell commands aligned with your development environment by loading your shell profile. In [Copilot harness sessions](/docs/agents/run/agent-harnesses.md#copilot) running on your machine that use the SDK built-in shell tool, enable ``chat.agentHost.shellTool.initScript.enabled`` to load `~/.bashrc` on macOS and Linux or your PowerShell profiles on Windows before each command.

With [Python Environments](/docs/python/environments.md#terminal-settings) installed and ``python-envs.terminal.autoActivationType`` set to `shellStartup`, the selected workspace environment is also activated.

This setting does not apply to remote sessions or the custom terminal tool override.

## Control desktop applications

`feature(computer-use)`

Use [copilot.computer_use] when a task needs a desktop application that the agent's other tools can't reach. For web applications, use [browser tools](#use-browser-tools) instead.

[copilot.computer_use_caps] is available for local [Copilot harness sessions](/docs/agents/run/agent-harnesses.md#copilot) on macOS and Windows. It isn't available for the Local, Claude, or Codex harnesses, Linux, or remote or cloud hosts.

For shared capabilities, permission controls, and limitations, see [[product.prodname_github]'s [copilot.computer_use] guide](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/computer-use).

> [!CAUTION]
> [copilot.computer_use_caps] can read and change content in applications outside your workspace. Avoid exposing sensitive content in application windows, and review requested access and results.

### Turn on [copilot.computer_use]

[copilot.computer_use_caps] is off by default. To use it:

1. Turn on ``chat.agentHost.computerUse.enabled`` in Settings, and restart VS Code.

1. Start a new local Copilot chat in the Chat view or Agents window. The plugin downloads automatically on first use.

1. Run `/computer on` in the chat, or ask the agent to perform a task in a desktop application and follow the activation prompt.

1. On macOS, select **Set Up Computer Use** in the chat card and follow the prompts to grant the required system permissions. Review application-access requests when prompted.

> [!IMPORTANT]
> Activation persists across chats and also applies to Copilot CLI on the same computer.

### Turn off [copilot.computer_use]

Run `/computer off` in a Copilot chat to turn off [copilot.computer_use], including for Copilot CLI on the same computer.

To stop offering the integration in VS Code, turn off ``chat.agentHost.computerUse.enabled`` and restart.

### Troubleshoot [copilot.computer_use]

* **[copilot.computer_use_caps] isn't offered**: Check the supported platform and harness, confirm that the setting is on, and restart before starting a new chat. On first use, allow time for the plugin to download.
* **The agent doesn't ask to turn it on**: The activation prompt isn't shown in Autopilot or chats with automatic replies. Run `/computer on` yourself. Use the command if you previously selected **Not Now**, which suppresses further activation prompts in that chat.
* **The macOS setup dialog closes before you finish**: Finish granting permissions in System Settings, then ask the agent to retry the task.

## Built-in tools and context reference

For individual names, descriptions, and availability, see the [Tools and context reference](/docs/agents/reference/tools-reference.md). The reference groups tools by purpose and lists context items separately.

## Frequently asked questions

**How do I know which tools are available?**

Type `#` in the chat input field to browse available tools and context items. For Copilot harness sessions, open the Agent Customizations editor and select the **Tools** tab to view and manage enabled tools. For Local harness sessions `feature(local-harness)`, use **Configure Tools** in the chat input.

**I'm getting an error that says "Cannot have more than 128 tools per request."**

A chat request can have a maximum of 128 tools enabled at a time. If you see an error about exceeding 128 tools per request:

* Open the tools picker in the Chat view and deselect some tools or entire MCP servers to reduce the count.

* Alternatively, enable virtual tools with the ``github.copilot.chat.virtualTools.threshold`` setting to automatically manage large tool sets.

**Why isn't the agent using my configured terminal shell?**

The agent uses the shell you have configured as the default for the terminal, except for `cmd` (Command Prompt) on Windows and `sh` on macOS/Linux. This is because [shell integration](/docs/terminal/shell-integration.md) is not supported with these shells, which means the agent has very limited visibility into what's going on inside the terminal. Instead of getting direct signals for when commands are being run or have finished running, the agent needs to rely on timeouts and watching for the terminal to idle to continue. This leads to a slow and flaky experience.

You can still configure the agent to use these shells with the terminal profile settings, however this will result in an inferior experience compared to using PowerShell on Windows or `bash`/`zsh` on macOS/Linux.

* ``chat.tools.terminal.terminalProfile.windows`` - Override the shell on Windows
* ``chat.tools.terminal.terminalProfile.osx`` - Override the shell on macOS
* ``chat.tools.terminal.terminalProfile.linux`` - Override the shell on Linux

**Can I create my own tools?**

Yes. You can create tools in two ways:

* **Develop a VS Code extension** that contributes tools using the [Language Model Tools API](/api/extension-guides/ai/tools.md)
* **Create an MCP server** that provides tools. See the [MCP tool extensibility overview](/api/extension-guides/ai/ai-extensibility-overview.md#mcp-tool).

## Related resources

* [AI features cheat sheet](/docs/agents/reference/ai-features-cheat-sheet.md)
* [Migrate existing customizations](/docs/agent-customization/migrate-customizations.md)
* [Security considerations for using AI in VS Code](/docs/agents/run/security.md)
