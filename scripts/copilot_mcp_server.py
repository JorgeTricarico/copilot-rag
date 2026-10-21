#!/usr/bin/env python3
"""
Servidor MCP Stdio para VS Code Copilot Docs & Agent Architecture.
Expone herramientas para buscar en el corpus RAG determinista, consultar
especificaciones tecnicas oficiales y generar scaffolding de agentes.
"""
from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Configurar logging hacia stderr para no corromper el canal stdio JSON-RPC
logger = logging.getLogger("CopilotMCPServer")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(handler)

REPO_ROOT = Path(__file__).parent.parent.resolve()
WORKSPACE_DIR = REPO_ROOT / "copilot_rag_workspace"
CLEAN_SOURCES_DIR = WORKSPACE_DIR / "clean_sources"
BUNDLES_DIR = WORKSPACE_DIR / "notebooklm_bundles"
MANIFEST_PATH = WORKSPACE_DIR / "state_manifest.json"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
try:
    from copilot_scaffold import (
        scaffold_skill,
        scaffold_agent,
        scaffold_hooks,
        scaffold_dual_mcp,
        scaffold_plugin,
    )
except ImportError:
    scaffold_skill = scaffold_agent = scaffold_hooks = scaffold_dual_mcp = scaffold_plugin = None


class CopilotMCPServer:
    def __init__(self):
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> Dict[str, Any]:
        if not MANIFEST_PATH.exists():
            return {}
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("documents", {})
        except Exception as e:
            logger.warning("No se pudo leer manifiesto: %s", e)
            return {}

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "search_copilot_docs",
                "description": (
                    "Busca términos técnicos o conceptos en el corpus oficial de VS Code Copilot, "
                    "GitHub Copilot CLI/SDK, Agent Harnesses y definiciones de APIs propuestas."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Término, clase, interfaz o concepto a buscar (ej: 'AgentHost', 'preToolUse', 'languageModel').",
                        },
                        "bundle": {
                            "type": "string",
                            "description": "Filtro opcional por compendio temático (ej: '01_Architecture_And_Agent_Harnesses', '03_MCP_Servers_And_Tools_Execution').",
                        },
                        "limit": {
                            "type": "integer",
                            "default": 5,
                            "description": "Cantidad máxima de resultados a retornar (1-10).",
                        },
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "get_copilot_document",
                "description": "Obtiene el texto canónico normalizado de un documento específico mediante su doc_id.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "doc_id": {
                            "type": "string",
                            "description": "Identificador exacto del documento (ej: 'microsoft_vscode-docs::docs/agents/overview.md').",
                        }
                    },
                    "required": ["doc_id"],
                },
            },
            {
                "name": "list_copilot_bundles",
                "description": "Lista los compendios temáticos maestros optimizados para Google NotebookLM junto con sus estadísticas.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                },
            },
            {
                "name": "scaffold_agent_asset",
                "description": "Genera una plantilla arquitectónica válida para VS Code Copilot (skill, custom agent, hooks, MCP o plugin).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "asset_type": {
                            "type": "string",
                            "enum": ["skill", "agent", "hooks", "mcp", "plugin"],
                            "description": "Tipo de primitivo a generar.",
                        },
                        "name": {
                            "type": "string",
                            "default": "custom-harness",
                            "description": "Nombre identificador para la skill, agente o plugin.",
                        },
                        "target_dir": {
                            "type": "string",
                            "description": "Directorio relativo o absoluto donde generar el artefacto (por defecto, directorio actual).",
                        },
                    },
                    "required": ["asset_type"],
                },
            },
        ]

    def call_tool(self, name: str, args: Dict[str, Any]) -> str:
        if name == "search_copilot_docs":
            query = args.get("query", "").strip()
            bundle = args.get("bundle")
            limit = min(max(int(args.get("limit", 5)), 1), 10)
            return self._tool_search_docs(query, bundle, limit)

        elif name == "get_copilot_document":
            doc_id = args.get("doc_id", "").strip()
            return self._tool_get_document(doc_id)

        elif name == "list_copilot_bundles":
            return self._tool_list_bundles()

        elif name == "scaffold_agent_asset":
            asset_type = args.get("asset_type", "skill")
            name_val = args.get("name", "custom-harness")
            target = Path(args.get("target_dir", "."))
            return self._tool_scaffold(asset_type, name_val, target)

        else:
            return f"Error: Herramienta '{name}' no reconocida."

    def _tool_search_docs(self, query: str, bundle: Optional[str], limit: int) -> str:
        if not query:
            return "Por favor ingresa un término de búsqueda."

        q_terms = [re.escape(w.lower()) for w in query.split() if w]
        pattern = re.compile("|".join(q_terms), re.IGNORECASE) if q_terms else None
        if not pattern:
            return "Términos de búsqueda inválidos."

        matches = []
        for doc_id, meta in self.manifest.items():
            if bundle and meta.get("bundle_name") != bundle:
                continue

            rel_path = meta.get("local_clean_path")
            if not rel_path:
                continue
            abs_file = WORKSPACE_DIR / rel_path
            if not abs_file.exists():
                continue

            try:
                content = abs_file.read_text(encoding="utf-8")
            except Exception:
                continue

            found_spans = list(pattern.finditer(content))
            if found_spans:
                score = len(found_spans)
                # Extraer snippet alrededor del primer match
                first_m = found_spans[0]
                start_pos = max(0, first_m.start() - 150)
                end_pos = min(len(content), first_m.end() + 250)
                snippet = content[start_pos:end_pos].strip().replace("\n", " ")

                matches.append({
                    "doc_id": doc_id,
                    "canonical_url": meta.get("canonical_web_url"),
                    "bundle": meta.get("bundle_name"),
                    "score": score,
                    "snippet": f"...{snippet}...",
                })

        matches.sort(key=lambda m: m["score"], reverse=True)
        top = matches[:limit]
        if not top:
            return f"No se encontraron coincidencias para '{query}'."

        res = [f"Resultados para '{query}' ({len(matches)} coincidencias totales):\n"]
        for idx, m in enumerate(top, 1):
            res.append(
                f"{idx}. **`{m['doc_id']}`** (Coincidencias: {m['score']})\n"
                f"   - **URL Oficial**: {m['canonical_url']}\n"
                f"   - **Compendio**: {m['bundle']}\n"
                f"   - **Fragmento**: {m['snippet']}\n"
            )
        return "\n".join(res)

    def _tool_get_document(self, doc_id: str) -> str:
        meta = self.manifest.get(doc_id)
        if not meta:
            # Búsqueda difusa por nombre final
            for k, v in self.manifest.items():
                if doc_id.lower() in k.lower():
                    meta = v
                    doc_id = k
                    break

        if not meta:
            return f"Documento con doc_id '{doc_id}' no encontrado en el manifiesto."

        rel_path = meta.get("local_clean_path")
        abs_file = WORKSPACE_DIR / rel_path
        if not abs_file.exists():
            return f"Archivo local no encontrado en disco: {rel_path}"

        header = (
            f"# Documento Técnico Canónico: {doc_id}\n"
            f"- **URL Canónica**: {meta.get('canonical_web_url')}\n"
            f"- **Compendio**: {meta.get('bundle_name')}\n"
            f"- **SHA-256**: `{meta.get('content_sha256')}`\n"
            f"- **Palabras**: {meta.get('word_count')}\n\n---\n\n"
        )
        return header + abs_file.read_text(encoding="utf-8")

    def _tool_list_bundles(self) -> str:
        if not BUNDLES_DIR.exists():
            return "No se ha generado el directorio de compendios aún."

        bundles = sorted(BUNDLES_DIR.glob("*.md"))
        if not bundles:
            return "No hay compendios generados en copilot_rag_workspace/notebooklm_bundles/."

        lines = ["# Compendios Temáticos para Google NotebookLM\n"]
        for b in bundles:
            words = len(b.read_text(encoding="utf-8").split())
            lines.append(f"- **`{b.name}`**: {words:,} palabras ({b.stat().st_size / 1024:.1f} KB)")
        return "\n".join(lines)

    def _tool_scaffold(self, asset_type: str, name: str, target: Path) -> str:
        target.mkdir(parents=True, exist_ok=True)
        if asset_type == "skill" and scaffold_skill:
            f = scaffold_skill(target, name)
            return f"Skill generada exitosamente en: {f}"
        elif asset_type == "agent" and scaffold_agent:
            f = scaffold_agent(target, name)
            return f"Custom Agent generado exitosamente en: {f}"
        elif asset_type == "hooks" and scaffold_hooks:
            f = scaffold_hooks(target)
            return f"Lifecycle hooks generados en: {f}"
        elif asset_type == "mcp" and scaffold_dual_mcp:
            res = scaffold_dual_mcp(target)
            return f"Configuración dual MCP generada:\n- {res['portable']}\n- {res['vscode']}"
        elif asset_type == "plugin" and scaffold_plugin:
            res = scaffold_plugin(target, name)
            return f"Agent Plugin 1.0 generado:\n- {res['plugin']}\n- {res['settings']}"
        else:
            return f"Tipo de artefacto '{asset_type}' no soportado."

    def run_stdio(self) -> None:
        """Ciclo de eventos JSON-RPC 2.0 sobre stdio conforme a la especificación Model Context Protocol."""
        logger.info("Iniciando CopilotMCPServer en modo Stdio...")
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                line = line.strip()
                if not line:
                    continue

                msg = json.loads(line)
                msg_id = msg.get("id")
                method = msg.get("method")
                params = msg.get("params", {})

                if method == "initialize":
                    response = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {
                                "tools": {
                                    "listChanged": False,
                                }
                            },
                            "serverInfo": {
                                "name": "copilot-rag-mcp-server",
                                "version": "1.0.0",
                            },
                        },
                    }
                    self._send(response)

                elif method == "notifications/initialized":
                    pass

                elif method == "ping":
                    self._send({"jsonrpc": "2.0", "id": msg_id, "result": {}})

                elif method == "tools/list":
                    response = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "tools": self.get_tools(),
                        },
                    }
                    self._send(response)

                elif method == "tools/call":
                    tool_name = params.get("name", "")
                    arguments = params.get("arguments", {})
                    content_str = self.call_tool(tool_name, arguments)
                    response = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [
                                {
                                    "type": "text",
                                    "text": content_str,
                                }
                            ]
                        },
                    }
                    self._send(response)

                else:
                    if msg_id is not None:
                        self._send({
                            "jsonrpc": "2.0",
                            "id": msg_id,
                            "error": {
                                "code": -32601,
                                "message": f"Method '{method}' not found",
                            },
                        })
            except Exception as exc:
                logger.error("Error en procesamiento stdio: %s", exc)

    def _send(self, payload: Dict[str, Any]) -> None:
        out = json.dumps(payload, ensure_ascii=False)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    server = CopilotMCPServer()
    server.run_stdio()
