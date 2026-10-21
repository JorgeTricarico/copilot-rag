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
    ContentCanonicalizer,
)


def test_bundle_resolution_longest_prefix():
    syncer = CopilotDocumentationSynchronizer(base_dir=Path("./tmp_test_sync"))

    rule = REPO_RULES[0]  # vscode-docs
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

    vscode_rule = REPO_RULES[0]
    url_vscode = syncer._build_canonical_web_url(
        vscode_rule, "docs/agents/overview.md"
    )
    assert url_vscode == "https://code.visualstudio.com/docs/agents/overview"

    # BUG-05: Release notes should map to /updates/
    url_rn = syncer._build_canonical_web_url(
        vscode_rule, "release-notes/v1_98.md"
    )
    assert url_rn == "https://code.visualstudio.com/updates/v1_98"

    url_skill = syncer._build_canonical_web_url(
        vscode_rule, ".github/skills/docs-product-alignment/SKILL.md"
    )
    assert url_skill == "https://github.com/microsoft/vscode-docs/blob/main/.github/skills/docs-product-alignment/SKILL.md"

    github_rule = REPO_RULES[1]
    url_gh = syncer._build_canonical_web_url(
        github_rule, "content/copilot/concepts/agents/overview.md"
    )
    assert url_gh == "https://docs.github.com/en/copilot/concepts/agents/overview"


def test_safe_clean_filename_no_double_extension():
    syncer = CopilotDocumentationSynchronizer(base_dir=Path("./tmp_test_sync"))

    filename_from_md = syncer._get_safe_clean_filename("owner_repo::docs/agent/overview.md")
    assert filename_from_md == "owner_repo__docs_agent_overview.md"
    assert not filename_from_md.endswith(".md.md")

    filename_from_web = syncer._get_safe_clean_filename("web::api_reference")
    assert filename_from_web == "web__api_reference.md"


def test_manifest_load_save_and_backward_compatibility(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    assert len(syncer.manifest) == 0

    record = DocumentRecord(
        doc_id="test_doc_1",
        source_url="https://example.com/raw.md",
        canonical_web_url="https://example.com/clean",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="abc12345",
        content_sha256="deadbeef" * 8,
        word_count=150,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/test_doc_1.md",
    )

    # Test backward compatibility property
    assert record.Canonical_web_url == "https://example.com/clean"

    syncer.manifest["test_doc_1"] = record
    syncer._save_manifest()

    # Re-instantiate synchronizer
    syncer_reloaded = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    assert "test_doc_1" in syncer_reloaded.manifest
    loaded_rec = syncer_reloaded.manifest["test_doc_1"]
    assert loaded_rec.content_sha256 == "deadbeef" * 8
    assert loaded_rec.word_count == 150
    assert loaded_rec.canonical_web_url == "https://example.com/clean"


def test_delete_document_upstream(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    clean_file = tmp_path / "clean_sources" / "deleted_doc.md"
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_file.write_text("Old content to delete", encoding="utf-8")

    record = DocumentRecord(
        doc_id="microsoft_vscode-docs::docs/deprecated.md",
        source_url="https://example.com/old",
        canonical_web_url="https://example.com/old",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="112233",
        content_sha256="abcdef",
        word_count=4,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/deleted_doc.md",
    )
    syncer.manifest["microsoft_vscode-docs::docs/deprecated.md"] = record

    assert clean_file.exists()
    syncer._delete_document("microsoft_vscode-docs::docs/deprecated.md", record)

    assert not clean_file.exists()
    assert "microsoft_vscode-docs::docs/deprecated.md" not in syncer.manifest
    assert "01_Architecture_And_Agent_Harnesses" in syncer.dirty_bundles
    assert any("[DOCUMENTO ELIMINADO UPSTREAM]" in r for r in syncer.change_reports)


def test_verify_integrity(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    clean_file = tmp_path / "clean_sources" / "valid_doc.md"
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    clean_text = "# Valid\nIntegrity check content\n"
    clean_file.write_text(clean_text, encoding="utf-8")
    actual_hash = ContentCanonicalizer.compute_sha256(clean_text)

    record = DocumentRecord(
        doc_id="valid_doc",
        source_url="https://example.com/valid",
        canonical_web_url="https://example.com/valid",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="112233",
        content_sha256=actual_hash,
        word_count=4,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/valid_doc.md",
    )
    syncer.manifest["valid_doc"] = record

    assert syncer.verify_integrity() is True

    # Tamper with file
    clean_file.write_text("Tampered content", encoding="utf-8")
    assert syncer.verify_integrity() is False


def test_manifest_not_saved_if_no_changes(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    assert syncer.manifest_dirty is False

    # Mark dirty and save
    syncer.manifest_dirty = True
    saved = syncer._save_manifest()
    assert saved is True
    assert syncer.manifest_path.exists()
    assert syncer.manifest_dirty is False


def test_notebooklm_bundle_excludes_low_density_stubs(tmp_path):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)

    # Document A: Stub (< 25 words)
    stub_file = tmp_path / "clean_sources" / "stub_doc.md"
    stub_file.parent.mkdir(parents=True, exist_ok=True)
    stub_file.write_text("# Overview\nShort stub index.", encoding="utf-8")
    syncer.manifest["doc_stub"] = DocumentRecord(
        doc_id="doc_stub",
        source_url="https://example.com/stub",
        canonical_web_url="https://example.com/stub",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="111",
        content_sha256="abc",
        word_count=5,
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/stub_doc.md",
    )

    # Document B: Rich technical document (>= 25 words)
    rich_file = tmp_path / "clean_sources" / "rich_doc.md"
    rich_text = "This is a comprehensive technical document explaining the internal architecture, memory context compaction, and tool calling mechanics of Copilot Agents in Visual Studio Code with clear explanations and comprehensive details."
    rich_file.write_text(rich_text, encoding="utf-8")
    syncer.manifest["doc_rich"] = DocumentRecord(
        doc_id="doc_rich",
        source_url="https://example.com/rich",
        canonical_web_url="https://example.com/rich",
        bundle_name="01_Architecture_And_Agent_Harnesses",
        git_blob_sha="222",
        content_sha256="def",
        word_count=len(rich_text.split()),
        last_updated_utc="2026-10-20T12:00:00Z",
        local_clean_path="clean_sources/rich_doc.md",
    )

    bundles = syncer.build_notebooklm_bundles(rebuild_all=True)
    assert len(bundles) == 1
    bundle_content = bundles[0].read_text(encoding="utf-8")

    # Rich doc must be present
    assert "doc_rich" in bundle_content
    # Stub (< 25 words) must be excluded (OPT-01)
    assert "doc_stub" not in bundle_content


def test_repo_rules_subpath_configuration():
    gh_rule = next(r for r in REPO_RULES if r.repo == "docs")
    assert gh_rule.tree_subpath == "content/copilot"


def test_langgraph_documentation_sync_mocked(tmp_path, monkeypatch):
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)

    sample_llms_txt = (
        "# Docs by LangChain: LangGraph (Python)\n\n"
        "- [Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart.md)\n"
        "- [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers.md)\n"
    )

    class MockResponse:
        def __init__(self, text, status_code=200):
            self.text = text
            self.status_code = status_code

        def raise_for_status(self):
            pass

    def mock_get(url, *args, **kwargs):
        if "llms.txt" in url:
            return MockResponse(sample_llms_txt)
        return MockResponse("# Title\n\nThis is technical documentation content with sufficient words for verification.")

    monkeypatch.setattr(syncer.session, "get", mock_get)

    added, updated, skipped, deleted = syncer.sync_langgraph_documentation()
    assert added == 2
    assert skipped == 0
    assert "langgraph::quickstart" in syncer.manifest
    assert "langgraph::checkpointers" in syncer.manifest
    assert syncer.manifest["langgraph::quickstart"].bundle_name == "08_Agent_Workflows_LangGraph_And_Ecosystem"

    # Segunda corrida sin cambios debe dar skipped = 2, added = 0
    a2, u2, s2, d2 = syncer.sync_langgraph_documentation()
    assert a2 == 0
    assert s2 == 2

