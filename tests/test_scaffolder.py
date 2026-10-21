import json
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from copilot_scaffold import (
    scaffold_skill,
    scaffold_agent,
    scaffold_hooks,
    scaffold_dual_mcp,
    scaffold_plugin,
    main as scaffold_main,
)


def test_scaffold_skill(tmp_path):
    skill_file = scaffold_skill(tmp_path, "Testing Guardian")
    assert skill_file.exists()
    assert skill_file.name == "SKILL.md"
    content = skill_file.read_text(encoding="utf-8")
    assert "name: testing-guardian" in content
    assert "# Skill: Testing Guardian" in content
    assert "Step-by-Step Execution Protocol" in content


def test_scaffold_agent(tmp_path):
    agent_file = scaffold_agent(tmp_path, "Code Reviewer")
    assert agent_file.exists()
    assert agent_file.name == "code-reviewer.agent.md"
    content = agent_file.read_text(encoding="utf-8")
    assert "name: code-reviewer" in content
    assert "tools:" in content
    assert "- codebase" in content


def test_scaffold_hooks(tmp_path):
    hooks_file = scaffold_hooks(tmp_path)
    assert hooks_file.exists()
    assert hooks_file.name == "hooks.json"
    data = json.loads(hooks_file.read_text(encoding="utf-8"))
    assert "hooks" in data
    assert "preToolUse" in data["hooks"]
    assert "subagentStart" in data["hooks"]


def test_scaffold_dual_mcp(tmp_path):
    mcp_paths = scaffold_dual_mcp(tmp_path)
    portable = mcp_paths["portable"]
    vscode = mcp_paths["vscode"]

    assert portable.exists()
    assert vscode.exists()

    portable_data = json.loads(portable.read_text(encoding="utf-8"))
    assert "mcpServers" in portable_data
    assert "memoryServer" in portable_data["mcpServers"]

    vscode_data = json.loads(vscode.read_text(encoding="utf-8"))
    assert "servers" in vscode_data
    assert "workspaceSandboxedServer" in vscode_data["servers"]
    assert "sandboxEnabled" in vscode_data["servers"]["workspaceSandboxedServer"]


def test_scaffold_plugin(tmp_path):
    plugin_paths = scaffold_plugin(tmp_path, "Security Radar")
    plugin_file = plugin_paths["plugin"]
    settings_file = plugin_paths["settings"]

    assert plugin_file.exists()
    assert settings_file.exists()

    plugin_data = json.loads(plugin_file.read_text(encoding="utf-8"))
    assert plugin_data["name"] == "security-radar"
    assert "plugin.schema.json" in plugin_data["$schema"]

    settings_data = json.loads(settings_file.read_text(encoding="utf-8"))
    assert "security-radar" in settings_data["enabledPlugins"]


def test_scaffold_all_primitives_cli(tmp_path, monkeypatch):
    test_args = [
        "copilot_scaffold.py",
        "--type",
        "all",
        "--name",
        "harness-orchestrator",
        "--target-dir",
        str(tmp_path),
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    ret = scaffold_main()
    assert ret == 0

    assert (tmp_path / ".github" / "skills" / "harness-orchestrator" / "SKILL.md").exists()
    assert (tmp_path / ".github" / "agents" / "harness-orchestrator.agent.md").exists()
    assert (tmp_path / ".github" / "hooks" / "hooks.json").exists()
    assert (tmp_path / ".mcp.json").exists()
    assert (tmp_path / ".vscode" / "mcp.json").exists()
    assert (tmp_path / "plugin.json").exists()
    assert (tmp_path / ".github" / "copilot" / "settings.json").exists()
