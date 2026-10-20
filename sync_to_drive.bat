@echo off
REM Sincronización a Google Drive para NotebookLM
cd /d "%~dp0"
echo =================================================================
echo Sincronizando documentacion determinista con Google Drive...
echo Destino: G:\My Drive\NotebookLM_Copilot_Docs
echo =================================================================
python scripts\copilot_docs_sync.py --drive %*
pause
