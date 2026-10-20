# Script de sincronización directa a Google Drive para Google NotebookLM
param (
    [switch]$ForceRecheck,
    [switch]$RebuildAllBundles,
    [switch]$Verify,
    [int]$Workers = 8
)

$PSScriptRoot_Safe = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $PSScriptRoot_Safe

$argsList = @("--drive", "--workers", $Workers.ToString())
if ($ForceRecheck) { $argsList += "--force-recheck" }
if ($RebuildAllBundles) { $argsList += "--rebuild-all-bundles" }
if ($Verify) { $argsList += "--verify" }

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "Sincronizador Determinista RAG -> Google Drive (NotebookLM)" -ForegroundColor Cyan
Write-Host "Destino: G:\My Drive\NotebookLM_Copilot_Docs" -ForegroundColor DarkCyan
Write-Host "=================================================================" -ForegroundColor Cyan

python scripts/copilot_docs_sync.py @argsList
