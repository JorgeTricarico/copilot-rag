# Desinstalar la sincronización automática en segundo plano
Unregister-ScheduledTask -TaskName "VSCodeCopilotDocsSync" -Confirm:$false -ErrorAction SilentlyContinue
Write-Host "Tarea programada 'VSCodeCopilotDocsSync' removida exitosamente." -ForegroundColor Yellow
