import sys
from pathlib import Path
import pytest

# Ensure repo root and scripts dir are in path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from copilot_docs_sync import ContentCanonicalizer, LIQUID_VARIABLES_MAP


def test_frontmatter_multiline_folded_scalars():
    raw_md = (
        "---\n"
        "title: Authentication\n"
        "shortTitle: Authenticate\n"
        "intro: >-\n"
        "  Learn how to configure authentication for the Copilot SDK\n"
        "  using tokens and server configurations.\n"
        "---\n"
        "# Section Content\n"
    )
    normalized = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "**intro**: Learn how to configure authentication for the Copilot SDK using tokens and server configurations." in normalized
    assert ">-" not in normalized


def test_autotitle_link_resolution():
    raw_md = "For details, see [AUTOTITLE](/copilot/how-tos/copilot-sdk/auth/server-to-server-tokens#scopes)."
    normalized = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "[Server To Server Tokens](https://docs.github.com/en/copilot/how-tos/copilot-sdk/auth/server-to-server-tokens#scopes)" in normalized
    assert "AUTOTITLE" not in normalized


def test_html_details_summary_cleanup():
    raw_md = (
        "<a name=\"intro-anchor\"></a>\n"
        "<details open>\n"
        "<summary><strong>TypeScript / Node.js</strong></summary>\n"
        "Code example here\n"
        "</details>"
    )
    normalized = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "<a name=" not in normalized
    assert "<details" not in normalized
    assert "</details>" not in normalized
    assert "**TypeScript / Node.js**" in normalized
    assert "Code example here" in normalized


def test_canonical_release_notes_url(tmp_path):
    from scripts.copilot_docs_sync import CopilotDocumentationSynchronizer, RepoTreeRule
    syncer = CopilotDocumentationSynchronizer(base_dir=tmp_path)
    rule = RepoTreeRule(
        owner="microsoft",
        repo="vscode-docs",
        branch="main",
        path_prefixes=[],
        web_base_url="https://code.visualstudio.com/",
        bundle_router={},
    )
    url = syncer._build_canonical_web_url(rule, "release-notes/v1_104.md")
    assert url == "https://code.visualstudio.com/updates/v1_104"



def test_markdown_frontmatter_extraction():
    raw_md = """---
title: "Custom Agents in VS Code"
shortTitle: Agents
description: "A description of custom agents."
MetaDescription: "Learn how to build custom agents for Visual Studio Code."
internal_audit_score: 95
last_reviewed: 2026-05-12
---

# Introduction

This is the main body.
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "**title**: Custom Agents in VS Code" in clean
    assert "**shortTitle**: Agents" in clean
    assert "**description**: A description of custom agents." in clean
    assert "**MetaDescription**: Learn how to build custom agents for Visual Studio Code." in clean
    assert "internal_audit_score" not in clean
    assert "last_reviewed" not in clean
    assert "# Introduction" in clean


def test_markdown_frontmatter_multiline_folded_and_literal():
    raw_md = """---
title: Custom Agents Guide
intro: >-
  This is a multiline intro block
  that is folded by YAML
  across multiple indented lines.
description: |
  A literal block description
  with essential details.
---

Body content here.
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "**title**: Custom Agents Guide" in clean
    assert "**intro**: This is a multiline intro block that is folded by YAML across multiple indented lines." in clean
    assert "**description**: A literal block description with essential details." in clean
    assert "Body content here." in clean


def test_autotitle_resolution():
    raw_md = """
Check [AUTOTITLE](/copilot/how-tos/auth#token) for credentials.
Also see [AUTOTITLE](/copilot/concepts/agents) and [AUTOTITLE](https://docs.github.com/en/copilot/quickstart).
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "[Auth](https://docs.github.com/en/copilot/how-tos/auth#token)" in clean
    assert "[Agents](https://docs.github.com/en/copilot/concepts/agents)" in clean
    assert "[Quickstart](https://docs.github.com/en/copilot/quickstart)" in clean


def test_html_sanitization_empty_anchors_and_details():
    raw_md = """
# Section
<a name="custom-anchor"></a>
<a id="another-anchor"></a>
<details>
<summary><strong>Expandable Details Title</strong></summary>
Inner details content here.
</details>

<details>
<summary>Plain Summary Title</summary>
More inner content.
</details>
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "<a name" not in clean
    assert "<a id" not in clean
    assert "<details" not in clean
    assert "</details>" not in clean
    assert "<summary" not in clean
    assert "</summary>" not in clean
    assert "**Expandable Details Title**" in clean
    assert "**Plain Summary Title**" in clean
    assert "Inner details content here." in clean



def test_html_comments_removal():
    raw_md = """# Title
<!-- This is an internal comment that should be stripped -->
Visible paragraph.
<!-- Multi-line
comment
here -->
Another visible line.
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "internal comment" not in clean
    assert "Multi-line" not in clean
    assert "Visible paragraph." in clean
    assert "Another visible line." in clean


def test_liquid_variables_replacement():
    raw_md = """Use {% data variables.product.prodname_vscode %} with {% data variables.product.prodname_copilot_short %} to manage {% data variables.copilot.copilot_custom_agent_short %}.
Also unknown: {% data variables.custom.unknown_var %}.
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "Use Visual Studio Code with Copilot to manage custom agent." in clean
    assert "Also unknown: [custom.unknown_var]." in clean


def test_liquid_codetab_replacement():
    raw_md = """{% codetabs %}
{% codetab python %}
```python
import copilot
```
{% endcodetab %}
{% codetab typescript %}
```typescript
import { CopilotClient } from "@github/copilot-sdk";
```
{% endcodetab %}
{% endcodetabs %}
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "**Language (python):**" in clean
    assert "**Language (typescript):**" in clean
    assert "import copilot" in clean
    assert "import { CopilotClient }" in clean


def test_vscode_macros_replacement():
    raw_md = """Press kb(workbench.action.chat.open) or kbstyle(Ctrl+Alt+I) to open chat.
Configure via setting(chat.mcp.autostart).
"""
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "`Shortcut: workbench.action.chat.open`" in clean
    assert "`Ctrl+Alt+I`" in clean
    assert "`chat.mcp.autostart`" in clean


def test_unicode_nfkc_and_whitespace_cleanup():
    raw_md = "Heading   \n\n\n\n\nParagraph with trailing spaces   \t \n"
    clean = ContentCanonicalizer.normalize_markdown(raw_md)
    assert "\n\n\n" not in clean
    assert "trailing spaces" in clean


def test_html_to_text_stripping_and_noise_removal():
    raw_html = """
    <!DOCTYPE html>
    <html>
    <head><title>Test</title><style>body { color: red; }</style></head>
    <body>
        <nav><a href="/">Home</a></nav>
        <header>Header info</header>
        <main>
            <h1>Agent Harness Architecture</h1>
            <p>The agent harness coordinates tool invocation.</p>
            <div class="action-btn">Copy as Markdown</div>
            <div class="action-btn">Open in VS Code</div>
            <ul>
                <li>Local Harness</li>
                <li>Copilot Harness</li>
            </ul>
            <pre><code>def run(): pass</code></pre>
            <table>
                <tr><th>Col1</th><th>Col2</th></tr>
                <tr><td>Val1</td><td>Val2</td></tr>
            </table>
        </main>
        <footer>Footer noise</footer>
        <script>console.log("noisy script");</script>
    </body>
    </html>
    """
    clean = ContentCanonicalizer.normalize_html_to_text(raw_html)
    assert "# Agent Harness Architecture" in clean
    assert "The agent harness coordinates tool invocation." in clean
    assert "- Local Harness" in clean
    assert "- Copilot Harness" in clean
    assert "```\ndef run(): pass\n```" in clean
    assert "| Col1 | Col2 |" in clean
    assert "| Val1 | Val2 |" in clean
    # Noise tags must be stripped
    assert "noisy script" not in clean
    assert "Footer noise" not in clean
    assert "Copy as Markdown" not in clean
    assert "Open in VS Code" not in clean


def test_rss_feed_normalization():
    raw_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
      <channel>
        <title>GitHub Copilot Changelog</title>
        <item>
          <title>Copilot Agents Support MCP</title>
          <link>https://github.blog/changelog/2026-04-copilot-mcp</link>
          <pubDate>Wed, 15 Apr 2026 12:00:00 GMT</pubDate>
          <description><![CDATA[<p>MCP servers are now directly supported.</p>]]></description>
        </item>
      </channel>
    </rss>
    """
    clean = ContentCanonicalizer.normalize_rss_feed(raw_xml)
    assert "# GitHub Copilot Official Changelog Feed" in clean
    assert "## Copilot Agents Support MCP" in clean
    assert "https://github.blog/changelog/2026-04-copilot-mcp" in clean
    assert "MCP servers are now directly supported." in clean


def test_sha256_determinism():
    text_a = "Deterministic content line 1\nLine 2"
    text_b = "Deterministic content line 1\nLine 2"
    text_c = "Deterministic content line 1\nLine 3"

    hash_a = ContentCanonicalizer.compute_sha256(text_a)
    hash_b = ContentCanonicalizer.compute_sha256(text_b)
    hash_c = ContentCanonicalizer.compute_sha256(text_c)

    assert hash_a == hash_b
    assert hash_a != hash_c
    assert len(hash_a) == 64


def test_normalize_dts_and_json_schema():
    raw_dts = "declare module 'vscode' {\n  export interface ChatContext {\n    history: any[];\n  }\n}\n"
    dts_clean = ContentCanonicalizer.normalize_dts(raw_dts, "src/vscode-dts/vscode.proposed.chat.d.ts")
    assert "# VS Code Proposed AI API Definition: `src/vscode-dts/vscode.proposed.chat.d.ts`" in dts_clean
    assert "```typescript\ndeclare module 'vscode'" in dts_clean
    assert len(ContentCanonicalizer.compute_sha256(dts_clean)) == 64

    raw_json = '{"version": "1.0.0", "name": "sample-plugin", "skills": ["skill-a"]}'
    json_clean = ContentCanonicalizer.normalize_json_schema(raw_json, "Agent Plugins 1.0")
    assert "# Official JSON Schema: Agent Plugins 1.0" in json_clean
    assert '```json\n{\n  "name": "sample-plugin"' in json_clean
    assert len(ContentCanonicalizer.compute_sha256(json_clean)) == 64
