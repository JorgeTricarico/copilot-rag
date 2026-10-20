import sys
from pathlib import Path
import pytest

# Ensure scripts dir is in path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from copilot_docs_sync import ContentCanonicalizer, LIQUID_VARIABLES_MAP


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
