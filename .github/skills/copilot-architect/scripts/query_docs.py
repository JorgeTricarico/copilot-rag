#!/usr/bin/env python3
"""
Buscador de Alto Rendimiento para el Corpus RAG de VS Code Copilot.
Permite a las skills y agentes consultar especificaciones oficiales indexadas
sin sobrecargar la ventana de contexto.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Configurar encoding UTF-8 en consola de Windows si es necesario
if sys.platform == "win32":
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def find_workspace_dir(start_dir: Path) -> Optional[Path]:
    curr = start_dir.resolve()
    for _ in range(5):
        cand = curr / "copilot_rag_workspace"
        if cand.exists() and (cand / "state_manifest.json").exists():
            return cand
        if curr.parent == curr:
            break
        curr = curr.parent
    return None


def query_docs(
    workspace_dir: Path,
    query: str,
    bundle: Optional[str] = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    manifest_file = workspace_dir / "state_manifest.json"
    if not manifest_file.exists():
        return []

    try:
        manifest_data = json.loads(manifest_file.read_text(encoding="utf-8")).get("documents", {})
    except Exception:
        return []

    terms = [re.escape(t.lower()) for t in query.split() if t.strip()]
    if not terms:
        return []

    pattern = re.compile("|".join(terms), re.IGNORECASE)
    results = []

    for doc_id, meta in manifest_data.items():
        if bundle and meta.get("bundle_name") != bundle:
            continue

        rel_path = meta.get("local_clean_path", "")
        file_path = workspace_dir / rel_path
        if not file_path.exists():
            continue

        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            continue

        matches = list(pattern.finditer(content))
        if matches:
            first_match = matches[0]
            start_idx = max(0, first_match.start() - 120)
            end_idx = min(len(content), first_match.end() + 200)
            snippet = content[start_idx:end_idx].replace("\n", " ").strip()

            results.append({
                "doc_id": doc_id,
                "score": len(matches),
                "canonical_url": meta.get("canonical_web_url"),
                "bundle": meta.get("bundle_name"),
                "snippet": f"...{snippet}...",
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Consulta rápida del corpus documental de Copilot RAG")
    parser.add_argument("--query", type=str, required=True, help="Términos a buscar.")
    parser.add_argument("--bundle", type=str, default=None, help="Filtrar por compendio temático específico.")
    parser.add_argument("--limit", type=int, default=5, help="Máximo número de resultados a retornar.")
    parser.add_argument("--workspace-dir", type=Path, default=None, help="Ruta hacia copilot_rag_workspace.")
    parser.add_argument("--json", action="store_true", help="Emitir resultados en formato JSON.")
    args = parser.parse_args()

    ws_dir = args.workspace_dir or find_workspace_dir(Path(__file__).parent)
    if not ws_dir or not ws_dir.exists():
        print(f"Error: No se encontró el directorio 'copilot_rag_workspace'. Ejecuta copilot_docs_sync.py primero.", file=sys.stderr)
        return 1

    matches = query_docs(ws_dir, args.query, args.bundle, args.limit)
    if args.json:
        print(json.dumps(matches, indent=2, ensure_ascii=False))
    else:
        if not matches:
            print(f"No se encontraron coincidencias para '{args.query}'.")
            return 0

        print(f"\n🔍 Coincidencias para '{args.query}' ({len(matches)} encontradas):\n")
        for idx, m in enumerate(matches, 1):
            print(f"{idx}. [{m['doc_id']}] (Coincidencias: {m['score']})")
            print(f"   URL Canónica: {m['canonical_url']}")
            print(f"   Compendio:    {m['bundle']}")
            print(f"   Extracto:     {m['snippet']}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
