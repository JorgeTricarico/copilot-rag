# COMPENDIO RAG NOTEBOOKLM: 04_Customization_Skills_Hooks_And_Plugins
- **Generado (UTC)**: 2026-10-20T22:05:36.685844+00:00
- **Total Palabras**: 30,924 / 500,000 máx.
- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` declarados en el encabezado de cada sección.


---
# DOCUMENT_SOURCE: github_docs::content/copilot/reference/hooks-reference.md
- **CANONICAL_URL**: https://docs.github.com/en/copilot/reference/hooks-reference
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/github/docs/main/content/copilot/reference/hooks-reference.md
- **SHA256_FINGERPRINT**: `3b9649c93476f2b7870f06579c4745dcdfb33adaefaa3e5e02bb395d03c6b8e7`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:34.113299+00:00
---

**title**: GitHub Copilot hooks reference
**shortTitle**: Hooks reference
**intro**: Find hook events, configuration formats, and input payloads for hooks in Copilot CLI and Copilot cloud agent.

## Introduction

Hooks are external commands that execute at specific lifecycle points during a session, enabling custom automation, security controls, and integrations.

Hooks are supported in two Copilot surfaces: Copilot CLI and Copilot cloud agent. Most of the configuration format and event payloads are identical, but the execution environment and the set of events that can fire differ.

Throughout this article, behavior that differs between the two surfaces is called out in "CLI only" and "Cloud agent only" notes. Anything not marked applies to both.

## Hooks locations

The locations where hooks run, and where you can store hook configuration files, depend on the surface:

* **Copilot CLI** — hooks run on the developer's local machine in the same shell as the CLI. All hook events described in this article are supported by the CLI.

  Hooks are loaded from the following sources in order (policy, then user, then project, then plugins) and combined. When the same event appears in multiple sources, all hook entries from all sources are run.

  * **Policy-level hook files** — JSON files in the platform-appropriate policy directory, loaded in alphabetical order. Policy hooks are machine-wide and load before all other hooks. They cannot be disabled by `disableAllHooks` and are available regardless of folder trust state. See [Policy hooks](#policy-hooks) below.
  * **Repository-level hook files** — `.github/hooks/*.json` in the repository root.
  * **User-level hook files** — `*.json` files in the user-level hooks directory. By default this is `~/.copilot/hooks/` on macOS and Linux, or `%USERPROFILE%\.copilot\hooks\` on Windows. If `COPILOT_HOME` is set, it is `$COPILOT_HOME/hooks/`.
  * **Inline `hooks` block in repository settings** — the `hooks` field at the top level of `.github/copilot/settings.json` (Git committed) or `.github/copilot/settings.local.json` (typically gitignored and user specific) in the repository. Cross-tool `.claude/settings.json` and `.claude/settings.local.json` files in the repository are also read.
  * **Inline `hooks` block in user-level config** — the `hooks` field at the top level of `~/.copilot/settings.json`. The CLI no longer reads `~/.copilot/config.json` for hooks.
  * **Hooks contributed by installed plugins** — declared by each plugin in its own `hooks.json` (or under `hooks/hooks.json`) inside the plugin's installation directory.

* **Copilot cloud agent** — hooks run inside the ephemeral Linux sandbox that cloud agent provisions for each job. The sandbox is non-interactive, has a constrained network, and is destroyed when the job ends. A subset of events fires, and only `bash` (or `command`) entries are honored.

  Hook configuration is loaded from `.github/hooks/*.json` files in the cloned repository.

### Policy hooks

> [!NOTE]
> **Copilot CLI only.** Policy hooks are not supported under Copilot cloud agent.

Policy hooks are machine-wide hooks loaded by administrators. They load before all other hooks and cannot be disabled by `disableAllHooks`.

Policy hooks are discovered from two sources:

* **Filesystem**: JSON files in the platform-appropriate policy directory, loaded in alphabetical order:
  * Linux/macOS: `/etc/github-copilot/policy.d/*.json`
  * Windows: `C:\ProgramData\GitHub\Copilot\policy.d\*.json`
* **Windows Registry**: Values under `HKLM\Software\Policies\GitHub\Copilot` (each subkey holds a `Policy` REG_SZ value containing a JSON policy document).

Policy hook files use the same hook configuration format as user and project hooks (`{ "version": 1, "hooks": { ... } }`). On POSIX systems, policy files must be owned by root and must not be group- or world-writable.

Policy hooks are intended for use by enterprise IT administrators and require elevated privileges to install. End users cannot modify them. Policy hooks always run on the host, even when the session sandbox is enabled—see [Sandboxed sessions](#sandboxed-sessions).

### Agent-scoped hooks

> [!NOTE]
> **Copilot CLI only.**

Declare a `hooks` event map in a custom agent's frontmatter to run command or HTTP hooks only while that agent is selected. These hooks run in addition to session, user, repository, plugin, and policy hooks.

```yaml
---
name: formatter
description: Formats changed files
hooks:
  PostToolUse:
    - type: command
      command: ./scripts/format-changed-files.sh
      windows: ./scripts/format-changed-files.ps1
---
Format the files you change.
```

| Behavior | Details |
|----------|---------|
| Event names | Runtime names such as `postToolUse` and aliases such as `PostToolUse` are accepted. |
| Commands | `command` is the fallback. `windows`, `linux`, and `osx` override it per platform. Paths resolve from the repository root. |
| Subagent `Stop` | A subagent's scoped `Stop` (`agentStop`) hooks run at `SubagentStop`. After eight consecutive scoped blocks, further blocks are ignored. |
| Trust | Repository and inherited-agent hooks require workspace admission. Hook-disable settings, enterprise restrictions, and timeouts still apply. |
| Unsupported | Remote or organization-hosted agent definitions do not run scoped hooks. |

## Cloud agent execution environment

This section applies to **Copilot cloud agent only**. It describes constraints that affect how you write hook scripts and configure hook entries for cloud agent jobs.

| Property | Value |
|----------|-------|
| Operating system | Linux. Only the `bash` field on command hooks is honored; `powershell` entries are ignored. The cross-platform `command` field is honored as a fallback. |
| Working directory | `/workspace` when a repository is cloned, otherwise `/root`. Use this path when setting `cwd` on a hook entry or when referencing files from a script. |
| Filesystem | Ephemeral. Files written by hooks (logs, CSVs, transcripts) are discarded when the job ends. To retain hook output, send it via an `http` hook entry. |
| Outbound network | Restricted by the cloud agent firewall. By default only GitHub and Copilot hostnames are reachable; reaching any other host (for example `https://hooks.example.com`) requires an admin-configured firewall allow rule. |
| Available environment variables | `GITHUB_COPILOT_API_TOKEN` and `GITHUB_COPILOT_GIT_TOKEN` are set in the sandbox. `COPILOT_AGENT_PROMPT` holds the prompt the job was invoked with. `HOME` is set to `/root`, so any hook script that resolves `~/...` paths writes into the ephemeral sandbox. `GITHUB_TOKEN` is not set. |
| Interactivity | Fully non-interactive. The agent runs with all tool permissions pre-granted, so no permission dialogs are shown and no notifications are surfaced to a user. |
| Configuration discovery | In a cloud agent job, the only hook configuration that exists by default is `.github/hooks/*.json` inside the cloned repository. The sandbox does not ship with user-level hook files, `settings.json`, `config.json`, or installed plugins. |

## Hook configuration format

Hook configuration files use JSON format with version `1`.

> [!NOTE]
> If a hook configuration file loaded from a directory (for example, `.github/hooks/`) contains a malformed hook item, only that item is dropped and logged—valid sibling hooks in the same file still load. Structural errors (invalid JSON, a bad `version`, or a non-array event list) still reject the entire file. Hooks defined inline in `settings.json` remain strict: any item-level validation error rejects the whole `hooks` field. Other configuration files always load independently.

### Command hooks

Command hooks run shell scripts or executables and are supported on all hook types.

> [!NOTE]
> **Cloud agent only.** Cloud agent runs hooks in a Linux sandbox. Only the `bash` field is honored; `powershell` entries are ignored. The cross-platform `command` field is honored as a fallback.

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": "YOUR_BASH_COMMAND",
        "powershell": "YOUR_POWERSHELL_COMMAND",
        "cwd": "OPTIONAL/WORKING/DIRECTORY",
        "env": { "VAR": "VALUE" },
        "timeoutSec": 30
      }
    ]
  }
}
```

In Copilot CLI, you can use `exec` and `args` to run an executable directly instead of using a shell:

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "exec": "YOUR_EXECUTABLE",
        "args": ["YOUR_ARGUMENT"],
        "cwd": "OPTIONAL/WORKING/DIRECTORY",
        "env": { "VAR": "VALUE" },
        "timeoutSec": 30
      }
    ]
  }
}
```

Replace `YOUR_EXECUTABLE` with the executable name or path and `YOUR_ARGUMENT` with an argument to pass to it. You can include additional arguments in the `args` array.

Do not combine `exec` with `bash`, `powershell`, or `command`. Arguments are passed directly to the executable without shell interpretation, so shell features such as pipes, redirection, and glob expansion are not available.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `args` | array of strings | No | Arguments passed directly to `exec`. Only supported in Copilot CLI. |
| `bash` | string | One of `bash`, `powershell`, or `command`, unless `exec` is specified | Shell command for Unix. |
| `command` | string | One of `bash`, `powershell`, or `command`, unless `exec` is specified | Cross-platform fallback. Copied to both `bash` and `powershell` when those fields are absent; explicit `bash` or `powershell` entries take precedence on their respective platforms. |
| `cwd` | string | No | Working directory for the command (relative to repository root or absolute). |
| `env` | object | No | Environment variables to set (supports variable expansion). |
| `exec` | string | Instead of `bash`, `powershell`, and `command` | Executable name or path. Runs the executable directly without a shell. Only supported in Copilot CLI. |
| `powershell` | string | One of `bash`, `powershell`, or `command`, unless `exec` is specified | Shell command for Windows. |
| `timeout` | number | No | Alias for `timeoutSec`, in seconds. Used only when `timeoutSec` is absent; `timeoutSec` takes precedence when both are present. |
| `timeoutSec` | number | No | Timeout in seconds. Default: `30`. |
| `type` | `"command"` | No | Hook type. Defaults to `"command"` when omitted. |

#### Progress messages

Command hooks can emit progress status lines to the CLI timeline while executing. Write a `{"type": "progress", "message": "..."}` JSON object to stdout before writing the final output:

```bash
echo '{"type": "progress", "message": "Checking policy..."}'
# ... perform work ...
echo '{"permissionDecision": "allow"}'
```

Set `"temporary": true` to emit a transient status line. A transient line replaces the previous transient line and is cleared when the assistant responds, instead of accumulating in the timeline:

```bash
echo '{"type": "progress", "message": "Routing...", "temporary": true}'
echo '{"type": "progress", "message": "Thinking...", "temporary": true}'
# ... perform work ...
echo '{"permissionDecision": "allow"}'
```

Progress messages are display-only and do not affect hook output or decision logic.

**How stdout is parsed when progress messages are mixed in.** — The CLI scans stdout line-by-line as the hook runs. Any line that, after trimming, is a single complete JSON object with `"type": "progress"` is consumed as a progress event and **removed from the hook's output stream**. Every other line—blank lines, plain text, and JSON objects that are not progress messages—is preserved verbatim. When the hook exits, the preserved lines are concatenated, trimmed, and parsed with a single `JSON.parse` call: that result is the hook's output (the "hook output JSON" referenced elsewhere in this article). This means:

* Emitting progress lines alongside a final decision object (as in the examples above) is safe and is the intended pattern—the progress lines never reach the JSON parser.
* Each progress message must be on its own line and must be valid JSON on that single line. Multi-line / pretty-printed progress objects are not recognized as progress and will be left in the output stream, where they will likely cause the final `JSON.parse` to fail.
* The final decision object, by contrast, may span multiple lines—only progress *recognition* is line-oriented; what remains after progress stripping is parsed as one JSON document, not as line-delimited JSON.
* If the leftover output is empty, or fails to parse as JSON, the hook is treated as having produced no output and falls through to default behavior. Two or more non-progress JSON objects on stdout (for example, two `echo '{"permissionDecision": ...}'` calls) will therefore concatenate into invalid JSON and be ignored—emit exactly one final decision object.

#### Sandboxed sessions

> [!NOTE]
> **Copilot CLI only.**

When the session sandbox is enabled, command hooks from the repository, your user settings, and plugins run inside it, with the same access as the agent's shell commands. A hook can also read the directory it was loaded from, so a plugin can run the scripts it ships, and a plugin hook can write to its data directory (`$COPILOT_PLUGIN_DATA`).

A hook's `cwd` and `env` fields don't widen that access: a `cwd` outside the session's grants gives the hook no access there, and variables such as `TMPDIR` or `PATH` set in the hook's `env` grant nothing. When a hook fails in the sandbox, Copilot shows a warning once per hook and session. To give a hook more access, add the required paths to `sandbox.userPolicy` in your settings. See [AUTOTITLE](/copilot/reference/copilot-cli-reference/cli-config-dir-reference#user-settings-copilotsettingsjson).

Policy hooks always run on the host, outside the sandbox, even when the session sandbox is enabled. A policy hook should not run scripts from the workspace.

### HTTP hooks

HTTP hooks send the input payload as a JSON `POST` to a URL.

> [!NOTE]
> * By default, only `https://` URLs are allowed. Non-TLS `http://` requests are rejected, except for `http://localhost`, `http://127.*`, and `http://[::1]` when `COPILOT_HOOK_ALLOW_LOCALHOST=1` is set.
> * **Cloud agent only.** Outbound network from the sandbox is restricted by the cloud agent firewall, so `url` must target an allow-listed host.

```json
{
  "version": 1,
  "hooks": {
    "postToolUse": [
      {
        "type": "http",
        "url": "https://hooks.example.com/copilot",
        "headers": { "X-Source": "copilot-cli" },
        "allowedEnvVars": ["GITHUB_TOKEN"],
        "timeoutSec": 30
      }
    ]
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allowedEnvVars` | string[] | No | Environment variable names that may be expanded inside `headers` values. When set, `url` must use `https://`. |
| `headers` | object | No | Request headers to include. |
| `timeout` | number | No | Alias for `timeoutSec`, in seconds. Used only when `timeoutSec` is absent; `timeoutSec` takes precedence when both are present. |
| `timeoutSec` | number | No | Timeout in seconds. Default: `30`. |
| `type` | `"http"` | Yes | Must be `"http"`. |
| `url` | string | Yes | Target URL. Must use `http:` or `https:`. For `preToolUse` and `permissionRequest`, must use `https://` because the response can grant tool permissions. |

### Prompt hooks

Prompt hooks auto-submit text as if the user typed it. They are only supported on `sessionStart`. The text can be a natural language prompt or a slash command.

> [!NOTE]
> **Copilot CLI only.** Prompt hooks fire only for **new interactive sessions**. They do not fire on resume, and they do not fire in non-interactive prompt mode (`-p`).

> [!NOTE]
> **Cloud agent.** Cloud agent jobs run non-interactively (similar to `-p`), so `prompt` hook entries may not fire. Confirm the behavior in your environment before relying on them.

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "prompt",
        "prompt": "YOUR_PROMPT_TEXT_OR_SLASH_COMMAND"
      }
    ]
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | `"prompt"` | Yes | Must be `"prompt"`. |
| `prompt` | string | Yes | Text to submit—can be a natural language message or a slash command. |

## Hook events

The table below lists every supported event. The **Cloud agent** column shows whether the event fires under cloud agent and notes any behavior differences.

| Event | Fires when | Output processed | Cloud agent |
|-------|-----------|------------------|-------------|
| `agentStop` | The main agent finishes a turn. | Yes — can block and force continuation. | Fires. `decision: "block"` forces another turn, which still counts against the job's timeout. |
| `errorOccurred` | An error occurs during execution. | No | Fires. |
| `notification` | Fires asynchronously when the CLI emits a system notification (shell completion, agent completion or idle, permission prompts, elicitation dialogs). Fire-and-forget: never blocks the session. Supports a `matcher` regex pattern (the value of the `matcher` field) on `notification_type`. | Optional — can inject `additionalContext` into the session. | **Does not fire.** Cloud agent does not surface notifications to a user (see the **Interactivity** row in the Cloud agent execution environment table above). |
| `permissionRequest` | Fires before the permission service runs (rules engine, session approvals, auto-allow/auto-deny, and user prompting). If the merged hook output returns `behavior: "allow"` or `"deny"`, that decision short-circuits the normal permission flow—except for a sandbox-bypass request (`requestSandboxBypass: true`), where an `allow` does not pre-approve the escape and only `deny` propagates (see the [`permissionRequest` decision control](#permissionrequest-decision-control) sandbox-bypass exception). Supports a `matcher` regex pattern (the value of the `matcher` field) on `toolName`. | Yes — can allow or deny programmatically. | Tool calls are pre-approved, so this hook either does not fire or has no effect. Use `preToolUse` to make permission decisions instead. |
| `postToolUse` | After each tool completes successfully. | Yes — can modify the tool result or inject additional context for the model. | Fires. |
| `postToolUseFailure` | After a tool completes with a failure. | Yes — can provide recovery guidance via `additionalContext` (exit code `2` for command hooks). | Fires. |
| `preCompact` | Context compaction is about to begin (manual or automatic). Supports a `matcher` regex pattern (the value of the `matcher` field) to filter by trigger (`"manual"` or `"auto"`). | No — notification only. | Fires only with `trigger: "auto"`. There is no user to request manual compaction. |
| `preToolUse` | Before each tool executes. | Yes — can allow, deny, or modify. | Fires. A decision of `"ask"` is treated as `"deny"` because no user is available to answer. |
| `sessionEnd` | The session terminates. | No | Fires once per job. `reason` is typically `"complete"`, `"error"`, or `"timeout"`; `"abort"` and `"user_exit"` are not expected because there is no user. |
| `sessionStart` | A new or resumed session begins. | Optional — can inject `additionalContext` into the session. | Fires once per job, as a new session (not a resume). See the Prompt hooks note above for the behavior of `prompt` entries under cloud agent. |
| `subagentStart` | A subagent is spawned (before it runs). Supports a `matcher` regex pattern (the value of the `matcher` field) to filter by agent name. | Optional — cannot block creation, but `additionalContext` is prepended to the subagent's prompt. | Fires. |
| `subagentStop` | A subagent completes. | Yes — can block and force continuation. | Fires. |
| `userPromptSubmitted` | The user submits a prompt. | Optional—`modifiedPrompt` is honored only by SDK programmatic hooks. | Fires at most once, for the prompt supplied to the job. There is no follow-up user input. |
| `userPromptTransformed` | Fires after the runtime transforms a submitted prompt into its model-facing content, just before that content is emitted and persisted to session history. Runs for the primary message and for every preceding message in a batched submission. Mutation-only — it can rewrite the content the model receives, but not block or handle the turn. System notifications never trigger it. | Yes — can rewrite the model-facing content. | Fires. |

## Hook event input payloads

Each hook event delivers a JSON payload to the hook handler. Two payload formats are supported, selected by the event name used in the hook configuration:

* **camelCase format** — Configure the event name in camelCase (for example, `sessionStart`). Fields use camelCase.
* **VS Code compatible format** — Configure the event name in PascalCase (for example, `SessionStart`). Fields use snake_case to match the VS Code Copilot extension format.

Hooks that fire inside a subagent include extra fields in their input. Root-agent hook inputs are unchanged.

| Field (camelCase) | Field (VS Code compatible) | Description |
|-------------------|------------------------|-------------|
| `agentId` | `agent_id` | Identifier of the subagent firing the hook. |
| `agentType` | `agent_type` | Subagent type, when known. |
| `parentAgentId` | `parent_agent_id` | Identifier of the parent agent, when known. |

### `sessionStart` / `SessionStart`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;      // Unix timestamp in milliseconds
    cwd: string;
    source: "startup" | "resume" | "new";
    initialPrompt?: string;
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "SessionStart";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    source: "startup" | "resume" | "new";
    initial_prompt?: string;
}
```

**Output:**

```typescript
{
    additionalContext?: string;
}
```

Only `additionalContext` is consumed for `sessionStart` (command and HTTP variants). Return `{}` or empty for no action.

When multiple `sessionStart` hooks run, successful hooks that return a non-empty string `additionalContext` contribute in execution order, separated by exactly `"\n\n"`. An empty or whitespace-only string does not erase already-accumulated context; if every hook returns only empty or whitespace-only strings, the last one is kept. The combined string (including separators) is bounded by the same 10 MiB hook-output limit—a contribution that would cross it is dropped, the previously accumulated context is kept, and a size-only warning is logged and raised in the session.

### `sessionEnd` / `SessionEnd`

> [!NOTE]
> **Copilot CLI only — `/clear` in interactive mode.** `/clear` closes the old session and fires its `sessionEnd` hooks with `reason: "user_exit"` while the CLI keeps running. The replacement session has its own independent lifecycle. Because the CLI itself isn't exiting, these hooks dispatch detached—they run in the background with their full `timeoutSec` while `/clear` returns immediately, so a hook doing real work is neither cut short nor able to stall the prompt. A detached hook still running when you later quit the CLI is terminated along with the process.

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    reason: "complete" | "error" | "abort" | "timeout" | "user_exit";
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "SessionEnd";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    reason: "complete" | "error" | "abort" | "timeout" | "user_exit";
}
```

### `userPromptSubmitted` / `UserPromptSubmit`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    prompt: string;
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "UserPromptSubmit";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    prompt: string;
}
```

**Output:**

```typescript
{
    modifiedPrompt?: string; // Replaces the prompt for the rest of the turn (SDK programmatic hooks only)
}
```

Return `{}` or empty to leave the prompt unchanged.

> [!NOTE]
> * `modifiedPrompt` is only honored by SDK programmatic hooks. Command and HTTP config-file `userPromptSubmitted` hooks have their output dropped, including `modifiedPrompt`. The lighter hooks-processing runtime used by hosted or steering Copilot cloud agent sessions also ignores it. This is the same runtime split as `preToolUse`.
> * A non-string `modifiedPrompt`, `modifiedTransformedPrompt`, or a handled `responseContent` value is ignored rather than corrupting the session—a type warning naming the field is logged and emitted as a `session.warning` event. An empty-string override is rejected instead of blanking the model-facing content. A `null` `additionalContext` value is treated as absent instead of being injected as the literal text `null`. Hook output (stdout for command hooks, the response body for HTTP hooks) is bounded at 10 MiB per invocation—a larger response is truncated rather than exhausting memory.

### `userPromptTransformed`

Fires after the runtime transforms a submitted prompt into its model-facing content, just before that content is emitted and persisted to session history. Runs for the primary message and for every preceding message in a batched submission. Mutation-only—it can rewrite the content the model receives, but not block or handle the turn. System notifications never trigger it.

**Input:**

```typescript
{
    sessionId: string;
    timestamp: number;         // epoch-ms integer
    cwd: string;
    prompt: string;            // user prompt after userPromptSubmitted hooks have run
    transformedPrompt: string; // runtime-transformed content the model will receive
}
```

**Output:**

```typescript
{
    modifiedTransformedPrompt?: string; // Replaces the model-facing content
}
```

Return `{}` or empty to leave the transformed content unchanged. `modifiedTransformedPrompt` replaces only the content sent to the model and stored in session history—the prompt displayed in the timeline is unaffected—and the replacement is replayed unchanged if the session is resumed.

### `preToolUse` / `PreToolUse`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    toolName: string;
    toolArgs: unknown;
}
```

**VS Code compatible input:**

When configured with the PascalCase event name `PreToolUse`, the payload uses snake_case field names to match the VS Code Copilot extension format:

```typescript
{
    hook_event_name: "PreToolUse";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    tool_name: string;
    tool_input: unknown;    // Tool arguments (parsed from JSON string when possible)
}
```

**Claude-format matchers (PascalCase `PreToolUse`):** Hooks configured with the PascalCase event name `PreToolUse`—as used in Claude Code plugins and the Open Plugins format—apply Claude's matcher semantics instead of the native regex rule:

* `*`, `**`, or an empty `matcher` value fires for every tool.
* A literal name or `|`-separated alternation (for example, `Bash` or `Edit|Write`) fires when any token equals the runtime tool name or its Claude tool name from the table below.
* Any other value is treated as a case-sensitive regex anchored as `^(?:PATTERN)$` tested against the Claude tool name (or the runtime name for tools with no Claude equivalent).

Payloads for PascalCase `PreToolUse` report `tool_name` as the Claude tool name (for example, `Bash`, not `bash`).

| Runtime tool | Claude tool name |
|---|---|
| `bash`, `powershell` | `Bash` |
| `view` | `Read` |
| `create` | `Write` |
| `edit`, `str_replace_editor`, `apply_patch` | `Edit` |
| `grep`, `rg` | `Grep` |
| `glob` | `Glob` |
| `web_fetch` | `WebFetch` |
| `web_search` | `WebSearch` |
| `ask_user` | `AskUserQuestion` |
| `update_todo` | `TodoWrite` |
| `task` | `Agent` (the literal `Task` is also accepted) |

Tools with no Claude equivalent keep their runtime names.

> [!IMPORTANT]
> **Command vs HTTP fail behavior for `preToolUse`:** Command `preToolUse` hooks are **fail-closed** on errors—a crash or non-zero exit (including exit `2`) denies the tool call, even if the hook's stdout JSON reports `permissionDecision: "allow"`. Command hook **timeouts are always fail-open, even for `preToolUse` and admin-deployed policy hooks**—a timed-out hook surfaces a warning and lets the tool call proceed through the normal permission flow instead of denying it. HTTP `preToolUse` hooks are **fail-open**—a network error, timeout, or non-2xx response falls through to the default permission flow. Choose the variant that matches your security requirements.

### `postToolUse` / `PostToolUse`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    toolName: string;
    toolArgs: unknown;
    toolResult: {
        resultType: "success";
        textResultForLlm: string;
    }
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "PostToolUse";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    tool_name: string;
    tool_input: unknown;
    tool_result: {
        result_type: "success";
        text_result_for_llm: string;
    }
}
```

### `postToolUseFailure` / `PostToolUseFailure`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    toolName: string;
    toolArgs: unknown;
    error: string;
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "PostToolUseFailure";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    tool_name: string;
    tool_input: unknown;
    error: string;
}
```

### `agentStop` / `Stop`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    transcriptPath: string;
    stopReason: "end_turn";
    stop_hook_active: boolean; // true when this turn was already forced to continue by a prior "block" decision from this hook
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "Stop";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    transcript_path: string;
    stop_reason: "end_turn";
    stop_hook_active: boolean;
}
```

### `subagentStart`

> [!NOTE]
> The built-in `general-purpose` agent does not emit `subagentStart` or `subagentStop` events. All other built-in YAML-based agents—including `explore`, `task`, `code-review`, `rubber-duck`, `research`, and `security-review`—and user-defined custom agents emit these events.

**Input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    transcriptPath: string;
    agentName: string;
    agentDisplayName?: string;
    agentDescription?: string;
}
```

**Output:**

```typescript
{
    additionalContext?: string;
}
```

If `additionalContext` is returned, it is prepended to the subagent's first user message, giving hooks a way to inject project-specific context, policies, or instructions into every subagent invocation.

When multiple `subagentStart` hooks run, they accumulate the same way as `sessionStart`: successful hooks with a non-empty string `additionalContext` contribute in execution order joined by `"\n\n"`, empty or whitespace-only strings don't erase already-accumulated context, and the combined string is bounded by the 10 MiB hook-output limit (an over-limit contribution is dropped, the prior context is kept, and a size-only warning is logged and raised in the session).

**Matcher:** Supports an optional `matcher` field that filters by agent name. The value is treated as a regular expression wrapped as `^(?:matcher)$` and tested against `agentName`. The pattern must match the **entire** agent name, not just a substring. If the pattern is not a valid regular expression, the hook is skipped entirely (it will not fire for any agent).

### `subagentStop` / `SubagentStop`

Fires when a subagent completes normally, before returning results to the parent. `stopReason` is currently always `"end_turn"`. This hook fires before large-response spill handling, so `response` (or `last_assistant_message` in the VS Code compatible format) carries the full final subagent response text.

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    transcriptPath: string;
    agentId: string;
    agentType: string;
    agentName: string;
    agentDisplayName?: string;
    response: string;       // Full final subagent response text
    stopReason: "end_turn";
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "SubagentStop";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    transcript_path: string;
    agent_id: string;
    agent_type: string;
    agent_name: string;
    agent_display_name?: string;
    last_assistant_message: string; // The `response` text
    stop_reason: "end_turn";
}
```

### `errorOccurred` / `ErrorOccurred`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    error: {
        message: string;
        name: string;
        stack?: string;
    };
    errorContext: "model_call" | "tool_execution" | "system" | "user_input";
    recoverable: boolean;
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "ErrorOccurred";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    error: {
        message: string;
        name: string;
        stack?: string;
    };
    error_context: "model_call" | "tool_execution" | "system" | "user_input";
    recoverable: boolean;
}
```

### `preCompact` / `PreCompact`

**camelCase input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    transcriptPath: string;
    trigger: "manual" | "auto";
    customInstructions: string;
}
```

**VS Code compatible input:**

```typescript
{
    hook_event_name: "PreCompact";
    session_id: string;
    timestamp: string;      // ISO 8601 timestamp
    cwd: string;
    transcript_path: string;
    trigger: "manual" | "auto";
    custom_instructions: string;
}
```

## `preToolUse` decision control

The `preToolUse` hook can control tool execution by writing a JSON object to stdout.

| Field | Values | Description |
|-------|--------|-------------|
| `permissionDecision` | `"allow"`, `"deny"`, `"ask"` | Whether the tool executes. Empty output uses default behavior. Under cloud agent, `"ask"` is treated as `"deny"` because no user is available to answer. In Copilot CLI autopilot mode, no prompt is shown and `"ask"` is denied, so the agent sees that the CLI was unable to ask the user for confirmation. |
| `permissionDecisionReason` | string | Reason shown to the agent. Required when decision is `"deny"`. |
| `modifiedArgs` | object | Substitute tool arguments to use instead of the originals. |

When Copilot CLI can show the hook-permission prompt, the user can type optional feedback along with a denial. That feedback is appended to the message the agent receives: `Denied by user via preToolUse hook prompt: <permissionDecisionReason>. The user provided the following feedback: <feedback>`.

## `agentStop` / `subagentStop` decision control

| Field | Values | Description |
|-------|--------|-------------|
| `decision` | `"block"`, `"allow"` | `"block"` forces another agent turn using `reason` as the prompt. |
| `reason` | string | Prompt for the next turn when `decision` is `"block"`. |
| `modifiedResponse` | string | **`subagentStop` only.** Replaces the response returned to the parent when the subagent is allowed to complete—useful for redacting or reformatting subagent output. Not applicable to `agentStop`. |

`decision` and `reason` behave the same for both `agentStop` and `subagentStop`. `modifiedResponse` applies only to `subagentStop`:

* A valid `block` decision wins over `modifiedResponse`: if a hook returns both, the subagent continues and the rewrite is discarded.
* Rewrites do not compose across multiple matching hooks. Every hook receives the same original `response`, and the last hook to return `modifiedResponse` wins—chaining a redactor and a formatter does not feed the redacted text into the formatter.
* The output field names (`decision`, `reason`, `modifiedResponse`) are the same for both the camelCase and VS Code compatible configs.
* Command and HTTP hooks keep the permissive behavior of other hook events: unsupported verdict fields and non-object JSON outputs are ignored, and `reason` only takes effect alongside a `block` decision with a nonempty string.
* SDK callback outputs are validated before merging: an invalid `decision`, a `reason` without `block`, a `block` without a nonempty `reason`, or a non-object output fails the subagent hook. An explicit `null` in an optional field is treated as absent.

> [!NOTE]
> **Runaway guard.** After 8 consecutive `block` continuations, the CLI overrides the hook and ends the turn anyway, to prevent an unbounded loop. Use the `stop_hook_active` input field on `agentStop` to detect that this turn was already forced to continue, and self-limit before hitting the cap.

## `postToolUse` output

The `postToolUse` hook can modify the tool result or inject additional context for the model by writing a JSON object to stdout.

```typescript
{
    modifiedResult?: {
        resultType: "success";
        textResultForLlm: string;
    };
    additionalContext?: string;
}
```

| Field | Type | Description |
|-------|------|-------------|
| `modifiedResult` | object | Replacement tool result. Must have `resultType: "success"`. If returned with `resultType: "failure"`, the failure routes downstream and `postToolUseFailure` fires next. |
| `additionalContext` | string | Additional guidance appended to `textResultForLlm` so the model sees it after the tool output on the same turn. When multiple hooks return `additionalContext`, the results are joined with a double newline and capped at 10 KB. |

Return `{}` or empty output to keep the original successful result.

> [!NOTE]
> `modifiedResult` is honored by both SDK programmatic hooks and command/HTTP config-file `postToolUse` hooks.

**Matcher:** Optional regex tested against `toolName`. The regex pattern is the value of the `matcher` field, compiled as `^(?:PATTERN)$`, and must match the entire tool name. If the pattern is not a valid regular expression, the hook is skipped. Omit `matcher` to receive results from all tools.

```json
{
    "type": "command",
    "matcher": "bash|edit",
    "bash": "./scripts/log-tool.sh"
}
```

## `permissionRequest` decision control

> [!NOTE]
> **Copilot CLI only.** The `permissionRequest` hook does not apply under Copilot cloud agent—tool calls there are pre-approved (see the **Interactivity** row in the Cloud agent execution environment table). Use `preToolUse` to make permission decisions in cloud agent.

The `permissionRequest` hook fires before the permission service runs—before rule checks, session approvals, auto-allow/auto-deny, and user prompting. If hooks return `behavior: "allow"` or `"deny"`, that decision short-circuits the normal permission flow. Returning nothing falls through to normal permission handling. Use it to approve or deny tool calls programmatically—especially useful in CLI pipe mode (`-p`) and other CLI CI usages where no interactive prompt is available. It does not apply to cloud agent.

All configured `permissionRequest` hooks run for each request (except `read` and `hook` permission kinds, which short-circuit before hooks). Hook outputs are merged with later hook outputs overriding earlier ones.

**Sandbox-bypass exception:** for any request that asks to escape the sandbox (`requestSandboxBypass: true` in `toolInput`), a hook `allow` does not pre-approve the request or short-circuit the user prompt—leaving the sandbox is a privilege escalation the user must always confirm interactively. This covers a shell command asking to run outside the sandbox and a `web_fetch` whose URL the sandbox network policy denies. Only `deny` still propagates (so a policy hook can block the escape); an `allow` (or no decision) falls through to the normal prompt.

**Matcher:** Optional regex tested against `toolName`. The regex pattern is the value of the `matcher` field, anchored as `^(?:PATTERN)$`, and must match the full tool name. When set, the hook fires only for matching tool names.

> [!NOTE]
> **Claude-format matchers (PascalCase `PermissionRequest`):** Hooks configured with the PascalCase event name `PermissionRequest` use the same Claude matcher semantics as `PreToolUse`. See [Claude-format matchers (PascalCase PreToolUse)](#claude-format-matchers-pascalcase-pretooluse) for the matcher rules and tool name table.

Output JSON to stdout to control the permission decision:

| Field | Values | Description |
|-------|--------|-------------|
| `behavior` | `"allow"`, `"deny"` | Whether to approve or deny the tool call. |
| `message` | string | Reason fed back to the LLM when denying. |
| `interrupt` | boolean | When `true` combined with `"deny"`, stops the agent entirely. |

Return empty output or `{}` to fall through to the normal permission flow. For command hooks, exit code `2` is treated as a deny; stdout JSON (if any) is merged with `{"behavior":"deny"}`, and stderr is ignored.

## `notification` hook

> [!NOTE]
> **Copilot CLI only.** The `notification` hook does not fire under Copilot cloud agent.

The `notification` hook fires asynchronously when the CLI emits a system notification. These hooks are fire-and-forget: they never block the session, and any errors are logged and skipped.

**Input:**

```typescript
{
    sessionId: string;
    timestamp: number;
    cwd: string;
    hook_event_name: "Notification";
    message: string;           // Human-readable notification text
    title?: string;            // Short title (e.g., "Permission needed", "Shell completed")
    notification_type: string; // One of the types listed below
}
```

**Notification types:**

| Type | When it fires |
|------|---------------|
| `shell_completed` | A background (async) shell command finishes |
| `shell_detached_completed` | A detached shell session completes |
| `agent_completed` | A background subagent finishes (completed or failed) |
| `agent_idle` | A background agent finishes a turn and enters idle state (waiting for `write_agent`) |
| `permission_prompt` | The agent requests permission to execute a tool |
| `elicitation_dialog` | The agent requests additional information from the user |

**Output:**

```typescript
{
    additionalContext?: string; // Injected into the session as a user message
}
```

If `additionalContext` is returned, the text is injected into the session as a prepended user message. This can trigger further agent processing if the session is idle. Return `{}` or empty output to take no action.

**Matcher:** Optional regex on `notification_type`. The regex pattern is the value of the `matcher` field, anchored as `^(?:PATTERN)$`. Omit `matcher` to receive all notification types.

## Matcher filtering

Several events accept an optional `matcher` regex on each hook entry that filters which invocations the hook fires for. It is compiled as `^(?:PATTERN)$` and must match the full value. Invalid regexes cause the hook entry to be skipped.

| Event | `matcher` is matched against |
|-------|------------------------------|
| `notification` | `notification_type` |
| `permissionRequest` | `toolName` |
| `postToolUse` | `toolName` |
| `preCompact` | `trigger` (`"manual"` or `"auto"`) |
| `preToolUse` | `toolName` |
| `subagentStart` | `agentName` |

## Tool names for hook matching

| Tool name | Description |
|-----------|-------------|
| `ask_user` | Ask the user a clarifying question. Under cloud agent there is no user, so `ask_user` does not produce a useful result. |
| `bash` | Execute shell commands (Unix). |
| `create` | Create new files. |
| `edit` | Modify file contents. |
| `glob` | Find files by pattern. |
| `grep` | Search file contents. |
| `powershell` | Execute shell commands (Windows). Does not appear under cloud agent (Linux sandbox). |
| `task` | Run subagent tasks. |
| `view` | Read file contents. |
| `web_fetch` | Fetch web pages. |

If multiple hooks of the same type are configured, they execute in order. For `preToolUse`, if any hook returns `"deny"`, the tool is blocked. For most events, hook failures (non-zero exit codes other than `2`, or timeouts) are logged and skipped. **Exception: `preToolUse` command hooks are fail-closed on exit `2` and on non-timeout errors**—exit `2`, a crash, or any other non-zero exit (other than a timeout) denies the tool call, even if the hook's stdout JSON reports `permissionDecision: "allow"`. **Timeouts are always fail-open, including for `preToolUse` and admin-deployed policy hooks**: a warning is surfaced and the tool call proceeds through the normal permission flow rather than being denied.

## Exit codes for command hooks

| Exit code | Meaning |
|-----------|---------|
| `0` | Success. `stdout` is parsed as the hook output JSON if present. |
| `2` | Treated as a warning by default. `stderr` is surfaced to the user but the run continues. For `permissionRequest` and `preToolUse`, exit `2` is treated as a deny: any `stdout` JSON is merged with the deny decision and the tool call is denied even if that JSON reports `permissionDecision: "allow"`. For `postToolUseFailure`, exit `2` is treated as `additionalContext` and `stdout` is appended to the failure shown to the agent. |
| Other non-zero | Logged as a hook failure. The run continues (fail-open). **Exception: `preToolUse` is fail-closed**—a non-zero exit (other than exit 2) denies the tool call with `"Denied by preToolUse hook (hook errored)"`. |
| Timeout        | Killed after `timeoutSec`. Error logged, execution continues. **Timeouts are fail-open for every event, including `preToolUse` and admin-deployed policy hooks**—a warning is surfaced and processing proceeds as if the hook had not run. For `preToolUse`, the tool call proceeds through the normal permission flow rather than being denied. A crashed or explicitly-denying hook still fails-closed; only timeouts are exempt. The logged message includes the command that timed out, for example `Hook command timed out after 30 seconds: my-validation-script.sh` (the bash/PowerShell script text, or `program arg1 arg2 ...` for exec hooks), truncated to 80 characters. |

For most events, non-zero exits and timeouts are logged and skipped—agent execution continues. For `preToolUse` command hooks, exit 2, crashes, and other non-zero exits all fail-closed and deny the tool call—exit 2 always denies, even if the hook's `stdout` JSON reports `permissionDecision: "allow"`—but **timeouts always fail-open**—a slow or unreachable hook must not silently block tool calls or work, even when the hook was deployed by an administrator as policy.

## Disable all hooks

Use `disableAllHooks` when you want to keep your hook configuration on disk but stop it from running—for example:

* Debugging an issue and you want to confirm a hook is the cause without deleting your config.
* Pausing automation during a sensitive task (a code review, a release branch, working with secrets) without losing the setup. (**Copilot CLI only.**)
* Shipping a hooks file in source control that contributors can opt out of locally by setting the option in their repository `settings.json`. (**Copilot CLI only.**)
* Temporarily silencing slow or noisy hooks during an interactive session. (**Copilot CLI only.**)

Set `disableAllHooks` to `true` at the top level to skip every hook in the file without deleting it.

```json
{
  "version": 1,
  "disableAllHooks": false,
  "hooks": {
    "preToolUse": [ /* hook entries */ ]
  }
}
```

Behavior depends on where you set the flag:

* **Inside a single `.github/hooks/*.json` file** — only the hooks declared in that file are skipped. Honored by both Copilot CLI and Copilot cloud agent.
* **At the top level of repository `settings.json`** — **Copilot CLI only.** Every hook from every source (repository files, user files, plugins, and inline hook blocks) is skipped for sessions in that repository. Policy hooks are not affected and continue to run. Cloud agent does not load `settings.json`.

## Further reading

* [AUTOTITLE](/copilot/how-tos/copilot-cli/customize-copilot/use-hooks)
* [AUTOTITLE](/copilot/reference/hooks-reference)
* [AUTOTITLE](/copilot/reference/copilot-cli-reference/cli-command-reference)
* [AUTOTITLE](/copilot/concepts/copilot-surfaces/copilot-on-github)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/agent-plugins.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/agent-plugins
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/agent-plugins.md
- **SHA256_FINGERPRINT**: `9780c2fae3fb77611a653d74672dbb394471ae496d847fbd65d5e21e90fea830`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.707312+00:00
---

**MetaDescription**: Discover, install, configure, and troubleshoot agent plugins in VS Code.

# Agent plugins in VS Code

Agent plugins bundle related customizations into one installable setup. Use a plugin to adopt a shared workflow instead of assembling its skills, agents, and tool integrations individually. For example, a testing plugin can package a test-running skill, review agent, and reporting integration that are intended to work together.

This article shows you how to discover, install, configure, update, and troubleshoot plugins. To create or package a plugin, see the [agent plugin authoring reference](/docs/agents/reference/agent-plugin-reference.md).

If you only need a project rule or a single skill, start with an [individual customization](/docs/agents/concepts/customization.md#customization-options-at-a-glance). Choose a bundle when its components support a workflow you want to adopt together.

> [!NOTE]
> Enable or disable support for agent plugins with the ``chat.plugins.enabled`` setting.

## What plugins provide

Plugins can provide the following customizations. The selected harness and plugin format determine which components are available.

| Capability | Purpose |
|------------|---------|
| [Skills](/docs/agent-customization/agent-skills.md) | Instructions, scripts, and resources for specialized workflows |
| [MCP servers](/docs/agent-customization/mcp-servers.md) | Tools for interacting with external systems |
| [Custom agents](/docs/agent-customization/custom-agents.md) | Specialized roles and tool configurations |
| [Hooks](/docs/agent-customization/hooks.md) | Commands that run at agent lifecycle points |
| [Automation templates](/docs/agents/run/automations.md#start-from-a-template) | Starting prompts and schedules to review before creating an automation |
| Slash commands | Commands you can invoke with `/` in chat |

Installed plugin customizations appear alongside your locally defined ones. For example, skills from a plugin show up in **Configure Skills**, and MCP servers appear in the MCP server list. Installing an automation template does not start an automation; review and configure it before turning it on.

Check the plugin's supported clients and components before installing. See [Cross-tool compatibility](#cross-tool-compatibility) for how portable and client-specific components differ.

> [!CAUTION]
> Plugins can include hooks and MCP servers that run code on your machine. Review the plugin contents and publisher before installing, especially for plugins from community marketplaces.

## Discover and install plugins

You can browse and install plugins from marketplaces or directly from a Git repository.

### Manage plugins with slash commands

In a Copilot harness session, enter `/plugin ` in the chat input to view completions for plugin and marketplace operations.

| Command | Purpose |
|---------|---------|
| `/plugin list` | List installed plugins and their status. |
| `/plugin install <source>` | Install a plugin from a marketplace or Git repository. |
| `/plugin update <plugin>` | Update an installed plugin. |
| `/plugin enable <plugin>` | Enable an installed marketplace plugin. |
| `/plugin disable <plugin>` | Disable an installed marketplace plugin. |
| `/plugin uninstall <plugin>` | Remove an installed plugin. |
| `/plugin marketplace list` | List included and registered marketplaces. |
| `/plugin marketplace browse <name>` | Browse the plugins in a marketplace. |
| `/plugin marketplace add <source>` | Add a marketplace from a Git repository. |
| `/plugin marketplace update [name]` | Update one marketplace or all registered marketplaces. |
| `/plugin marketplace remove <name> [--force]` | Remove a registered marketplace. Use `--force` if plugins from the marketplace are installed. |

Marketplace plugins use the qualified identity `<plugin>@<marketplace>`. Use this identity when plugins in multiple marketplaces have the same name. Command completion suggests valid marketplace and plugin identities for each operation.

Plugins installed directly from a Git repository can be updated or uninstalled, but they can't be enabled or disabled. To stop using a directly installed plugin, uninstall it. Included and centrally managed marketplaces can't be removed.

> [!NOTE]
> The `/plugin` commands and the Agent Customizations editor currently use separate plugin inventories. Manage a plugin from the interface where you installed it.

### Install a plugin from a marketplace

1. Open the Extensions view (``Shortcut: workbench.view.extensions``) and enter `@agentPlugins` in the search field.

    Alternatively, select the **More Actions** (three dots) icon in the Extensions sidebar and choose **Views** > **Agent Plugins**.

1. Browse the list of available plugins from your [configured marketplaces](#configure-plugin-marketplaces).

    ![Screenshot of browsing agent plugins in the Extensions sidebar.](images/agent-plugins/extensions-view.png)

1. Select **Install** to install a plugin.

    The first time you install a plugin from a new marketplace, VS Code shows a trust prompt. Review the marketplace source before confirming.

1. Open the Agent Customizations editor by running **Chat: Open Customizations** from the Command Palette, selecting **Open Customizations** in the Chat view title bar, or selecting **Plugins** in the Agents window.

1. Browse available plugins from your [configured marketplaces](#configure-plugin-marketplaces):

    * To use the unified **Discover** experience (Experimental), enable ``chat.customizations.marketplace.enabled`` and select **Discover**.
    * Otherwise, select the **Plugins** tab and then select **Browse Marketplace**.

1. Select **Install** to install a plugin.

    The first time you install a plugin from a new marketplace, VS Code shows a trust prompt. Review the marketplace source before confirming.

### Install a plugin from source

You can install a plugin directly from a Git repository URL without adding a full marketplace first.

* Run **Chat: Install Plugin From Source** from the Command Palette.

* Alternatively, select **Install Plugin from Source** on the **Plugins** page of the Agent Customizations editor.

Enter a Git repository URL (for example, `https://github.com/rwoll/markdown-review`) and VS Code clones and installs the plugin.

### Plugins installed by GitHub Copilot CLI

VS Code automatically discovers plugins that you install with the [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing) to enable you to use them also in VS Code. Plugins from `~/.copilot/installed-plugins/` appear in the **Agent Plugins - Installed** view alongside plugins you installed from a marketplace or from source.

The CLI stores plugins under `~/.copilot/installed-plugins/<marketplace>/<plugin>/`. Plugins installed directly from a Git URL (rather than from a marketplace) live under the `_direct` bucket, for example `~/.copilot/installed-plugins/_direct/github--moda-linter--copilot-plugin/`.

### View installed plugins

The **Agent Plugins - Installed** view in the Extensions view shows the plugins you have installed. From this view, you can enable, disable, or uninstall plugins.

![Screenshot of the Agent Plugins - Installed view in the Extensions view.](images/agent-plugins/installed-plugins.png)

You can also manage installed plugins from the Chat view by selecting **Open Customizations** in the title bar, and then selecting **Plugins**.

### Enable or disable plugins

You can enable or disable a plugin globally or for a specific workspace:

* Use the context menu on a plugin in the **Agent Plugins - Installed** section of the Extensions view.

* Use the [Agent Customizations editor](/docs/agent-customization/overview.md#agent-customizations-editor) to toggle a plugin's enabled state.

The enable/disable state is stored separately from the plugin configuration, so it does not affect shared workspace settings.

When a plugin is disabled, its skills, agents, hooks, MCP servers, slash commands, and automation templates are no longer available. For example, skills from a disabled plugin do not appear in **Chat: Configure Skills**, and automation templates do not appear in **Templates from Plugins**. Disabled plugins appear with a dimmed style in the Agent Customizations editor and Extensions view.

### Uninstall plugins

To remove a plugin, right-click it in the **Agent Plugins - Installed** view and select **Uninstall**. Plugins installed from an external source (such as npm, PyPI, or an external Git repository) are removed from disk. Plugins that are inlined in a marketplace repository remain on disk but are no longer active.

## Configure plugin marketplaces

You can discover plugins from marketplaces such as [copilot-plugins](https://github.com/github/copilot-plugins) and [awesome-copilot](https://github.com/github/awesome-copilot/). To configure additional marketplaces, use ``chat.plugins.marketplaces`` (Experimental).

Marketplaces are Git repositories that contain plugin definitions. You can reference them in several formats:

* **Shorthand**: `owner/repo` for public GitHub repositories. For example, `anthropics/claude-code`. Append `#<ref>` to select a branch, tag, or full 40-character commit SHA.
* **HTTPS git remote**: a full URL ending in `.git`. For example, `https://github.com/anthropics/claude-code.git`.
* **SCP-style git remote**: SSH-style references. For example, `git@github.com:anthropics/claude-code.git`.
* **file URI**: a `file:///` path to a marketplace repository already cloned on disk.

For reproducible installations, use a full 40-character commit SHA, such as `owner/repo#<commit-sha>`. VS Code installs plugins from that exact revision. Branch and tag references use the revision they resolve to when the marketplace is fetched.

Private repositories are also supported. If a public lookup fails, VS Code falls back to cloning the repository directly.

When a marketplace index declares a plugin at a relative path, VS Code verifies the repository, resolved revision, and path before installation. Sources with a missing revision, an invalid path, or an ambiguous path match are rejected.

Marketplace plugins can also reference external package sources such as npm or PyPI packages. For the full marketplace plugin schema, see the [Claude Code plugin marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

```json
// settings.json
"chat.plugins.marketplaces": [
    "anthropics/claude-code"
]
```

> [!NOTE]
> Enterprise admins can centrally control which plugins and marketplaces are available to developers. For more information, see [Manage agent plugins and marketplaces](/docs/enterprise/manage-ai-settings.md#manage-agent-plugins-and-marketplaces).

## Use local plugins

If you manually clone or download a plugin, you can register it with ``chat.pluginLocations`` (Experimental). This setting maps local plugin directory paths to an enabled or disabled state. Set the value to `true` to enable the plugin, or `false` to keep it registered but disabled.

```json
// settings.json
"chat.pluginLocations": {
    "/path/to/my-plugin": true,
    "/path/to/another-plugin": false
}
```

## Update plugins

VS Code checks for plugin updates when you run **Extensions: Check for Extension Updates** from the Command Palette, or automatically every 24 hours when ``extensions.autoUpdate`` is enabled.

Updating pulls down changes from cloned marketplace repositories and checks for new versions of externally sourced plugins.

Plugins sourced from npm or PyPI never update automatically. Instead, they show an **Update** button in the Extensions view. Selecting the button prompts you to confirm before running the install command. If an update is found during a background check, no action is taken until you explicitly select **Update**.

## Workspace plugin recommendations

Projects can recommend plugins for team members by configuring plugin settings in the workspace settings (`.claude/settings.json` or `.github/copilot/settings.json`).

VS Code shows a notification the first time a chat message is sent. You can view the recommended plugins by opening the Extensions view and filtering by `@agentPlugins @recommended`.

Specify the following fields in the settings file to configure workspace plugin recommendations:

* **`extraKnownMarketplaces`**: registers additional marketplaces for the project. These marketplaces appear when you search `@agentPlugins` in the Extensions view.

* **`enabledPlugins`**: lists plugins that should be enabled by default.

```json
{
    "extraKnownMarketplaces": {
        "company-tools": {
            "source": {
                "source": "github",
                "repo": "your-org/plugin-marketplace"
            }
        }
    },
    "enabledPlugins": {
        "code-formatter@company-tools": true
    }
}
```

## Cross-tool compatibility

[Agent Plugins](https://agent-plugins.org/) is an open standard for packaging skills and MCP servers across compatible clients, including GitHub Copilot in VS Code, GitHub Copilot CLI, and the GitHub Copilot app. Other components, such as custom agents, slash commands, rules, hooks, and automation templates, can be client-specific.

VS Code also supports existing Copilot, Claude, and legacy OpenPlugin formats. Support for a package format doesn't guarantee that every component works in every harness or client. Check the plugin's requirements. For file layouts and client-specific namespaces, see the [plugin authoring compatibility reference](/docs/agents/reference/agent-plugin-reference.md#cross-tool-compatibility).

## Troubleshooting

### Plugin does not appear after installation

* Confirm that agent plugins are enabled: check that ``chat.plugins.enabled`` is set to `true`.
* Verify the plugin's `name` field follows the naming rules for its format. Agent Plugins 1.0 names use lowercase letters, numbers, hyphens, and periods. Legacy Copilot plugin names use lowercase letters, numbers, and hyphens. Slashes and colons aren't supported.
* Check that `plugin.json` is in a [recognized location](/docs/agents/reference/agent-plugin-reference.md#plugin-formats).

### Skills from a plugin do not load

* Open the `SKILL.md` file and check the `name` field in the YAML frontmatter. The name must be plain kebab-case without namespace prefixes (for example, `test-runner`, not `myorg/test-runner`). Invalid names cause the skill to be silently skipped.
* Make sure the skill directory name matches the `name` field in the `SKILL.md` frontmatter.

### Plugin version does not update

* Run **Extensions: Check for Extension Updates** from the Command Palette to trigger an update check.
* If you maintain the plugin, review its [versioning and update requirements](/docs/agents/reference/agent-plugin-reference.md#test-and-distribute-a-plugin).

### Plugin installation fails after retry

Retry the installation. VS Code validates marketplace repository caches and replaces incomplete or invalid caches automatically.

If installation still fails, review the error for an invalid repository, revision, or plugin path. If the source is valid and retry continues to fail, run **Help: Report Issue**. Don't delete or modify the internal plugin cache manually.

## Author a plugin

Use the [agent plugin authoring reference](/docs/agents/reference/agent-plugin-reference.md) to create a package or inspect its configuration:

* **Package structure:** [Manifest fields](/docs/agents/reference/agent-plugin-reference.md#plugin-manifest-pluginjson), [supported formats](/docs/agents/reference/agent-plugin-reference.md#plugin-formats), and [plugin environment variables](/docs/agents/reference/agent-plugin-reference.md#plugin-environment-variables).

* **Automation templates:** [Package prompts and schedules](/docs/agents/reference/agent-plugin-reference.md#automations-in-plugins).

* **MCP servers:** [Server configuration, paths, and interaction with other servers](/docs/agents/reference/agent-plugin-reference.md#mcp-servers-in-plugins).

* **Hooks:** [Hook configuration, paths, and events](/docs/agents/reference/agent-plugin-reference.md#hooks-in-plugins).

## Related resources

* [Finding and installing plugins for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing)
* [GitHub Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/agent-skills.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/agent-skills
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/agent-skills.md
- **SHA256_FINGERPRINT**: `0d4444d9c8beb40e3c01fa6cb0399cfa3ac6ab1a8a0c52ba1820f06abaaf4631`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.857320+00:00
---

**MetaDescription**: Create portable Agent Skills in VS Code for specialized AI workflows across supported coding agents.

# Use Agent Skills in VS Code

Agent Skills are folders of instructions, scripts, and resources that AI agents can load when relevant to perform specialized tasks. Agent Skills is an [open standard](https://agentskills.io) that works across multiple AI agents, including GitHub Copilot in VS Code, GitHub Copilot CLI, the GitHub Copilot app, Copilot cloud agent, and the [experimental [product.prodname_openai_codex] integration](/docs/agents/run/agent-harnesses.md#codex).

Unlike [custom instructions](/docs/agent-customization/custom-instructions.md) that primarily define coding guidelines, skills enable specialized capabilities and workflows that can include scripts, examples, and other resources. Skills you create are portable across skills-compatible agents, but supported locations and optional features vary by agent. Unless otherwise noted, the configuration options and controls on this page apply to Copilot.

For how skills compare with the other customization options, see [Customization concepts](/docs/agents/concepts/customization.md).

Key benefits of Agent Skills:

* **Specialize Copilot**: Tailor capabilities for domain-specific tasks without repeating context
* **Reduce repetition**: Create once, use automatically across all conversations
* **Compose capabilities**: Combine multiple skills to build complex workflows
* **Efficient loading**: Only relevant content loads into context when needed

> [!TIP]
> Use the [Agent Customizations editor](/docs/agent-customization/overview.md#agent-customizations-editor) (Preview) to discover, create, and manage all your agent customizations in one place. Run **Chat: Open Customizations** from the Command Palette.

## Agent Skills vs custom instructions

While both Agent Skills and custom instructions help customize Copilot's behavior, they serve different purposes:

| Feature | Agent Skills | Custom Instructions |
| ------- | ------------ | ------------------- |
| **Purpose** | Teach specialized capabilities and workflows | Define coding standards and guidelines |
| **Portability** | Reusable across [skills-compatible coding agents](#agent-skills-standard), subject to each agent's supported locations and features | Reusable across experiences that support the selected [instruction format](/docs/agent-customization/custom-instructions.md#choose-a-format) |
| **Content** | Instructions, scripts, examples, and resources | Instructions only |
| **Scope** | Task-specific, loaded on-demand | Always applied (or via glob patterns) |
| **Standard** | Open standard ([agentskills.io](https://agentskills.io)) | Multiple formats, such as `AGENTS.md` and `.github/copilot-instructions.md` |

For example, you can share a repository's `.github/copilot-instructions.md` between VS Code and [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions). Check the supported file locations and activation rules for each experience.

Use Agent Skills when you want to:

* Create reusable capabilities that work across different AI tools
* Include scripts, examples, or other resources alongside instructions
* Share capabilities with the wider AI community
* Define specialized workflows like testing, debugging, or deployment processes

Use custom instructions when you want to:

* Define project-specific coding standards
* Set language or framework conventions
* Specify code review or commit message guidelines
* Apply rules based on file types using glob patterns

## Create a skill

> [!TIP]
> With **Local** selected in the Chat view, type `/skills` in the chat input to quickly open the **Configure Skills** menu. For other harnesses, such as **Copilot**, use **Open Customizations** instead.

Skills are stored in directories with a `SKILL.md` file that defines the skill's behavior. VS Code supports two types of skills:

| Skill type | Location |
| ---------- | -------- |
| Project skills, stored in your repository | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| Personal skills, stored in your home directory | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` |

> [!NOTE]
> To reuse repository skills with [product.prodname_openai_codex], [configure the experimental Codex integration](/docs/agents/run/agent-harnesses.md#codex). This integration discovers workspace skills in `.github/skills/` before your first prompt, without additional skill-location configuration. Codex also discovers `.agents/skills/` natively.
>
> If skills in `.github/skills/` have duplicate names across workspace roots, the primary root takes precedence. Discovery makes skills available to the model but does not guarantee that it invokes a skill for every relevant prompt.

> [!NOTE]
> **For Local harness sessions:** The ``chat.agentSkillsLocations`` setting adds other skill locations. This setting is deprecated and isn't read by Copilot harness sessions. To reuse those skills with the Copilot harness, [move them to supported locations](/docs/agent-customization/migrate-customizations.md#move-customizations-from-configured-locations).

> [!TIP]
> In a monorepo, enable ``chat.useCustomizationsInParentRepositories`` to discover skills from the parent repository root. Learn more about [parent repository discovery](/docs/agent-customization/overview.md#use-customizations-in-a-monorepo).

To create a skill:

1. In the Chat view, select **Open Customizations** in the title bar to open the Agent Customizations editor, and then select **Skills**.

1. Select **New Skill** (plus icon) next to the **Workspace** or **User** group, depending on where you want to store the skill.

    ![Screenshot of the Agent Customizations editor, showing the Skills tab and the dropdown to create a new skill.](images/customization/create-skill-v2.png)

1. Select the location and enter a name for the skill.

1. Complete the `SKILL.md` file by filling in the YAML frontmatter and adding instructions in the body of the file.

    ```markdown
    ---
    name: skill-name
    description: Description of what the skill does and when to use it
    ---

    # Skill Instructions

    Your detailed instructions, guidelines, and examples go here...
    ```

1. Optionally, add scripts, examples, or other resources to your skill's directory.

    For example, a skill for testing web applications might include:

    * `SKILL.md` - Instructions for running tests
    * `test-template.js` - A template test file
    * `examples/` - Example test scenarios

    > [!NOTE]
    > Make sure to reference any additional files in your `SKILL.md` for them to be picked up by the agent. Use Markdown links or `#file:` references with paths relative to the `SKILL.md` file, such as `[test template](./test-template.js)` or `#file:./test-template.js`.

### Generate a skill with AI

You can use AI to generate a skill based on a description of the capability. In chat, ask the agent to create a skill and describe the capability you want (for example, "create a skill for running and debugging integration tests"). This works for every harness, including **Copilot**. The agent asks clarifying questions and generates a `SKILL.md` file with the directory structure, instructions, and frontmatter.

With **Local** selected, you can also type `/create-skill` in chat followed by the description. The `/create-skill` command isn't available for other harnesses.

You can also extract a reusable skill from an ongoing conversation. For example, after a multi-turn session where you debugged a complex issue, ask "create a skill from how we just debugged that" to capture the multi-step procedure as a reusable skill.

With **Local** selected in the Chat view, you can also generate a skill from the Agent Customizations editor by selecting **Generate with AI** next to the **Workspace** group in the **Skills** section.

### Install a skill from the Customization Marketplace (Experimental)

Use the Customization Marketplace to find and install complete skill packages from configured sources:

1. Turn on the ``chat.customizations.marketplace.enabled`` setting.
1. Open the Agent Customizations editor and select **Discover**.
1. From the source menu, select **GitHub Feed**, and then search for a skill by name or add `@type:skill` to your search.
1. Select a skill and review its publisher, source, and included files.
1. Select **Install**, and then choose the user or workspace skills directory where you want to store the skill.

VS Code doesn't overwrite an existing skill at the selected destination. If another supported location contains a skill with the same name, both skills appear on the **Skills** page. The source or publisher image identifies the Marketplace installation, and **Copy Relative Path** shows its exact location.

Marketplace ownership applies to the exact installed skill directory. Deleting a Marketplace-installed skill from the **Skills** page uninstalls only that skill and doesn't remove a same-name local skill in another location.

If files from a Marketplace-installed skill are missing, **Discover** shows **Missing files**. Select **Repair** to restore only the missing packaged files. Files that you changed or added remain unchanged.

For more information about browsing sources and installation states, see [Discover marketplace customizations](/docs/agent-customization/overview.md#discover-marketplace-customizations-experimental).

## SKILL.md file format

The `SKILL.md` file is a Markdown file with YAML frontmatter that defines the skill's metadata and behavior.

### Header (required)

The header is formatted as YAML frontmatter with the following fields:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | A unique identifier for the skill. Only lowercase letters, numbers, and hyphens are allowed (for example, `webapp-testing`). Do not use slashes, colons, dots, or namespace prefixes. Must match the parent directory name. Maximum 64 characters. Names with invalid characters cause the skill to silently fail to load. |
| `description` | Yes | A description of what the skill does **and when to use it**. Be specific about both capabilities and use cases to help Copilot decide when to load the skill. Maximum 1024 characters. |
| `argument-hint` | No | Hint text shown in the chat input field when the skill is invoked as a slash command. Helps users understand what additional information to provide (for example, `[test file] [options]`). |
| `user-invocable` | No | Controls whether the skill appears as a slash command in the chat menu. Defaults to `true`. Set to `false` to hide the skill from the `/` menu while still allowing the agent to load it automatically. |
| `disable-model-invocation` | No | Controls whether the agent can automatically load the skill based on relevance. Defaults to `false`. Set to `true` to require manual invocation through the `/` slash command only. |
| `context` `feature(forked-skill-context)` | No | Controls how the skill is loaded. Defaults to inline (the skill's instructions are added to the parent agent's context). Set to `fork` to run the skill in a dedicated subagent context. See [Run a skill in a forked context](#run-a-skill-in-a-forked-context). |

> [!IMPORTANT]
> When a skill is distributed through a [plugin](/docs/agent-customization/agent-plugins.md), the plugin name is automatically used as a command prefix (for example, `/my-plugin:test-runner`). Do not manually add namespace prefixes to the skill `name` field. Using prefixes like `myorg/skillname` or `myorg:skillname` causes the skill to silently fail to load.

### Body

The skill body contains the instructions, guidelines, and examples that Copilot should follow when using this skill. Write clear, specific instructions that describe:

* What the skill helps accomplish
* When to use the skill
* Step-by-step procedures to follow
* Examples of the expected input and output
* References to any included scripts or resources

You can reference files by using Markdown links or the `#file:` syntax. For files within the skill directory, use paths relative to the `SKILL.md` file, such as `[test script](./test-template.js)`. To reference your environment user home folder, use `~`, or start a path with `~/`, such as `#file:~/skill-resources/test-template.js`. Use Unix-style `/` path separators to keep skills portable across operating systems.

### Run a skill in a forked context

`feature(forked-skill-context)`

By default, when VS Code loads a skill, the skill's instructions are added to the parent agent's context window. For large skills, or skills whose intermediate reasoning isn't relevant to the rest of your conversation, you can instead run the skill in a **forked context**. In a forked context, the skill executes in a dedicated subagent and only its final result is returned to the parent agent. This keeps your main conversation's context clean.

To run a skill in a forked context, set the `context` field in the `SKILL.md` frontmatter to `fork`:

```markdown
---
name: review-pr
description: Review a pull request for code quality, style, and correctness. Use when asked to review a PR.
context: fork
---

# PR review

Follow these steps to review the pull request...
```

Use `context: fork` for skills that:

* Read many files or run lengthy investigations whose details don't need to stay in the main conversation
* Produce a focused result (such as a summary, a report, or a small set of edits) that the parent agent can act on directly
* Should not influence the parent agent's behavior beyond their final output

> [!NOTE]
> To run a skill in a forked context, enable the ``github.copilot.chat.skillTool.enabled`` setting in VS Code.

## Example skills

The following examples demonstrate different types of skills you can create.

<details>
<summary>Example: Web application testing skill</summary>

````markdown
---
name: webapp-testing
description: Guide for testing web applications using Playwright. Use this when asked to create or run browser-based tests.
---

# Web Application Testing with Playwright

This skill helps you create and run browser-based tests for web applications using Playwright.

## When to use this skill

Use this skill when you need to:
- Create new Playwright tests for web applications
- Debug failing browser tests
- Set up test infrastructure for a new project

## Creating tests

1. Review the [test template](./test-template.js) for the standard test structure
2. Identify the user flow to test
3. Create a new test file in the `tests/` directory
4. Use Playwright's locators to find elements (prefer role-based selectors)
5. Add assertions to verify expected behavior

## Running tests

To run tests locally:
```bash
npx playwright test
```

To debug tests:
```bash
npx playwright test --debug
```

## Best practices

- Use data-testid attributes for dynamic content
- Keep tests independent and atomic
- Use Page Object Model for complex pages
- Take screenshots on failure
````

</details>

<details>
<summary>Example: GitHub Actions debugging skill</summary>

````markdown
---
name: github-actions-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows.
---

# GitHub Actions Debugging

This skill helps you debug failing GitHub Actions workflows in pull requests.

## Process

1. Use the `list_workflow_runs` tool to look up recent workflow runs for the pull request and their status
2. Use the `summarize_job_log_failures` tool to get an AI summary of the logs for failed jobs
3. If you need more information, use the `get_job_logs` or `get_workflow_run_logs` tool to get the full failure logs
4. Try to reproduce the failure locally in your environment
5. Fix the failing build and verify the fix before committing changes

## Common issues

- **Missing environment variables**: Check that all required secrets are configured
- **Version mismatches**: Verify action versions and dependencies are compatible
- **Permission issues**: Ensure the workflow has the necessary permissions
- **Timeout issues**: Consider splitting long-running jobs or increasing timeout values
````

</details>

## Use skills as slash commands

Skills are available as slash commands in chat, alongside [prompt files](/docs/agent-customization/prompt-files.md). Type `/` in the chat input field to see a list of available skills and prompts, and select a skill to invoke it.

You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`.

By default, all skills appear in the `/` menu. Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each skill is accessed:

| Configuration | Slash command | Auto-loaded by Copilot | Use case |
|---|---|---|---|
| Default (both properties omitted) | Yes | Yes | General-purpose skills |
| `user-invocable: false` | No | Yes | Background knowledge skills that the model loads when relevant |
| `disable-model-invocation: true` | Yes | No | Skills you only want to run on demand |
| Both set | No | No | Disabled skills |

## How Copilot uses skills

Skills load content progressively to keep your context efficient. Here is an example of how Copilot uses the `webapp-testing` skill:

1. **Discovery**: Copilot reads the skill's `name` and `description` from the YAML frontmatter. When you ask "help me test the login page", Copilot matches this to the `webapp-testing` skill based on its description.

2. **Instructions loading**: Copilot loads the `SKILL.md` body into its context, giving it access to the detailed testing procedures and guidelines. You can also trigger this step directly by typing `/webapp-testing` in chat.

3. **Resource access**: As Copilot works through the instructions, it accesses additional files in the skill directory, such as `test-template.js` or example scenarios, only when it references them. If a file isn't referenced in the instructions, it won't be loaded.

This three-level loading system means you can install many skills without consuming context. Copilot loads only what is relevant for each task.

Skills that opt in to a [forked context](#run-a-skill-in-a-forked-context) follow the same discovery step, but their instructions and any files they read are loaded into a separate subagent. Only the skill's final result is returned to the parent agent.

## Use shared skills

You can use skills created by others to enhance Copilot's capabilities. The [github/awesome-copilot](https://github.com/github/awesome-copilot) repository contains a growing community collection of skills, custom agents, instructions, and prompts. The [anthropics/skills](https://github.com/anthropics/skills) repository contains additional reference skills.

You can also discover and install skills that are bundled in [agent plugins](/docs/agent-customization/agent-plugins.md). Skills from installed plugins appear alongside your locally defined skills in the **Configure Skills** menu.

To use a shared skill:

1. Browse the available skills in the repository
1. Copy the skill directory to your `.github/skills/` folder
1. Review and customize the `SKILL.md` file for your needs
1. Optionally, modify or add resources as needed

> [!TIP]
> Always review shared skills before using them to ensure they meet your requirements and security standards. VS Code's [terminal tool](/docs/agents/run/tools.md#run-terminal-commands) provides controls for script execution, including [auto-approve options](/docs/agents/run/approvals.md#automatically-approve-terminal-commands) with configurable allow-lists and tight controls over which code runs. Learn more about [security considerations](/docs/agents/run/security.md#approvals-and-review) for auto-approval features.

## Contribute skills from extensions

Extensions can contribute skills using the `chatSkills` contribution point in their `package.json`. The path must point to a directory that contains a `SKILL.md` file, following the [Agent Skills specification](https://agentskills.io/specification).

### Required folder structure

The skill directory must follow this structure:

```text
extension-root/
└── skills/
    └── my-skill/           # Directory name must match the `name` field in SKILL.md
        └── SKILL.md         # Required
```

### Register the skill in package.json

Add the `chatSkills` contribution point in your extension's `package.json`. The `path` property must point to the corresponding `SKILL.md` file:

```json
{
  "contributes": {
    "chatSkills": [
      {
        "path": "./skills/my-skill/SKILL.md"
      }
    ]
  }
}
```

> [!IMPORTANT]
> The `name` field in the `SKILL.md` frontmatter must match the parent directory name. For example, if the directory is `skills/my-skill/`, the `name` field must be `my-skill`. If the name does not match, the skill is not loaded.

The `SKILL.md` file follows the same format as [project and personal skills](#create-a-skill). For example:

```markdown
---
name: my-skill
description: Description of what the skill does and when to use it.
---

# My Skill

Detailed instructions for the skill...
```

## Agent Skills standard

Agent Skills is an open standard that enables portability across different AI agents. Skills you create in VS Code work with multiple agents, including:

* **GitHub Copilot in VS Code**: Available in chat and agent mode
* **GitHub Copilot CLI**: Accessible when working in the terminal
* **GitHub Copilot app**: Available in the dedicated desktop experience.
* **Copilot cloud agent**: Used during automated coding tasks
* **[product.prodname_openai_codex] integration (Experimental)**: Discovers workspace skills in `.github/skills/` after you [set up the integration](/docs/agents/run/agent-harnesses.md#codex).

Learn more about the Agent Skills standard at [agentskills.io](https://agentskills.io).

## Related resources

* [Customize AI responses overview](/docs/agent-customization/overview.md)
* [Create custom instructions](/docs/agent-customization/custom-instructions.md)
* [Create reusable prompt files](/docs/agent-customization/prompt-files.md)
* [Create custom agents](/docs/agent-customization/custom-agents.md)
* [Agent Skills specification](https://agentskills.io)
* [Reference skills repository](https://github.com/anthropics/skills)
* [Discover and manage agent plugins](/docs/agent-customization/agent-plugins.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/custom-agents.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/custom-agents
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md
- **SHA256_FINGERPRINT**: `307ba85bc0c173b26fd0b6432a208178221b4d028496aafed441398e1af58a23`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.861725+00:00
---

**MetaDescription**: Create and manage custom agents in VS Code for specialized development roles, tools, and workflows.

# Custom agents in VS Code

Custom agents combine instructions, tools, and an optional language model into a reusable configuration for a specific role, such as planning or code review. Switch to a custom agent instead of repeating the same instructions and selecting tools for every conversation.

This article shows you how to create, use, and manage custom agents in VS Code, configure their files, and connect them with handoffs.

> [!TIP]
> **Not sure which customization to use?** See the [decision matrix](/docs/agents/concepts/customization.md#customization-options-at-a-glance) to compare custom agents with prompt files, agent skills, and the other options.

## When to use a custom agent

Create a custom agent when a recurring task needs its own instructions, tools, or model. For example:

* Restrict a code review agent to read-only tools and give it your team's review criteria.
* Give a planning agent your team's plan template and hand off to an implementation agent.
* Run a focused research agent as a [subagent](/docs/agents/run/subagents.md#run-a-custom-agent-as-a-subagent) to keep its work out of the main conversation's context.
* Share the same workflow with your repository or organization.

Custom agents appear in the agent picker alongside the [built-in agents](/docs/agents/run/agent-harnesses.md#choose-a-built-in-agent). The tools and controls available to a custom agent depend on the selected [agent harness](/docs/agents/run/agent-harnesses.md).

When you select a custom agent, it applies to your requests until you switch agents. In the Copilot harness, the agent's instructions are added to your [custom instructions](/docs/agent-customization/custom-instructions.md) and take precedence if they conflict. If the agent specifies a `tools` list, only those tools are available. Another agent can also run a custom agent as a subagent, or a [handoff](#handoffs) can switch the conversation to it.

## Create a custom agent

Use the [Agent Customizations editor](/docs/agent-customization/overview.md#agent-customizations-editor) (Preview) to create an agent in your workspace or at the user level.

Use the **Session Target** UI control to [select the agent harness](/docs/agents/run/agent-harnesses.md#select-a-harness) you intend to use, then open the editor from either surface:

* **Agents window**: Select **Agents** in the **Customizations** panel in the left sidebar.

* **Chat view**: Select **Open Customizations** in the Chat view title bar, or run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``). Then select **Agents**.

The editor shows customizations for the selected harness. Follow these steps to create an agent file:

1. Select **New Agent** (plus icon) next to the **Workspace** or **User** group, depending on where you want to store the agent file.

    ![Screenshot showing the Agent Customizations editor and the dropdown to create a new custom agent.](images/customization/create-custom-agent-2.png)

    Alternatively, run the **Chat: New Custom Agent** command from the Command Palette (``Shortcut: workbench.action.showCommands``).

1. Select the location and enter a file name for the custom agent. This is the default name that appears in the agents dropdown.

1. Provide the details in the newly created `.agent.md` file, and then save it.

    * Fill in the YAML frontmatter to configure the agent's name, description, tools, and other options.
    * Add instructions for the agent in the body of the file. Use the [planning agent example](#custom-agent-file-structure) as a starting point.

1. [Select your custom agent in chat](#use-a-custom-agent) and try a prompt to check that it follows your instructions.

You can modify existing custom agents by opening them in the Agent Customizations editor.

> [!TIP]
> You can let an agent generate a custom agent for you based on a description. For example, enter a prompt like "Create a workspace custom agent for code reviews."

### Custom agent file structure

A custom agent file combines an optional FrontMatter header with Markdown instructions. The header configures the agent's name, description, tools, and other options. The Markdown body describes what the agent should do and what it should return.

For all supported fields and defaults, see the [Custom agent file reference](/docs/agents/reference/custom-agent-file-reference.md).

For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:

```markdown
---
name: Planner
description: Generate an implementation plan without changing code
tools: ['read', 'search']
---
Research the requested feature or refactoring task.
Do not edit files. Return a Markdown plan with these sections:
* Overview
* Requirements
* Implementation steps
* Tests to add or update
```

To try it, select **Planner** and describe a change you want to plan. Review its plan before starting implementation. You can later [add a handoff](#handoffs) to continue with an implementation agent in Local.

For more examples, see the community-contributed [Awesome Copilot agents](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md).

## Use a custom agent

Select the intended harness from the **Session Target** UI control, then choose your custom agent from the **Agent** dropdown in chat. Enter a prompt for its role and review the response and tool calls. The custom agent remains selected until you switch agents.

If the agent doesn't appear, check that its file is in a [supported location](#custom-agent-file-locations) for the selected harness and that its [visibility configuration](#customize-the-agents-dropdown-list) permits user invocation.

## Customize the agents dropdown list

To keep a custom agent available as a [subagent](/docs/agents/run/subagents.md) without listing it in the **Agent** dropdown, set `user-invocable: false` in its YAML frontmatter:

```yaml
user-invocable: false
```

This property controls picker visibility in both **Local** and **Copilot**. To show the agent again, set it to `true` or remove the property. Subagent invocation is controlled separately by `disable-model-invocation`.

Editing this property changes the agent definition, not a personal visibility preference. If you share the file in a repository, the change applies to everyone who uses that definition. It doesn't delete the agent file.

> [!NOTE]
> The Agent Customizations editor doesn't provide an eye-icon show or hide control for custom agents in either **Local** or **Copilot**. For agents contributed by an extension, manage the contributing extension instead. See [How do I remove a custom agent?](#how-do-i-remove-a-custom-agent).

## Custom agent file locations

You can define custom agents for a specific workspace or at the user level, where they are available across all your workspaces. Select the intended harness before you create an agent so the Agent Customizations editor stores it in a supported location.

| Scope | Default file location | File format |
|-------|-----------------------|-------------|
| Workspace | `.github/agents` folder | `.agent.md` or `.md` files |
| Workspace (Claude format) | `.claude/agents` folder | `.md` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |
| User (Copilot) | `~/.copilot/agents` folder | `.agent.md` or `.md` files |
| User ([product.prodname_anthropic_claude]) | `~/.claude/agents` folder | `.md` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |

To create a user-level custom agent, use the Agent Customizations editor or the **Chat: New Custom Agent** command. Store the file in a supported folder on the machine where the selected harness runs.

<a id="claude-agent-format"></a>

For Claude-specific fields and compatibility with Local, see the [Claude agent format reference](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format).

> [!TIP]
> In a monorepo, enable ``chat.useCustomizationsInParentRepositories`` to discover custom agents from the parent repository root. Learn more about [parent repository discovery](/docs/agent-customization/overview.md#use-customizations-in-a-monorepo).

### Local harness locations and migration

The **Local** harness stores user-level custom agents in VS Code profile storage, separate from harness user folders such as `~/.copilot/agents` and `~/.claude/agents`. To reuse profile-based agents with another harness, [move them to that harness's user folder](/docs/agent-customization/migrate-customizations.md#move-user-agents-and-instructions).

The deprecated ``chat.agentFilesLocations`` and ``chat.modeFilesLocations`` settings add other locations for the Local harness only. To reuse agents from these locations with the Copilot harness, [move them to supported locations](/docs/agent-customization/migrate-customizations.md#move-customizations-from-configured-locations).

## Handoffs

In the **Local** harness, handoffs connect agents into a workflow with suggested next steps. After a chat response completes, handoff buttons let you switch to another agent with the conversation context and a pre-filled prompt.

Use handoffs to review one stage of a task before starting the next. For example:

* **Planning to implementation**: Review a plan, then hand off to an implementation agent to start coding.
* **Implementation to review**: Complete implementation, then switch to a code review agent.
* **Failing tests to passing tests**: Review generated tests, then hand off to an agent that implements the changes needed to pass them.

For example, extend the [Planner agent](#custom-agent-file-structure) with a transition to the built-in **Agent** for implementation:

1. Add this `handoffs` entry to the Planner file's existing YAML header, before its closing `---` delimiter:

    ```yaml
    handoffs:
      - label: Implement Plan
        agent: agent
        prompt: Implement the plan outlined above.
        send: false
    ```

1. In a Local harness session, select **Planner** and ask it to plan a change.
1. Review the completed plan, then select **Implement Plan**.
1. Review the pre-filled implementation prompt and send it when you're ready for code changes.

Set `send: true` to submit the handoff prompt automatically. For all properties, including selecting a model for the next step, see the [handoff field reference](/docs/agents/reference/custom-agent-file-reference.md#handoff-fields).

Handoffs switch the active agent in your conversation. To delegate work without switching the main agent, use [subagents](/docs/agents/run/subagents.md#delegate-implementation-to-a-worker).

## Tool list priority

For how Local resolves tool lists from a custom agent and a prompt file, see [Tool list priority in the file reference](/docs/agents/reference/custom-agent-file-reference.md#tool-list-priority).

## Share custom agents across teams

To share custom agents across your team, you can create a workspace-level custom agent (`.github/agents` folder). If you want to share custom agents across multiple workspaces within your organization, you can define them at the GitHub organization level.

VS Code automatically detects custom agents defined at the organization level to which your account has access. These agents appear in the Agents dropdown in chat alongside the built-in agents, and your personal and workspace custom agents.

Discovery of organization-level custom agents is enabled by default. To stop showing organization-level custom agents in chat, set ``github.copilot.chat.organizationCustomAgents.enabled`` to `false`.

Learn how you can [create custom agents for your organization](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) in the GitHub documentation.

## Frequently asked questions

### Are custom agents different from chat modes?

Custom agents were previously known as custom chat modes. The functionality remains the same, but the terminology has been updated to better reflect their purpose in customizing AI behavior for specific tasks.

If you have existing `.chatmode.md` files, rename them to `.agent.md` and place them in one of the [supported custom agent locations](#custom-agent-file-locations).

### How do I remove a custom agent?

To remove a custom agent you maintain, use either of these methods:

* Delete its file from the workspace or [user-level location](#custom-agent-file-locations).
* Select **Configure Custom Agents** from the agents dropdown to open the Agent Customizations editor, hover over the custom agent, and select the trash icon.

Deleting a shared workspace agent also removes it for others when they receive the repository change. To keep the definition but remove it from the picker, see [Customize the agents dropdown list](#customize-the-agents-dropdown-list).

You can't delete extension-provided agents from the Agent Customizations editor. Disable or uninstall the contributing extension to remove its agents. This also affects the extension's other features.

### How do I know where a custom agent comes from?

The agents dropdown includes built-in agents and custom agents from user-level files, your workspace, organizations, extensions, and plugins.

To identify the source of a custom agent:

1. Select **Configure Custom Agents** from the agents dropdown.
1. Hover over the custom agent in the list. The source location is displayed in a tooltip.

> [!TIP]
> Use the chat customization diagnostics view to see all loaded custom agents, prompt files, instruction files, and skills along with any errors. Right-click in the Chat view and select **Diagnostics**. Learn more about [troubleshooting AI in VS Code](/docs/agents/agent-troubleshooting/troubleshooting.md).

## Security considerations

Custom agents can restrict which tools are available, which gives you control over what the AI can do. For security-sensitive workflows, create agents with read-only tools to prevent unintended modifications. When sharing agents in a repository, review the tool list and instructions to ensure they follow the principle of least privilege.

## Related resources

* [Custom agent file reference](/docs/agents/reference/custom-agent-file-reference.md)
* [Coordinate research and implementation with subagents](/docs/agents/run/subagents.md#delegate-implementation-to-a-worker)
* [Add agent-scoped hooks](/docs/agent-customization/hooks.md#agent-scoped-hooks-for-the-local-harness)
* [Planning with agents](/docs/agents/run/planning.md)
* [Customize AI with custom instructions](/docs/agent-customization/custom-instructions.md)
* [Use tools with agents](/docs/agents/run/tools.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/custom-instructions.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-instructions.md
- **SHA256_FINGERPRINT**: `0f63c89b684c82224eb83894bf346abff1376bc93f2c1d938b3f3927cff8e6ee`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.787420+00:00
---

**MetaDescription**: Create custom instructions in VS Code that align AI responses with project standards and development practices.

# Use custom instructions in VS Code

Custom instructions provide reusable context that helps AI follow your coding practices and project requirements. Instead of repeating guidelines in every chat prompt, store them in Markdown files that you can share with your team or reuse across projects.

This article helps you choose an instruction type and location, configure when instructions apply, and verify that your agent uses them. For a guided setup workflow, see [Configure AI for your codebase](/docs/agents/guides/customize-copilot-guide.md).

Instruction support depends on the [agent harness](/docs/agents/concepts/agent-harnesses.md) selected for your session. Each harness uses its own discovery rules and file formats. If you select the Local harness, VS Code uses the Local harness-specific instruction settings described in this article.

> [!TIP]
> Use the [Agent Customizations editor](/docs/agent-customization/overview.md#agent-customizations-editor) to discover, create, and manage customizations for the selected agent harness. Run **Chat: Open Customizations** from the Command Palette.

> [!NOTE]
> Custom instructions are not taken into account for [inline suggestions](/docs/editing/ai-powered-suggestions.md) as you type in the editor.

## Types of instruction files

Select the intended harness before you open the Agent Customizations editor. The editor shows the customizations available to that harness.

### Choose a format

Use an instruction format supported by the selected harness.

| Harness | Recommended project instructions | Targeted instructions |
|---------|----------------------------------|-----------------------|
| Copilot | [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) or [`AGENTS.md`](#use-an-agentsmd-file) | [`.github/instructions/**/*.instructions.md`](#use-instructionsmd-files) |
| [product.prodname_anthropic_claude] | [`CLAUDE.md`](#use-a-claudemd-file) | Markdown files in `.claude/rules` |
| [product.prodname_openai_codex] | [`AGENTS.md`](#use-an-agentsmd-file) | `AGENTS.md` files in subfolders |

> [!NOTE]
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.

`AGENTS.md` is not specific to Codex. It is a cross-agent format that you can use as the shared project instructions file when your selected harnesses support it. Some harnesses also recognize additional formats.

If your team uses multiple harnesses, use a shared format that they all support when possible. When you need separate files, keep shared requirements consistent and avoid contradictory copies.

### Choose a scope

Store instructions at the narrowest scope that matches how you want to use and share them.

| Scope | Use it for | Storage |
|-------|------------|---------|
| Workspace | Project conventions shared with contributors | A supported folder in the repository or session working folder |
| User | Personal preferences across projects | A user folder supported by the selected harness |
| Organization | Centrally managed requirements for supported Copilot sessions | GitHub organization settings |

User instructions in harness folders, such as `~/.copilot/instructions` and `~/.claude/rules`, do not roam through Settings Sync. Local harness instructions stored in your VS Code profile can roam through Settings Sync.

### Choose activation behavior

Project instructions are automatically included according to the selected harness. Use targeted instructions when guidance applies only to specific files or tasks:

* **File pattern**: VS Code automatically attaches an `.instructions.md` file when its `applyTo` pattern matches a file that the agent creates or modifies.
* **Task relevance**: a descriptive `description` helps the agent decide whether to load an instructions file for the current task.
* **Manual**: attach an instructions file to an individual chat request.

For Claude rules, use the `paths` frontmatter property instead of `applyTo`.

To reference files or URLs in instructions, use Markdown links. Relative file paths resolve from the instructions file. Use `/` path separators to keep instructions portable across operating systems.

## Use a `.github/copilot-instructions.md` file

For Copilot sessions, use `.github/copilot-instructions.md` for project-wide guidance. Store the file in the `.github` folder at the repository root.

The Local harness also discovers this workspace file when ``github.copilot.chat.codeGeneration.useInstructionFiles`` is enabled.

Use `copilot-instructions.md` for:

* Coding style and naming conventions that apply across the project.
* Technology stack declarations and preferred libraries.
* Architectural patterns to follow or avoid.
* Security requirements and error handling approaches.
* Documentation standards.

For personal, always-on instructions in Copilot sessions, use `~/.copilot/copilot-instructions.md`.

Follow these steps to create a `.github/copilot-instructions.md` file in your workspace:

1. Create a `.github/copilot-instructions.md` file at the root of your repository. If needed, create a `.github` directory first.

1. Add concise, project-specific instructions in Markdown.

<details>
<summary>Example: General coding guidelines</summary>

```markdown
# Project instructions

## Architecture

* Add HTTP handlers under `src/api/routes`.
* Keep database access in `src/repositories` so handlers remain independently testable.

## Validation

* Run `npm test -- <changed-package>` after changing application code.
* Add or update tests for every behavior change.
```

</details>

## Use `.instructions.md` files

You can create file-based instructions with `*.instructions.md` Markdown files. VS Code automatically attaches files with an `applyTo` pattern that matches the files being changed. The agent can also load an instructions file on demand when its `description` matches the current task.

Use `.instructions.md` files for:

* Different conventions for frontend and backend code.
* Language-specific guidelines in a monorepo.
* Framework-specific patterns for specific modules.
* Specialized rules for test files or documentation.

### Instructions file locations

The supported location depends on the session type and selected harness.

| Session and scope | Default file location |
|-------------------|-----------------------|
| Copilot workspace | `.github/instructions` |
| [product.prodname_anthropic_claude] workspace | `.claude/rules` |
| Copilot user | `~/.copilot/instructions` |
| [product.prodname_anthropic_claude] user | `~/.claude/rules` |

Use the Agent Customizations editor to create user instructions in a location supported by the selected harness. To move profile-based instructions to a supported harness user folder, use [user customization migration](/docs/agent-customization/migrate-customizations.md#move-user-agents-and-instructions).

> [!NOTE]
> **For Local harness sessions:** Workspace instruction files use `.github/instructions` or `.claude/rules`, and user instructions use VS Code profile storage. The deprecated ``chat.instructionsFilesLocations`` setting adds other locations for the Local harness only. To reuse those instructions with the Copilot harness, [move them to supported locations](/docs/agent-customization/migrate-customizations.md#move-customizations-from-configured-locations).

VS Code searches these folders recursively, which enables you to organize instructions files in subdirectories. For example, you can group instructions by team, language, or module:

```text
.github/instructions/
  frontend/
    react.instructions.md
    accessibility.instructions.md
  backend/
    api-design.instructions.md
  testing/
    unit-tests.instructions.md
```

> [!TIP]
> In a monorepo, enable ``chat.useCustomizationsInParentRepositories`` to discover instructions from the parent repository root. Learn more about [parent repository discovery](/docs/agent-customization/overview.md#use-customizations-in-a-monorepo).

### Instructions file format

For `.instructions.md` files, YAML frontmatter controls how the instructions are discovered and applied:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Display name shown in the UI. Defaults to the file name. |
| `description` | No | Describes the tasks for which the file is relevant. Include it for on-demand discovery. |
| `applyTo` | No | Glob pattern that automatically applies the instructions to matching files, relative to the workspace root. Use `**` to match all files. |

The body contains the instructions in Markdown format.

```markdown
---
name: 'Python testing'
description: 'Use when creating or updating Python unit tests.'
applyTo: '**/*.py'
---
# Python testing

* Use `pytest` fixtures from `tests/conftest.py` instead of creating duplicate setup helpers.
* Name tests `test_<behavior>_<condition>`.
* Run `python -m pytest <test-file>` after changing a test.
```

If you omit both `description` and `applyTo`, attach the file manually when you want to use it. For Claude rules, use the `paths` property instead of `applyTo`.

### Create an instructions file

When you create an instructions file, choose whether to store it at workspace or user scope. Workspace instructions apply only to that workspace, while user instructions are available across multiple workspaces for the corresponding harness.

To create an instructions file:

1. Select the agent harness that should use the instructions.

1. In the Chat view, select **Open Customizations** in the title bar, or run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).

1. In the Agent Customizations editor, select **Instructions**.

1. Select **New Instruction** (plus icon) next to the **Workspace** or **User** group, depending on where you want to store the file.

1. Select a supported location and enter a file name.

1. Add the frontmatter and Markdown instructions, and then save the file.

You can also run **Chat: New Instructions File** from the Command Palette (``Shortcut: workbench.action.showCommands``).

![Screenshot showing the Instructions section and the menu for creating an instructions file in the Agent Customizations editor.](images/customization/create-instructions-file.png)

### Generate an instructions file with AI

In chat, describe the convention or guideline you want to enforce and ask the agent to create an instructions file. This works for every harness, including **Copilot**. Confirm that the generated file uses the format and location for the selected harness.

With **Local** selected, you can also use these shortcuts, which aren't available for other harnesses:

* Type `/create-instructions` in chat and describe the convention or guideline.
* Type `/init` to generate project-wide instructions. In the Chat view, the **Customize Your Agent** box on the **Overview** page of the Agent Customizations editor also uses `/init`.

Review generated instructions before you use them. Verify commands, paths, and conventions against the repository.

## Use an `AGENTS.md` file

`AGENTS.md` is a cross-agent format for project guidance. Multiple harnesses, including Copilot and [product.prodname_openai_codex], support it. The Local harness also supports this format. Place the primary file at the repository root.

Use `AGENTS.md` when:

* You work with multiple compatible AI coding agents and want to share one set of instructions.
* You want subfolder-level instructions that apply to specific parts of a monorepo.

For the Local harness, configure the ``chat.useAgentsMdFile`` setting to enable or disable support for `AGENTS.md` files.

### Use multiple `AGENTS.md` files

`feature(nested-agents-md-files)`

Use nested `AGENTS.md` files when different folders need different guidance. Follow the selected harness's working-folder and nested-instruction rules for discovery and activation.

> [!NOTE]
> **For Local harness sessions:** The ``chat.useNestedAgentsMdFiles`` setting controls support for nested `AGENTS.md` files and is disabled by default. When enabled, VS Code lists these files with their folder locations so the agent can load relevant instructions for the task.

> [!TIP]
> For folder-specific instructions, you can also use multiple [`.instructions.md`](#use-instructionsmd-files) files with different `applyTo` patterns that match the folder structure.

## Use a `CLAUDE.md` file

For [product.prodname_anthropic_claude] sessions, use `CLAUDE.md` at the repository root for project-wide guidance. The [product.prodname_anthropic_claude] harness also supports additional native locations and formats, such as `.claude/CLAUDE.md` and `.claude/rules`.

The Local harness searches for Claude instructions in these locations when ``chat.useClaudeMdFile`` is enabled:

| Location | Description |
|----------|-------------|
| Workspace root | `CLAUDE.md` in the root of your workspace |
| `.claude` folder | `.claude/CLAUDE.md` in your workspace |
| User home | `~/.claude/CLAUDE.md` for personal instructions across all projects |
| Local variant | `CLAUDE.local.md` for local-only instructions (not committed to version control) |

To enable or disable support for `CLAUDE.md` files, configure the ``chat.useClaudeMdFile`` setting.

> [!NOTE]
> For `.claude/rules` instructions files, use a `paths` property instead of `applyTo` for glob patterns, following the [Claude rules format](https://code.claude.com/docs/en/memory#basic-structure). The `paths` property accepts an array of glob patterns and defaults to `**` when omitted.

## Generate custom instructions for your workspace

The Agent Customizations editor can start a chat that analyzes your repository and creates instructions for the selected harness. Review the result before saving it because generated commands, architecture details, or conventions might be incomplete.

For a complete generation and verification workflow, see [Configure AI for your codebase](/docs/agents/guides/customize-copilot-guide.md).

## Verify your instructions

Test instructions with a representative task where your project guidance affects the result.

1. Select the intended harness, open the Agent Customizations editor, and confirm that the instructions file is listed. This verifies discovery, but not whether the instructions are followed.
1. Start a new chat with the same harness and repository.
1. Ask the agent to complete a small task with a clear success criterion.
1. Expand **References** in the response and confirm that the expected instructions were used.
1. Review the result and tool activity to check that the agent followed the relevant conventions and validation steps.

If the file is missing or the result does not follow the instructions, see [Why is my instructions file not being applied?](#why-is-my-instructions-file-not-being-applied).

## Other instruction sources

### Share custom instructions across teams

To share custom instructions across multiple workspaces and repositories within your GitHub organization, you can define them at the GitHub organization level.

Supported Copilot sessions automatically include organization instructions that your account can access. Organization instructions are additive to user and repository instructions.

To enable discovery of organization-level custom instructions, set ``github.copilot.chat.organizationInstructions.enabled`` to `true`.

Learn how you can [add custom instructions for your organization](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions) in the GitHub documentation.

<a name="sync-local-agent-instructions-across-devices"></a>

### Sync Local harness instructions across devices

VS Code can sync Local harness instructions stored in your user profile by using [Settings Sync](/docs/configure/settings-sync.md). User instructions in harness folders, such as `~/.copilot/instructions` and `~/.claude/rules`, do not roam through Settings Sync.

To sync profile instructions, enable Settings Sync and run **Settings Sync: Configure** from the Command Palette (``Shortcut: workbench.action.showCommands``). Select **Prompts and Instructions** from the list of settings to sync.

### Specify instructions for generated content

> [!NOTE]
> Settings-based code generation and test generation instructions are deprecated as of VS Code 1.102. Use [file-based instructions](#types-of-instruction-files) instead.

For code review, commit messages, and pull request descriptions, you can still use VS Code settings to define custom instructions. These settings accept an array of objects with either a `text` property (inline instruction) or a `file` property (path to a Markdown file).

| Scenario | Setting |
|----------|---------|
| Review selected code | ``github.copilot.chat.reviewSelection.instructions`` |
| Commit messages | ``github.copilot.chat.commitMessageGeneration.instructions`` |
| Pull request descriptions | ``github.copilot.chat.pullRequestDescriptionGeneration.instructions`` |

## Resolve conflicting instructions

Applicable instruction sources are additive. Do not depend on a file order or precedence rule to resolve conflicts because discovery and merge behavior can differ by harness.

Keep shared requirements consistent across user, repository, and organization instructions. Remove duplicate guidance and resolve contradictions at their source.

For example, suppose organization instructions require an approved HTTP client, repository instructions identify the project's wrapper for that client, and personal instructions request a different library. A targeted instruction for API files might add another conflicting rule. Don't add a new instruction or assume that one source overrides the others.

1. Start a new chat with the intended harness and ask for a small change that matches the targeted instruction.
1. Use the Agent Customizations editor and Agent Debug Logs to check which instruction sources are discovered and whether they contain errors.
1. Expand **References** in the response to confirm which instructions were included for the request.
1. Compare the generated code, tool activity, and validation results with the repository requirement.
1. Resolve the contradiction in the source files. Remove or narrow the personal rule, and align the repository and targeted instructions with the reviewed organization requirement.
1. Repeat the same task in another new chat and compare the observed result.

For more diagnostic steps, see [Troubleshoot AI in VS Code](/docs/agents/agent-troubleshooting/troubleshooting.md) and [inspect the instructions sent in the model request](/docs/agents/agent-troubleshooting/chat-debug-view.md#instructions-or-a-prompt-file-are-not-applied).

## Tips for writing effective instructions

* Keep your instructions short and self-contained. Each instruction should be a single, simple statement. If you need to provide multiple pieces of information, use multiple instructions.

* Include the reasoning behind rules. When instructions explain _why_ a convention exists, the AI makes better decisions in edge cases. For example: "Use `date-fns` instead of `moment.js` because moment.js is deprecated and increases bundle size."

* Show preferred and avoided patterns with concrete code examples. The AI responds more effectively to examples than to abstract rules.

* Focus on non-obvious rules. Skip conventions that standard linters or formatters already enforce.

* For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.

* Store project-specific instructions in your workspace to share them with other team members and include them in your version control.
* Reuse and reference instructions files in your [prompt files](/docs/agent-customization/prompt-files.md) and [custom agents](/docs/agent-customization/custom-agents.md) to keep them clean and focused, and to avoid duplicating instructions.

## Frequently asked questions

### Why is my instructions file not being applied?

> [!TIP]
> Use the Agent Customizations editor to confirm that the selected harness discovers the file. To inspect loading details and errors, run **Developer: Open Agent Debug Logs** from the Command Palette, or select **Show Agent Debug Logs** from the ellipsis (**...**) menu in the Chat view. Learn more about [troubleshooting agent customizations](/docs/agents/agent-troubleshooting/troubleshooting.md).

If your instructions file is not being applied, check the following:

* Verify that the intended agent harness is selected.

* Verify that your instructions file is in a [supported location](#instructions-file-locations) for that harness and scope.

* For `*.instructions.md` files, check that `applyTo` matches a file the agent creates or modifies, or that `description` clearly identifies the relevant task. If neither applies, attach the file manually.

* For the Local harness, check that relevant settings are enabled. These include ``chat.includeApplyingInstructions`` for pattern-based instructions, ``chat.includeReferencedInstructions`` for linked instructions, and ``chat.useAgentsMdFile`` for `AGENTS.md`.

* Expand **References** in the chat response to check which instructions were used.

For advanced diagnostics, [inspect the instructions sent in the model request](/docs/agents/agent-troubleshooting/chat-debug-view.md#instructions-or-a-prompt-file-are-not-applied).

### How do I find an instruction file?

1. Select the agent harness that should use the instruction.
1. Run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).
1. Select **Instructions**, and then select the instruction to view its source and location.

If the instruction is missing, run **Developer: Open Agent Debug Logs** to inspect discovery and loading errors.

## Related resources

* [Create and manage agent customizations](/docs/agent-customization/overview.md)
* [Configure AI for your codebase](/docs/agents/guides/customize-copilot-guide.md)
* [Troubleshoot agent customizations](/docs/agents/agent-troubleshooting/troubleshooting.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/hooks.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/hooks
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/hooks.md
- **SHA256_FINGERPRINT**: `cf0b8eb526f3d21cbf3420ee8d412d6228c34eced8fff86b0ff6e209d5f35b5d`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.977158+00:00
---

**MetaDescription**: Configure agent hooks in VS Code for the Copilot, Claude, Codex, and Local harnesses.

# Configure agent hooks in Visual Studio Code (Preview)

Hooks run custom actions at specific points in an agent's lifecycle. Use hooks to automate workflows, validate operations, create audit trails, or enforce policies independently of the language model.

The selected [agent harness](/docs/agents/concepts/agent-harnesses.md) determines which hook implementation runs. Before you create or reuse a hook, identify the harness and use its configuration and event schema.

This article helps you choose the correct hook implementation, manage hooks from VS Code, and configure hooks for the Local harness.

> [!NOTE]
> The VS Code hooks experience is in Preview. Individual provider implementations might have a different lifecycle status. For example, hooks in the [copilot.copilot_sdk_short] are generally available.

> [!IMPORTANT]
> Your organization might restrict which hooks can run. Contact your administrator for more information. Administrators can learn how to [manage hooks in enterprise environments](/docs/enterprise/manage-ai-settings.md#enable-or-disable-hooks).

## Choose the hook implementation for your session

The **Session Target** UI control selects the agent harness. The harness owns the hook lifecycle and payloads.

| **Session Target** choice | Hook implementation | Configuration and event reference |
|----------------|---------------------|-----------------------------------|
| **Copilot** | Shared [copilot.copilot_sdk_short] implementation | Use the [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference). |
| **Claude** | Claude Agent SDK | Use the [Claude hooks reference](https://code.claude.com/docs/en/hooks). |
| **Codex** | Codex runtime | Use the [Codex hooks documentation](https://developers.openai.com/codex/hooks/). |
| **Cloud** | Selected cloud agent | Use the provider documentation. For Copilot cloud agent, see the [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference). |

> [!NOTE]
> **For Local harness sessions:** Use the [Local configuration](#configure-hooks-for-the-local-harness) in this article and the [Local hooks reference](/docs/agents/reference/hooks-reference.md). These hooks have their own events, settings, and payloads.

Some harnesses discover the same hook files, such as `.github/hooks/*.json` or `.claude/settings.json`. This file compatibility does not make their behavior identical. Supported events, event names, matchers, command properties, tool names, payloads, and output decisions can differ.

Copilot harness sessions use the same SDK hook implementation as Copilot CLI. Use the Copilot CLI sections of the GitHub reference for runtime configuration and payloads, but verify that the event is available in the selected VS Code version.

### Migrate hooks between harnesses

Before you switch harnesses for an existing workflow:

* Confirm that the destination harness discovers the hook file.
* Compare the supported events and command properties.
* Check tool names and input shapes before you reuse filters or validation logic.
* Validate scripts that read chat transcripts. Transcript formats are not a stable cross-harness API.
* Test output decisions, such as blocking a tool call or adding context.
* Confirm where the hook command runs and which files and environment variables it can access.

Do not validate a migration by changing only the language model. Select the destination harness from the **Session Target** UI control and start a test session.

## Create and manage hooks

Select the harness before you open the hooks interface. This ensures that VS Code shows the customizations for that harness.

To view and manage hooks:

1. Open the Chat view or Agents window.

1. Select the harness or Cloud target from the **Session Target** UI control.

1. Open the Agent Customizations editor:

    * In the Chat view, select **Open Customizations** in the title bar, and then select **Hooks**.
    * In the Agents window, select **Hooks** in the **Customizations** panel.
    * In the Chat view, with **Local** or **Copilot** selected, enter `/hooks` in the chat input.

1. Review the hook sources for the selected harness or Cloud target. Select a hook to open its configuration.

You can also run **Chat: Configure Hooks** from the Command Palette (``Shortcut: workbench.action.showCommands``) to manage Local hook files.

To generate a hook with AI, describe the hook you want in chat. With **Local** selected, you can also enter `/create-hook <description>` in chat or run **Chat: Generate Hook** from the Command Palette. These shortcuts aren't available for other harnesses. The `/create-hook` command generates hooks in `.github/hooks/`. Review the result against the destination harness reference before you use it.

For Claude and Codex, use the provider documentation for additional configuration and management options.

## Configure hooks for the Local harness

The following sections describe Local hook events, settings, payloads, and output decisions. These do not automatically apply to other harnesses.

### Create your first Local hook

The following hook records the name of every tool before the Local harness invokes it. Create `.github/hooks/audit.json` in your workspace:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "node .github/hooks/log-tool-use.cjs"
      }
    ]
  }
}
```

Create `.github/hooks/log-tool-use.cjs`:

```javascript
const fs = require('node:fs');

let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  const event = JSON.parse(input);
  fs.appendFileSync(
    '.github/hooks/tool-use.log',
    `${event.timestamp} ${event.tool_name}\n`
  );
});
```

Start a Local harness session and ask the agent to perform a task that uses tools. The hook adds each tool name to `.github/hooks/tool-use.log`. Add this log file to `.gitignore` if you don't want to commit it.

This example also helps you discover the exact Local tool names to use in validation hooks. Tool names and arguments differ between harnesses.

### Local hook file locations

The Local harness discovers hooks from these built-in locations:

| Scope | File location | Notes |
|-------|---------------|-------|
| Workspace | `.github/hooks/*.json` | Native VS Code or Copilot-compatible hook files. |
| Workspace, Claude format | `.claude/settings.json`, `.claude/settings.local.json` | Requires ``chat.useClaudeHooks``, which is off by default. |
| User | `~/.copilot/hooks/*.json` | Available across Local harness sessions. |
| User, Claude format | `~/.claude/settings.json` | Requires ``chat.useClaudeHooks``. |
| Custom agent | `hooks` in `.agent.md` frontmatter | Runs only for that custom agent in the Local harness. |
| Plugin | `hooks.json` or `hooks/hooks.json`, depending on the plugin format | See [hooks in plugins](/docs/agents/reference/agent-plugin-reference.md#hooks-in-plugins). |

The ``chat.useHooks`` setting controls Local hook execution and is on by default. Workspace hook files are subject to [Workspace Trust](/docs/editing/workspaces/workspace-trust.md).

Use ``chat.hookFilesLocations`` to add or disable Local hook locations. The setting's default value is empty because the built-in locations are registered separately. Specify a folder to load all its `*.json` files, or specify an individual `.json` file. Paths can be relative to the workspace or start with `~`.

```jsonc
"chat.hookFilesLocations": {
  "custom/hooks": true,              // Load all JSON hook files in this folder.
  "~/my-hooks/security.json": true,  // Load one hook file.
  ".claude/settings.json": false     // Disable a built-in location.
}
```

> [!TIP]
> In a monorepo, enable ``chat.useCustomizationsInParentRepositories`` to discover hooks from the parent repository root. Learn more about [parent repository discovery](/docs/agent-customization/overview.md#use-customizations-in-a-monorepo).

### Local hook configuration formats

For new Local hooks, use a JSON file with PascalCase event names and command properties:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/validate-tool.sh",
        "windows": "powershell -File scripts\\validate-tool.ps1",
        "timeout": 15
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "npx prettier --write ."
      }
    ]
  }
}
```

The Local parser also accepts other hook file formats:

| Source format | How Local recognizes it | Local behavior to review |
|---------------|-------------------------|--------------------------|
| Native VS Code | PascalCase events without a numeric `version` property | Uses `command`, `windows`, `linux`, `osx`, and `timeout`. |
| Copilot | Numeric `version` property and lower camel case events | Maps Copilot event and command property names to the Local format. Runtime payloads still use the Local schema. |
| Claude | A `settings.json` or `settings.local.json` file in a `.claude` folder | Requires ``chat.useClaudeHooks``. Local parses nested commands but ignores matcher values, so every command for the event runs. |

For the complete Local command properties, input fields, output fields, and exit-code behavior, see the [Local hooks reference](/docs/agents/reference/hooks-reference.md).

> [!NOTE]
> An operating system override is selected from the extension host platform. In Remote Development windows, this platform might differ from the operating system that displays the VS Code UI.

### Local hook lifecycle events

The Local harness supports these events:

| Event | When it fires | Common uses |
|-------|---------------|-------------|
| [`SessionStart`](/docs/agents/reference/hooks-reference.md#sessionstart) | The first prompt starts a session. | Initialize resources or add project context. |
| [`UserPromptSubmit`](/docs/agents/reference/hooks-reference.md#userpromptsubmit) | The user submits a prompt. | Audit requests or add context. |
| [`PreToolUse`](/docs/agents/reference/hooks-reference.md#pretooluse) | Before the agent invokes a tool. | Block an operation, request approval, or change tool input. |
| [`PostToolUse`](/docs/agents/reference/hooks-reference.md#posttooluse) | After a tool completes successfully. | Validate results, run a formatter, or add context. |
| [`PreCompact`](/docs/agents/reference/hooks-reference.md#precompact) | Before conversation context is compacted. | Save state that should survive compaction. |
| [`SubagentStart`](/docs/agents/reference/hooks-reference.md#subagentstart) | A subagent starts. | Track nested agent use or add subagent context. |
| [`SubagentStop`](/docs/agents/reference/hooks-reference.md#subagentstop) | A subagent is about to stop. | Validate subagent results or require more work. |
| [`Stop`](/docs/agents/reference/hooks-reference.md#stop) | The current agent execution is about to stop. | Validate completion or require another action. |

When an event fires, the Local harness passes a JSON object to the command through standard input (stdin). The command can write JSON to standard output (stdout) to add context or control the next action. The event does not necessarily correspond to the end of the entire session.

<a name="agent-scoped-hooks-for-local"></a>

### Agent-scoped hooks for the Local harness

> [!NOTE]
> Agent-scoped hooks are in Preview and are supported only by the Local harness.

Add a `hooks` map to a [custom agent](/docs/agent-customization/custom-agents.md) to run commands only while that agent is active. Agent-scoped hooks run in addition to applicable user, workspace, and plugin hooks.

For example, save the following as `.github/agents/strict-formatter.agent.md`. Replace the command with your project's formatting script. The `PostToolUse` hook runs after every successful tool call while this agent is active, whether you select it directly or invoke it as a subagent.

```markdown
---
name: Strict Formatter
description: Format code after the agent uses a tool
hooks:
  PostToolUse:
    - type: command
      command: "./scripts/format-changed-files.sh"
---

Follow the project's formatting requirements.
```

When the custom agent runs as a subagent, its `Stop` hook is treated as `SubagentStop`. Agent-scoped hooks require ``chat.useHooks`` and a trusted workspace.

For the other fields in an agent definition, see the [custom agent file reference](/docs/agents/reference/custom-agent-file-reference.md#header-fields).

For custom agents contributed by Claude-format or legacy OpenPlugin plugins, use [plugin-root tokens](/docs/agents/reference/agent-plugin-reference.md#reference-plugin-paths-in-hook-commands) to reference bundled scripts without hardcoding installation paths.

### Local hook examples

<details>
<summary>Request approval for a specific tool</summary>

First, use the audit hook in the [quick start](#create-your-first-local-hook) or the agent debug logs to identify the exact Local tool name and input schema.

Create `.github/hooks/approval.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "node .github/hooks/require-approval.cjs",
        "env": {
          "SENSITIVE_TOOL_NAME": "<tool-name>"
        }
      }
    ]
  }
}
```

Create `.github/hooks/require-approval.cjs`:

```javascript
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  const event = JSON.parse(input);
  const decision = event.tool_name === process.env.SENSITIVE_TOOL_NAME
    ? {
        hookSpecificOutput: {
          hookEventName: 'PreToolUse',
          permissionDecision: 'ask',
          permissionDecisionReason: 'This tool requires manual approval.'
        }
      }
    : { continue: true };

  process.stdout.write(JSON.stringify(decision));
});
```

Replace `<tool-name>` with the exact Local tool name. Do not copy a tool name from another harness.

</details>

<details>
<summary>Add project context when a session starts</summary>

Create `.github/hooks/context.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "node .github/hooks/project-context.cjs"
      }
    ]
  }
}
```

Create `.github/hooks/project-context.cjs`:

```javascript
const packageJson = require('../../package.json');

process.stdout.write(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: 'SessionStart',
    additionalContext: `Project: ${packageJson.name} ${packageJson.version}`
  }
}));
```

</details>

## Troubleshoot hooks

First, confirm that the selected harness matches the hook reference you followed. A hook that appears in the Agent Customizations editor might still use different events or payloads when you switch harnesses.

For Local hooks:

* Run **Chat: Configure Hooks** to check which files the Local harness discovers.
* Open the [agent debug logs](/docs/agents/agent-troubleshooting/chat-debug-view.md#agent-debug-logs-panel) to inspect event names, tool schemas, hook input, and hook output.
* Open the **Output** panel and select the **GitHub Copilot Chat Hooks** channel to review command output and errors.
* Verify that ``chat.useHooks`` is enabled and the workspace is trusted.
* If you use a Claude-format file, enable ``chat.useClaudeHooks`` and remember that Local ignores matcher values.
* Increase `timeout` only after you confirm that the command is making progress.

For other harnesses, use the provider's hook reference and diagnostics. The Local settings ``chat.useHooks``, ``chat.hookFilesLocations``, and ``chat.useClaudeHooks`` configure only Local hook execution.

## Security considerations

> [!CAUTION]
> Hooks execute code with the permissions of their harness process. Review every hook and referenced script before you run it, especially in a shared repository or plugin.

* Treat hook configuration and scripts as executable code.
* Require approval before an agent edits a script that a later hook can execute.
* Validate all JSON input before you use values in a shell command.
* Give hook commands only the file, process, and network access they need.
* Store credentials in approved secret storage. Do not place secrets in hook configuration, scripts, output, or agent context.
* Review the trust and policy model for the selected harness. These controls are not portable across runtimes.

## Related resources

* [Local hooks reference](/docs/agents/reference/hooks-reference.md)
* [Choose an agent harness](/docs/agents/run/agent-harnesses.md)
* [Security considerations for AI agents](/docs/agents/run/security.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/language-models.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/language-models
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/language-models.md
- **SHA256_FINGERPRINT**: `12e8beded5cf37f757bab27ae8608aa6eb175617a6618920c1929d988cb4d460`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:30.002279+00:00
---

**MetaDescription**: Configure chat and inline models in VS Code, adjust thinking effort, and use your own API key.

# AI language models in VS Code

Visual Studio Code gives you access to multiple built-in language models, each optimized for different tasks. You can switch models for chat, inline suggestions, and utility tasks, and you can add more models by bringing your own API key.

For background on how language models work, their characteristics, and how to choose the right model, see [Language models concepts](/docs/agents/concepts/language-models.md).

## Change the model for chat

Use the language model picker in the chat input field to change the model for chat conversations and code editing.

![Screenshot that shows the model picker in the Chat view.](images/language-models/model-dropdown-change-model-v2.png)

Different models have different strengths. Use a fast model for quick edits and simple questions, and a reasoning model for complex refactoring, architectural decisions, or multi-step tasks. Depending on the [harness](/docs/agents/concepts/agent-harnesses.md) you are using, the list of available models might differ.

You can further extend the list of available models by [using your own language model API key](#bring-your-own-language-model-key).

> [!NOTE]
> In an untrusted workspace in [Restricted Mode](/docs/editing/workspaces/workspace-trust.md#restricted-mode), the chat model picker only shows **Auto**. Trust the workspace to restore the full model list.

> [!TIP]
> Install the AI Toolkit extension to add more language models to enhance GitHub Copilot capabilities.
>
> For more information, see [Change the chat model](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model#adding-more-models).

> [!NOTE]
> If you are a Copilot Business or Enterprise user, your administrator needs to enable certain models for your organization by opting in to `Editor Preview Features` in the [Copilot policy settings](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization) on GitHub.com.

## Configure thinking effort

Some models support configurable thinking effort, which controls how much reasoning the model applies to each request. For background on thinking and reasoning, see [Thinking and reasoning](/docs/agents/concepts/language-models.md#thinking-and-reasoning).

By default, VS Code sets recommended effort levels and has adaptive reasoning enabled, where the model dynamically determines how much to think based on the complexity of each request. For most use cases, the defaults work well.

> [!TIP]
> Higher thinking effort produces more thinking tokens, which increases [AI credit](/docs/agents/concepts/language-models.md#ai-credits-and-model-costs) consumption. Only increase thinking effort for genuinely complex tasks. Learn more about [optimizing AI credit usage](/docs/agents/guides/optimize-usage.md).

To configure the thinking effort:

1. Open the model picker in the chat input field and select a reasoning model.

1. Select the **>** arrow that appears next to the model name to open the **Thinking Effort** submenu.

    > [!NOTE]
    > Non-reasoning models, such as GPT-4.1 and GPT-4o, do not show the thinking effort submenu.

1. Select an effort level.

    ![Screenshot showing the Thinking Effort submenu in the model picker, with different effort levels such as None, Low, Medium, and High.](images/language-models/thinking-effort-submenu.png)

The model picker label updates to show the selected effort level, for example "Claude Sonnet 4.6 · High". The effort level is remembered per session, so revisiting an earlier session keeps the effort level it was using. New conversations start from the effort level you last set for that model.

> [!NOTE]
> The ``github.copilot.chat.anthropic.thinking.effort`` and ``github.copilot.chat.responsesApiReasoningEffort`` settings are deprecated. Configure thinking effort directly from the language model picker.

## Use auto model selection

With auto model selection, VS Code evaluates task complexity and real-time model availability to route each request to the optimal model. For background on how auto model selection works, see [Auto model selection](/docs/agents/concepts/language-models.md#auto-model-selection).

To use auto model selection, select **Auto** from the model picker in chat. Then use **Optimize for** to choose the tier that matches your priorities:

* **Efficiency** favors lower AI credit consumption.
* **Balance** balances capability and credit consumption.
* **Intelligence** favors more capable models for complex tasks.

Your organization can set a starting tier for new chats. The managed tier appears as **Default** in the **Optimize for** menu, but you can still choose a different tier. An explicit choice is preserved when the managed default changes or is removed.

You can see which model is used for generating a response by hovering over the chat response.

![Screenshot of a chat response, showing the selected model on hover.](images/language-models/chat-response-selected-model.png)

## Manage language models

You can use the language models editor to view all available models, choose which models are shown in the model picker, and add more models by adding from built-in providers or from extension-provided model providers.

To open the Language Models editor, open the model picker in the Chat view and select **Manage Language Models** (gear icon) or run the **Chat: Manage Language Models** command from the Command Palette. The Language Models editor opens by default in a [modal overlay](/docs/editing/getting-started/userinterface.md#modal-editors) on top of the editor area.

![Screenshot that shows the Language Models editor.](images/language-models/language-models-editor.png)

The editor lists all models available to you, showing key information such as the model capabilities, context size, billing details, and visibility status. By default, models are grouped by provider, but you can also group them by visibility.

You can search and filter models by using the following options:

* Text search with the search box
* Provider: `@provider:"OpenAI"`
* Capability: `@capability:tools`, `@capability:vision`, `@capability:agent`
* Visibility: `@visible:true/false`

### Customize the model picker

You can customize which models are shown in the model picker by changing the visibility status of models in the Language Models editor. You can show or hide models from any provider.

Hover over a model in the list and select the eye icon to show or hide the model in the model picker.

![Screenshot that shows the Language Models editor with the eye icon to show or hide models in the model picker.](images/language-models/language-models-hide.png)

### Pin favorite models

Pin models to keep them in a fixed position at the top of the model picker. Pinned models appear in a dedicated **Pinned** section and don't shift around as you use other models.

To pin or unpin a model:

1. Open the model picker in the chat input field.

1. Hover over a model and select the pin icon to add it to the **Pinned** section.

1. To unpin a model, hover over it in the **Pinned** section and select the unpin icon.

## Bring your own language model key

Bring Your Own Key (BYOK) lets you connect to any compatible model provider while still using the VS Code chat experience and tools. You can use BYOK to access models from other providers, to run models locally, or to use models that are not yet available as built-in options in VS Code.

BYOK models work without signing into a GitHub account and without a Copilot plan. This enables you to use AI chat features entirely with your own models, including fully offline scenarios with local models such as Ollama.

> [!NOTE]
> To use supported BYOK models in Copilot harness sessions in the Chat view or [Agents window](/docs/agents/run/agents-window.md), enable ``chat.agentHost.byokModels.enabled`` `feature(agent-host-byok-models)`.

You can also use these models to [override the models used for utility tasks in VS Code](#configure-models-for-other-features) (such as title generation and intent detection).

> [!NOTE]
> Some features still require a GitHub account: semantic search, inline suggestions (code completions), and features that rely on embeddings. BYOK applies to the chat experience and utility tasks only.

VS Code provides different options to add more language models:

* [Built-in providers](#add-a-model-from-a-built-in-provider): The provider you want is already listed (Azure, Anthropic, Gemini, OpenAI, and others).

* [Extensions](#add-a-model-provider-extension): A marketplace extension provides the model, for example AI Toolkit for local models.

* [Custom endpoint](#add-a-custom-endpoint-model): You have a self-hosted, enterprise, or other endpoint that speaks Chat Completions, Responses, or Messages API.

> [!NOTE]
> If you are a Copilot Business or Enterprise user, your administrator can disable the **Bring Your Own Language Model Key in VS Code** policy in the [Copilot policy settings](https://github.com/settings/copilot/features) on GitHub.com. For more details, see the [GitHub Copilot documentation](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys).

### Add a model from a built in provider

Pick from a set of common providers that are ready to use in VS Code. Depending on the provider, you need an API key and other configuration details like the endpoint URL.

> [!IMPORTANT]
> The built-in Ollama provider is deprecated. For local Ollama models, install the official Ollama extension from the [Ollama publisher on the [product.prodname_vs_marketplace]](https://marketplace.visualstudio.com/publishers/Ollama) instead. The extension is maintained by the Ollama team, so it can support new Ollama models and capabilities faster than the built-in provider. If you use the built-in Ollama provider for BYOK local models, install the extension and remove the built-in provider configuration to keep using Ollama models without interruption.

To configure a language model from a built-in provider:

1. Open the Language Models editor by selecting **Manage Language Models** (gear icon) from the language model picker or via the **Chat: Manage Language Models** command from the Command Palette.

1. Select **Add Models**, and then select a model provider from the list.

    ![Screenshot that shows the model provider Quick Pick.](images/language-models/model-provider-quick-pick-v2.png)

1. Enter a group name for the models. This is the grouping label shown in the model picker and Language Models editor.

    You can change the group name later from the Language Models editor if needed.

1. Enter the provider-specific details, such as the API key or endpoint URL.

1. If the provider requires additional configuration, VS Code opens a `chatLanguageModels.json` file where you can configure the provider and model details. See the [Model configuration reference](#model-configuration-reference) for details on the configuration properties.

    The following example shows an Azure OpenAI configuration that uses Entra ID authentication:

    ```json
    [
      {
        "name": "Azure",
        "vendor": "azure",
        "models": [
          {
            "id": "<my-deployment-name>",
            "name": "GPT-5.5",
            "url": "https://<my-endpoint>.openai.azure.com",
            "toolCalling": true,
            "vision": true,
            "maxInputTokens": 200000,
            "maxOutputTokens": 64000
          }
        ]
      }
    ]
    ```

1. After configuring the model, you can now select it from the model picker in chat.

    For a model to be available when using agents in chat, it must support tool calling. If the model doesn't support tool calling, it won't be shown in the model picker.

### Add a model provider extension

You can install extensions from the [product.prodname_vs_marketplace] that add language model providers to VS Code. These extensions can provide access to additional cloud-hosted or locally running models. For example, the Foundry Toolkit for VS Code extension provides access to Foundry's local and cloud-hosted models.

To add a model provider extension:

1. Open the Language Models editor by selecting **Manage Language Models** (gear icon) from the language model picker or via the **Chat: Manage Language Models** command from the Command Palette.

1. Select **Install Model Providers**.

    VS Code opens the Extensions view, filtered to language model provider extensions. Alternatively, open the Extensions view and search for `@tag:language-models`.

1. Select **Install** to install the extension, for example, [Foundry Toolkit for VS Code](https://aka.ms/AIToolkit).

1. Follow the extension's setup instructions to configure model access.

1. The extension's models appear in the model picker in chat and in the Language Model editor. If the models don't appear, reload VS Code.

### Add a custom endpoint model

> [!NOTE]
> It replaces the deprecated OpenAI Compatible provider and supports additional API types. The ``github.copilot.chat.customOAIModels`` setting is deprecated.

The Custom Endpoint provider lets you connect any compatible API endpoint to chat in VS Code. It supports three API types, which you can select per provider or per model: Chat Completions, Responses, and the Anthropic Messages API. This makes it a good fit for self-hosted models, enterprise gateways, and providers that aren't available as a built-in provider.

To add a model with the Custom Endpoint provider:

1. Open the Language Models editor by selecting **Manage Language Models** (gear icon) from the language model picker or via the **Chat: Manage Language Models** command from the Command Palette.

1. Select **Add Models**, and then select **Custom Endpoint** from the list.

1. Enter a group name for the models. This is the grouping label shown in the model picker and Language Models editor.

    You can change the group name later from the Language Models editor if needed.

1. Enter a display name and API key for the endpoint.

1. Select the API type: **Chat Completions**, **Responses**, or **Messages**. Make sure the model supports this API type.

1. VS Code opens a `chatLanguageModels.json` file where you can configure the model details. Update the model properties and save the file. See the [Custom Endpoint configuration reference](#custom-endpoint-configuration-reference) for details on the configuration properties.

    The following example shows a Messages API configuration for an Anthropic endpoint:

    ```json
    [
      {
        "name": "Anthropic",
        "vendor": "customendpoint",
        "apiKey": "${input:anthropicApiKey}",
        "apiType": "messages",
        "models": [
          {
            "id": "claude-sonnet-4-6",
            "name": "Claude Sonnet 4.6",
            "url": "https://api.anthropic.com/v1/messages",
            "toolCalling": true,
            "vision": true,
            "maxInputTokens": 200000,
            "maxOutputTokens": 64000
          }
        ]
      }
    ]
    ```

1. After configuring the model, select it from the model picker in chat.

    > [!TIP]
    > If the model you added does not immediately appear in the model picker, restart VS Code.

#### Custom Endpoint configuration reference

The Custom Endpoint provider supports all of the [common model configuration properties](#model-configuration-reference), plus additional provider-level and model-level properties described in this section. The provider-level properties are set on the provider object, and the model-level properties are set on each entry of the `models` array. When a property is set on both levels, the model-level value takes precedence.

Provider-level properties (in addition to the [common provider properties](#model-configuration-reference)):

| Property | Description |
|----------|-------------|
| `vendor` | Must be `customendpoint` to use the Custom Endpoint provider. |
| `apiKey` | The API key used to authenticate requests. Store the key securely by using an input variable, for example `"apiKey": "${input:myApiKey}"`, instead of committing a raw key. |
| `apiType` | _(Optional)_ Default API type for all models in the provider: `chat-completions` (default), `responses`, or `messages`. Override it per model with the model-level `apiType`. |
| `url` | _(Optional)_ Base URL used to discover models automatically. When set, VS Code queries the endpoint for the list of available models instead of using the `models` array. Omit it to configure models explicitly with the `models` array. |

In addition to the [common model properties](#model-configuration-reference) the Custom Endpoint provider supports the following model-level properties:

| Property | Description |
|----------|-------------|
| `apiType` | _(Optional)_ Override the API type for this model (`chat-completions`, `responses`, or `messages`). Defaults to the provider-level `apiType`, or is inferred from the `url` when neither is set. |
| `contextWindow` | _(Optional)_ The model's full context window (input + output) in tokens, for example `1000000` for a 1M-token model. When set, you can omit `maxInputTokens` and VS Code derives it as `contextWindow - maxOutputTokens`. |
| `modelOptions` | _(Optional)_ An object of request parameters sent with every request to the model, such as `temperature` and `top_p`. For example, `"modelOptions": { "temperature": 0.2 }`. |
| `requestHeaders` | _(Optional)_ An object of additional HTTP headers to include with requests to this model, for example to authenticate through a gateway or vanity domain. See [Custom authentication headers](#custom-authentication-headers). |
| `statefulResponses` | _(Optional)_ Whether the Responses API server retains prior responses. Defaults to `true`. Set to `false` for stateless servers to send full conversation history with each request. Applies only to the Responses API. See [Stateful Responses API endpoints](#stateful-responses-api-endpoints). |

##### Endpoint URL resolution

The `url` you provide for a model is resolved based on its API type:

* If the URL already contains an explicit API path (`/chat/completions`, `/responses`, or `/messages`), it is used as-is.
* Otherwise, VS Code appends the path for the model's API type. If the URL doesn't already end in a version segment such as `/v1`, VS Code inserts `/v1` first. For example, with the Responses API type, `https://my-host.example.com` resolves to `https://my-host.example.com/v1/responses`.

To avoid ambiguity, provide the full endpoint URL including the API path, as shown in the examples.

##### Stateful Responses API endpoints

Responses API models default to `statefulResponses: true`, sending only new history with `previous_response_id`. For stateless servers, set `statefulResponses` to `false` to omit that ID and send full history, including tool calls and results, avoiding missing-tool-call errors.

For a stateless server, add these properties to its model entry in `chatLanguageModels.json`:

```json
{
  "apiType": "responses",
  "statefulResponses": false
}
```

This option describes the server's capabilities and does not change its data retention policy. When `zeroDataRetentionEnabled` is `true`, `statefulResponses` is ignored and requests send full conversation history without `previous_response_id`.

##### Custom authentication headers

By default, the Custom Endpoint provider infers the authentication header from the API type and URL. For the Messages API, it sends `x-api-key`. For Azure OpenAI URLs, it sends `api-key`. Otherwise, it sends `Authorization: Bearer <apiKey>`.

You can override the authentication header with `requestHeaders`. When you supply a well-known auth header (such as `Authorization`, `api-key`, `x-api-key`, `x-goog-api-key`, or `apikey`), VS Code does not also send the default inferred auth header, so the endpoint doesn't receive conflicting credentials.

To keep your API key in secret storage while still using it in a custom header, use the `${apiKey}` token in the header value. VS Code replaces it with the configured `apiKey` at request time:

```json
[
  {
    "name": "Gateway",
    "vendor": "customendpoint",
    "apiKey": "${input:myApiKey}",
    "models": [
      {
        "id": "my-model",
        "name": "My Model",
        "url": "https://gateway.example.com/v1/chat/completions",
        "toolCalling": true,
        "vision": false,
        "maxInputTokens": 128000,
        "maxOutputTokens": 16000,
        "thinking": true,
        "supportsReasoningEffort": ["low", "medium", "high"],
        "reasoningEffortFormat": "chat-completions",
        "modelOptions": {
          "temperature": 0.2,
          "top_p": 0.9
        },
        "requestHeaders": {
          "Authorization": "Bearer ${apiKey}",
          "Ocp-Apim-Subscription-Key": "my-subscription-key"
        }
      }
    ]
  }
]
```

## Update model provider details

To update the details of a model provider you configured previously:

1. Select **Manage Language Models** (gear icon) from the language model picker in the Chat view or run the **Chat: Manage Language Models** command from the Command Palette.

1. In the Language Models editor, select the gear icon next to the model provider you want to update.

   ![Screenshot that shows the model provider Quick Pick, with a gear icon next to the provider name.](images/language-models/reconfigure-model-provider.png)

1. Update the provider details, such as the API key or endpoint URL.

## Configure models for other features

In addition to the main chat model, you can configure which model is used for inline chat, inline suggestions, and background utility tasks.

### Change the model for inline chat

You can configure a default language model for editor inline chat. This enables you to use a different model for inline chat than for chat conversations.

To configure the default model for inline chat, use the ``inlineChat.defaultModel`` setting. The setting lists all available models from the model picker.

If you change the model during an inline chat session, the selection persists for the remainder of the session. After you reload VS Code, the model resets to the value specified in the ``inlineChat.defaultModel`` setting.

### Change the model for inline suggestions

To change the language model that is used for generating inline suggestions in the editor:

1. Select **Configure Inline Suggestions...** from the Chat menu in the VS Code title bar.

1. Select **Change Completions Model...**, and then select one of the models from the list.

> [!NOTE]
> The list of available models might vary and change over time. When no alternative models are available, the option to change the model is not available.
>
> If you are a Copilot Business or Enterprise user, your Administrator needs to enable certain models for your organization by opting in to `Editor Preview Features` in the [Copilot policy settings](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization) on GitHub.com.

### Change the model for utility tasks

In addition to the main chat model, VS Code uses lightweight models in the background for utility tasks such as generating titles, creating commit messages and pull request descriptions, and detecting intent. The model you select for a chat or agent session does not control these utility tasks. By default, these tasks use built-in utility models provided by GitHub Copilot. You can override which model is used for these tasks with any available model, including [BYOK](#bring-your-own-language-model-key) and extension-provided models.

There are two settings for utility models, depending on the type of task:

* ``chat.utilityModel``: Override the model used for general utility flows, such as generating titles and summaries, settings search, and Git review.
* ``chat.utilitySmallModel``: Override the model used for fast, lightweight utility flows, such as commit messages, pull request titles and descriptions, rename suggestions, branch name generation, prompt categorization, and intent detection. A fast and inexpensive model is recommended for this setting.

Both settings default to **Default**, which uses the built-in utility model from GitHub Copilot.

If you use BYOK models without signing into a GitHub account, the built-in utility models are not available. VS Code shows a notification in the Chat view that prompts you to configure utility models. Set ``chat.utilityModel`` and ``chat.utilitySmallModel`` to a BYOK model to enable utility features like title generation, commit message creation, and pull request description creation.

#### Configure the default utility model for BYOK models

When you select a [BYOK](#bring-your-own-language-model-key) model as the main agent model, use the ``chat.byokUtilityModelDefault`` setting to control which model built-in utility flows use by default. This setting accepts the following values:

* **None**: Do not use a default utility model.
* **Main Agent Model**: Use the selected BYOK main agent model for utility flows.
* **GitHub Copilot**: Use the default GitHub Copilot utility models.

> [!NOTE]
> By default, utility flows use GitHub Copilot utility models when a Copilot token is available. If no Copilot token is available, configure ``chat.utilityModel`` and ``chat.utilitySmallModel``, or select **Main Agent Model**, to enable utility features.

This setting has no effect when the main agent model is provided by GitHub Copilot. A specific model configured in ``chat.utilityModel`` or ``chat.utilitySmallModel`` takes precedence over this default.

## Model configuration reference

When you add BYOK model, you can configure the model properties in the `chatLanguageModels.json` file. The configuration has two levels: provider-level and model-level.

Depending on the provider, some provider and model properties might be required while others are optional. For example, some providers only require an API key and endpoint URL and discover the available models automatically, while others require you to specify the details for each model.

The provider-level properties include:

| Property | Description |
|----------|-------------|
| `vendor` | The provider of the model, for example `azure`, `openai`, `customendpoint` |
| `name` | The display name (group name) of the provider shown in the UI. |
| `models` | _(Optional)_ An array of model configurations provided by this provider. |

Each model in the `models` array supports the following properties:

| Property | Description |
|----------|-------------|
| `id` | Model identifier sent to the API. For example, for Foundry this is the deployment name. |
| `name` | Display name shown in the model picker. |
| `url` | Full endpoint URL for the model. |
| `apiType` | _(Optional)_ Override the API type per model (`chat-completions`, `responses`, or `messages`). Defaults to the provider-level `apiType`. |
| `toolCalling` | Set to `true` if the model supports tool calling. |
| `vision` | Set to `true` if the model supports image inputs. |
| `maxInputTokens` | Maximum number of input tokens the model accepts. Together with `maxOutputTokens`, this defines the model's context window. |
| `maxOutputTokens` | Maximum number of output tokens the model generates. Together with `maxInputTokens`, this defines the model's context window. |
| `editTools` | _(Optional)_ An array of edit tools the model supports. If not configured, the editor tries multiple edit tools and picks the best one. Possible values: `find-replace`, `multi-find-replace`, `apply-patch`, `code-rewrite`. |
| `thinking` | _(Optional)_ Set to `true` if the model supports thinking capabilities. Defaults to `false`. |
| `streaming` | _(Optional)_ Set to `true` if the model supports streaming responses. Defaults to `true`. |
| `zeroDataRetentionEnabled` | _(Optional)_ Set to `true` if Zero Data Retention (ZDR) is enabled for this endpoint. When enabled, `previous_response_id` is not sent in requests via the Responses API. Defaults to `false`. |
| `supportsReasoningEffort` | _(Optional)_ An array of reasoning effort levels the model accepts (for example, `["low", "medium", "high"]`). When set, a **Thinking Effort** picker is shown in the model picker. Common levels are `minimal`, `low`, `medium`, `high`. |
| `reasoningEffortFormat` | _(Optional)_ Body shape used to forward reasoning effort to the model. `chat-completions` sends a top-level `reasoning_effort` string, `responses` sends a nested `reasoning.effort` object, and `messages` sends `output_config.effort`. When unset, the format follows the URL. |
| `requestHeaders` | _(Optional)_ An object of additional HTTP headers to include with requests to this model. Certain reserved headers (forbidden, forwarding, and internal headers) are not allowed and are ignored if present. |

> [!NOTE]
> The sum of `maxInputTokens` and `maxOutputTokens` must not exceed the model's context window. VS Code uses the sum of these two values as the model's total context window, for example to show context usage in the Chat view. Typically, you set `maxInputTokens` to the model's context window size minus `maxOutputTokens`. Check your provider's model documentation for the context window size.

## Frequently asked questions

### How do I enable bring your own model key for Copilot Business or Copilot Enterprise?

If you are a Copilot Business or Enterprise user, your organization administrator must enable the **Bring Your Own Language Model Key in VS Code** policy in the [Copilot policy settings](https://github.com/settings/copilot/features) on GitHub.com. After the policy is enabled, you can use your own API keys to add models, just like individual plan users. For more details, see the [GitHub Copilot documentation](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys).

### Can I use locally hosted models with Copilot in VS Code?

You can use locally hosted models in chat by using [bring your own model key](#bring-your-own-language-model-key) (BYOK) and using a model provider that supports connecting to a local model. You have different options to connect to a local model:

* Use a built-in model provider that supports local models
* Install an extension from the [[product.prodname_vs_marketplace]](https://marketplace.visualstudio.com/search?term=tag%3Alanguage-models&target=VSCode&category=All%20categories&sortBy=Relevance), for example, [AI Toolkit for VS Code with Foundry Local](https://aka.ms/AIToolkit)

Locally hosted models work without a GitHub account, without a Copilot plan, and without an internet connection. To get the full set of utility features (title generation, commit messages, and others), configure ``chat.utilityModel`` and ``chat.utilitySmallModel`` to point to a local model.

Currently, you cannot connect to a local model for inline suggestions. VS Code provides an extension API [`InlineCompletionItemProvider`](/api/references/vscode-api.md#InlineCompletionItemProvider) that enables extensions to contribute a custom completion provider. You can get started with our [Inline Completions sample](https://github.com/microsoft/vscode-extension-samples/blob/main/inline-completions).

> [!NOTE]
> Some features require a GitHub account and internet connectivity: semantic search, inline suggestions (code completions), and features that rely on embeddings. These features are not available through BYOK models.

### Can I use a local model without an internet connection?

Yes, you can use a local model completely offline. Add a local model provider such as Ollama by using the **Chat: Manage Language Models** command, select the model in chat, and start using it. To also enable utility features like title generation and commit messages, set ``chat.utilityModel`` and ``chat.utilitySmallModel`` to a local model. Features that depend on the GitHub Copilot service, such as semantic search, inline suggestions, and embeddings, are not available offline.

### Can I use a local model without a Copilot plan?

Yes, you can use BYOK models, including local models, without a Copilot plan and without signing into a GitHub account. Add a model with the **Chat: Manage Language Models** command and select it in chat. Features that depend on the GitHub Copilot service, such as semantic search, inline suggestions, and embeddings, require a Copilot plan.

## Related resources

* [Language models concepts](/docs/agents/concepts/language-models.md)
* [Available language models in GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=vscode)
* [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)
* [Security considerations for AI in VS Code](/docs/agents/run/security.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/migrate-customizations.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/migrate-customizations
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/migrate-customizations.md
- **SHA256_FINGERPRINT**: `49cb2034d8587eb1fac68ad3b938381e6c707d0c77569fc51b8d255892fc9671`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.902505+00:00
---

**MetaDescription**: Move existing agent customizations to folders and formats supported by the Copilot harness in VS Code.

# Migrate customizations to the Copilot harness in VS Code

When VS Code shows a customization migration notice, it found a file, setting, or MCP server that the Copilot harness does not read in its current location or format. Use the migration list to move or convert each affected customization.

This article explains why migration is needed, how to complete each migration that VS Code supports, and what to review manually.

> [!NOTE]
> This article covers migration to the Copilot harness. For the Claude or Codex harness, use the locations and formats in the provider documentation.

## Open the migration list

A notice appears in chat when a workspace requires customization migrations. Select **Review Migrations** to open the list of migrations. To directy open the list of migrations:

1. In the Chat view or Agents window, select **Copilot** as the **Session Target**.
1. Run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).
1. Select **Migrations**.

The migration tree groups the detected work by workspace and user scope.

Choose how to handle the migration:

* **Migrate**: select items in a group, review or change the destination when available, and select **Migrate**. VS Code performs the supported file move or conversion.
* **Migrate with Agent**: start a guided migration in chat for customizations that need semantic changes or repository work. This action uses Copilot credits. The agent creates a recovery bundle, preserves source files by default, and asks separately before it cleans up the source. For workspace migrations, it can prepare a pull request.
* **Review**: open an item under **Needs manual review** to understand why it cannot migrate automatically and edit its source configuration.

Use **Ignore** from a migration group's actions when you do not want to handle that group now. Select **Show Ignored Migrations** to restore ignored groups.

Before you migrate:

* Commit or back up workspace files that you might change.
* Review the source and destination shown for each item.
* Remember that the original and migrated copies do not synchronize.
* If you do not maintain the repository, use **Migrate with Agent** to prepare a pull request, or ask a repository maintainer to make the change.

You only need to migrate each item once. Keep the original until you verify the migrated customization, and then remove it when you no longer need it.

## Why migration is needed

The Copilot harness reads customizations from Copilot folders and portable formats. If a customization is stored in your VS Code profile or a location configured through `chat.*FilesLocations` settings, move it to a supported location to use it in a Copilot harness session.

> [!NOTE]
> **For Local harness sessions:** The agent reads VS Code profile customizations and the additional locations configured through those settings. Moving a customization for the Copilot harness doesn't change which sources the Local harness reads.

Moving customizations to those locations has these benefits:

* The Copilot harness can load them directly without relying on an editor to provide them.
* Workspace customizations stay with the repository and can be shared through source control.
* VS Code and GitHub Copilot CLI read the same Copilot customization files. The GitHub Copilot app also uses repository and Copilot CLI skills and MCP server configuration.
* You can remove old location settings and avoid maintaining duplicate copies.

The destination depends on the migration type and scope. User-data migrations stay at user scope. Workspace migrations stay with the workspace. The migration tree shows the destination selected for each group.

For a complete list of customization types and supported locations, see the [Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet). Learn how these customizations appear in the [GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app).

## Migrate MCP servers

MCP server migration moves compatible configurations to files that the Copilot harness reads directly:

| Existing configuration | Destination |
|------------------------|-------------|
| Workspace `.vscode/mcp.json` | `.mcp.json` at the corresponding workspace root |
| VS Code profile `mcp.json` | `$COPILOT_HOME/mcp-config.json`, or `~/.copilot/mcp-config.json` when `COPILOT_HOME` is not set |

The automatic migration writes workspace servers to `.mcp.json` at the workspace root. Commit the file to source control when your team should share the configuration. For a remote or Dev Container session, paths and user configuration belong to the machine or container where the agent runs.

To migrate MCP servers:

1. Expand the **MCP Servers** group for the workspace or your profile.
1. Select the servers you want to migrate.
1. Review the source, destination, and any properties that the destination format cannot preserve.
1. Select **Migrate** for the group. You can also open one server and select **Migrate** from its detail page.
1. Open the destination file and test the server with the Copilot harness.

VS Code writes and verifies each destination entry before removing the migrated entry from its source file. Unselected servers and servers that cannot be migrated stay in their current files.

A migration with changes can remove VS Code-specific metadata, including registry update information, version metadata, development-mode behavior, or per-server sandbox settings. The migration page lists the changes for each server.

> [!IMPORTANT]
> Disabled state is not stored in `.mcp.json` or `mcp-config.json`. VS Code preserves workspace disablement in the current profile when possible, but user-level disablement can be lost. Other Copilot clients and other machines can treat the migrated server as enabled. Review the server's enabled state in each client before use.

Servers that cannot migrate automatically appear under **Needs manual review**. Select **Review** to open the server details and the source configuration. Resolve configuration errors, missing values, or duplicate server names, and then retry. You can also use **Migrate with Agent** for guided help. For MCP formats and supported locations, see the [MCP configuration reference](/docs/agents/reference/mcp-configuration.md#configuration-file).

### Check MCP values before migration

Use the following table to decide whether a server can migrate automatically and what to review.

| Source configuration | Migration result | What to do |
|----------------------|------------------|------------|
| Standard `command`, `args`, `env`, `url`, and `headers` values | Migrates automatically and adds `tools: ["*"]` | Inspect the server's tools. Replace `*` with the specific tools Copilot should invoke when you do not want every server tool available. |
| `${workspaceFolder}`, `${workspaceRoot}`, `${workspaceFolderBasename}`, `${workspaceRootFolderName}`, `${cwd}`, or `${pathSeparator}` | Migrates after VS Code resolves the variable and writes its current value | Review the resulting value before you share the destination file or use it on another machine. |
| `gallery`, `version`, `dev`, or `sandboxEnabled` | Migrates with changes and removes these properties | Review the migration warning. Decide how to handle updates, development behavior, or sandboxing after migration. |
| `${input:...}`, `${config:...}`, `${command:...}`, or other interactive VS Code variables | Does not migrate automatically | Reconfigure the value for the Copilot harness. Do not copy a resolved secret into the MCP file. |
| `${env:NAME}` | Does not migrate automatically | Use `$NAME`, `${NAME}`, or `${NAME:-default}`, and define the variable in the environment used to start the agent. |
| `cwd` | Does not migrate automatically | Add `cwd` manually only when the server requires it, and verify the path on the machine where the agent runs. |
| `envFile` | Does not migrate automatically | Export the required variables in the environment used to start the agent and reference them from `env`. Do not copy secret values into the MCP file. |
| SSE transport | Does not migrate automatically | Use `type: "sse"` only when the server does not support Streamable HTTP. SSE is deprecated. |
| A VS Code `oauth` object | Does not migrate automatically | Remove the nested object to use OAuth discovery, or translate supported client settings to the flat Copilot OAuth fields. Authenticate when Copilot prompts you. |
| Environment variables with `null` values | Does not migrate automatically | Remove the entry or provide a supported value. |
| Additional VS Code-specific properties | Does not migrate automatically | Remove or replace the unsupported property before you retry. |
| A different server with the same name in the destination or another workspace root | Migration stops without changing the source | Rename or remove the conflicting server, and then retry. |

Input variables need special attention. The VS Code MCP format can prompt for values such as API keys through `${input:api-key}`. The Copilot MCP format does not use this VS Code input flow, so these servers require manual configuration.

> [!IMPORTANT]
> VS Code per-server sandbox settings and top-level `sandbox` rules do not transfer to the Copilot harness configuration. The Copilot harness uses session-level sandbox settings. Local stdio MCP servers run in the Copilot harness sandbox only when local sandboxing and MCP server sandboxing are enabled. Remote HTTP and SSE servers are not locally sandboxed. Review these settings before enabling a migrated server.

When a server requires manual work:

1. Keep the original configuration until the Copilot server starts and provides the expected tools.
1. Open the source configuration and identify each unsupported field or variable.
1. Follow the [Copilot CLI MCP server guidance](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) for the destination configuration.
1. Decide how to provide secrets, authentication, or environment-specific paths. Do not copy sensitive values into a committed file.
1. Test the server with the Copilot harness before you remove the original entry.

## Convert prompt files to skills

Copilot harness sessions use [agent skills](/docs/agent-customization/agent-skills.md) for reusable workflows and do not load `*.prompt.md` files. Convert workspace and user prompt files to skills to use those workflows with the Copilot harness. Prompt files remain supported in Local harness sessions.

> [!IMPORTANT]
> Converting a workspace prompt to a project skill changes how the Copilot harness can use it. A prompt file runs only when someone invokes it. The Copilot harness can select a committed skill automatically in VS Code, GitHub Copilot CLI, the GitHub Copilot app, Copilot cloud agent, and Copilot code review. Review the skill's description and instructions with the repository maintainer before you commit it. Convert a personal workflow to a user skill instead.

To convert prompt files:

1. Expand **Convert Prompt to Skills** for the workspace or your profile.
1. Select the prompt files to convert.
1. Review the source and destination. Open a prompt if you want to inspect it.
1. Select **Migrate**.

The generated skill includes `disable-model-invocation: true`, so it remains an explicitly invoked workflow. Conversion maps the prompt file's `name`, `description`, and argument guidance to the skill. It does not preserve prompt-specific `agent`, `model`, or `tools` selection. VS Code lists omitted properties after migration. If the prompt depends on a specific agent, model, or tool set, use **Migrate with Agent** to create a corresponding custom agent or adapt the workflow.

Test each skill before you remove the old prompt file.

## Move user agents and instructions

The Copilot harness does not read custom agents and instructions stored in VS Code profile user data. User customization migration copies agents to `~/.copilot/agents` and instructions to `~/.copilot/instructions` without changing their names, types, or contents.

To move user customizations:

1. Expand **User Data** under **Your profile**.
1. Select the custom agents and instructions to move.
1. Review the user destination shown for the group.
1. Select **Migrate**.

The migrated files are not included in [Settings Sync](/docs/configure/settings-sync.md).

After migration, start a Copilot harness session and verify that the agents and instructions are available. See [custom agent locations](/docs/agent-customization/custom-agents.md#custom-agent-file-locations) and [instruction file locations](/docs/agent-customization/custom-instructions.md#instructions-file-locations) for the supported destinations.

## Move customizations from configured locations

The following settings add file locations for the Local harness, but the Copilot harness does not read them:

* ``chat.agentFilesLocations``
* ``chat.modeFilesLocations``
* ``chat.instructionsFilesLocations``
* ``chat.agentSkillsLocations``

Location migration moves detected custom agents, instructions, and skills to the Copilot folders for their scope:

| Customization | Workspace destination | User destination |
|---------------|-----------------------|------------------|
| Custom agents | `.github/agents` | `~/.copilot/agents` |
| Instructions | `.github/instructions` | `~/.copilot/instructions` |
| Skills | `.github/skills` or `.agents/skills` | `~/.copilot/skills` or `~/.agents/skills` |

To migrate custom locations:

1. Expand **Custom location settings** for the workspace or your profile.
1. Select the agents, instructions, and skills to move.
1. Review or change the destination for the group.
1. Select **Migrate**.

Prompt files from ``chat.promptFilesLocations`` are handled by [prompt file migration](#convert-prompt-files-to-skills), not location migration.

This migration applies only to the deprecated VS Code `chat.*FilesLocations` settings. GitHub Copilot CLI separately supports additional instruction directories through `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`. VS Code does not migrate or clear that environment variable.

## Customizations without automatic migration

The migration list does not automatically convert every customization type:

* **Custom agents with Local harness-specific behavior**: use **Migrate with Agent** when an agent depends on Local harness tool names, tool sets, hooks, or other behavior that needs semantic changes.
* **Tool sets**: The Copilot harness does not support VS Code tool-set files. There is no automatic migration. Review the tools directly in the custom agent or chat tools picker. See [Create and use tool sets](/docs/agent-customization/tool-sets.md).
* **Hooks**: there is no automatic hook migration. Configure hooks for the Copilot harness using the [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference) and [Configure agent hooks](/docs/agent-customization/hooks.md).
* **Plugins and marketplaces**: manage these separately from the migration list. See [Discover and install plugins](/docs/agent-customization/agent-plugins.md#discover-and-install-plugins).
* **Extension-provided customizations**: extensions can provide tools, MCP servers, custom agents, skills, and instructions. Keep the contributing extension installed. Extension tools are available only in editor chat while the extension runs. Learn how to [manage extension tools for the Copilot harness](/docs/agents/run/tools.md#add-extension-tools-for-the-copilot-harness).

## Verify the migration

After you complete a migration:

1. Start a new Copilot harness session.
1. Confirm that the migrated agents, instructions, skills, MCP servers, or plugins appear in the Agent Customizations editor.
1. Run a representative task that uses the customization.
1. Check that old and migrated copies are not both active.
1. Commit workspace migrations to source control when your team should share them.
1. Remove old files and settings after the migrated customization works.

For remote or Dev Container sessions, perform this check in the destination environment. User customization folders belong to the machine or container where the agent runs.

## Related resources

* [Create and manage agent customizations](/docs/agent-customization/overview.md)
* [Choose and configure an agent harness](/docs/agents/run/agent-harnesses.md)
* [Agent customization concepts](/docs/agents/concepts/customization.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/overview.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/overview
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/overview.md
- **SHA256_FINGERPRINT**: `0cc87f5d52b99dc64eb97a1a77fede6b136ed95a5bf37790a8a6e937b7ac1cba`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.896903+00:00
---

**MetaDescription**: Create, manage, migrate, and troubleshoot agent customizations in VS Code across profiles and workspaces.

# Create and manage agent customizations

Agent customizations adapt agents to your coding standards, workflows, and development systems. This article explains how to create, manage, evaluate, and troubleshoot customizations in Visual Studio Code. To compare the customization types and understand how they work together, see [Agent customization concepts](/docs/agents/concepts/customization.md).

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Core concepts">
Learn about the different customization types and when to use each one.

* [Customization concepts](/docs/agents/concepts/customization.md)

</div>

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Tutorial">
Follow a hands-on walkthrough to customize AI for your project.

* [Customize AI for your project](/docs/agents/guides/customize-copilot-guide.md)

</div>

## Check harness compatibility

Select the [agent harness](/docs/agents/run/agent-harnesses.md#select-a-harness) you intend to use before choosing a customization type or creating a file. The harness determines which formats, locations, and capabilities are supported. Changing the language model doesn't change those requirements.

| Customization | Check before creating it |
|---------------|--------------------------|
| [Instructions](/docs/agent-customization/custom-instructions.md) and [skills](/docs/agent-customization/agent-skills.md) | Use a format and file location that the selected harness reads. Check its activation rules and supported user, workspace, or organization scope. |
| [Custom agents](/docs/agent-customization/custom-agents.md), [hooks](/docs/agent-customization/hooks.md), and [MCP servers](/docs/agent-customization/mcp-servers.md) | Follow the configuration for your harness. Tool names, supported fields, lifecycle events, and connection locations can differ. |
| [Prompt files](/docs/agent-customization/prompt-files.md) and [tool sets](/docs/agent-customization/tool-sets.md) | Use a **Local** harness session in the Chat view. For reusable workflows in other skills-compatible harnesses, create a skill instead of a prompt file. |
| [Plugins](/docs/agent-customization/agent-plugins.md) | Check that the selected harness supports the plugin and its bundled customization types. |

The Chat view and Agents window both run agents, but the available harnesses differ. Local sessions are editor-only. Select the intended harness before opening the Customizations editor so you see its supported types and destinations.

## Agent Customizations editor

The Agent Customizations editor provides a central place to discover, create, and manage customizations. It organizes customization types into separate sections. Depending on the customization type and source, it provides a configuration form, an inline file editor with syntax highlighting and validation, or a read-only details view.

When you open the Customizations editor, the customizations are scoped to the selected [agent harness](/docs/agents/concepts/agent-harnesses.md). Select the harness from the dropdown in the chat input before you open the editor to ensure the customizations apply to the correct context.

![Screenshot showing the Agent Customizations editor with Copilot CLI custom agents and customization categories.](images/customization/agents-customizations.png)

Follow these steps to open the Agent Customizations editor:

In the left sidebar, select a customization type in the **Customizations** panel.

![Screenshot showing the Agent Customizations panel in the Agents window, with the list of available customizations visible.](images/customization/agents-window-customizations.png)

In the Chat view, select **Open Customizations** in the title bar, or run **Chat: Open Customizations** from the Command Palette (``Shortcut: workbench.action.showCommands``).

![Screenshot showing the Agent Customizations editor with customization categories in the sidebar and custom agents in the main view.](images/customization/chat-customizations-editor.png)

### Discover marketplace customizations (Experimental)

The Customization Marketplace provides a unified **Discover** page for finding skills, MCP servers, plugins, and other agent customizations from configured sources. To use the marketplace, turn on the ``chat.customizations.marketplace.enabled`` setting.

The GitHub Feed source is available by default when the marketplace is enabled. Use the ``chat.customizations.marketplace.sources.publicFeed.enabled`` setting to show or hide this source.

To find and install a customization:

1. Open the Agent Customizations editor and select **Discover**.
1. Use the source menu to browse all sources or select a specific source, such as **GitHub Feed**.
1. Search by name or use a type filter, such as `@type:skill` or `@type:mcp`.
1. Select an item and review its publisher, source, installation details, and any setup requirements.
1. Select **Install** and choose a destination when prompted.

Some items are available for discovery but don't support automatic installation. Follow the publisher's setup instructions when they are provided.

Marketplace items show a source or publisher image in **Discover** and, when available, on the installed item and its details page. Use this information together with the item details to verify the source before installation.

VS Code associates marketplace state with the exact installed target, not only its display name. A local customization and a Marketplace-installed customization with the same name remain separate:

* **Installed** indicates that the recorded target is available.
* **Missing files** indicates that files from a Marketplace-installed skill are no longer present. Select **Repair** to restore only the missing files. Repair preserves files that you edited or added.
* Deleting a Marketplace-installed customization removes its exact installation. It doesn't remove an unrelated local customization with the same name.

## Choose a customization scope

Store a customization at the narrowest scope that matches how you want to use and share it:

* **User**: use the customization across your workspaces. User customizations are specific to you and are not committed to the project.
* **Workspace**: share the customization with project contributors through source control.
* **Organization**: centrally manage supported customization types and share them across repositories. Organization customizations are configured through GitHub rather than created in the Agent Customizations editor.

Scope determines where a customization is available and who can share it. Not every customization type supports every scope. The selected agent harness also determines which customization types and locations it supports. See the guide for each customization type for its supported locations.

> [!NOTE]
> Store user-level customizations in a folder that the selected harness supports on the machine where the agent runs. For example, Copilot reads customizations from `~/.copilot`, and [product.prodname_anthropic_claude] reads them from `~/.claude`. These folders are separate from your VS Code profile user data and aren't shared automatically between machines. See [instructions](/docs/agent-customization/custom-instructions.md#instructions-file-locations), [custom agents](/docs/agent-customization/custom-agents.md), and [prompt files](/docs/agent-customization/prompt-files.md#prompt-file-locations) for supported user-level locations.

## Create a customization

You can create customization files with AI or create them manually. Creating a file doesn't mean the selected harness can load or run it. Specify the target harness and user or workspace scope, save the file in a supported location, and verify it in a session that uses that harness.

### Create a customization with AI

1. Open the Agent Customizations editor.
1. In the **Overview** section, enter a prompt that describes what you want to create.
1. Answer any questions the agent asks about missing details.
1. Review the generated customization, correct any inaccurate information, and save the file.

For example, to create a code reviewer skill, you can enter the following prompt:

```prompt
Create a workspace code reviewer skill for Python and JavaScript files. Check the code against the conventions in this repository, identify correctness and maintainability issues, and report findings with file locations and suggested fixes.
```

### Create a customization manually

1. Open the Agent Customizations editor and select a customization type.
1. From the **New** dropdown, choose a user or workspace customization.
1. Enter a name and choose a storage location when prompted.
1. Edit the customization in the inline editor, which provides syntax highlighting and validation.
1. Review and save the customization.

You can also run the **Chat: New \<customization-type\>** command from the Command Palette (``Shortcut: workbench.action.showCommands``). The command creates the corresponding file in a supported location for that customization type.

To add an MCP server manually, select **MCP Servers**, select **Add Server** (**+**) in the **User** or **Workspace** group, and follow the guided flow. For detailed steps, see [Add MCP servers](/docs/agent-customization/mcp-servers.md#connect-a-server). To update an existing connection, see [Edit an MCP server configuration](/docs/agents/run/manage-mcp-servers.md#edit-an-mcp-server-configuration).

For Agent Skills, MCP servers, and agent plugins, use [Discover](#discover-marketplace-customizations-experimental) to browse marketplace sources and install an item. Manage the installation from the corresponding section.

See the guides for [custom instructions](/docs/agent-customization/custom-instructions.md), [agent skills](/docs/agent-customization/agent-skills.md), [prompt files](/docs/agent-customization/prompt-files.md), [custom agents](/docs/agent-customization/custom-agents.md), [MCP servers](/docs/agent-customization/mcp-servers.md), [hooks](/docs/agent-customization/hooks.md), and [agent plugins](/docs/agent-customization/agent-plugins.md) for their file formats and configuration options.

## Manage existing customizations

Use the Agent Customizations editor to find and update customizations for the selected harness:

1. Open the Agent Customizations editor and select the customization type.
1. Use the search box to find the customization.
1. Select the customization to open its details.
1. If the customization is editable, update its form or file and save your changes. For a read-only customization, use the available action to open the source file.

The available actions depend on the customization type and its source. Use the inline actions or context menu to access supported operations, such as revealing an editable file in your operating system or deleting it. Manage plugin-provided customizations from the **Plugins** section.

`feature(user-customization-migration)`

> [!IMPORTANT]
> If the Agent Customizations editor shows **Migrations**, Copilot cannot use one or more customizations in their current location or format. Select **Migrations** to review the required work, and follow [Migrate Copilot customizations in VS Code](/docs/agent-customization/migrate-customizations.md) for detailed steps.

## Verify a customization

Test a new or updated customization in a fresh chat with the intended harness and workspace. Use a representative task and confirm that the harness discovers the file before assessing its behavior. This separates the saved customization from instructions in the conversation that created it.

Check that the agent follows the expected instructions, workflow, tool configuration, or lifecycle action. For instructions and skills, use the response's **References** section, where available, to check which customizations were included.

If the result doesn't match your intent, make the customization more specific, resolve conflicting guidance, and repeat the task. For a complete project workflow, including how to review and share generated instructions, see [Configure AI for your codebase](/docs/agents/guides/customize-copilot-guide.md).

## Troubleshoot customization issues

If a customization isn't applied or causes unexpected behavior, check the following:

* The intended agent harness is selected.
* The customization is stored in a location that the harness supports.
* Any activation conditions match the current file or task.
* The customization file has no validation errors.

If the issue continues, open the **Agent Debug Logs** view to [troubleshoot agent issues](/docs/agents/agent-troubleshooting/troubleshooting.md). Run **Developer: Open Agent Debug Logs** from the Command Palette (``Shortcut: workbench.action.showCommands``), or in the Chat view select the ellipsis (**...**) menu and select **Show Agent Debug Logs**.

## Use customizations in a monorepo

In monorepo setups, you might open a subfolder of a repository in VS Code rather than the repo root. By default, VS Code only discovers customization files within your open workspace folder(s). Enable the ``chat.useCustomizationsInParentRepositories`` setting to also discover customizations from the parent repository.

When this setting is enabled, VS Code walks up the folder hierarchy from each workspace folder until it finds a `.git` folder. If found, it collects customizations from all folders between the workspace folder and the repository root (inclusive). This applies to all customization types: always-on instructions (`copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`), file-based instructions, prompt files, custom agents, agent skills, and hooks.

For example, consider the following monorepo structure:

```text
my-monorepo/              # repo root (has .git folder)
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   └── style.instructions.md
│   ├── prompts/
│   │   └── review.prompt.md
│   └── agents/
│       └── reviewer.agent.md
├── packages/
│   └── frontend/          # opened as workspace folder
│       └── src/
```

If you open only `packages/frontend/` in VS Code and enable the setting, VS Code discovers the customization files at the repo root, such as `copilot-instructions.md`, `style.instructions.md`, `review.prompt.md`, and `reviewer.agent.md`.

Conditions for parent repository discovery:

* The workspace folder does not contain a `.git` folder (it is not itself a repository root).
* A parent folder contains a `.git` folder.
* The parent repository folder is [trusted](/docs/editing/workspaces/workspace-trust.md). VS Code prompts you to trust the parent folder when the workspace is opened.

> [!NOTE]
> The ``chat.useCustomizationsInParentRepositories`` setting is disabled by default.

## Evaluate and improve customization files (Preview)

As your collection of customization files grows, it can be hard to tell whether they actually guide the AI the way you intend. Vague wording, contradictory rules, or overly complex instructions can degrade results. The [Chat Customizations Evaluations](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-chat-customizations-evaluations) extension helps you catch these problems before you rely on a customization, by analyzing your files and suggesting concrete improvements.

> [!NOTE]
> The Chat Customizations Evaluations extension is published separately from VS Code. Install it from the [[product.prodname_vs_marketplace]](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-chat-customizations-evaluations).

The extension works with skill files (`SKILL.md`), custom agent files (`*.agent.md`), instructions files (`*.instructions.md`), and prompt files (`*.prompt.md`).

Open a customization file and run the **Chat Customizations Evaluations: Analyze** command from the Command Palette (``Shortcut: workbench.action.showCommands``).
The extension uses GitHub Copilot to detect issues such as:

* Logical, behavioral, and format contradictions
* Ambiguous wording, with suggested rewrites
* Conflicting persona traits and tone drift
* Excessive cognitive load from deeply nested conditions
* Gaps in intent handling and missing error paths
* Conflicts between a file and other customization files it links to

Diagnostics appear in the **Problems** panel (``Shortcut: workbench.actions.view.problems``) with line and column locations. After the analysis completes, select **Implement Suggestions** to apply the suggested improvements.

> [!TIP]
> You can also start an analysis from chat with the `/analyze-prompt` slash command, which summarizes the diagnostics for the active customization file directly in the Chat view.

For skill files, the extension integrates with the [Waza](https://github.com/microsoft/waza) evaluation framework to measure how well a skill performs against a set of test cases. Run **Chat Customizations Evaluations: Download Waza Binary** to install Waza, **Chat Customizations Evaluations: Create Waza Eval Scaffold** to generate evaluation files for the active skill, and **Chat Customizations Evaluations: Run Waza Evaluation** to run the suite. For step-by-step guidance, run **Chat Customizations Evaluations: Open Analysis and Fix User Guide**.

## Related resources

* [Customization concepts](/docs/agents/concepts/customization.md)
* [Customize AI for your project guide](/docs/agents/guides/customize-copilot-guide.md)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/prompt-files.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/prompt-files
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/prompt-files.md
- **SHA256_FINGERPRINT**: `b0df15b23c7e434000c9d8018645cc9fd4e6ab0d898bc5056b29bc2a1579c97b`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.899613+00:00
---

**MetaDescription**: Use prompt files in VS Code for reusable Local harness workflows, or migrate them to agent skills.

# Use prompt files in VS Code

Prompt files simplify prompting for common tasks by encoding them as standalone Markdown files that you invoke as slash commands in chat. Each prompt file includes task-specific context and guidelines about how the task should be performed.

Unlike [custom instructions](/docs/agent-customization/custom-instructions.md) that are applied automatically, you invoke prompt files manually in chat. See the [decision matrix](/docs/agents/concepts/customization.md#customization-options-at-a-glance) to compare prompt files with custom agents, agent skills, and the other options.

Use prompt files to:

* Simplify prompting for common tasks, such as scaffolding a new component, running and fixing tests, or preparing a pull request
* Override default behavior of a custom agent, such as creating a minimal implementation plan or generating mockups for API calls

With **Local** selected, use the [Agent Customizations editor](/docs/agent-customization/overview.md#agent-customizations-editor) (Preview) to discover, create, and manage prompt files. Run **Chat: Open Customizations** from the Command Palette.

> [!IMPORTANT]
> Prompt files run only in **Local** harness sessions in the Chat view. For reusable workflows in other harnesses, create an [agent skill](/docs/agent-customization/agent-skills.md) or [convert an existing prompt file to a skill](/docs/agent-customization/migrate-customizations.md#convert-prompt-files-to-skills).

## Prompt file locations

You can define prompt files for a specific workspace or at the user level, where they are available across all your workspaces. The following table lists the default file locations that the Local harness uses for prompt files.

| Scope | Default file location |
|-------|-----------------------|
| Workspace | `.github/prompts` folder |
| User profile | Your user data (specific to your VS Code profile) |

To create a user-level prompt file, use the Agent Customizations editor or the **Chat: New Prompt File** command.

> [!TIP]
> In a monorepo, enable ``chat.useCustomizationsInParentRepositories`` to discover prompt files from the parent repository root. Learn more about [parent repository discovery](/docs/agent-customization/overview.md#use-customizations-in-a-monorepo).

## Prompt file format

Prompt files are Markdown files with the `.prompt.md` extension. The optional YAML frontmatter header configures the prompt's behavior:

| Field | Required | Description |
| --- | --- | --- |
| `description` | No | A short description of the prompt. |
| `name` | No | The name of the prompt, used after typing `/` in chat. If not specified, the file name is used. |
| `argument-hint` | No | Hint text shown in the chat input field to guide users on how to interact with the prompt. |
| `agent` | No | The agent used for running the prompt: `ask`, `agent`, `plan`, or the name of a [custom agent](/docs/agent-customization/custom-agents.md). By default, the current agent is used. If tools are specified, the default agent is `agent`. |
| `model` | No | The language model used when running the prompt. If not specified, the currently selected model in model picker is used. |
| `tools` | No | A list of tool or [tool set](/docs/agent-customization/tool-sets.md) names that are available for this prompt. Can include built-in tools, tool sets, MCP tools, or tools contributed by extensions. To include all tools of an MCP server, use the `<server name>/*` format.<br/>Learn more about [tools with agents](/docs/agents/run/tools.md). |

> [!NOTE]
> If a given tool is not available when running the prompt, it is ignored.

The body contains the prompt text in Markdown format. Provide specific instructions, guidelines, or any other relevant information that you want the AI to follow.

### Reference files

You can reference files in the prompt body by using Markdown links or the `#file:` syntax.

* For files in your workspace, use paths relative to the prompt file. For example, `[coding standards](../instructions/coding.instructions.md)` references a file in a sibling `instructions` folder.
* For files in your environment user home folder, use `~` or start the path with `~/`. A standalone `~` references the user home folder, and a path such as `~/prompts/style-guide.md` resolves from that folder.

Use Unix-style `/` path separators to keep prompt files portable across operating systems.

The following example uses both reference formats to reference files in the user home folder:

```markdown
Review [my personal instructions](~/copilot/instructions.md).
Use #file:~/templates/component.md as the component template.
```

To reference agent tools in the body text, use the `#tool:<tool-name>` syntax. For example, to reference the `browser` tool, use `#tool:browser`.

> [!TIP]
> If you want the user to provide additional information, you can use the `vscode/askQuestion` tool. You can also use a syntax like `${input:variableName}`, `${input:variableName:placeholder}`. Most language models understand this syntax and will prompt for these inputs.

The following examples demonstrate how to use prompt files. For more community-contributed examples, see the [Awesome Copilot repository](https://github.com/github/awesome-copilot/tree/main).

<details>
<summary>Example: generate a React form component</summary>

```markdown
---
agent: 'agent'
model: GPT-4o
tools: ['search/codebase', 'vscode/askQuestions']
description: 'Generate a new React form component'
---
Your goal is to generate a new React form component based on the templates in the Github repo contoso/react-templates.

Use the #tool:vscode/askQuestions to ask for the form name and fields if not provided.

Requirements for the form:
* Use form design system components: [design-system/Form.md](../docs/design-system/Form.md)
* Use `react-hook-form` for form state management:
* Always define TypeScript types for your form data
* Prefer *uncontrolled* components using register
* Use `defaultValues` to prevent unnecessary rerenders
* Use `yup` for validation:
* Create reusable validation schemas in separate files
* Use TypeScript types to ensure type safety
* Customize UX-friendly validation rules
```

</details>

<details>
<summary>Example: perform a security review of a REST API</summary>

```markdown
---
agent: 'ask'
model: Claude Sonnet 4
description: 'Perform a REST API security review'
---
Perform a REST API security review and provide a TODO list of security issues to address.

* Ensure all endpoints are protected by authentication and authorization
* Validate all user inputs and sanitize data
* Implement rate limiting and throttling
* Implement logging and monitoring for security events

Return the TODO list in a Markdown format, grouped by priority and issue type.
```

</details>

## Create a prompt file

Before creating a prompt file, select the **Local** harness in the Chat view. Choose whether to store the file in your workspace or user profile. Workspace prompt files are available to Local sessions in that workspace. User prompt files are available to Local sessions across workspaces in the same profile.

To create a prompt file:

> [!TIP]
> With **Local** selected in the Chat view, type `/prompts` in the chat input to quickly open the **Configure Prompt Files** menu.

1. In the Chat view, select **Open Customizations** in the title bar to open the Agent Customizations editor, and then select **Prompts**.

1. Select **New Prompt** (plus icon) next to the **Workspace** or **User** group, depending on where you want to store the prompt file.

    ![Screenshot of the Agent Customizations editor, showing the Prompts tab and the dropdown to create a new prompt file.](images/customization/create-prompt-file.png)

    Alternatively, use the **Chat: New Prompt File** or **Chat: New Untitled Prompt File** command from the Command Palette (``Shortcut: workbench.action.showCommands``).

1. Select the location and enter a file name for your prompt file. This is the default name that appears when you type `/` in chat.

1. Author the chat prompt by using Markdown formatting.

    * Fill in the YAML frontmatter at the top of the file to configure the prompt's description, agent, tools, and other settings.
    * Add instructions for the prompt in the body of the file.

You can modify existing prompt files by opening them in the Agent Customizations editor.

### Generate a prompt file with AI

An agent with file-editing tools can help author a prompt file, even if you use a different harness to write it. Tell the agent that the file will run in a Local session and describe the task, expected output, and storage location. Review the generated file before using it.

Authoring a `.prompt.md` file in a Copilot session doesn't make that file runnable by the Copilot harness. To reuse a workflow in that harness, [create a skill](/docs/agent-customization/agent-skills.md#create-a-skill) or [convert an existing prompt file](/docs/agent-customization/migrate-customizations.md#convert-prompt-files-to-skills).

With **Local** selected, you can also type `/create-prompt` in chat followed by the description. The agent asks clarifying questions, generates a `.prompt.md` file with appropriate frontmatter and instructions, and offers you a choice between workspace and user storage. The `/create-prompt` command isn't available for other harnesses.

You can also ask an agent to capture an ongoing conversation as a prompt file for Local sessions. Specify the target harness so that it doesn't create a customization in a format you can't use.

With **Local** selected in the Chat view, you can also generate a prompt file from the Agent Customizations editor by selecting **Generate with AI** next to the **Workspace** group in the **Prompts** section.

## Use a prompt file in chat

Select **Local** in the Chat view before running the prompt. The following options run prompt files in Local sessions:

* In the Chat view, type `/` followed by the prompt name in the chat input field. [Agent skills](/docs/agent-customization/agent-skills.md) also appear as slash commands alongside prompt files.

    You can add extra information in the chat input field. For example, `/create-react-form formName=MyForm` or `/create-api for listing customers`.

* Run the **Chat: Run Prompt** command from the Command Palette (``Shortcut: workbench.action.showCommands``) and select a prompt file from the Quick Pick.

* Open the prompt file in the editor, and press the play button in the editor title area. You can choose to run the prompt in the current chat session or open a new chat session.

    This option is useful for quickly testing and iterating on your prompt files.

> [!TIP]
> Use the ``chat.promptFilesRecommendations`` setting to show prompts as recommended actions when starting a new chat session.
>
> ![Screenshot showing a "explain" prompt file recommendation in the Chat view.](images/customization/prompt-file-recommendations.png)

## Tool list priority

You can specify the list of available tools for both a custom agent and prompt file by using the `tools` metadata field. Prompt files can also reference a custom agent by using the `agent` metadata field.

The list of available tools in chat is determined by the following priority order:

1. Tools specified in the prompt file (if any)
2. Tools from the referenced custom agent in the prompt file (if any)
3. Default tools for the selected agent (if any)

## Sync user prompt files across devices

VS Code can sync your user prompt files across multiple devices by using [Settings Sync](/docs/configure/settings-sync.md).

To sync your user prompt files, enable Settings Sync and run **Settings Sync: Configure** from the Command Palette (``Shortcut: workbench.action.showCommands``). Select **Prompts and Instructions** from the list of settings to sync.

## Tips for writing effective prompts

* Clearly describe what the prompt should accomplish and what output format is expected.

* Provide examples of the expected input and output to guide the AI's responses.

* Use Markdown links to reference custom instructions rather than duplicating guidelines in each prompt.

* Take advantage of built-in variables like `${selection}` and input variables to make prompts more flexible.

* Use the editor play button to test your prompts and refine them based on the results.

## Frequently asked questions

### How do I know where a prompt file comes from?

Prompt files can come from different sources: built-in, user-defined in your profile, workspace-defined prompts in your current workspace, or extension-contributed prompts.

To identify the source of a prompt file:

1. Select **Chat: Configure Prompt Files** from the Command Palette (``Shortcut: workbench.action.showCommands``).
1. Hover over the prompt file in the list. The source location is displayed in a tooltip.

> [!TIP]
> Use the Agent Debug Log panel to inspect prompt file discovery and related errors. In the Chat view, select the ellipsis (**...**) menu, then select **Show Agent Debug Logs**. Learn more about [troubleshooting AI in VS Code](/docs/agents/agent-troubleshooting/troubleshooting.md).

## Related resources

* [Create custom instructions](/docs/agent-customization/custom-instructions.md)
* [Configure agent tools](/docs/agents/run/tools.md)
* [Community contributed instructions, prompts, and custom agents](https://github.com/github/awesome-copilot)


---
# DOCUMENT_SOURCE: microsoft_vscode-docs::docs/agent-customization/tool-sets.md
- **CANONICAL_URL**: https://code.visualstudio.com/docs/agent-customization/tool-sets
- **RAW_SOURCE_URL**: https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/tool-sets.md
- **SHA256_FINGERPRINT**: `7f34fa90fe4f0ea5b1b387a768c90988584fe89d57b698e0ef7ea3b5ccda87f7`
- **LAST_VERIFIED_UTC**: 2026-10-20T22:05:29.938826+00:00
---

**MetaDescription**: Group tools for Local harness prompts and custom agents with reusable tool sets in Visual Studio Code.

# Create and use tool sets

A tool set is a reusable collection of agent tools that you can reference as a single entity. This article describes user-defined tool-set files for organizing related tools in prompts, [prompt files](/docs/agent-customization/prompt-files.md), and [custom agents](/docs/agent-customization/custom-agents.md) in Local sessions.

> [!IMPORTANT]
> User-defined tool-set files are supported only in **Local** harness sessions. For the **Copilot** harness, configure tools through its tool controls or a custom agent's tool list instead. See [customizations without automatic migration](/docs/agent-customization/migrate-customizations.md#customizations-without-automatic-migration).

VS Code also provides predefined tool sets, such as `#edit` and `#search`.

## Create a tool set

Select **Local** as the **Session Target** in the Chat view, then create a tool set:

1. Run **Chat: Configure Tool Sets** from the Command Palette and select **Create new tool sets file**.

    Alternatively, select the ellipsis (**...**) menu in the Chat view, select **Tool Sets**, and then select **Create new tool sets file**.

1. Define your tool set in the `.jsonc` file that opens.

    The following example creates a tool set named `reader`:

    ```json
    {
        "reader": {
            "tools": [
                "search/changes",
                "search/codebase",
                "read/problems",
                "search/usages"
            ],
            "description": "Tools for reading and gathering context",
            "icon": "book"
        }
    }
    ```

    A tool set has the following properties:

    * `tools`: array of built-in, MCP, or extension tool names.
    * `description`: brief description displayed in the tools picker.
    * `icon`: icon for the tool set. See the [Product Icon Reference](/api/references/icons-in-labels.md).

## Use a tool set

Reference a tool set in a prompt by typing `#` followed by its name:

```prompt
Analyze the codebase for security issues #reader
```

In the tools picker, tool sets appear as collapsible groups. Select or deselect a tool set to change the availability of all its tools at once.

You can also reference tool sets in [prompt files](/docs/agent-customization/prompt-files.md) and [custom agents](/docs/agent-customization/custom-agents.md).

## Related resources

* [Use tools with agents](/docs/agents/run/tools.md)
* [Add MCP servers](/docs/agent-customization/mcp-servers.md)
* [Create custom agents](/docs/agent-customization/custom-agents.md)
