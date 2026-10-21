#!/usr/bin/env python3
"""
Sincronizador Zero-Touch hacia Google NotebookLM para GitHub Actions.
Actualiza únicamente los compendios maestros marcados como 'dirty' en la corrida actual.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("NotebookLMZeroTouch")


def run_nlm_cmd(args: List[str], env: Dict[str, str]) -> subprocess.CompletedProcess:
    cmd = ["notebooklm"] + args
    return subprocess.run(cmd, env=env, capture_output=True, text=True, check=False)


def sync_dirty_bundles_to_notebooklm(workspace_dir: Path, notebook_id: str) -> int:
    dirty_file = workspace_dir / "dirty_bundles.json"
    if not dirty_file.exists():
        logger.info("No existe dirty_bundles.json. Nada que sincronizar con NotebookLM.")
        return 0

    meta = json.loads(dirty_file.read_text(encoding="utf-8"))
    dirty_paths: List[str] = meta.get("dirty_bundles", []) or meta.get("dirty_bundle_files", [])
    if not dirty_paths:
        logger.info("Ningún compendio sufrió cambios semánticos. NotebookLM está al día.")
        return 0

    env = os.environ.copy()
    auth_json = env.get("NOTEBOOKLM_AUTH_JSON", "").strip()
    if auth_json:
        profile_dir = Path.home() / ".notebooklm"
        profile_dir.mkdir(parents=True, exist_ok=True)
        (profile_dir / "storage_state.json").write_text(auth_json, encoding="utf-8")

    # 1. Listar fuentes actuales en el cuaderno
    list_res = run_nlm_cmd(["source", "list", "-n", notebook_id, "--json"], env)
    if list_res.returncode != 0:
        logger.error("Error al listar fuentes en NotebookLM: %s", list_res.stderr)
        return 1

    try:
        current_sources = json.loads(list_res.stdout)
        if isinstance(current_sources, dict):
            current_sources = current_sources.get("sources", [])
    except Exception as exc:
        logger.error("Respuesta JSON inválida de notebooklm source list: %s", exc)
        return 1

    existing_by_title: Dict[str, str] = {}
    for src in current_sources:
        title = src.get("title") or src.get("name") or ""
        src_id = src.get("id") or src.get("source_id") or ""
        if title and src_id:
            existing_by_title[title] = src_id

    # 2. Reemplazar únicamente los compendios modificados
    for bundle_rel_path in dirty_paths:
        bundle_path = Path(bundle_rel_path)
        if not bundle_path.exists():
            bundle_path = workspace_dir.parent / bundle_rel_path
        if not bundle_path.exists():
            logger.warning("Archivo compendio no encontrado: %s", bundle_rel_path)
            continue

        bundle_filename = bundle_path.name
        logger.info("Sincronizando compendio '%s' hacia NotebookLM...", bundle_filename)

        # Eliminar versión anterior si existe en el cuaderno
        old_source_id = existing_by_title.get(bundle_filename) or existing_by_title.get(bundle_path.stem)
        if old_source_id:
            logger.info("Eliminando instantánea anterior (%s) de %s...", old_source_id, bundle_filename)
            del_res = run_nlm_cmd(
                ["source", "delete", old_source_id, "-n", notebook_id, "--yes"], env
            )
            if del_res.returncode != 0:
                logger.warning("Aviso al eliminar fuente previa %s: %s", old_source_id, del_res.stderr)

        # Subir nuevo compendio
        add_res = run_nlm_cmd(
            ["source", "add", str(bundle_path), "-n", notebook_id, "--json"], env
        )
        if add_res.returncode != 0:
            logger.error("Fallo al subir '%s': %s", bundle_filename, add_res.stderr)
            return 1

        try:
            add_data = json.loads(add_res.stdout)
            new_source_id = (
                add_data.get("source", {}).get("id")
                or add_data.get("id")
                or add_data.get("source_id")
            )
        except Exception:
            new_source_id = None

        if new_source_id:
            logger.info("Esperando indexación de '%s' (source_id=%s)...", bundle_filename, new_source_id)
            wait_res = run_nlm_cmd(
                ["source", "wait", new_source_id, "-n", notebook_id, "--timeout", "600"],
                env,
            )
            if wait_res.returncode != 0:
                logger.warning("Timeout o aviso esperando indexación: %s", wait_res.stderr)
            else:
                logger.info("Compendio '%s' indexado y READY en NotebookLM.", bundle_filename)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Zero-Touch Sync de Compendios hacia Google NotebookLM")
    parser.add_argument("--workspace-dir", type=Path, default=Path("./copilot_rag_workspace"))
    parser.add_argument("--notebook-id", type=str, default=os.environ.get("NOTEBOOKLM_NOTEBOOK_ID", ""))
    args = parser.parse_args()

    if not args.notebook_id:
        logger.info("NOTEBOOKLM_NOTEBOOK_ID no configurado. Omitiendo sincronización remota con NotebookLM.")
        return 0

    return sync_dirty_bundles_to_notebooklm(args.workspace_dir, args.notebook_id)


if __name__ == "__main__":
    sys.exit(main())
