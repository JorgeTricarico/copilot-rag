#!/usr/bin/env python3
"""
Sistema Determinista de Monitoreo Documental y Empaquetado RAG para VS Code Copilot.
Extrae, normaliza, calcula hashes SHA-256 sobre contenido semántico limpio, detecta
modificaciones reales sin falsos positivos y construye compendios para Google NotebookLM.
"""

from __future__ import annotations

import argparse
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
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment

# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("CopilotDocsSync")


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
]


# =====================================================================
# 3. MOTOR DE NORMALIZACIÓN DETERMINISTA Y HASHING SHA-256
# =====================================================================
class ContentCanonicalizer:
    """
    Transforma Markdown con sintaxis Liquid o HTML web dinámico en una
    representación textual estrictamente canónica e invariante a estilos.
    """

    # Expresiones regulares precompiladas para máxima velocidad y determinismo
    RE_LIQUID_DATA = re.compile(
        r"\{%\s*data\s+variables\.([a-zA-Z0-9_.-]+)\s*%\}"
    )
    RE_LIQUID_GENERIC = re.compile(r"\{%.*?%\}")
    RE_VSCODE_KB = re.compile(r"kb\(([a-zA-Z0-9_.-]+)\)")
    RE_VSCODE_KBSTYLE = re.compile(r"kbstyle\(([^)]+)\)")
    RE_VSCODE_SETTING = re.compile(r"setting\(([a-zA-Z0-9_.-]+)\)")
    RE_HTML_COMMENTS = re.compile(r"<!--[\s\S]*?-->")
    RE_FRONTMATTER = re.compile(r"\A---\s*\n([\s\S]*?)\n---\s*\n")
    RE_TRAILING_SPACES = re.compile(r"[ \t]+$", re.MULTILINE)
    RE_MULTI_BLANK_LINES = re.compile(r"\n{3,}")

    @classmethod
    def normalize_markdown(cls, raw_md: str) -> str:
        """Limpia un archivo Markdown crudo de GitHub resolviendo variables y macros."""
        text = raw_md.replace("\r\n", "\n").replace("\r", "\n")

        # 1. Extraer metadatos relevantes del frontmatter YAML (title, description)
        # ignorando campos volátiles de auditoría interna.
        frontmatter_summary = []
        fm_match = cls.RE_FRONTMATTER.search(text)
        if fm_match:
            fm_content = fm_match.group(1)
            for key in ("title", "shortTitle", "intro", "MetaDescription"):
                m = re.search(rf"^{key}:\s*(.+)$", fm_content, re.MULTILINE)
                if m:
                    val = m.group(1).strip().strip("'\"")
                    frontmatter_summary.append(f"**{key}**: {val}")
            text = text[fm_match.end():]

        if frontmatter_summary:
            text = "\n".join(frontmatter_summary) + "\n\n" + text

        # 2. Eliminar comentarios HTML
        text = cls.RE_HTML_COMMENTS.sub("", text)

        # 3. Resolver variables Liquid conocidas de manera determinista
        def _replace_liquid_var(match: re.Match) -> str:
            var_key = match.group(1).strip()
            return LIQUID_VARIABLES_MAP.get(var_key, f"[{var_key}]")

        text = cls.RE_LIQUID_DATA.sub(_replace_liquid_var, text)
        text = cls.RE_LIQUID_GENERIC.sub("", text)

        # 4. Normalizar macros propios de microsoft/vscode-docs
        text = cls.RE_VSCODE_KB.sub(r"`Shortcut: \1`", text)
        text = cls.RE_VSCODE_KBSTYLE.sub(r"`\1`", text)
        text = cls.RE_VSCODE_SETTING.sub(r"`\1`", text)

        # 5. Normalización Unicode NFKC y limpieza de espacios en blanco
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
    Canonical_web_url: str
    bundle_name: str
    git_blob_sha: Optional[str]
    content_sha256: str
    word_count: int
    last_updated_utc: str
    local_clean_path: str


class CopilotDocumentationSynchronizer:
    def __init__(self, base_dir: Path, github_token: Optional[str] = None):
        self.base_dir = base_dir
        self.clean_cache_dir = base_dir / "clean_sources"
        self.bundles_dir = base_dir / "notebooklm_bundles"
        self.diffs_dir = base_dir / "changelog_diffs"
        self.manifest_path = base_dir / "state_manifest.json"

        for d in (self.clean_cache_dir, self.bundles_dir, self.diffs_dir):
            d.mkdir(parents=True, exist_ok=True)

        self.session = requests.Session()
        headers = {
            "User-Agent": "VSCode-Copilot-Deterministic-RAG-Sync/2.0",
            "Accept": "application/vnd.github+json",
        }
        if github_token:
            headers["Authorization"] = f"Bearer {github_token}"
        self.session.headers.update(headers)

        self.manifest: Dict[str, DocumentRecord] = self._load_manifest()
        self.dirty_bundles: set[str] = set()
        self.change_reports: List[str] = []

    def _load_manifest(self) -> Dict[str, DocumentRecord]:
        if not self.manifest_path.exists():
            return {}
        try:
            raw = json.loads(self.manifest_path.read_text(encoding="utf-8"))
            return {
                k: DocumentRecord(**v) for k, v in raw.get("documents", {}).items()
            }
        except Exception as exc:
            logger.warning("Manifiesto previo inválido, iniciando limpio: %s", exc)
            return {}

    def _save_manifest(self) -> None:
        payload = {
            "schema_version": "2.0",
            "last_sync_utc": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(self.manifest),
            "documents": {k: asdict(v) for k, v in sorted(self.manifest.items())},
        }
        self.manifest_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def _resolve_bundle(self, path: str, router: Dict[str, str]) -> str:
        # Ordenar prefijos de mayor a menor especificidad
        for prefix in sorted(router.keys(), key=len, reverse=True):
            if path.startswith(prefix):
                return router[prefix]
        return "05_Workflows_Planning_And_Remote_AHP"

    def _build_canonical_web_url(self, rule: RepoTreeRule, file_path: str) -> str:
        if file_path.startswith(".github/"):
            return f"https://github.com/{rule.owner}/{rule.repo}/blob/{rule.branch}/{file_path}"
        clean_path = re.sub(r"\.md$", "", file_path)
        if rule.owner == "github" and clean_path.startswith("content/"):
            clean_path = clean_path[len("content/"):]
        if clean_path.endswith("/index"):
            clean_path = clean_path[: -len("/index")]
        return urljoin(rule.web_base_url, clean_path)

    def sync_github_repositories(self, force_recheck: bool = False) -> Tuple[int, int, int]:
        """
        Consulta los árboles Git de microsoft/vscode-docs y github/docs,
        incluyendo las últimas notas de lanzamiento (release-notes/v1_*.md).
        """
        added, updated, skipped = 0, 0, 0

        for rule in REPO_RULES:
            tree_url = f"https://api.github.com/repos/{rule.owner}/{rule.repo}/git/trees/{rule.branch}?recursive=1"
            logger.info("Consultando árbol Git de %s/%s...", rule.owner, rule.repo)
            resp = self.session.get(tree_url, timeout=30)
            resp.raise_for_status()
            tree_data = resp.json().get("tree", [])

            # Seleccionar archivos relevantes según prefijos
            matched_nodes = []
            release_note_nodes = []

            for node in tree_data:
                if node.get("type") != "blob":
                    continue
                path: str = node.get("path", "")
                if not path.endswith(".md"):
                    continue

                if any(path.startswith(p) for p in rule.path_prefixes):
                    matched_nodes.append(node)
                elif rule.repo == "vscode-docs" and re.match(r"^release-notes/v1_\d+\.md$", path):
                    release_note_nodes.append(node)

            # Tomar las 3 versiones más recientes de release-notes de VS Code
            if release_note_nodes:
                release_note_nodes.sort(
                    key=lambda n: int(re.search(r"v1_(\d+)", n["path"]).group(1)),
                    reverse=True,
                )
                matched_nodes.extend(release_note_nodes[:3])

            for node in matched_nodes:
                path = node["path"]
                git_sha = node["sha"]
                doc_id = f"{rule.owner}_{rule.repo}::{path}"
                bundle = (
                    "07_Release_Notes_And_Changelog_Radar"
                    if path.startswith("release-notes/")
                    else self._resolve_bundle(path, rule.bundle_router)
                )

                existing = self.manifest.get(doc_id)

                # Optimización O(1): Si el Git Blob SHA es idéntico, el archivo en
                # el repositorio no ha sufrido ni un solo byte de cambio.
                if (
                    existing
                    and not force_recheck
                    and existing.git_blob_sha == git_sha
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    skipped += 1
                    continue

                raw_url = f"https://raw.githubusercontent.com/{rule.owner}/{rule.repo}/{rule.branch}/{path}"
                raw_resp = self.session.get(raw_url, timeout=30)
                raw_resp.raise_for_status()

                clean_text = ContentCanonicalizer.normalize_markdown(raw_resp.text)
                new_sha256 = ContentCanonicalizer.compute_sha256(clean_text)

                if (
                    existing
                    and not force_recheck
                    and existing.content_sha256 == new_sha256
                    and (self.base_dir / existing.local_clean_path).exists()
                ):
                    # El blob de Git cambió por un cambio cosmético/espaciado ignorado,
                    # pero el contenido canónico limpio tiene exactamente el mismo SHA-256.
                    existing.git_blob_sha = git_sha
                    skipped += 1
                    continue

                web_url = self._build_canonical_web_url(rule, path)
                was_added = existing is None
                self._persist_document_change(
                    doc_id=doc_id,
                    source_url=raw_url,
                    web_url=web_url,
                    bundle_name=bundle,
                    git_blob_sha=git_sha,
                    new_sha256=new_sha256,
                    clean_text=clean_text,
                    existing=existing,
                )
                if was_added:
                    added += 1
                else:
                    updated += 1

        return added, updated, skipped

    def sync_direct_web_sources(self, force_recheck: bool = False) -> Tuple[int, int, int]:
        """Sincroniza páginas HTML directas y feeds RSS aplicando limpieza DOM/XML."""
        added, updated, skipped = 0, 0, 0

        for src in DIRECT_WEB_SOURCES:
            doc_id = f"web::{src['id']}"
            url = src["url"]
            bundle = src["bundle"]
            src_type = src["type"]

            logger.info("Verificando fuente web directa: %s", url)
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()

            if src_type == "rss":
                clean_text = ContentCanonicalizer.normalize_rss_feed(resp.text)
            else:
                clean_text = ContentCanonicalizer.normalize_html_to_text(resp.text)

            new_sha256 = ContentCanonicalizer.compute_sha256(clean_text)
            existing = self.manifest.get(doc_id)

            if (
                existing
                and not force_recheck
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

        return added, updated, skipped

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
        safe_filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", doc_id) + ".md"
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
            if diff_lines:
                diff_snippet = "\n".join(diff_lines[:120])
                self.change_reports.append(
                    f"### [MODIFICADO] `{doc_id}`\n"
                    f"- **URL Canónica**: {web_url}\n"
                    f"- **Hash Anterior**: `{existing.content_sha256}`\n"
                    f"- **Hash Nuevo**: `{new_sha256}`\n\n"
                    f"```diff\n{diff_snippet}\n```\n"
                )
            logger.info("ACTUALIZADO: %s (Hash: %s)", doc_id, new_sha256[:10])
        else:
            self.change_reports.append(
                f"### [NUEVO RECURSO] `{doc_id}`\n"
                f"- **URL Canónica**: {web_url}\n"
                f"- **Hash Inicial**: `{new_sha256}`\n"
            )
            logger.info("NUEVO: %s (Hash: %s)", doc_id, new_sha256[:10])

        abs_clean_path.write_text(clean_text, encoding="utf-8")
        word_count = len(clean_text.split())

        self.manifest[doc_id] = DocumentRecord(
            doc_id=doc_id,
            source_url=source_url,
            Canonical_web_url=web_url,
            bundle_name=bundle_name,
            git_blob_sha=git_blob_sha,
            content_sha256=new_sha256,
            word_count=word_count,
            last_updated_utc=datetime.now(timezone.utc).isoformat(),
            local_clean_path=str(rel_clean_path),
        )
        self.dirty_bundles.add(bundle_name)

    def build_notebooklm_bundles(self, rebuild_all: bool = False) -> List[Path]:
        """
        Empaqueta los documentos limpios en Compendios Maestros (.md) optimizados
        para Google NotebookLM, verificando el límite de 500,000 palabras por archivo.
        """
        MAX_WORDS_PER_BUNDLE = 450_000  # Margen seguro bajo el tope de 500,000 de NotebookLM
        bundles_map: Dict[str, List[DocumentRecord]] = {}

        for record in self.manifest.values():
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
                    f"- **CANONICAL_URL**: {rec.Canonical_web_url}\n"
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

    def write_audit_report(self, added: int, updated: int, skipped: int) -> Optional[Path]:
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
            f"- **Compendios de NotebookLM Recompilados**: {', '.join(sorted(self.dirty_bundles))}\n\n"
        )
        report_path.write_text(
            header + "\n".join(self.change_reports), encoding="utf-8"
        )
        logger.info("Reporte de diferencias guardado en: %s", report_path)
        return report_path


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
        "--force-recheck",
        action="store_true",
        help="Ignorar caché de hashes y recalcular todas las fuentes.",
    )
    parser.add_argument(
        "--rebuild-all-bundles",
        action="store_true",
        help="Regenerar todos los compendios de NotebookLM aunque no haya cambios.",
    )
    args = parser.parse_args()

    github_token = os.environ.get("GITHUB_TOKEN")
    syncer = CopilotDocumentationSynchronizer(
        base_dir=args.output_dir, github_token=github_token
    )

    g_add, g_upd, g_skip = syncer.sync_github_repositories(
        force_recheck=args.force_recheck
    )
    w_add, w_upd, w_skip = syncer.sync_direct_web_sources(
        force_recheck=args.force_recheck
    )

    total_add = g_add + w_add
    total_upd = g_upd + w_upd
    total_skip = g_skip + w_skip

    syncer.build_notebooklm_bundles(rebuild_all=args.rebuild_all_bundles)
    syncer._save_manifest()
    syncer.write_audit_report(total_add, total_upd, total_skip)

    logger.info(
        "Resumen Final -> Nuevos: %d | Actualizados: %d | Sin Cambios (Hash Match): %d",
        total_add,
        total_upd,
        total_skip,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
