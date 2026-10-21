#!/usr/bin/env python3
"""
Auditor Determinista de Proyectos para VS Code Copilot & Agent Architectures.
Evalúa el grado de preparación de un repositorio frente a los estándares oficiales
de Agent Harnesses, MCP Dual, Skills, Hooks y Plugins.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Configurar encoding UTF-8 en consola de Windows si es necesario
if sys.platform == "win32":
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def audit_project(project_dir: Path) -> Dict[str, Any]:
    project_dir = project_dir.resolve()
    checks: List[Dict[str, Any]] = []

    # 1. MCP Portable (.mcp.json)
    mcp_portable = project_dir / ".mcp.json"
    has_mcp_portable = mcp_portable.exists()
    portable_valid = False
    if has_mcp_portable:
        try:
            data = json.loads(mcp_portable.read_text(encoding="utf-8"))
            portable_valid = "mcpServers" in data
        except Exception:
            pass
    checks.append({
        "id": "MCP_PORTABLE",
        "name": "Configuración Portable MCP (.mcp.json en raíz)",
        "passed": has_mcp_portable and portable_valid,
        "weight": 20,
        "detail": "Presente y con objeto 'mcpServers' válido." if (has_mcp_portable and portable_valid) else "Ausente o con JSON inválido. Requerido para Copilot Agent Host y CLI.",
        "remediation": "python scripts/copilot_scaffold.py --type mcp",
    })

    # 2. MCP Editor (.vscode/mcp.json) con Sandboxing
    mcp_vscode = project_dir / ".vscode" / "mcp.json"
    has_mcp_vscode = mcp_vscode.exists()
    vscode_valid = False
    has_sandboxing = False
    if has_mcp_vscode:
        try:
            data = json.loads(mcp_vscode.read_text(encoding="utf-8"))
            vscode_valid = "servers" in data
            # Revisar si algún servidor tiene sandboxing
            for s in data.get("servers", {}).values():
                if s.get("sandboxEnabled"):
                    has_sandboxing = True
                    break
        except Exception:
            pass
    checks.append({
        "id": "MCP_VSCODE_SANDBOX",
        "name": "Configuración MCP de VS Code (.vscode/mcp.json) con Sandboxing",
        "passed": has_mcp_vscode and vscode_valid and has_sandboxing,
        "weight": 20,
        "detail": "Presente con directivas de aislamiento sandboxEnabled: true." if (has_mcp_vscode and vscode_valid and has_sandboxing) else "Falta configuración de editor o sandboxing estricto (allowWrite/denyRead).",
        "remediation": "python scripts/copilot_scaffold.py --type mcp",
    })

    # 3. Agent Skills (.github/skills/*/SKILL.md)
    skills_dir = project_dir / ".github" / "skills"
    has_skills = False
    skills_count = 0
    if skills_dir.exists():
        found = list(skills_dir.glob("*/SKILL.md"))
        skills_count = len(found)
        has_skills = skills_count > 0
    checks.append({
        "id": "AGENT_SKILLS",
        "name": "Modularización de Habilidades (Agent Skills en .github/skills/)",
        "passed": has_skills,
        "weight": 20,
        "detail": f"Se detectaron {skills_count} habilidades estructuradas." if has_skills else "No hay habilidades modularizadas. Las instrucciones monolíticas saturan el prompt cache.",
        "remediation": "python scripts/copilot_scaffold.py --type skill --name \"<nombre-habilidad>\"",
    })

    # 4. Custom Agents (.github/agents/*.agent.md)
    agents_dir = project_dir / ".github" / "agents"
    has_agents = False
    agents_count = 0
    if agents_dir.exists():
        found = list(agents_dir.glob("*.agent.md"))
        agents_count = len(found)
        has_agents = agents_count > 0
    checks.append({
        "id": "CUSTOM_AGENTS",
        "name": "Roles Especializados (.github/agents/*.agent.md)",
        "passed": has_agents,
        "weight": 15,
        "detail": f"Se detectaron {agents_count} roles de agente personalizados." if has_agents else "Sin agentes personalizados. Recomendado para desacoplar tareas (Ask, Plan, Reviewer).",
        "remediation": "python scripts/copilot_scaffold.py --type agent --name \"<nombre-agente>\"",
    })

    # 5. Lifecycle Hooks (.github/hooks/hooks.json)
    hooks_file = project_dir / ".github" / "hooks" / "hooks.json"
    has_hooks = False
    if hooks_file.exists():
        try:
            data = json.loads(hooks_file.read_text(encoding="utf-8"))
            has_hooks = "hooks" in data and ("preToolUse" in data["hooks"] or "postToolUse" in data["hooks"])
        except Exception:
            pass
    checks.append({
        "id": "LIFECYCLE_HOOKS",
        "name": "Interceptores de Ciclo de Vida y Seguridad (.github/hooks/hooks.json)",
        "passed": has_hooks,
        "weight": 15,
        "detail": "Compuertas preToolUse / postToolUse configuradas." if has_hooks else "Ausente. Sin hooks no hay defensas deterministas contra comandos destructivos o fallos de linter.",
        "remediation": "python scripts/copilot_scaffold.py --type hooks",
    })

    # 6. Manifiesto de Plugin (plugin.json)
    plugin_file = project_dir / "plugin.json"
    has_plugin = False
    if plugin_file.exists():
        try:
            data = json.loads(plugin_file.read_text(encoding="utf-8"))
            has_plugin = "name" in data and "$schema" in data
        except Exception:
            pass
    checks.append({
        "id": "AGENT_PLUGIN",
        "name": "Manifiesto Agent Plugins 1.0 (plugin.json)",
        "passed": has_plugin,
        "weight": 10,
        "detail": "Presente y compatible con Agent Plugins 1.0." if has_plugin else "Opcional pero recomendado para empaquetar y distribuir el repositorio como plugin portable.",
        "remediation": "python scripts/copilot_scaffold.py --type plugin --name \"<nombre-plugin>\"",
    })

    # Cálculo de Score
    total_score = sum(c["weight"] for c in checks if c["passed"])
    max_score = sum(c["weight"] for c in checks)
    score_pct = int((total_score / max_score) * 100)

    return {
        "project_dir": str(project_dir),
        "score_pct": score_pct,
        "checks": checks,
    }


def format_markdown_report(audit_data: Dict[str, Any]) -> str:
    score = audit_data["score_pct"]
    status_icon = "🟢 EXCELENTE" if score >= 80 else ("🟡 MEJORABLE" if score >= 50 else "🔴 DEFICIENTE")

    lines = [
        f"# Reporte de Auditoría de Arquitectura de Agentes: VS Code Copilot\n",
        f"- **Directorio Evaluado**: `{audit_data['project_dir']}`",
        f"- **Puntuación de Preparación Arquitectónica (Readiness Score)**: **{score}%** ({status_icon})\n",
        "## Matriz de Evaluación de Primitivas Técnicas\n",
        "| Estado | Primitiva Evaluada | Detalle | Peso |",
        "| :---: | :--- | :--- | :---: |",
    ]

    for c in audit_data["checks"]:
        icon = "✅ CUMPLE" if c["passed"] else "❌ FALTA"
        lines.append(f"| {icon} | **{c['name']}** | {c['detail']} | {c['weight']}% |")

    lines.append("\n## Recomendaciones Accionables de Mitigación\n")
    missing = [c for c in audit_data["checks"] if not c["passed"]]
    if not missing:
        lines.append("🎉 **El proyecto cumple al 100% con los estándares de arquitectura de agentes de VS Code Copilot.**")
    else:
        for idx, m in enumerate(missing, 1):
            lines.append(f"{idx}. **{m['name']}**:")
            lines.append(f"   - *Diagnóstico*: {m['detail']}")
            lines.append(f"   - *Comando de remediación sugerido*: `{m['remediation']}`\n")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Auditor de Arquitectura de Agentes para VS Code Copilot")
    parser.add_argument("--project-dir", type=Path, default=Path("."), help="Ruta al proyecto a auditar.")
    parser.add_argument("--json", action="store_true", help="Emitir reporte en formato JSON.")
    args = parser.parse_args()

    results = audit_project(args.project_dir)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_markdown_report(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
