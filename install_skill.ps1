<#
.SYNOPSIS
Instalador PowerShell de la Agent Skill 'copilot-architect'.

.PARAMETER TargetDir
Ruta al proyecto destino (instala en <TargetDir>\.github\skills\copilot-architect).

.PARAMETER Global
Instala en el almacén global de skills del usuario (~/.agents/skills/copilot-architect).

.PARAMETER Force
Sobrescribe la instalación previa si ya existe.
#>
param(
    [string]$TargetDir = "",
    [switch]$Global,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$PythonScript = Join-Path $ScriptDir "scripts\install_skill.py"

$ArgsList = @()
if ($Global) {
    $ArgsList += "--global"
} elseif ($TargetDir) {
    $ArgsList += "--target-dir"
    $ArgsList += $TargetDir
}

if ($Force) {
    $ArgsList += "--force"
}

Write-Host "Ejecutando instalador de Copilot Architect Skill..." -ForegroundColor Cyan
python $PythonScript @ArgsList
