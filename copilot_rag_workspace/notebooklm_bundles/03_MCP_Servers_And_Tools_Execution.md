# COMPENDIO RAG NOTEBOOKLM: 03_MCP_Servers_And_Tools_Execution
- **Generado (UTC)**: 2026-10-20T22:05:36.406787+00:00
- **Total Palabras**: 7,035 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/mcp-servers.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/mcp-servers
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/mcp-servers.md
- **SHA256_FINGERPRINT**: `601053fe1f6c6e4c9bd7d5dbf57e0f64235edb4210cbc541f0e4c0647ed11933`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.997103+00:00
---

**MetaDescription**: Connect MCP servers in VS Code to give agents external tools, then verify the first tool call.

# Add MCP servers in VS Code

Add an MCP server when your agent needs a capability its existing tools don't provide, such as querying a database or retrieving information from an external service. [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) connects agents to these tools and data sources. If your existing tools meet your needs, you don't need another server.

This article takes you from adding a server to verifying its first tool call. Choose your starting point:

* **I have a server URL or command:** [Connect a server](#connect-a-server).
* **Help me find a server:** [Choose a server to try](#choose-a-server-to-try).
* **My server is configured but isn't working:** [Check the connection](#if-the-server-does-not-work).

## Before you start

* [Enable AI features](/docs/getstarted/overview.md#enable-ai-features) and open a local project folder in VS Code.
* Check the server publisher's prerequisites. A remote HTTP server can require an account or sign-in. A server launched by a command needs its runtime installed on the machine that runs it.

> [!CAUTION]
> Local MCP servers can run code on your machine, and tools can access external services using your permissions. Review the publisher, command or endpoint, and requested access before installing or starting a server. Only trust configurations you have reviewed. Learn about [MCP server trust](/docs/agents/run/manage-mcp-servers.md#mcp-server-trust).

## Choose a server to try

For a concrete local example, use the [Playwright MCP server](https://github.com/microsoft/playwright-mcp). It requires **Node.js 18 or newer**, with `npx` available. Check your installation in a terminal:

```bash
node --version
npx --version
```

The walkthrough uses Playwright to demonstrate connecting an external tool provider. For everyday browser interaction, try the [built-in browser tools](/docs/agents/run/browser-tools.md) first: they don't require an MCP server.

To try a remote documentation server instead, follow the [Context7 setup requirements](https://context7.com/docs/resources/all-clients) for its current authentication requirements and service limits. Use the HTTP endpoint `https://mcp.context7.com/mcp` in the connection steps below. A remote server doesn't require a local Node.js installation.

<a name="add-an-mcp-server"></a>
<a name="add-a-server-from-the-agent-customizations-editor"></a>

## Connect a server

Use the publisher's URL or launch command. For the Playwright example, use the command in step two.

1. Open the Command Palette (``Shortcut: workbench.action.showCommands``) and run **MCP: Add Server**.

1. Choose the option that matches what the publisher provides:

    | What you have | Choose | Enter |
    |---------------|--------|-------|
    | A server URL | **HTTP (HTTP or Server-Sent Events)** | The publisher's MCP endpoint. |
    | A launch command | **Command (stdio)** | The command and its arguments. The server communicates through standard input and output. |

    For Playwright, choose **Command (stdio)** and enter:

    ```bash
    npx -y @playwright/mcp@latest
    ```

1. Enter a server ID, such as `playwright` or `context7`, that isn't already used in the destination configuration. Use distinct IDs for different servers you plan to use together.

1. For a personal configuration, select **Global**, and then **Copilot Global** when prompted. This stores the server outside your project. For team configurations or other harnesses, [choose a configuration destination](#choose-a-configuration-destination).

    If **Copilot Global** isn't available, check the [Copilot harness requirements](/docs/agents/run/agent-harnesses.md#copilot) before continuing with this walkthrough.

1. Review any server trust or authentication prompts before accepting them. Follow the publisher's sign-in instructions if the service requires authentication. Do not paste credentials into chat or commit them to your project.

You can also start the guided flow from **Chat: Open Customizations** > **MCP Servers** > **Add Server**. The editor is scoped to the selected agent harness.

For other ways to add a server, see [Find another server](#find-another-server).

## Verify the first tool call

Adding a configuration isn't proof that the agent can use the server. Complete a request and inspect the tool call:

1. In the agent session, enter a prompt that explicitly names the server and a low-impact action. For Playwright:

    ```prompt
    Use the Playwright MCP server to open <your URL here> and report the page title. Use its tools, not the built-in browser tools. Do not change files.
    ```

    For Context7:

    ```prompt
    Use the Context7 MCP tools to look up the React documentation for useState. Summarize the basic usage and cite the documentation returned by the tool. Do not change files.
    ```

1. Review startup, sign-in, and tool approval requests as they appear. Approve only actions you understand.

1. Expand the tool call in the conversation. Check that it belongs to the server you added and inspect its returned output.

**Your connection works when all three checks pass:**

* A tool from the intended MCP server was called in your session.
* The tool returned the requested page or documentation without a connection error.
* The agent's answer reflects that tool output. A plausible answer alone isn't sufficient.

To control available tools in a Copilot session, open **Chat: Open Customizations** > **Tools**. For Local harness sessions, use **Configure Tools** in the chat input. See [Manage available tools](/docs/agents/run/tools.md#manage-available-tools) for the differences.

## Find another server

Use the MCP server gallery (Preview) to browse publishers and capabilities:

1. Open the Extensions view (``Shortcut: workbench.view.extensions``) and search for `@mcp`.

1. Select a server and review its publisher, capabilities, and installation requirements.

1. Select **Install** for a personal installation, or right-click and select **Install in Workspace** to share its configuration with the project.

1. Complete the publisher's setup, and then [verify a tool call](#verify-the-first-tool-call).

If the gallery isn't available, use a publisher-provided URL or command with [MCP: Add Server](#connect-a-server). Your organization can restrict which servers are available.

You can also open the gallery with **MCP: Add Server** > **Browse MCP Servers...**. Choose **Add from another application...** in the same picker to [discover existing server configurations](/docs/agents/reference/mcp-configuration.md#automatic-mcp-server-discovery).

<details>
<summary>Add from a package or Docker image (model-assisted)</summary>

If you have a package or image name instead of a launch command, use model assistance to generate the server configuration:

1. Run **MCP: Add Server** and select **NPM Package**, **Pip Package**, or **Docker Image**.
1. [Choose a configuration destination](#choose-a-configuration-destination), then enter the package or image name when prompted. For example, enter `@playwright/mcp` for **NPM Package**.
1. Review the package name, version, and publisher shown in the confirmation. Select **Allow** only if you trust the source, then follow the model-assisted setup prompts.
1. Confirm a server ID that isn't already used in the destination configuration. Review the generated command, arguments, and credential requirements before accepting any server trust or tool approval prompts.
1. [Verify a tool call](#verify-the-first-tool-call) from the added server.

These options appear only when model-assisted setup is supported in your current configuration. If they aren't available, use the publisher's launch command with **Command (stdio)**. Runtime prerequisites still apply: generating a configuration doesn't replace installing the required runtime.

</details>

<details>
<summary>Discover servers in the Customization Marketplace (Experimental)</summary>

For a Copilot session, turn on ``chat.customizations.marketplace.enabled``, open **Chat: Open Customizations**, and select **Discover**. Select **GitHub Feed** from the source menu and search by name or with `@type:mcp`. Review the server and select **Install**.

Availability depends on the harness and your organization's marketplace policies. If automatic installation isn't supported, follow the publisher's instructions. Learn about [marketplace discovery](/docs/agent-customization/overview.md#discover-marketplace-customizations-experimental).

</details>

## Choose a configuration destination

Choose a destination based on who needs the server and which harness runs it:

| Your goal | Configuration |
|-----------|---------------|
| Use a server across your workspaces | **Global** > **Copilot Global** writes to `$COPILOT_HOME/mcp-config.json`, or `~/.copilot/mcp-config.json` when `COPILOT_HOME` is unset. |
| Share a server with a team using compatible Copilot tools | Workspace-root `.mcp.json`. The guided flow offers this destination when the Experimental ``chat.mcp.workspaceRootConfig.enabled`` setting is on. |
| Use a Local harness configuration with input variables or per-server sandboxing | Workspace `.vscode/mcp.json` or user-profile `mcp.json`. These destinations remain available for compatibility and are labeled deprecated in the guided flow. |

Portable files use a top-level `mcpServers` object. The VS Code format uses `servers`. Don't copy a configuration between them without checking the [format and capability reference](/docs/agents/reference/mcp-configuration.md#configuration-file).

> [!IMPORTANT]
> Portable configurations don't support VS Code input variables or environment files. Servers requiring interactive inputs aren't forwarded to Copilot harness sessions. Use the [authentication guidance for your configuration](/docs/agents/reference/mcp-configuration.md#authentication-and-secrets), rather than adding unsupported credential placeholders.

To reuse an existing setup from other applications, see [automatic discovery](/docs/agents/reference/mcp-configuration.md#automatic-mcp-server-discovery). For [Dev Containers](/docs/agents/run/manage-mcp-servers.md#remote-workspaces-and-dev-containers) or [command-line installation](/docs/agents/reference/mcp-configuration.md#command-line-installation), follow the environment-specific instructions.

## Use context and prompts from your server

Servers can provide more than tools. Available capabilities depend on the server and your session:

* **Resources:** attach server-provided data to a request from **Add Context** > **MCP Resources**, or run **MCP: Browse Resources**.

* **Prompts:** use a server's prompt template by typing `/<server>.<prompt>` in chat.

* **MCP Apps (Experimental):** supported servers can display interactive forms or visualizations in chat. See [MCP Apps support](https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support).

## If the server does not work

| What you observe | Next step |
|------------------|-----------|
| The server doesn't appear or cannot start | Check its configuration scope, runtime requirements, and [server output](/docs/agents/run/manage-mcp-servers.md#view-server-output). |
| Sign-in or a connection fails | Check the publisher's authentication instructions and your organization's access restrictions. See [MCP troubleshooting](/docs/agents/run/manage-mcp-servers.md#troubleshoot-mcp-servers). |
| The server runs, but no tool from it is called | Check [tool availability and invocation](/docs/agents/agent-troubleshooting/chat-debug-view.md#an-mcp-tool-is-not-being-invoked). |

After correcting the problem, repeat the request and inspect the tool output again.

## Manage an existing server

Continue with [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md) to change a connection, stop or remove a server, review trust and startup behavior, or share configuration across environments.

For specific tasks, see [MCP sandboxing](/docs/agents/run/manage-mcp-servers.md#sandbox-mcp-servers), [configuration synchronization](/docs/agents/run/manage-mcp-servers.md#synchronize-mcp-configuration-across-devices), or [enterprise access management](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist).

## Related resources

* [Use tools with agents](/docs/agents/run/tools.md)
* [MCP configuration reference](/docs/agents/reference/mcp-configuration.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/reference/mcp-configuration.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/reference/mcp-configuration
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/reference/mcp-configuration.md
- **SHA256_FINGERPRINT**: `dea186e8913463af3fd3138b356de353095cecf4eadd13a2f7e0b8e4132ab271`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.233435+00:00
---

**MetaDescription**: Configure MCP servers in Visual Studio Code with reference details for file formats, commands, settings, and sandboxing.

# MCP configuration reference

This article provides the MCP configuration formats, supported fields, commands, and settings in VS Code. To connect your first server, see [Add MCP servers](/docs/agent-customization/mcp-servers.md). For operational tasks, see [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md).

## Configuration file

MCP server configuration uses one of the following file formats:

* The VS Code format is stored in `.vscode/mcp.json` in your workspace or in your [user profile](/docs/configure/profiles.md). It defines servers in a top-level `servers` object. VS Code provides IntelliSense for this format.
* The portable Copilot format is stored in `.mcp.json` at the root of your workspace or in `$COPILOT_HOME/mcp-config.json` for your user, with `~/.copilot/mcp-config.json` as the fallback location. It defines servers in a top-level `mcpServers` object.

Copilot harness sessions read the portable format directly. VS Code forwards eligible servers from the VS Code format to the session, except servers that require interactive input, such as `${input:...}` variables. The agent doesn't read `.vscode/mcp.json` directly. For setup steps, see [Choose a configuration destination](/docs/agent-customization/mcp-servers.md#choose-a-configuration-destination).

For other providers, use the provider's MCP configuration documentation. Their configuration locations and schemas can differ from the two formats described here.

The formats and locations differ in the capabilities they support:

| Capability | Workspace or profile `mcp.json` | Workspace-root `.mcp.json` | Copilot user `mcp-config.json` |
|------------|---------------------------------|----------------------------|--------------------------------|
| Top-level server object | `servers` | `mcpServers` | `mcpServers` |
| Agent Customizations editor | Read-only JSON | Configuration form | Configuration form |
| Server transports | stdio, HTTP, and SSE | stdio and HTTP | stdio, HTTP, and SSE |
| Working directory | Yes | No | Yes |
| Environment file | Yes | No | No |
| VS Code input variables | Yes | No | No |
| Development mode and per-server sandboxing | Yes | No | No |

The configuration form preserves properties that it doesn't display. Select **Other Properties** in the form to open the complete server entry in JSON.

### Portable configuration

Use a top-level `mcpServers` object in workspace-root `.mcp.json` or Copilot user `mcp-config.json`. This example configures one local Playwright server:

```json
{
    "mcpServers": {
        "playwright": {
            "command": "npx",
            "args": ["-y", "@playwright/mcp@latest"]
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
            "url": "https://mcp.context7.com/mcp"
        }
    }
}
```

Follow the [Context7 setup instructions](https://context7.com/docs/resources/all-clients) for authentication and service limits. An endpoint alone doesn't grant access to a service.

The property tables below describe the VS Code format, not a shared schema for all MCP clients. Check the [capability comparison](#configuration-file) before copying properties into a portable file.

### Configuration structure

The following structure applies to the VS Code format. The portable Copilot format uses a separate schema with a top-level `mcpServers` object.

The configuration file has three main sections:

* **`"servers": {}`**: an object that maps server names to their configurations. Each key is the server name, and the value is the server configuration object. Depending on the server type, different fields are required.

* **`"inputs": []`**: an optional array of input variable definitions for sensitive information like API keys.

* **`"sandbox": {}`**: an optional object that defines file system and network access rules for sandboxed servers. See [Sandbox configuration](#sandbox-configuration). Only applies on macOS and Linux.

You can use [predefined variables](/docs/reference/variables-reference.md) in the server configuration, for example to refer to the workspace folder (`${workspaceFolder}`).

### Standard I/O (stdio) servers

Use this configuration for servers that communicate through standard input and output streams. This is the most common type for locally-run MCP servers.

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

<details>
<summary>Example local server configuration</summary>

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

</details>

### Sandbox configuration

You can enable sandboxing for locally-running stdio MCP servers to restrict their access to the file system and network. Sandbox rules can deny file access, grant write access, and grant access to specific network domains. Sandboxing is available on macOS and Linux only.

To enable sandboxing for a server, set `"sandboxEnabled": true` in its configuration. Add a `sandbox` object to the server to define its file system and network permissions. You can also add a top-level `sandbox` object as a sibling of `servers` and `inputs` to define deny rules that apply to all sandboxed servers in the file.

Allow rules are supported only in a server's `sandbox` object. Top-level `allowWrite` and `allowedDomains` rules are ignored.

> [!NOTE]
> When sandboxing is enabled, tool confirmations are auto-approved because the server runs in a controlled environment.

The server-level and top-level `sandbox` objects support the following properties:

| Property | Type | Supported scope | Description |
|----------|------|-----------------|-------------|
| `filesystem.allowWrite` | string[] | Server only | File paths that the server is allowed to write to. |
| `filesystem.denyRead` | string[] | Server and top level | File paths that the server is not allowed to read. |
| `filesystem.denyWrite` | string[] | Server and top level | File paths that the server is not allowed to write to. |
| `network.allowedDomains` | string[] | Server only | Domains that the server is allowed to access. Wildcards are supported, for example `*.example.com`. |
| `network.deniedDomains` | string[] | Server and top level | Domains that the server is not allowed to access. |

You can use [predefined variables](/docs/reference/variables-reference.md), such as `${workspaceFolder}`, in file system path values.

<details>
<summary>Example sandbox configuration</summary>

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

</details>

### HTTP and Server-Sent Events (SSE) servers

Use this configuration for servers that communicate over HTTP. VS Code first tries the HTTP Stream transport and falls back to SSE if HTTP is not supported.

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

<details>
<summary>Example remote server configuration</summary>

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

</details>

<details>
<summary>Example HTTP server with OAuth</summary>

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

</details>

### Authentication and secrets

Authentication grants access to an external service. It is separate from trusting a server to start and approving individual tool calls.

Choose an authentication method that both the server and your configuration support:

| Server requirement | Guidance |
|--------------------|----------|
| Browser sign-in or OAuth | Follow the publisher's connection instructions and review the requested permissions. Complete the authorization flow when prompted. The `oauth` fields above apply to the VS Code format. |
| Environment variables for a local server | Follow the publisher's instructions to provide credentials in the environment that launches the server. Configure them on the machine where the server runs, not only in an unrelated terminal or on your local machine for a remote server. |
| VS Code input prompts | Use the [input variables](#input-variables-for-sensitive-data) supported by the VS Code format. Servers requiring these interactive inputs aren't forwarded to Copilot harness sessions. |
| An environment file | `envFile` is supported in the VS Code format, not in portable `.mcp.json` or Copilot user `mcp-config.json`. Keep files containing credentials out of source control. |

Do not commit tokens, passwords, or populated authentication headers. A personal configuration file is not a secret store. For a server that requires a fixed token, follow its publisher's secure configuration guidance for your client and harness rather than copying credentials into a shared example.

### Input variables for sensitive data

Input variables in the VS Code format let you define placeholders for values such as API keys or passwords. They aren't supported in portable configuration files, and servers that require them aren't forwarded to Copilot harness sessions.

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

<details>
<summary>Example server configuration with input variables</summary>

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

</details>

### Development mode

You can enable _development mode_ for MCP servers by adding a `dev` key to the server configuration. This is an object with two properties:

* `watch`: A glob pattern, or an array of glob patterns, to watch for file changes that restart the MCP server. Available for all server types.
* `debug`: Enables you to set up a debugger with the MCP server. Currently, VS Code supports debugging Node.js and Python MCP servers. Available for stdio servers only.

Learn more about [MCP development mode](/api/extension-guides/ai/mcp.md#mcp-development-mode-in-vs-code) in the MCP Dev Guide.

### Server naming conventions

When defining MCP servers, follow these naming conventions for the server name:

* Use camelCase for the server name, such as "uiTesting" or "githubIntegration"
* Avoid using whitespace or special characters
* Use a unique name for each server to avoid conflicts
* Use a descriptive name that reflects the server's functionality or brand, such as "github" or "database"

## Automatic MCP server discovery

VS Code can automatically detect and reuse MCP server configurations from supported applications. Use ``chat.mcp.discovery.enabled`` to select the discovery sources.

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

## Commands

The following table lists the MCP-related commands available in the Command Palette (``Shortcut: workbench.action.showCommands``).

| Command | Description |
|---------|-------------|
| **MCP: Add Server** | Add a new MCP server to your workspace or user profile. |
| **MCP: Browse MCP Servers** | Open the MCP server gallery in the Extensions view. |
| **MCP: Browse Resources** | Browse resources provided by MCP servers. |
| **MCP: Install Server from Manifest** | Install an MCP server from an MCP manifest file. |
| **MCP: List Servers** | List all configured MCP servers and perform actions like start, stop, restart, or show output. |
| **MCP: Open Remote User Configuration** | Open the `mcp.json` file for the remote environment. |
| **MCP: Open User Configuration** | Open the `mcp.json` file in your user profile. |
| **MCP: Open Workspace Folder MCP Configuration** | Open the `.vscode/mcp.json` file in your workspace. |
| **MCP: Reset Cached Tools** | Clear the cached list of tools for MCP servers. Use this when a server's tools have changed. |
| **MCP: Reset Trust** | Reset separate trust decisions for MCP servers from non-workspace sources. Workspace MCP servers inherit Workspace Trust and are unaffected. |
| **MCP: Show Installed Servers** | Show a list of all installed MCP servers. |

### Command-line installation

Use `code --add-mcp` with a JSON object containing a unique `name` and the server configuration. The command adds a server to the VS Code user-profile configuration.

For example, from a Bash shell:

```bash
code --add-mcp '{"name":"playwright","type":"stdio","command":"npx","args":["-y","@playwright/mcp@latest"]}'
```

This uses the VS Code format, not the portable Copilot user file. To choose a portable destination, use the [guided connection flow](/docs/agent-customization/mcp-servers.md#connect-a-server). After installation, [verify a tool call](/docs/agent-customization/mcp-servers.md#verify-the-first-tool-call).

## Settings

For a full list of VS Code AI settings, see the [AI Settings Reference](/docs/agents/reference/ai-settings.md). The following settings are specific to MCP servers.

| Setting | Description |
|---------|-------------|
| ``chat.mcp.access`` | Manage which MCP servers can be used in VS Code. |
| ``chat.mcp.discovery.enabled`` | Configure automatic discovery of MCP server configuration from other applications. |
| ``chat.mcp.workspaceRootConfig.enabled`` | (Experimental) Control whether **MCP: Add Server** offers the workspace-root `.mcp.json` destination. Existing `.mcp.json` files remain available when this setting is off. |
| ``chat.mcp.autostart`` `feature(mcp-autostart)` | Control which MCP servers VS Code starts automatically when you submit a chat message. This setting doesn't prevent a Copilot harness session from starting servers it manages independently. See [MCP autostart behavior](/docs/agents/run/manage-mcp-servers.md#automatically-start-mcp-servers). |
| ``chat.mcp.serverSampling`` | Configure which models are exposed to MCP servers for sampling (making requests in the background). |
| ``chat.mcp.apps.enabled`` `feature(mcp-apps)` | Enable or disable MCP Apps, which are rich user interfaces provided by MCP servers. |
| ``accessibility.verbosity.mcpServerConfiguration`` | Control whether the MCP server configuration form announces information about opening Accessibility Help. |

## Related resources

* [Add MCP servers](/docs/agent-customization/mcp-servers.md)
* [Manage and troubleshoot MCP servers](/docs/agents/run/manage-mcp-servers.md)
* [MCP tool extensibility overview](/api/extension-guides/ai/ai-extensibility-overview.md#mcp-tool)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agents/run/tools.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agents/run/tools
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/run/tools.md
- **SHA256_FINGERPRINT**: `1509497cf306f5d2781c4d44c1c751bf628e34f420337192ee218a05dbf6ebe6`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:31.716328+00:00
---

**MetaDescription**: Use and manage agent tools in VS Code, including automatic selection, approvals, and terminal commands.

# Use tools with agents

Tools let an agent inspect your project and check results instead of only suggesting code or commands for you to apply. For example, it can read the implementation behind a failing test, make a change, and run the test to check whether the change works.

Start with the tools already available in your session. Visual Studio Code supports built-in tools, Model Context Protocol (MCP) tools, and extension tools. Add an [MCP server](/docs/agent-customization/mcp-servers.md) or extension when the task needs a capability the available tools don't provide.

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

1. Review each tool call as the agent works. If an approval prompt appears, expand the tool details to review its inputs, and then select **Allow** to run it.

1. Expand a tool summary in the conversation to inspect the call and its output. When the task is complete, review the agent's response, code changes, and validation results.

To control which calls require approval and how much autonomy the agent has, see [Manage approvals and permissions](/docs/agents/run/approvals.md).

<details>
<summary>Change how tool calls are grouped in chat</summary>

By default, tool call details are collapsed in the chat conversation. Use ``chat.agent.thinking.collapsedTools`` (experimental) to change the grouping behavior. Use `off` to keep tool calls separate, `withThinking` to group tools with thinking when available, or `always` to always group tools. When ``chat.agent.thinkingStyle`` is set to `collapsed`, reasoning and grouped tool calls can appear in separate collapsible sections.

</details>

## Reference a tool explicitly

Type `#` in the chat input to reference a specific tool or tool set. Use an explicit reference when you want to direct the agent to a particular capability instead of letting it choose.

For example, use the `#web/fetch` tool to retrieve a specific web page:

```prompt
Summarize the latest release notes at code.visualstudio.com/updates with #web/fetch.
```

Use a tool set, such as `#web`, to make a group of related tools available:

```prompt
Research how Next.js handles routing. Use #web tools and summarize the relevant guidance.
```

The `#` menu also contains context items, such as files, folders, and editor selections. Context items provide information for the request, while tools give the agent capabilities to gather information or take actions. Learn more about [adding context to chat prompts](/docs/chat/chat-overview.md#add-context-to-your-prompts).

> [!NOTE]
> **For Local harness sessions:** To group related tools and reuse them across prompts, prompt files, and custom agents, [create a tool set](/docs/agent-customization/tool-sets.md).

<a name="select-tools-for-a-request"></a>

## Manage available tools

For Copilot harness sessions, manage tools from the Agent Customizations editor. Your selection persists in the active [user profile](/docs/configure/profiles.md), rather than applying to only one request:

1. In the chat input, select the **Copilot** harness.

1. Open the Agent Customizations editor:

    * In the Chat view, select **Open Customizations** in the title bar, or run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).
    * In the Agents window, go to the **Customizations** panel.

1. Select the **Tools** tab.

1. Select or deselect tools to control which ones are available to the agent.

Limit the selection to tools that are relevant to your request. Add capabilities by [installing MCP servers](/docs/agent-customization/mcp-servers.md) or [extensions](/docs/configure/extensions/extensions.md) that contribute tools.

To define a reusable tool selection for a workflow, specify tools in a [custom agent](/docs/agent-customization/custom-agents.md). For other harnesses, check their [setup requirements and configuration options](/docs/agents/run/agent-harnesses.md#requirements-and-setup).

<a name="manage-tool-availability-for-copilot"></a>

### Manage tool availability for the Copilot harness

All client-side tools are available to the Copilot harness by default. In the **Tools** tab, tools are organized into collapsible groups. You can:

* Enter text in the search box to filter tool groups and individual tools.
* Select a tool group checkbox to enable or disable every tool in the group.
* Expand a group and select individual tools. The group checkbox shows a mixed state when only some tools are enabled.
* Review the enabled and total tool counts shown for each group.

The count beside **Tools** in the customization navigation includes enabled client-side tools and excludes the read-only tools built into the Copilot harness.

The **Copilot** group lists the harness's built-in tools. These tools run in the Copilot runtime and are read-only in the **Tools** tab. Other tools run in the VS Code client and are available to the agent only while the client is connected.

Tool availability is separate from tool approval. Enabling a tool makes it available to the agent, but doesn't bypass the configured [approval and permission controls](/docs/agents/run/approvals.md).

<a name="add-extension-tools-for-copilot"></a>

### Add extension tools for the Copilot harness

In the main VS Code window, you can find extensions that contribute language model tools:

1. Open the **Tools** tab and select **Browse Marketplace**.

1. Search for an extension and select it to view its details and contributed tools.

1. Install the extension. Its tools then appear in the tool list, where you can manage their availability.

The Agents window shows the tool availability list but doesn't include Marketplace browsing.

To remove an extension from the tool list, right-click its tool group and select **Uninstall Extension**.

> [!CAUTION]
> Uninstalling a tool extension removes the entire extension, including contributions that aren't tools.

<details>
<summary>Select tools for a Local harness request</summary>

For Local harness sessions, select tools for an individual request from the Chat view:

1. In the chat input, select the **Local** harness and then select **Agent** from the agent picker.

1. Select **Configure Tools**.

    ![Screenshot showing the Chat view, highlighting the Configure Tools button in the chat input.](../images/chat-tools/agent-mode-select-tools.png)

1. Select or deselect tools to control which ones are available for the current request. Use the search box to filter the list.

You can also specify tools in a [prompt file](/docs/agent-customization/prompt-files.md) or [custom agent](/docs/agent-customization/custom-agents.md). Learn more about the [tool list priority order](/docs/agents/reference/custom-agent-file-reference.md#tool-list-priority).

</details>

## Edit tool parameters

For a tool call that requires approval, expand the confirmation dialog to review its input parameters. Generic and terminal tool confirmations are read-only. If a call needs different parameters, reject it and tell the agent what to change.

<details>
<summary>Edit parameters in Local harness and extension tool confirmations</summary>

Confirmations from the Local harness and extension-contributed tools can support parameter editing. When the confirmation provides editable fields:

1. When the tool confirmation dialog appears, select the chevron next to the tool name to expand its details.

1. Edit any tool input parameters as needed.

1. Select **Allow** to run the tool with the modified parameters.

</details>

## Common built-in tool workflows

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

Copilot harness sessions use the built-in shell tool by default. Workspace commands run in the session's environment, and you review the results in chat. To load your shell profile before each command, see [Configure shell initialization](#configure-shell-initialization). The integrated-terminal controls below apply to Local harness sessions and configurations that use the integrated terminal tool.

<details>
<summary>Integrated-terminal controls</summary>

When the agent decides to run a command, it uses the built-in terminal tool to execute it in an integrated terminal within VS Code.

In the chat conversation, the agent displays the commands it ran. You can view the output of the command inline in chat by selecting **Show Output** (`>`) next to the command. You can also view the full output in the integrated terminal by selecting **Show Terminal**.

![Screenshot showing terminal command output in chat.](../images/chat-tools/terminal-command-output.png)

<details>
<summary>Change where terminal output appears</summary>

Use ``chat.tools.terminal.outputLocation`` (experimental) to show terminal command output inline in chat or directly in the integrated terminal.

</details>

Terminal output previews reflow to fit the available chat width by default. Turn off ``chat.tools.terminal.outputReflow`` to preserve the terminal's column width and use horizontal scrolling for long lines. This setting changes only the preview in chat, not the terminal that runs the command.

#### Continue terminal commands in background

When the agent runs a long-running terminal command, such as starting a development server or running a build in watch mode, you can push the command to the background. This allows the agent to continue with other tasks without waiting for the command to finish.

While a command is running, a **Continue in Background** button appears next to the terminal command in the chat conversation. Select this button to move the command to the background. The command continues running, and the agent can check its output later or use the terminal for other tasks.

The agent can also specify a timeout when running terminal commands. When the timeout is reached, the agent stops waiting for the command and returns the output collected so far. Use the ``chat.tools.terminal.enforceTimeoutFromModel`` setting to control whether to enforce the timeout value that the agent specifies.

The agent can also choose to run commands directly in the background, without user interaction. Background terminals that you have not revealed are automatically cleaned up when their command finishes, which prevents stale terminals from accumulating over a long session. To reveal a background terminal and keep it open after the command completes, select the **Show** link in the chat tool invocation header. The terminal output remains visible in the chat conversation even after a terminal is cleaned up.

</details>

> [!TIP]
> To automatically approve terminal commands or restrict file system and network access for agent commands, see [Manage approvals and permissions](/docs/agents/run/approvals.md).

#### Configure shell initialization

`feature(agent-host-shell-initialization)`

Keep agent shell commands aligned with your development environment by loading your shell profile. In [Copilot harness sessions](/docs/agents/run/agent-harnesses.md#copilot) running on your machine that use the SDK built-in shell tool, enable ``chat.agentHost.shellTool.initScript.enabled`` to load `~/.bashrc` on macOS and Linux or your PowerShell profiles on Windows before each command.

With [Python Environments](/docs/python/environments.md#terminal-settings) installed and ``python-envs.terminal.autoActivationType`` set to `shellStartup`, the selected workspace environment is also activated.

This setting does not apply to remote sessions or the custom terminal tool override.

## Built-in tools and context reference

For individual names, descriptions, and availability, see the [Tools and context reference](/docs/agents/reference/tools-reference.md). The reference groups tools by purpose and lists context items separately.

## Frequently asked questions

<details>
<summary>How do I know which tools are available?</summary>

Type `#` in the chat input field to browse available tools, tool sets, and context items. For Copilot harness sessions, open the Agent Customizations editor and select the **Tools** tab to view and manage enabled tools. For Local harness sessions, use **Configure Tools** in the chat input.

</details>

<details>
<summary>I'm getting an error that says "Cannot have more than 128 tools per request."</summary>

A chat request can have a maximum of 128 tools enabled at a time. If you see an error about exceeding 128 tools per request:

* Open the tools picker in the Chat view and deselect some tools or entire MCP servers to reduce the count.

* Alternatively, enable virtual tools with the ``github.copilot.chat.virtualTools.threshold`` setting to automatically manage large tool sets.

</details>

<details>
<summary>Why isn't the agent using my configured terminal shell?</summary>

The agent uses the shell you have configured as the default for the terminal, except for `cmd` (Command Prompt) on Windows and `sh` on macOS/Linux. This is because [shell integration](/docs/terminal/shell-integration.md) is not supported with these shells, which means the agent has very limited visibility into what's going on inside the terminal. Instead of getting direct signals for when commands are being run or have finished running, the agent needs to rely on timeouts and watching for the terminal to idle to continue. This leads to a slow and flaky experience.

You can still configure the agent to use these shells with the terminal profile settings, however this will result in an inferior experience compared to using PowerShell on Windows or `bash`/`zsh` on macOS/Linux.

* ``chat.tools.terminal.terminalProfile.windows`` - Override the shell on Windows
* ``chat.tools.terminal.terminalProfile.osx`` - Override the shell on macOS
* ``chat.tools.terminal.terminalProfile.linux`` - Override the shell on Linux

</details>

<details>
<summary>Can I create my own tools?</summary>

Yes. You can create tools in two ways:

* **Develop a VS Code extension** that contributes tools using the [Language Model Tools API](/api/extension-guides/ai/tools.md)
* **Create an MCP server** that provides tools. See the [MCP tool extensibility overview](/api/extension-guides/ai/ai-extensibility-overview.md#mcp-tool).

</details>

## Related resources

* [AI features cheat sheet](/docs/agents/reference/ai-features-cheat-sheet.md)
* [Create and use tool sets](/docs/agent-customization/tool-sets.md)
* [Security considerations for using AI in VS Code](/docs/agents/run/security.md)
