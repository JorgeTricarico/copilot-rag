import sys
import json
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from copilot_docs_sync import (
    CopilotDocumentationSynchronizer,
    RepoTreeRule,
    REPO_RULES,
    DocumentRecord,
)


def test_bundle_resolution_longest_prefix():
    syncer = CopilotDocumentationSynchronizer(base_dir=Path("./tmp_test_sync"))

    rule = REPO_RULES[0]  # vscode-docs
    # "docs/agents/run/agent-harnesses" matches "01_Architecture_And_Agent_Harnesses"
    # while "docs/agents/run/" matches "05_Workflows_Planning_And_Remote_AHP"
    bundle_harness = syncer._resolve_bundle(
        "docs/agents/run/agent-harnesses.md", rule.bundle_router
    )
    assert bundle_harness == "01_Architecture_And_Agent_Harnesses"

    bundle_run = syncer._resolve_bundle(
        "docs/agents/run/custom-runner.md", rule.bundle_router
    )
    assert bundle_run == "05_Workflows_Planning_And_Remote_AHP"

    bundle_mcp = syncer._resolve_bundle(
        "docs/agent-customization/mcp-servers.md", rule.bundle_router
    )
    assert bundle_mcp == "03_MCP_Servers_And_Tools_Execution"

    bundle_customization = syncer._resolve_bundle(
        "docs/agent-customization/overview.md", rule.bundle_router
    )
    assert bundle_customization == "04_Customization_Skills_Hooks_And_Plugins"


def test_canonical_web_url_building():
    syncer = CopilotDocumentationSynchronizer(base_dir=Path("./tmp_test_sync"))

    # Test vscode rule
    vscode_rule = REPO_RULES[0]
    url_vscode = syncer._build_canonical_web_url(
        vscode_rule, "docs/agents/overview.md"
    )
    assert url_vscode == "https://code.visualstudio.com/docs/agents/overview"

    # Test internal skill in .github
    url_skill = syncer._build_canonical_web_url(
        vscode_rule, ".github/skills/docs-product-alignment/SKILL.md"
    )
    assert url_skill == "https://github.com/microsoft/vscode-docs/blob/main/.github/skills/docs-product-alignment/SKILL.md"

    # Test github docs rule (strips 'content/')
    github_rule = REPO_RULES[1]
    url_gh = syncer._build_canonical_web_url(
        github_rule, "content/copilot/concepts/agents/overview.md"
    )
    assert url_gh == "https://docs.github.com/en/copilot/concepts/agents/overview"


def test_manifest_load_save(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    assert len(syncer.manifest) == 0

    record = DocumentRecord(
        doc_id="test_doc_1",
        source_url="https://example.com/raw.md",
        Canonical_web_url="https://example.com/clean",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="abc12345",
        content_sha256="deadbeef" * 8,
        word_count=150,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/test_doc_1.md",
    )

    syncer.manifest["test_doc_1"] = record
    syncer._save_manifest()

    # Re-instantiate synchronizer
    syncer_reloaded = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    assert "test_doc_1" in syncer_reloaded.manifest
    loaded_rec = syncer_reloaded.manifest["test_doc_1"]
    assert loaded_rec.content_sha256 == "deadbeef" * 8
    assert loaded_rec.word_count == 150


def test_bundle_generation(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    clean_file = tmp_path / "clean_sources" / "doc1.md"
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_file.write_text("# Doc 1 Content\nSome text.", encoding="utf-8")

    record = DocumentRecord(
        doc_id="doc1",
        source_url="https://example.com/doc1",
        Canonical_web_url="https://example.com/canonical_doc1",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha=None,
        content_sha256="12345678",
        word_count=5,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/doc1.md",
    )
    syncer.manifest["doc1"] = record
    syncer.dirty_bundles.add("01_Architecture_And_Agent_Harnesses")

    bundles = syncer.build_notebooklm_bundles()
    assert len(bundles) == 1
    bundle_path = bundles[0]
    assert bundle_path.exists()
    content = bundle_path.read_text(encoding="utf-8")
    assert "COMPENDIO RAG NOTEBOOKLM: 01_Architecture_And_Agent_Harnesses" in content
    assert "DOCUMENT_SOURCE: doc1" in content
    assert "https://example.com/canonical_doc1" in content
