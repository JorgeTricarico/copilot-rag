#!/usr/bin/env python3
"""
Scaffolder Determinista de Arquitectura de Agentes para VS Code Copilot.
Genera plantillas verificadas de SKILL.md, Custom Agents, Lifecycle Hooks,
Configuración Dual MCP (.mcp.json + .vscode/mcp.json) y Agent Plugins 1.0.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", name.strip().lower()).strip("-")
    return slug or "custom-capability"


def scaffold_skill(target_dir: Path, name: str) -> Path:
    slug = slugify(name)
    skill_dir = target_dir / ".github" / "skills" / slug
    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_file = skill_dir / "SKILL.md"
    content = (
        f"---\n"
        f"name: {slug}\n"
        f"description: Specialized agent skill for {name}. Loaded on-demand when tasks match this domain.\n"
        f"---\n\n"
        f"# Skill: {name}\n\n"
        f"## When to Use This Skill\n"
        f"Use this skill whenever the task requires implementing, auditing, or testing components related to **{name}**.\n\n"
        f"## Step-by-Step Execution Protocol\n"
        f"1. **Context Discovery**: Search relevant files and inspect existing tests before proposing changes.\n"
        f"2. **Minimal Deterministic Edits**: Preserve existing architectural boundaries and types.\n"
        f"3. **Automated Verification**: Run unit tests and linters after applying changes.\n\n"
        f"## Guardrails\n"
        f"- Never hardcode secrets or bypass validation hooks.\n"
        f"- Return concise summaries of verified behavior.\n"
    )
    skill_file.write_text(content, encoding="utf-8")
    return skill_file


def scaffold_agent(target_dir: Path, name: str) -> Path:
    slug = slugify(name)
    agents_dir = target_dir / ".github" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    agent_file = agents_dir / f"{slug}.agent.md"
    content = (
        f"---\n"
        f"name: {slug}\n"
        f"description: Specialized custom agent for {name} workflows with isolated context and strict verification.\n"
        f"tools:\n"
        f"  - codebase\n"
        f"  - editFiles\n"
        f"  - runCommands\n"
        f"  - problems\n"
        f"---\n\n"
        f"# Custom Agent Role: {name}\n\n"
        f"You are an expert software engineering agent specialized in **{name}**.\n\n"
        f"## Operating Principles\n"
        f"1. **Plan Before Mutating**: Clarify ambiguous requirements and verify file dependencies first.\n"
        f"2. **Subagent Delegation**: Delegate isolated research or parallel test verification to subagents to prevent context pollution.\n"
        f"3. **Verification Loop**: Always validate code edits against the project's test suite before concluding a turn.\n"
    )
    agent_file.write_text(content, encoding="utf-8")
    return agent_file


def scaffold_hooks(target_dir: Path) -> Path:
    hooks_dir = target_dir / ".github" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    hooks_file = hooks_dir / "hooks.json"
    payload = {
        "hooks": {
            "preToolUse": [
                {
                    "matcher": "terminal|bash|pwsh",
                    "command": "echo '[Hook preToolUse] Auditing terminal command execution...'",
                }
            ],
            "postToolUse": [
                {
                    "matcher": "editFiles|write",
                    "command": "echo '[Hook postToolUse] File mutation completed. Ready for linter/test check.'",
                }
            ],
            "subagentStart": [
                {
                    "command": "echo '[Hook subagentStart] Initializing isolated subagent context...'"
                }
            ],
            "subagentStop": [
                {
                    "command": "echo '[Hook subagentStop] Subagent finished and returned synthesized result.'"
                }
            ],
        }
    }
    hooks_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return hooks_file


def scaffold_dual_mcp(target_dir: Path) -> Dict[str, Path]:
    # 1. Formato Portable Copilot (.mcp.json en raíz para Agent Host y CLI)
    portable_mcp_path = target_dir / ".mcp.json"
    portable_payload = {
        "mcpServers": {
            "memoryServer": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-memory"],
            }
        }
    }
    portable_mcp_path.write_text(
        json.dumps(portable_payload, indent=2) + "\n", encoding="utf-8"
    )

    # 2. Formato VS Code (.vscode/mcp.json con inputs, dev mode y sandboxing)
    vscode_dir = target_dir / ".vscode"
    vscode_dir.mkdir(parents=True, exist_ok=True)
    vscode_mcp_path = vscode_dir / "mcp.json"
    vscode_payload = {
        "inputs": [
            {
                "id": "service_api_key",
                "type": "promptString",
                "description": "API Key for external MCP service (stored encrypted by VS Code)",
                "password": True,
            }
        ],
        "servers": {
            "workspaceSandboxedServer": {
                "type": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"],
                "env": {
                    "SERVICE_API_KEY": "${input:service_api_key}"
                },
                "dev": {
                    "watch": "src/**/*.ts"
                },
                "sandboxEnabled": True,
                "sandbox": {
                    "filesystem": {
                        "allowWrite": ["${workspaceFolder}"]
                    },
                    "network": {
                        "allowedDomains": ["api.github.com", "code.visualstudio.com"]
                    },
                },
            }
        },
        "sandbox": {
            "filesystem": {
                "denyRead": ["~/.ssh", "~/.aws"]
            }
        },
    }
    vscode_mcp_path.write_text(
        json.dumps(vscode_payload, indent=2) + "\n", encoding="utf-8"
    )
    return {"portable": portable_mcp_path, "vscode": vscode_mcp_path}


def scaffold_plugin(target_dir: Path, name: str) -> Dict[str, Path]:
    slug = slugify(name)
    plugin_file = target_dir / "plugin.json"
    plugin_payload = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": slug,
        "version": "1.0.0",
        "description": f"Portable Agent Plugin 1.0 bundle for {name} (skills + MCP).",
    }
    plugin_file.write_text(json.dumps(plugin_payload, indent=2) + "\n", encoding="utf-8")

    copilot_settings_dir = target_dir / ".github" / "copilot"
    copilot_settings_dir.mkdir(parents=True, exist_ok=True)
    settings_file = copilot_settings_dir / "settings.json"
    settings_payload = {
        "enabledPlugins": [slug],
        "extraKnownMarketplaces": [],
    }
    settings_file.write_text(
        json.dumps(settings_payload, indent=2) + "\n", encoding="utf-8"
    )
    return {"plugin": plugin_file, "settings": settings_file}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generador de Boilerplates de Arquitectura de Agentes para VS Code Copilot"
    )
    parser.add_argument(
        "--type",
        choices=["skill", "agent", "hooks", "mcp", "plugin", "all"],
        required=True,
        help="Tipo de artefacto a generar.",
    )
    parser.add_argument(
        "--name",
        type=str,
        default="architecture-guardian",
        help="Nombre identificador para la skill, agente o plugin.",
    )
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=Path("."),
        help="Directorio raíz del proyecto donde se generarán los archivos.",
    )
    args = parser.parse_args()

    target = args.target_dir.resolve()
    target.mkdir(parents=True, exist_ok=True)
    created = []

    if args.type in ("skill", "all"):
        created.append(scaffold_skill(target, args.name))
    if args.type in ("agent", "all"):
        created.append(scaffold_agent(target, args.name))
    if args.type in ("hooks", "all"):
        created.append(scaffold_hooks(target))
    if args.type in ("mcp", "all"):
        mcp_paths = scaffold_dual_mcp(target)
        created.extend(mcp_paths.values())
    if args.type in ("plugin", "all"):
        plugin_paths = scaffold_plugin(target, args.name)
        created.extend(plugin_paths.values())

    for p in created:
        print(f"[OK] Generado: {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
