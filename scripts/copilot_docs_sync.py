#!/usr/bin/env python3
"""
Sistema Determinista de Monitoreo Documental y Empaquetado RAG para VS Code Copilot.
Extrae, normaliza, calcula hashes SHA-256 sobre contenido semántico limpio, detecta
modificaciones reales sin falsos positivos, gestiona eliminaciones y construye
compendios optimizados para Google NotebookLM.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import difflib
import hashlib
import json
import logging
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment

# Configurar encoding UTF-8 en consola de Windows si es necesario
if sys.platform == "win32":
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Configuración de logging estructurado con soporte UTF-8
logger = logging.getLogger("CopilotDocsSync")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler(sys.stdout)
    _handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(_handler)


# =====================================================================
# 1. DICCIONARIO DE RESOLUCIÓN CANÓNICA PARA MACROS LIQUID Y VSCODE
# =====================================================================
LIQUID_VARIABLES_MAP: Dict[str, str] = {
    "product.prodname_vscode_shortname": "VS Code",
    "product.prodname_vscode": "Visual Studio Code",
    "product.prodname_copilot": "GitHub Copilot",
    "product.prodname_copilot_short": "Copilot",
    "product.prodname_github_codespaces": "GitHub Codespaces",
    "product.prodname_actions": "GitHub Actions",
    "product.prodname_dotcom_the_website": "GitHub.com",
    "product.prodname_ghe_server": "GitHub Enterprise Server",
    "product.prodname_cli": "GitHub CLI",
    "product.github": "GitHub",
    "product.company_short": "GitHub",
    "copilot.chat_view": "Chat view",
    "copilot.agents_window": "Agents window",
    "copilot.copilot_cli": "GitHub Copilot CLI",
    "copilot.copilot_cli_short": "Copilot CLI",
    "copilot.copilot_cloud_agent": "Copilot cloud agent",
    "copilot.copilot_cloud_agent_short": "Copilot cloud agent",
    "copilot.copilot_chat": "GitHub Copilot Chat",
    "copilot.copilot_chat_short": "Copilot Chat",
    "copilot.copilot_free_short": "Copilot Free",
    "copilot.copilot_business_short": "Copilot Business",
    "copilot.copilot_enterprise_short": "Copilot Enterprise",
    "copilot.github_copilot_app": "GitHub Copilot app",
    "copilot.copilot_custom_agent_short": "custom agent",
    "copilot.copilot_code-review_short": "Copilot code review",
}


# =====================================================================
# 2. DEFINICIÓN DE FUENTES Y REGLAS DE AGRUPACIÓN PARA NOTEBOOKLM
# =====================================================================
@dataclass
class RepoTreeRule:
    owner: str
    repo: str
    branch: str
    path_prefixes: List[str]
    web_base_url: str
    bundle_router: Dict[str, str]
    root_subpath: str = ""
    allowed_extensions: Tuple[str, ...] = (".md",)
    file_regex_filter: Optional[str] = None

    @property
    def tree_subpath(self) -> str:
        return self.root_subpath


REPO_RULES: List[RepoTreeRule] = [
    RepoTreeRule(
        owner="microsoft",
        repo="vscode-docs",
        branch="main",
        path_prefixes=[
            "docs/agents/",
            "docs/agent-customization/",
            "docs/copilot/",
            "docs/chat/",
            "docs/setup/copilot.md",
            "api/extension-guides/ai/",
            ".github/skills/docs-product-alignment/SKILL.md",
        ],
        web_base_url="https://code.visualstudio.com/",
        bundle_router={
            "docs/agents/concepts/": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/run/agent-harnesses": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/overview": "01_Architecture_And_Agent_Harnesses",
            "docs/agents/best-practices": "01_Architecture_And_Agent_Harnesses",
            "docs/setup/copilot": "01_Architecture_And_Agent_Harnesses",
            ".github/skills/": "01_Architecture_And_Agent_Harnesses",
            "docs/chat/": "02_Context_Memory_And_Compaction",
            "docs/agents/reference/workspace-context": "02_Context_Memory_And_Compaction",
            "docs/agent-customization/mcp-servers": "03_MCP_Servers_And_Tools_Execution",
            "docs/agents/reference/mcp-configuration": "03_MCP_Servers_And_Tools_Execution",
            "docs/agents/run/tools": "03_MCP_Servers_And_Tools_Execution",
            "docs/agent-customization/": "04_Customization_Skills_Hooks_And_Plugins",
            "docs/agents/run/": "05_Workflows_Planning_And_Remote_AHP",
            "docs/agents/guides/": "05_Workflows_Planning_And_Remote_AHP",
            "docs/agents/": "05_Workflows_Planning_And_Remote_AHP",
            "api/extension-guides/ai/": "06_Extension_AI_APIs_And_Copilot_SDK",
        },
        root_subpath="",
        allowed_extensions=(".md",),
    ),
    RepoTreeRule(
        owner="github",
        repo="docs",
        branch="main",
        path_prefixes=[
            "content/copilot/concepts/agents/",
            "content/copilot/concepts/context/",
            "content/copilot/reference/hooks-reference.md",
            "content/copilot/reference/copilot-cli-reference/",
            "content/copilot/how-tos/copilot-sdk/",
            "content/copilot/how-tos/copilot-cli/index.md",
        ],
        web_base_url="https://docs.github.com/en/",
        bundle_router={
            "content/copilot/concepts/agents/copilot-cli/context-management": "02_Context_Memory_And_Compaction",
            "content/copilot/concepts/context/": "02_Context_Memory_And_Compaction",
            "content/copilot/concepts/agents/about-agent-skills": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/concepts/agents/about-plugins": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/reference/hooks-reference": "04_Customization_Skills_Hooks_And_Plugins",
            "content/copilot/how-tos/copilot-sdk/": "06_Extension_AI_APIs_And_Copilot_SDK",
            "content/copilot/": "05_Workflows_Planning_And_Remote_AHP",
        },
        root_subpath="content/copilot",
        allowed_extensions=(".md",),
    ),
    RepoTreeRule(
        owner="microsoft",
        repo="vscode",
        branch="main",
        path_prefixes=["src/vscode-dts/"],
        web_base_url="https://github.com/microsoft/vscode/blob/main/",
        bundle_router={
            "src/vscode-dts/": "06_Extension_AI_APIs_And_Copilot_SDK",
        },
        root_subpath="src/vscode-dts",
        allowed_extensions=(".d.ts",),
        file_regex_filter=r"^src/vscode-dts/vscode\.proposed\.(chat|languageModel|mcp|agent).*\.d\.ts$",
    ),
    RepoTreeRule(
        owner="github",
        repo="awesome-copilot",
        branch="main",
        path_prefixes=["skills/", "agents/", "instructions/", "README.md"],
        web_base_url="https://github.com/github/awesome-copilot/blob/main/",
        bundle_router={
            "": "04_Customization_Skills_Hooks_And_Plugins",
        },
        root_subpath="",
        allowed_extensions=(".md",),
    ),
    RepoTreeRule(
        owner="anthropics",
        repo="skills",
        branch="main",
        path_prefixes=["skills/", "spec/", "README.md"],
        web_base_url="https://github.com/anthropics/skills/blob/main/",
        bundle_router={
            "": "04_Customization_Skills_Hooks_And_Plugins",
        },
        root_subpath="",
        allowed_extensions=(".md",),
    ),
]

# URLs web directas y feeds de anuncios para detección temprana de cambios
DIRECT_WEB_SOURCES: List[Dict[str, str]] = [
    {
        "id": "vscode_api_contribution_points",
        "url": "https://code.visualstudio.com/api/references/contribution-points",
        "bundle": "06_Extension_AI_APIs_And_Copilot_SDK",
        "type": "html",
    },
    {
        "id": "github_changelog_copilot_rss",
        "url": "https://github.blog/changelog/label/copilot/feed/",
        "bundle": "07_Release_Notes_And_Changelog_Radar",
        "type": "rss",
    },
    {
        "id": "agent_plugins_1_0_schema",
        "url": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "bundle": "04_Customization_Skills_Hooks_And_Plugins",
        "type": "json",
    },
]

# Índice oficial de documentación de LangGraph para LLMs / RAG
LANGGRAPH_INDEX_URL = "https://raw.githubusercontent.com/langchain-ai/langgraph/main/docs/llms.txt"


# =====================================================================
# 3. MOTOR DE NORMALIZACIÓN DETERMINISTA Y HASHING SHA-256
# =====================================================================
class ContentCanonicalizer:
    """
    Transforma Markdown con sintaxis Liquid o HTML web dinámico en una
    representación textual estrictamente canónica e invariante a estilos.
    """

    # Expresión regular robusta para metadatos frontmatter (monolínea o multilínea indentada)
    RE_YAML_FIELD = re.compile(
        r"^(?P<key>title|shortTitle|intro|MetaDescription|description):\s*"
        r"(?:(?P<block>[>|][-+]?)\s*\n(?P<multiline>(?:[ \t]+.+\n?)+)|(?P<inline>.+))$",
        re.MULTILINE,
    )
    RE_AUTOTITLE_LINK = re.compile(r"\[AUTOTITLE\]\((?:https://docs\.github\.com/en)?(/[^)#\s]+)(#[^)\s]+)?\)")
    RE_HTML_ANCHOR = re.compile(r"<a\s+(?:name|id)=[\"'][^\"']*[\"']\s*>\s*</a>", re.IGNORECASE)
    RE_DETAILS_TAG = re.compile(r"</?details[^>]*>", re.IGNORECASE)
    RE_SUMMARY_TAG = re.compile(
        r"<summary>\s*(?:<strong>)?(.*?)(?:</strong>)?\s*</summary>",
        re.IGNORECASE | re.DOTALL,
    )

    RE_LIQUID_DATA = re.compile(
        r"\{%\s*data\s+variables\.([a-zA-Z0-9_.-]+)\s*%\}"
    )
    RE_CODETAB = re.compile(r"\{%\s*codetab\s+([a-zA-Z0-9_.-]+)\s*%\}")
    RE_LIQUID_GENERIC = re.compile(r"\{%.*?%\}")
    RE_VSCODE_KB = re.compile(r"kb\(([a-zA-Z0-9_.-]+)\)")
    RE_VSCODE_KBSTYLE = re.compile(r"kbstyle\(([^)]+)\)")
    RE_VSCODE_SETTING = re.compile(r"setting\(([a-zA-Z0-9_.-]+)\)")
    RE_HTML_COMMENTS = re.compile(r"<!--[\s\S]*?-->")
    RE_FRONTMATTER = re.compile(r"\A---\s*\n([\s\S]*?)\n---\s*\n")
    RE_TRAILING_SPACES = re.compile(r"[ \t]+$", re.MULTILINE)
    RE_MULTI_BLANK_LINES = re.compile(r"\n{3,}")

    @classmethod
    def _extract_frontmatter_metadata(cls, fm_content: str) -> List[str]:
        summary: List[str] = []
        for match in cls.RE_YAML_FIELD.finditer(fm_content):
            key = match.group("key")
            if match.group("multiline"):
                raw_lines = [
                    line.strip()
                    for line in match.group("multiline").splitlines()
                    if line.strip()
                ]
                val = " ".join(raw_lines)
            else:
                val = (match.group("inline") or "").strip().strip("'\"")
            if val and val not in (">-", "|", ">", "|-", ">+", "|+"):
                summary.append(f"**{key}**: {val}")
        return summary

    @staticmethod
    def _resolve_autotitle(match: re.Match) -> str:
        rel_path = match.group(1)
        anchor = match.group(2) or ""
        slug_part = rel_path.rstrip("/").split("/")[-1]
        readable_title = slug_part.replace("-", " ").title()
        full_url = f"https://docs.github.com/en{rel_path}{anchor}"
        return f"[{readable_title}]({full_url})"

    @classmethod
    def normalize_markdown(cls, raw_md: str) -> str:
        """Limpia un archivo Markdown crudo de GitHub resolviendo variables y macros."""
        text = raw_md.replace("\r\n", "\n").replace("\r", "\n")

        # 1. Extracción de Frontmatter
        frontmatter_summary = []
        fm_match = cls.RE_FRONTMATTER.search(text)
        if fm_match:
            fm_content = fm_match.group(1)
            frontmatter_summary = cls._extract_frontmatter_metadata(fm_content)
            text = text[fm_match.end():]
        if frontmatter_summary:
            text = "\n".join(frontmatter_summary) + "\n\n" + text

        # 2. Eliminación de comentarios HTML
        text = cls.RE_HTML_COMMENTS.sub("", text)

        # 3. Resolución de variables Liquid conocidas
        def _replace_liquid_var(match: re.Match) -> str:
            var_key = match.group(1).strip()
            return LIQUID_VARIABLES_MAP.get(var_key, f"[{var_key}]")

        text = cls.RE_LIQUID_DATA.sub(_replace_liquid_var, text)
        text = cls.RE_CODETAB.sub(r"\n**Language (\1):**\n", text)
        text = cls.RE_LIQUID_GENERIC.sub("", text)

        # 4. Normalización de macros VS Code
        text = cls.RE_VSCODE_KB.sub(r"`Shortcut: \1`", text)
        text = cls.RE_VSCODE_KBSTYLE.sub(r"`\1`", text)
        text = cls.RE_VSCODE_SETTING.sub(r"`\1`", text)

        # 5. Resolución de enlaces AUTOTITLE y etiquetas HTML específicas
        text = cls.RE_AUTOTITLE_LINK.sub(cls._resolve_autotitle, text)
        text = cls.RE_HTML_ANCHOR.sub("", text)
        text = cls.RE_DETAILS_TAG.sub("", text)
        text = cls.RE_SUMMARY_TAG.sub(r"\n**\1**\n", text)

        # 6. Normalización Unicode NFKC y espacios
        text = unicodedata.normalize("NFKC", text)
        text = cls.RE_TRAILING_SPACES.sub("", text)
        text = cls.RE_MULTI_BLANK_LINES.sub("\n\n", text)
        return text.strip() + "\n"

    @classmethod
    def normalize_html_to_text(cls, raw_html: str) -> str:
        """
        Extrae únicamente el contenido semántico principal de una página HTML,
        eliminando hojas de estilo, scripts, menús y widgets interactivos.
        """
        soup = BeautifulSoup(raw_html, "html.parser")

        # Aislar contenedor principal del artículo
        main_node = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", attrs={"role": "main"})
            or soup.body
            or soup
        )

        # Eliminar etiquetas ruidosas o dinámicas
        for tag in main_node.find_all(
            [
                "script",
                "style",
                "nav",
                "header",
                "footer",
                "aside",
                "noscript",
                "svg",
                "iframe",
                "button",
                "form",
            ]
        ):
            tag.decompose()

        # Eliminar comentarios del DOM
        for comment in main_node.find_all(
            string=lambda t: isinstance(t, Comment)
        ):
            comment.extract()

        # Eliminar widgets de interfaz de VS Code ("Open in VS Code", "Copy as Markdown")
        UI_NOISE_PATTERNS = {
            "Copy as Markdown",
            "Ask in VS Code",
            "Ask in VS Code Insiders",
            "Open in VS Code",
            "Open in VS Code Insiders",
            "Edit this document",
        }

        lines: List[str] = []
        for element in main_node.find_all(
            ["h1", "h2", "h3", "h4", "p", "li", "pre", "code", "table"]
        ):
            # Evitar duplicar nodos hijos ya procesados dentro de <pre> o <table>
            if element.name == "code" and element.parent.name == "pre":
                continue
            if element.find_parent("table") and element.name != "table":
                continue

            raw_txt = element.get_text(" ", strip=True)
            if not raw_txt or raw_txt in UI_NOISE_PATTERNS:
                continue

            if element.name in ("h1", "h2", "h3", "h4"):
                level = int(element.name[1])
                lines.append(f"\n{'#' * level} {raw_txt}\n")
            elif element.name == "pre":
                code_txt = element.get_text("\n", strip=True)
                lines.append(f"\n```\n{code_txt}\n```\n")
            elif element.name == "li":
                lines.append(f"- {raw_txt}")
            elif element.name == "table":
                for row in element.find_all("tr"):
                    cells = [
                        c.get_text(" ", strip=True).replace("|", "\\|")
                        for c in row.find_all(["th", "td"])
                    ]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
                lines.append("")
            else:
                lines.append(raw_txt)

        joined = "\n".join(lines)
        joined = unicodedata.normalize("NFKC", joined)
        joined = cls.RE_TRAILING_SPACES.sub("", joined)
        joined = cls.RE_MULTI_BLANK_LINES.sub("\n\n", joined)
        return joined.strip() + "\n"

    @classmethod
    def normalize_rss_feed(cls, raw_xml: str, max_items: int = 25) -> str:
        """Convierte el feed RSS del Changelog de GitHub Copilot en Markdown determinista."""
        root = ET.fromstring(raw_xml)
        channel = root.find("channel")
        if channel is None:
            return ""

        items_md: List[str] = ["# GitHub Copilot Official Changelog Feed\n"]
        for item in channel.findall("item")[:max_items]:
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub_date = (item.findtext("pubDate") or "").strip()
            desc_html = item.findtext("description") or ""
            clean_desc = cls.normalize_html_to_text(desc_html)
            items_md.append(
                f"## {title}\n- **Date**: {pub_date}\n- **URL**: {link}\n\n{clean_desc}\n"
            )

        joined = "\n".join(items_md)
        joined = unicodedata.normalize("NFKC", joined)
        return cls.RE_MULTI_BLANK_LINES.sub("\n\n", joined).strip() + "\n"

    @classmethod
    def normalize_dts(cls, raw_dts: str, file_path: str) -> str:
        """Normaliza archivos de definición TypeScript (.d.ts) de APIs propuestas de VS Code."""
        text = raw_dts.replace("\r\n", "\n").replace("\r", "\n")
        text = unicodedata.normalize("NFKC", text)
        text = cls.RE_TRAILING_SPACES.sub("", text)
        text = cls.RE_MULTI_BLANK_LINES.sub("\n\n", text).strip()
        header = f"# VS Code Proposed AI API Definition: `{file_path}`\n\n"
        return f"{header}```typescript\n{text}\n```\n"

    @classmethod
    def normalize_json_schema(cls, raw_json: str, title: str) -> str:
        """Normaliza esquemas JSON de forma determinista ordenando claves."""
        try:
            parsed = json.loads(raw_json)
            formatted = json.dumps(parsed, indent=2, sort_keys=True, ensure_ascii=False)
        except Exception:
            formatted = raw_json.strip()
        return f"# Official JSON Schema: {title}\n\n```json\n{formatted}\n```\n"

    @staticmethod
    def compute_sha256(clean_text: str) -> str:
        """Calcula el hash criptográfico SHA-256 sobre el texto canónico en UTF-8."""
        return hashlib.sha256(clean_text.encode("utf-8")).hexdigest()


# =====================================================================
# 4. GESTOR DE ESTADO, SINCRONIZACIÓN DIFERENCIAL Y EMPAQUETADO RAG
# =====================================================================
@dataclass
class DocumentRecord:
    doc_id: str
    source_url: str
    canonical_web_url: str
    bundle_name: str
    git_blob_sha: Optional[str]
    content_sha256: str
    word_count: int
    last_updated_utc: str
    local_clean_path: str

    @property
    def Canonical_web_url(self) -> str:
        """Propiedad de compatibilidad con versiones previas."""
        return self.canonical_web_url


class CopilotDocumentationSynchronizer:
    def __init__(
        self,
        base_dir: Path,
        github_token: Optional[str] = None,
        max_workers: int = 8,
    ):
        self.base_dir = Path(base_dir)
        self.clean_cache_dir = self.base_dir / "clean_sources"
        self.bundles_dir = self.base_dir / "notebooklm_bundles"
        self.diffs_dir = self.base_dir / "changelog_diffs"
        self.manifest_path = self.base_dir / "state_manifest.json"
        self.max_workers = max(1, max_workers)

        for d in (self.clean_cache_dir, self.bundles_dir, self.diffs_dir):
            d.mkdir(parents=True, exist_ok=True)

        self.session = requests.Session()
        headers = {
            "User-Agent": "VSCode-Copilot-Deterministic-RAG-Sync/2.1",
            "Accept": "application/vnd.github+json",
        }
        if github_token:
            headers["Authorization"] = f"Bearer {github_token}"
        self.session.headers.update(headers)

        self.manifest: Dict[str, DocumentRecord] = self._load_manifest()
        self.dirty_bundles: Set[str] = set()
        self.change_reports: List[str] = []
        self.modified_records: List[Dict[str, str]] = []
        self.manifest_dirty: bool = False

    def _load_manifest(self) -> Dict[str, DocumentRecord]:
        if not self.manifest_path.exists():
            return {}
        try:
            raw = json.loads(self.manifest_path.read_text(encoding="utf-8"))
            records = {}
            for k, v in raw.get("documents", {}).items():
                # Compatibilidad: mapear 'Canonical_web_url' (mayúscula) a 'canonical_web_url'
                if "Canonical_web_url" in v and "canonical_web_url" not in v:
                    v["canonical_web_url"] = v.pop("Canonical_web_url")

                # Migración de ruta: corregir posibles nombres previos terminados en .md.md
                local_path_str = v.get("local_clean_path", "")
                if local_path_str.endswith(".md.md"):
                    old_path = self.base_dir / local_path_str
                    new_path_str = local_path_str[:-3]  # quitar el último .md
                    new_path = self.base_dir / new_path_str
                    if old_path.exists() and not new_path.exists():
                        try:
                            old_path.rename(new_path)
                            logger.info("Ruta migrada: %s -> %s", old_path.name, new_path.name)
                        except Exception as e:
                            logger.debug("No se pudo renombrar archivo previo: %s", e)
                    v["local_clean_path"] = new_path_str

                records[k] = DocumentRecord(**v)
            return records
        except Exception as exc:
            logger.warning("Manifiesto previo inválido, iniciando limpio: %s", exc)
            return {}

    def _save_manifest(self) -> bool:
        payload = {
            "schema_version": "2.1",
            "last_sync_utc": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(self.manifest),
            "documents": {
                k: asdict(v) for k, v in sorted(self.manifest.items())
            },
        }
        self.manifest_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        self.manifest_dirty = False
        return True

    def _resolve_bundle(self, path: str, router: Dict[str, str]) -> str:
        # Ordenar prefijos de mayor a menor especificidad
        for prefix in sorted(router.keys(), key=len, reverse=True):
            if path.startswith(prefix):
                return router[prefix]
        return "05_Workflows_Planning_And_Remote_AHP"

    def _build_canonical_web_url(self, rule: RepoTreeRule, file_path: str) -> str:
        if (
            file_path.startswith(".github/")
            or file_path.endswith(".d.ts")
            or file_path.endswith(".json")
            or rule.web_base_url.startswith("https://github.com/")
        ):
            return f"https://github.com/{rule.owner}/{rule.repo}/blob/{rule.branch}/{file_path}"
        clean_path = re.sub(r"\.md$", "", file_path)
        if rule.owner == "github" and clean_path.startswith("content/"):
            clean_path = clean_path[len("content/"):]
        if clean_path.endswith("/index"):
            clean_path = clean_path[: -len("/index")]
        if rule.repo == "vscode-docs" and clean_path.startswith("release-notes/"):
            clean_path = "updates/" + clean_path[len("release-notes/"):]
        return urljoin(rule.web_base_url, clean_path)

    def _get_safe_clean_filename(self, doc_id: str) -> str:
        """
        Genera un nombre de archivo seguro y único evitando la duplicación de extensiones (.md.md).
        """
        clean_id = re.sub(r"\.md$", "", doc_id)
        return f"{re.sub(r'[^a-zA-Z0-9_.-]', '_', clean_id)}.md"

    def _delete_document(self, doc_id: str, record: DocumentRecord) -> None:
        """Elimina un documento obsoleto que ya no existe en el repositorio upstream."""
        abs_clean_path = self.base_dir / record.local_clean_path
        if abs_clean_path.exists():
            try:
                abs_clean_path.unlink()
            except Exception as e:
                logger.warning("No se pudo eliminar archivo local %s: %s", abs_clean_path, e)

        self.dirty_bundles.add(record.bundle_name)
        self.manifest_dirty = True
        self.change_reports.append(
            f"### [DOCUMENTO ELIMINADO UPSTREAM] `{doc_id}`\n"
            f"- **URL Canónica previa**: {record.canonical_web_url}\n"
            f"- **Último Hash**: `{record.content_sha256}`\n"
        )
        self.modified_records.append({
            "action": "DELETED",
            "doc_id": doc_id,
            "web_url": record.canonical_web_url,
            "diff_preview": "Documento eliminado en upstream.",
        })
        del self.manifest[doc_id]

    def sync_github_repositories(
        self, force_recheck: bool = False
    ) -> Tuple[int, int, int, int]:
        """
        Consulta los árboles Git de microsoft/vscode-docs y github/docs,
        descarga cambios de forma concurrente, elimina documentos obsoletos y
        detecta notas de lanzamiento (release-notes/v1_*.md).
        Retorna (agregados, actualizados, omitidos_sin_cambios, eliminados).
        """
        added, updated, skipped, deleted = 0, 0, 0, 0

        for rule in REPO_RULES:
            if rule.tree_subpath:
                subpath = rule.tree_subpath.strip("/")
                tree_url = f"https://api.github.com/repos/{rule.owner}/{rule.repo}/git/trees/{rule.branch}:{subpath}?recursive=1"
                logger.info("Consultando subárbol Git de %s/%s (%s)...", rule.owner, rule.repo, subpath)
            else:
                subpath = ""
                tree_url = f"https://api.github.com/repos/{rule.owner}/{rule.repo}/git/trees/{rule.branch}?recursive=1"
                logger.info("Consultando árbol Git de %s/%s...", rule.owner, rule.repo)
            try:
                resp = self.session.get(tree_url, timeout=30)
                if resp.status_code in (403, 429):
                    remaining = resp.headers.get("X-RateLimit-Remaining")
                    reset_ts = resp.headers.get("X-RateLimit-Reset")
                    reset_str = (
                        datetime.fromtimestamp(int(reset_ts), timezone.utc).isoformat()
                        if reset_ts
                        else "desconocido"
                    )
                    logger.error(
                        "Límite de tasa de la API de GitHub alcanzado (Remaining: %s). Se reinicia en: %s. "
                        "Recomendación: Configura la variable de entorno GITHUB_TOKEN para 5,000 req/hora.",
                        remaining,
                        reset_str,
                    )
                resp.raise_for_status()
                tree_resp_json = resp.json()
                if tree_resp_json.get("truncated"):
                    logger.warning("El árbol Git devuelto para %s/%s está truncado por superar el límite de GitHub.", rule.owner, rule.repo)
                tree_data = tree_resp_json.get("tree", [])
            except Exception as exc:
                logger.error("Error al obtener árbol Git de %s/%s: %s", rule.owner, rule.repo, exc)
                continue

            if subpath:
                for node in tree_data:
                    node["path"] = f"{subpath}/{node['path']}"

            # Seleccionar archivos relevantes según prefijos
            matched_nodes = []
            release_note_nodes = []

            for node in tree_data:
                if node.get("type") != "blob":
                    continue
                path: str = node.get("path", "")
                ext_match = any(path.endswith(ext) for ext in rule.allowed_extensions)
                if not ext_match:
                    continue

                if rule.file_regex_filter:
                    if not re.search(rule.file_regex_filter, path):
                        continue

                if any(path.startswith(p) for p in rule.path_prefixes):
                    matched_nodes.append(node)
                elif rule.repo == "vscode-docs" and re.match(
                    r"^release-notes/v1_\d+\.md$", path
                ):
                    release_note_nodes.append(node)

            # Tomar las 3 versiones más recientes de release-notes de VS Code
            if release_note_nodes:
                release_note_nodes.sort(
                    key=lambda n: int(re.search(r"v1_(\d+)", n["path"]).group(1)),
                    reverse=True,
                )
                matched_nodes.extend(release_note_nodes[:3])

            current_rule_doc_ids: Set[str] = set()
            nodes_to_fetch = []

            for node in matched_nodes:
                path = node["path"]
                git_sha = node["sha"]
                doc_id = f"{rule.owner}_{rule.repo}::{path}"
                current_rule_doc_ids.add(doc_id)

                bundle = (
                    "07_Release_Notes_And_Changelog_Radar"
                    if path.startswith("release-notes/")
                    else self._resolve_bundle(path, rule.bundle_router)
                )

                existing = self.manifest.get(doc_id)

                # Optimización O(1): Si el Git Blob SHA es idéntico, omitir sin descargar
                if (
                    existing
                    and not force_recheck
                    and existing.git_blob_sha == git_sha
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    skipped += 1
                    continue

                nodes_to_fetch.append((node, doc_id, bundle, existing))

            # Descarga y procesamiento concurrente para los nodos modificados o nuevos
            if nodes_to_fetch:
                logger.info(
                    "Descargando %d archivos de %s/%s con %d hilos...",
                    len(nodes_to_fetch),
                    rule.owner,
                    rule.repo,
                    self.max_workers,
                )

                def _fetch_node(item):
                    node_item, doc_id_item, bundle_item, existing_item = item
                    path_item = node_item["path"]
                    raw_url = f"https://raw.githubusercontent.com/{rule.owner}/{rule.repo}/{rule.branch}/{path_item}"
                    raw_resp = self.session.get(raw_url, timeout=30)
                    raw_resp.raise_for_status()
                    if path_item.endswith(".d.ts"):
                        clean_text = ContentCanonicalizer.normalize_dts(raw_resp.text, path_item)
                    elif path_item.endswith(".json"):
                        clean_text = ContentCanonicalizer.normalize_json_schema(raw_resp.text, path_item)
                    else:
                        clean_text = ContentCanonicalizer.normalize_markdown(raw_resp.text)
                    new_sha = ContentCanonicalizer.compute_sha256(clean_text)
                    return item, raw_url, clean_text, new_sha

                with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = [executor.submit(_fetch_node, item) for item in nodes_to_fetch]
                    for fut in concurrent.futures.as_completed(futures):
                        try:
                            item, raw_url, clean_text, new_sha256 = fut.result()
                            node_item, doc_id_item, bundle_item, existing_item = item
                            git_sha_item = node_item["sha"]
                            path_item = node_item["path"]

                            if (
                                existing_item
                                and existing_item.content_sha256 == new_sha256
                                and (self.base_dir / existing_item.local_clean_path).exists()
                            ):
                                if existing_item.git_blob_sha != git_sha_item:
                                    existing_item.git_blob_sha = git_sha_item
                                    self.manifest_dirty = True
                                skipped += 1
                                continue

                            web_url = self._build_canonical_web_url(rule, path_item)
                            was_added = existing_item is None
                            self._persist_document_change(
                                doc_id=doc_id_item,
                                source_url=raw_url,
                                web_url=web_url,
                                bundle_name=bundle_item,
                                git_blob_sha=git_sha_item,
                                new_sha256=new_sha256,
                                clean_text=clean_text,
                                existing=existing_item,
                            )
                            if was_added:
                                added += 1
                            else:
                                updated += 1
                        except Exception as exc:
                            logger.error("Error al procesar nodo: %s", exc)

            # Detección de documentos eliminados en upstream
            rule_prefix = f"{rule.owner}_{rule.repo}::"
            for doc_id, record in list(self.manifest.items()):
                if doc_id.startswith(rule_prefix) and doc_id not in current_rule_doc_ids:
                    logger.info("ELIMINADO UPSTREAM: %s", doc_id)
                    self._delete_document(doc_id, record)
                    deleted += 1

        return added, updated, skipped, deleted

    def sync_direct_web_sources(
        self, force_recheck: bool = False
    ) -> Tuple[int, int, int]:
        """Sincroniza páginas HTML directas y feeds RSS aplicando limpieza DOM/XML."""
        added, updated, skipped = 0, 0, 0

        for src in DIRECT_WEB_SOURCES:
            doc_id = f"web::{src['id']}"
            url = src["url"]
            bundle = src["bundle"]
            src_type = src["type"]

            logger.info("Verificando fuente web directa: %s", url)
            try:
                resp = self.session.get(url, timeout=30)
                resp.raise_for_status()

                if src_type == "rss":
                    clean_text = ContentCanonicalizer.normalize_rss_feed(resp.text)
                elif src_type == "json":
                    clean_text = ContentCanonicalizer.normalize_json_schema(resp.text, src["id"])
                else:
                    clean_text = ContentCanonicalizer.normalize_html_to_text(resp.text)

                new_sha256 = ContentCanonicalizer.compute_sha256(clean_text)
                existing = self.manifest.get(doc_id)

                if (
                    existing
                    and existing.content_sha256 == new_sha256
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    skipped += 1
                    continue

                was_added = existing is None
                self._persist_document_change(
                    doc_id=doc_id,
                    source_url=url,
                    web_url=url,
                    bundle_name=bundle,
                    git_blob_sha=None,
                    new_sha256=new_sha256,
                    clean_text=clean_text,
                    existing=existing,
                )
                if was_added:
                    added += 1
                else:
                    updated += 1
            except Exception as exc:
                logger.error("Error al sincronizar fuente web %s: %s", url, exc)

        return added, updated, skipped

    def sync_langgraph_documentation(
        self, force_recheck: bool = False
    ) -> Tuple[int, int, int, int]:
        """
        Sincroniza la documentación oficial de LangGraph desde su índice llms.txt en Markdown directo,
        agrupándola de forma aislada en el compendio 08_Agent_Workflows_LangGraph_And_Ecosystem.
        Retorna (agregados, actualizados, omitidos_sin_cambios, eliminados).
        """
        added, updated, skipped, deleted = 0, 0, 0, 0
        logger.info("Consultando índice oficial de documentación de LangGraph (%s)...", LANGGRAPH_INDEX_URL)

        try:
            resp = self.session.get(LANGGRAPH_INDEX_URL, timeout=20)
            resp.raise_for_status()
            raw_index = resp.text
        except Exception as exc:
            logger.error("Error al obtener índice de LangGraph: %s", exc)
            return added, updated, skipped, deleted

        doc_links: List[Tuple[str, str, str]] = []
        pattern = re.compile(r"-\s*\[(.*?)\]\((https?://docs\.langchain\.com/oss/python/langgraph/(.*?\.md))\)")
        for line in raw_index.splitlines():
            m = pattern.search(line)
            if m:
                title, url, rel_slug = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
                doc_links.append((title, url, rel_slug))

        if not doc_links:
            logger.warning("No se encontraron enlaces de documentación válidos en llms.txt de LangGraph.")
            return added, updated, skipped, deleted

        logger.info("Detectados %d documentos oficiales de LangGraph para sincronización.", len(doc_links))

        current_langgraph_ids: Set[str] = set()
        items_to_process = []

        for title, url, rel_slug in doc_links:
            clean_slug = rel_slug.replace("/", "_").replace(".md", "")
            doc_id = f"langgraph::{clean_slug}"
            current_langgraph_ids.add(doc_id)
            bundle = "08_Agent_Workflows_LangGraph_And_Ecosystem"
            existing = self.manifest.get(doc_id)
            items_to_process.append((doc_id, title, url, bundle, existing))

        def _fetch_lg_doc(item):
            d_id, t_title, d_url, b_name, exist_rec = item
            raw_resp = self.session.get(d_url, timeout=25)
            raw_resp.raise_for_status()
            clean_text = ContentCanonicalizer.normalize_markdown(raw_resp.text)
            new_sha = ContentCanonicalizer.compute_sha256(clean_text)
            return item, clean_text, new_sha

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(_fetch_lg_doc, it) for it in items_to_process]
            for fut in concurrent.futures.as_completed(futures):
                try:
                    item, clean_text, new_sha256 = fut.result()
                    d_id, t_title, d_url, b_name, exist_rec = item

                    if (
                        exist_rec
                        and not force_recheck
                        and exist_rec.content_sha256 == new_sha256
                        and (self.base_dir / exist_rec.local_clean_path).exists()
                    ):
                        skipped += 1
                        continue

                    was_added = exist_rec is None
                    self._persist_document_change(
                        doc_id=d_id,
                        source_url=d_url,
                        web_url=d_url.replace(".md", ""),
                        bundle_name=b_name,
                        git_blob_sha=None,
                        new_sha256=new_sha256,
                        clean_text=clean_text,
                        existing=exist_rec,
                    )
                    if was_added:
                        added += 1
                    else:
                        updated += 1
                except Exception as exc:
                    logger.error("Error al procesar documento de LangGraph: %s", exc)

        # Detección de documentos eliminados de LangGraph
        lg_prefix = "langgraph::"
        for doc_id, record in list(self.manifest.items()):
            if doc_id.startswith(lg_prefix) and doc_id not in current_langgraph_ids:
                logger.info("ELIMINADO UPSTREAM LANGGRAPH: %s", doc_id)
                self._delete_document(doc_id, record)
                deleted += 1

        return added, updated, skipped, deleted

    def _persist_document_change(
        self,
        doc_id: str,
        source_url: str,
        web_url: str,
        bundle_name: str,
        git_blob_sha: Optional[str],
        new_sha256: str,
        clean_text: str,
        existing: Optional[DocumentRecord],
    ) -> None:
        safe_filename = self._get_safe_clean_filename(doc_id)
        rel_clean_path = Path("clean_sources") / safe_filename
        abs_clean_path = self.base_dir / rel_clean_path

        # Si el archivo ya existía, generar diff semántico exacto
        if existing and abs_clean_path.exists():
            old_text = abs_clean_path.read_text(encoding="utf-8")
            diff_lines = list(
                difflib.unified_diff(
                    old_text.splitlines(),
                    clean_text.splitlines(),
                    fromfile=f"{doc_id} (prev: {existing.content_sha256[:8]})",
                    tofile=f"{doc_id} (new: {new_sha256[:8]})",
                    lineterm="",
                )
            )
            diff_snippet = "\n".join(diff_lines[:120]) if diff_lines else ""
            if diff_lines:
                self.change_reports.append(
                    f"### [MODIFICADO] `{doc_id}`\n"
                    f"- **URL Canónica**: {web_url}\n"
                    f"- **Hash Anterior**: `{existing.content_sha256}`\n"
                    f"- **Hash Nuevo**: `{new_sha256}`\n\n"
                    f"```diff\n{diff_snippet}\n```\n"
                )
            self.modified_records.append({
                "action": "MODIFIED",
                "doc_id": doc_id,
                "web_url": web_url,
                "diff_preview": diff_snippet if diff_lines else "Sin preview de diff.",
            })
            logger.info("ACTUALIZADO: %s (Hash: %s)", doc_id, new_sha256[:10])
        else:
            self.change_reports.append(
                f"### [NUEVO RECURSO] `{doc_id}`\n"
                f"- **URL Canónica**: {web_url}\n"
                f"- **Hash Inicial**: `{new_sha256}`\n"
            )
            self.modified_records.append({
                "action": "ADDED",
                "doc_id": doc_id,
                "web_url": web_url,
                "diff_preview": f"Nuevo recurso detectado con {len(clean_text.split())} palabras.",
            })
            logger.info("NUEVO: %s (Hash: %s)", doc_id, new_sha256[:10])

        abs_clean_path.write_text(clean_text, encoding="utf-8")
        word_count = len(clean_text.split())

        self.manifest[doc_id] = DocumentRecord(
            doc_id=doc_id,
            source_url=source_url,
            canonical_web_url=web_url,
            bundle_name=bundle_name,
            git_blob_sha=git_blob_sha,
            content_sha256=new_sha256,
            word_count=word_count,
            last_updated_utc=datetime.now(timezone.utc).isoformat(),
            local_clean_path=str(rel_clean_path).replace("\\", "/"),
        )
        self.dirty_bundles.add(bundle_name)
        self.manifest_dirty = True

    def build_notebooklm_bundles(self, rebuild_all: bool = False) -> List[Path]:
        """
        Empaqueta los documentos limpios en Compendios Maestros (.md) optimizados
        para Google NotebookLM, verificando el límite de 500,000 palabras por archivo.
        """
        MAX_WORDS_PER_BUNDLE = 450_000
        bundles_map: Dict[str, List[DocumentRecord]] = {}

        for record in self.manifest.values():
            # Filtro de documentos stub o sin sustancia técnica (< 25 palabras)
            if record.word_count < 25:
                continue
            bundles_map.setdefault(record.bundle_name, []).append(record)

        generated_files: List[Path] = []
        target_bundles = (
            set(bundles_map.keys()) if rebuild_all else self.dirty_bundles
        )

        for bundle_name in sorted(target_bundles):
            records = sorted(
                bundles_map.get(bundle_name, []), key=lambda r: r.doc_id
            )
            if not records:
                continue

            part_idx = 1
            current_words = 0
            current_chunks: List[str] = []

            for rec in records:
                abs_path = self.base_dir / rec.local_clean_path
                if not abs_path.exists():
                    continue
                body = abs_path.read_text(encoding="utf-8")

                doc_header = (
                    f"\n\n---\n"
                    f"# DOCUMENT_SOURCE: {rec.doc_id}\n"
                    f"- **CANONICAL_URL**: {rec.canonical_web_url}\n"
                    f"- **RAW_SOURCE_URL**: {rec.source_url}\n"
                    f"- **SHA256_FINGERPRINT**: `{rec.content_sha256}`\n"
                    f"- **LAST_VERIFIED_UTC**: {rec.last_updated_utc}\n"
                    f"---\n\n"
                )
                full_entry = doc_header + body
                entry_words = rec.word_count + 35

                if current_words + entry_words > MAX_WORDS_PER_BUNDLE and current_chunks:
                    out_path = self._write_bundle_file(
                        bundle_name, part_idx, current_chunks, current_words
                    )
                    generated_files.append(out_path)
                    part_idx += 1
                    current_chunks = []
                    current_words = 0

                current_chunks.append(full_entry)
                current_words += entry_words

            if current_chunks:
                out_path = self._write_bundle_file(
                    bundle_name, part_idx, current_chunks, current_words
                )
                generated_files.append(out_path)

        return generated_files

    def _write_bundle_file(
        self, bundle_name: str, part_idx: int, chunks: List[str], total_words: int
    ) -> Path:
        suffix = f"_part{part_idx}" if part_idx > 1 else ""
        out_path = self.bundles_dir / f"{bundle_name}{suffix}.md"
        master_header = (
            f"# COMPENDIO RAG NOTEBOOKLM: {bundle_name}{suffix}\n"
            f"- **Generado (UTC)**: {datetime.now(timezone.utc).isoformat()}\n"
            f"- **Total Palabras**: {total_words:,} / 500,000 máx.\n"
            f"- **Instrucción de Citación para NotebookLM**: Al responder consultas técnicas, "
            f"citar siempre el identificador `DOCUMENT_SOURCE` y la `CANONICAL_URL` "
            f"declarados en el encabezado de cada sección.\n"
        )
        out_path.write_text(master_header + "".join(chunks), encoding="utf-8")
        logger.info(
            "Compendio generado: %s (%d palabras)", out_path.name, total_words
        )
        return out_path

    def write_audit_report(
        self, added: int, updated: int, skipped: int, deleted: int = 0
    ) -> Optional[Path]:
        if not self.change_reports:
            logger.info("Sin cambios semánticos detectados. Todos los hashes coinciden.")
            return None

        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report_path = self.diffs_dir / f"diff_report_{ts}.md"
        header = (
            f"# Reporte de Novedades Documentales VS Code Copilot ({ts} UTC)\n\n"
            f"- **Nuevos Documentos**: {added}\n"
            f"- **Documentos Actualizados**: {updated}\n"
            f"- **Documentos Sin Cambios (Omitidos por Hash)**: {skipped}\n"
            f"- **Documentos Eliminados**: {deleted}\n"
            f"- **Compendios de NotebookLM Recompilados**: {', '.join(sorted(self.dirty_bundles))}\n\n"
        )
        report_path.write_text(
            header + "\n".join(self.change_reports), encoding="utf-8"
        )
        logger.info("Reporte de diferencias guardado en: %s", report_path)
        return report_path

    def export_dirty_bundles_metadata(self, generated_files: List[Path]) -> Path:
        """Exporta metadatos JSON de los compendios modificados para automatizaciones externas como NotebookLM."""
        metadata_path = self.base_dir / "dirty_bundles.json"
        payload = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "has_changes": len(generated_files) > 0,
            "dirty_bundles_count": len(generated_files),
            "dirty_bundles": [str(p.resolve()).replace("\\", "/") for p in generated_files],
            "modified_records_count": len(self.modified_records),
        }
        metadata_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        logger.info("Metadatos de compendios modificados exportados en: %s", metadata_path)
        return metadata_path

    def verify_integrity(self) -> bool:
        """Verifica la integridad de los hashes almacenados contra los archivos locales."""
        logger.info("Verificando integridad local de %d registros...", len(self.manifest))
        mismatches = 0
        missing = 0
        for doc_id, rec in self.manifest.items():
            abs_path = self.base_dir / rec.local_clean_path
            if not abs_path.exists():
                logger.error("Archivo faltante para %s: %s", doc_id, abs_path)
                missing += 1
                continue
            content = abs_path.read_text(encoding="utf-8")
            current_hash = ContentCanonicalizer.compute_sha256(content)
            if current_hash != rec.content_sha256:
                logger.error(
                    "Discrepancia de hash en %s: manifiesto=%s, disco=%s",
                    doc_id,
                    rec.content_sha256[:10],
                    current_hash[:10],
                )
                mismatches += 1

        if missing == 0 and mismatches == 0:
            logger.info("Integridad 100% verificada. Todos los hashes y archivos coinciden.")
            return True
        else:
            logger.error("Verificación fallida: %d faltantes, %d discrepancias.", missing, mismatches)
            return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincronizador Determinista de Documentación de VS Code Copilot para NotebookLM"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./copilot_rag_workspace"),
        help="Directorio raíz para manifiesto, caché limpio y compendios.",
    )
    parser.add_argument(
        "--drive",
        action="store_true",
        help="Sincronizar directamente con Google Drive (G:\\My Drive\\NotebookLM_Copilot_Docs).",
    )
    parser.add_argument(
        "--force-recheck",
        action="store_true",
        help="Ignorar caché de hashes y recalcular todas las fuentes.",
    )
    parser.add_argument(
        "--rebuild-all-bundles",
        action="store_true",
        help="Regenerar todos los compendios de NotebookLM aunque no haya cambios.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Número de hilos concurrentes para descarga de documentos.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verificar integridad de hashes y archivos locales sin hacer llamadas remotas.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Activar registro detallado (DEBUG).",
    )
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    output_dir = (
        Path(r"G:\My Drive\NotebookLM_Copilot_Docs") if args.drive else args.output_dir
    )

    github_token = os.environ.get("GITHUB_TOKEN")
    syncer = CopilotDocumentationSynchronizer(
        base_dir=output_dir,
        github_token=github_token,
        max_workers=args.workers,
    )

    if args.verify:
        success = syncer.verify_integrity()
        return 0 if success else 1

    g_add, g_upd, g_skip, g_del = syncer.sync_github_repositories(
        force_recheck=args.force_recheck
    )
    w_add, w_upd, w_skip = syncer.sync_direct_web_sources(
        force_recheck=args.force_recheck
    )
    l_add, l_upd, l_skip, l_del = syncer.sync_langgraph_documentation(
        force_recheck=args.force_recheck
    )

    total_add = g_add + w_add + l_add
    total_upd = g_upd + w_upd + l_upd
    total_skip = g_skip + w_skip + l_skip
    total_del = g_del + l_del

    generated_bundles: List[Path] = []
    # Guardar manifiesto ÚNICAMENTE si hubo modificaciones de contenido o de hashes git
    if total_add > 0 or total_upd > 0 or total_del > 0 or syncer.manifest_dirty or args.rebuild_all_bundles:
        generated_bundles = syncer.build_notebooklm_bundles(rebuild_all=args.rebuild_all_bundles)
        syncer._save_manifest()
        syncer.write_audit_report(total_add, total_upd, total_skip, total_del)
    else:
        logger.info("Sin cambios detectados. No se modifica state_manifest.json ni se recompilan bundles.")

    syncer.export_dirty_bundles_metadata(generated_bundles)

    if syncer.modified_records:
        try:
            from scripts.webhook_notifier import WebhookNotifier
        except ImportError:
            try:
                from webhook_notifier import WebhookNotifier
            except ImportError:
                WebhookNotifier = None

        if WebhookNotifier:
            try:
                notifier = WebhookNotifier()
                notifier.notify_changes(
                    added=total_add,
                    updated=total_upd,
                    removed=total_del,
                    skipped=total_skip,
                    dirty_bundles=list(syncer.dirty_bundles),
                    modified_records=syncer.modified_records,
                )
            except Exception as ex:
                logger.warning("No se pudo enviar notificación de webhook: %s", ex)

    logger.info(
        "Resumen Final -> Nuevos: %d | Actualizados: %d | Sin Cambios (Hash Match): %d | Eliminados: %d",
        total_add,
        total_upd,
        total_skip,
        total_del,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
