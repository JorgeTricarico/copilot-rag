#!/usr/bin/env python3
"""
Instalador de la Agent Skill 'copilot-architect'.
Permite instalar la habilidad en el proyecto local (.github/skills/),
a nivel global del usuario (~/.agents/skills/ o ~/.copilot/skills/) o en una ruta destino específica.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

# Configurar encoding UTF-8 en consola de Windows si es necesario
if sys.platform == "win32":
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SKILL_NAME = "copilot-architect"
SOURCE_SKILL_DIR = Path(__file__).parent.parent / "skills" / SKILL_NAME


def install_skill(target_path: Path, force: bool = False) -> Path:
    if not SOURCE_SKILL_DIR.exists():
        raise FileNotFoundError(f"Directorio fuente de la skill no encontrado en: {SOURCE_SKILL_DIR}")

    dest_dir = target_path / SKILL_NAME
    if dest_dir.exists():
        if force:
            shutil.rmtree(dest_dir)
        else:
            print(f"[AVISO] La skill ya existe en {dest_dir}. Usa --force para sobrescribir.")
            return dest_dir

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Copiar SKILL.md
    shutil.copy2(SOURCE_SKILL_DIR / "SKILL.md", dest_dir / "SKILL.md")

    # Copiar references/
    ref_src = SOURCE_SKILL_DIR / "references"
    if ref_src.exists():
        ref_dst = dest_dir / "references"
        shutil.copytree(ref_src, ref_dst, dirs_exist_ok=True)

    # Copiar scripts/
    scripts_src = SOURCE_SKILL_DIR / "scripts"
    if scripts_src.exists():
        scripts_dst = dest_dir / "scripts"
        shutil.copytree(scripts_src, scripts_dst, dirs_exist_ok=True)

    print(f"[OK] Skill '{SKILL_NAME}' instalada con éxito en: {dest_dir}")
    return dest_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=f"Instalador de la Agent Skill '{SKILL_NAME}'")
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=None,
        help="Directorio del proyecto donde instalar (se colocará en .github/skills/copilot-architect).",
    )
    parser.add_argument(
        "--global",
        dest="install_global",
        action="store_true",
        help="Instalar en el almacén global de skills del usuario (~/.agents/skills/).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescribir si la skill ya existe en el destino.",
    )
    args = parser.parse_args()

    if args.install_global:
        base_target = Path.home() / ".agents" / "skills"
    elif args.target_dir:
        base_target = args.target_dir / ".github" / "skills"
    else:
        # Por defecto: .github/skills en el directorio actual
        base_target = Path(".github") / "skills"

    try:
        install_skill(base_target, force=args.force)
        print("\nPara usar esta habilidad:")
        print(f"1. En VS Code Copilot o Claude: Menciona '@copilot-architect' o solicita auditar el proyecto.")
        print(f"2. CLI manual: Ejecuta 'python {base_target / SKILL_NAME / 'scripts' / 'audit_project.py'}'")
        return 0
    except Exception as exc:
        print(f"Error durante la instalación: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
