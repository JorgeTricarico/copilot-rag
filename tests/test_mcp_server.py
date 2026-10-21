import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from copilot_mcp_server import CopilotMCPServer


def test_mcp_server_tools_list():
    server = CopilotMCPServer()
    tools = server.get_tools()
    tool_names = [t["name"] for t in tools]

    assert "search_copilot_docs" in tool_names
    assert "get_copilot_document" in tool_names
    assert "list_copilot_bundles" in tool_names
    assert "scaffold_agent_asset" in tool_names


def test_mcp_server_list_bundles():
    server = CopilotMCPServer()
    res = server.call_tool("list_copilot_bundles", {})
    assert "Compendios Temáticos para Google NotebookLM" in res


def test_mcp_server_search_docs():
    server = CopilotMCPServer()
    res = server.call_tool("search_copilot_docs", {"query": "AgentHost", "limit": 3})
    assert "Resultados para 'AgentHost'" in res or "No se encontraron" in res


def test_mcp_server_scaffold(tmp_path):
    server = CopilotMCPServer()
    res = server.call_tool(
        "scaffold_agent_asset",
        {"asset_type": "skill", "name": "mcp-test-skill", "target_dir": str(tmp_path)},
    )
    assert "Skill generada exitosamente" in res
    assert (tmp_path / ".github" / "skills" / "mcp-test-skill" / "SKILL.md").exists()
