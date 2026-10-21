import sys
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).parent.parent
SKILL_SOURCE = REPO_ROOT / "skills" / "copilot-architect"
sys.path.insert(0, str(SKILL_SOURCE / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_project import audit_project, format_markdown_report
from query_docs import query_docs
from install_skill import install_skill


def test_skill_source_structure():
    assert SKILL_SOURCE.exists()
    skill_md = SKILL_SOURCE / "SKILL.md"
    assert skill_md.exists()
    content = skill_md.read_text(encoding="utf-8")
    assert "name: copilot-architect" in content
    assert "Protocolo de Auditoría y Mejora en 5 Fases" in content

    # Referencias
    references_dir = SKILL_SOURCE / "references"
    assert references_dir.exists()
    refs = list(references_dir.glob("*.md"))
    assert len(refs) >= 6

    # Scripts
    scripts_dir = SKILL_SOURCE / "scripts"
    assert (scripts_dir / "audit_project.py").exists()
    assert (scripts_dir / "query_docs.py").exists()


def test_audit_project_execution(tmp_path):
    # Probar sobre una carpeta vacía
    res = audit_project(tmp_path)
    assert res["score_pct"] == 0
    assert len(res["checks"]) == 6

    # Crear una estructura básica para simular cumplimiento
    (tmp_path / ".mcp.json").write_text('{"mcpServers": {}}', encoding="utf-8")
    (tmp_path / ".github" / "skills" / "sample").mkdir(parents=True, exist_ok=True)
    (tmp_path / ".github" / "skills" / "sample" / "SKILL.md").write_text("---\nname: s\n---\n", encoding="utf-8")

    res_updated = audit_project(tmp_path)
    assert res_updated["score_pct"] > 0

    report = format_markdown_report(res_updated)
    assert "Reporte de Auditoría de Arquitectura de Agentes" in report
    assert "Readiness Score" in report


def test_query_docs_execution():
    ws_dir = REPO_ROOT / "copilot_rag_workspace"
    if ws_dir.exists():
        matches = query_docs(ws_dir, query="AgentHarness", limit=3)
        assert isinstance(matches, list)


def test_install_skill_lifecycle(tmp_path):
    target = tmp_path / ".github" / "skills"
    installed_dir = install_skill(target, force=True)

    assert installed_dir.exists()
    assert installed_dir.name == "copilot-architect"
    assert (installed_dir / "SKILL.md").exists()
    assert (installed_dir / "references" / "01_harness_and_roles.md").exists()
    assert (installed_dir / "scripts" / "audit_project.py").exists()
    assert (installed_dir / "scripts" / "query_docs.py").exists()
