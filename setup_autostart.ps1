# Configurar sincronización automática periódica en Windows
param (
    [int]$IntervalHours = 6
)

$PSScriptRoot_Safe = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $PSScriptRoot_Safe

$pythonw = (Get-Command pythonw.exe -ErrorAction SilentlyContinue).Source
if (-not $pythonw) {
    $pythonw = "C:\Users\admin\AppData\Local\hermes\hermes-agent\venv\Scripts\pythonw.exe"
}

$action = New-ScheduledTaskAction `
    -Execute $pythonw `
    -Argument '"C:\Users\admin\Documents\Github\vscode-copilot-rag-sync\scripts\copilot_docs_sync.py" --drive' `
    -WorkingDirectory "C:\Users\admin\Documents\Github\vscode-copilot-rag-sync"

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours $IntervalHours)

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 20)

Register-ScheduledTask `
    -TaskName "VSCodeCopilotDocsSync" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Sincronizador determinista de documentacion de VS Code Copilot para NotebookLM y Google Drive" `
    -Force

Write-Host "Tarea programada 'VSCodeCopilotDocsSync' configurada exitosamente." -ForegroundColor Green
Write-Host "Se ejecutará de forma invisible en segundo plano cada $IntervalHours horas." -ForegroundColor Cyan
