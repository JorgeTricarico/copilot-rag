#!/usr/bin/env python3
"""
Módulo de Notificaciones Proactivas vía Webhook (Discord / Slack / Telegram)
para el Radar de Cambios Documentales de VS Code Copilot.
"""
from __future__ import annotations

import logging
import os
from typing import Dict, List, Optional
import requests

logger = logging.getLogger("CopilotDocsSync.Webhook")


class WebhookNotifier:
    def __init__(
        self,
        webhook_url: Optional[str] = None,
        telegram_token: Optional[str] = None,
        telegram_chat_id: Optional[str] = None,
    ):
        self.webhook_url = webhook_url or os.environ.get("RAG_WEBHOOK_URL")
        self.telegram_token = telegram_token or os.environ.get("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = telegram_chat_id or os.environ.get("TELEGRAM_CHAT_ID")

    def notify_changes(
        self,
        added: int = 0,
        updated: int = 0,
        removed: int = 0,
        skipped: int = 0,
        dirty_bundles: Optional[List[str]] = None,
        modified_records: Optional[List[Dict[str, str]]] = None,
    ) -> bool:
        # Permitir llamada alternativa notify_changes(records)
        if isinstance(added, list):
            modified_records = added
            added = sum(1 for r in modified_records if r.get("action") == "ADDED")
            updated = sum(1 for r in modified_records if r.get("action") == "MODIFIED")
            removed = sum(1 for r in modified_records if r.get("action") == "DELETED")
            skipped = 0
            dirty_bundles = []

        dirty_bundles = dirty_bundles or []
        modified_records = modified_records or []

        if added == 0 and updated == 0 and removed == 0 and not modified_records:
            return False

        summary_lines = [
            "🚀 **Radar VS Code Copilot RAG: Cambios Semánticos Detectados**",
            f"• **Nuevos**: `{added}` | **Actualizados**: `{updated}` | **Eliminados**: `{removed}` | **Sin cambios (SHA-256 Match)**: `{skipped}`",
            f"• **Compendios NotebookLM Recompilados**: `{', '.join(dirty_bundles) or 'Ninguno'}`",
            "",
            "**Documentos Afectados (Top 10):**",
        ]

        for item in modified_records[:10]:
            action = item.get("action", "MOD")
            doc_id = item.get("doc_id", "")
            url = item.get("web_url", "")
            diff_preview = item.get("diff_preview", "")
            summary_lines.append(f"- **[{action}]** [{doc_id}]({url})")
            if diff_preview:
                clean_preview = diff_preview[:300].replace("```", "'''")
                summary_lines.append(f"  ```diff\n{clean_preview}\n  ```")

        full_message = "\n".join(summary_lines)
        sent = False
        if self.webhook_url:
            sent = self._send_webhook(full_message) or sent
        if self.telegram_token and self.telegram_chat_id:
            sent = self._send_telegram(full_message) or sent

        if not self.webhook_url and not (self.telegram_token and self.telegram_chat_id):
            logger.info("No hay Webhooks ni credenciales de Telegram configuradas. Omitiendo notificación remota.")

        return sent

    def _send_webhook(self, message: str) -> bool:
        if not self.webhook_url:
            return False
        try:
            if "discord.com/api/webhooks" in self.webhook_url:
                payload = {"content": message[:1950]}
            else:
                # Formato compatible con Slack / Webhooks genéricos
                payload = {"text": message[:3900]}
            resp = requests.post(self.webhook_url, json=payload, timeout=15)
            resp.raise_for_status()
            logger.info("Notificación enviada exitosamente al Webhook.")
            return True
        except Exception as exc:
            logger.warning("No se pudo enviar notificación al Webhook: %s", exc)
            return False

    def _send_telegram(self, message: str) -> bool:
        if not self.telegram_token or not self.telegram_chat_id:
            return False
        try:
            api_url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            payload = {
                "chat_id": self.telegram_chat_id,
                "text": message[:4000],
                "disable_web_page_preview": True,
            }
            resp = requests.post(api_url, json=payload, timeout=15)
            resp.raise_for_status()
            logger.info("Notificación enviada exitosamente a Telegram.")
            return True
        except Exception as exc:
            logger.warning("No se pudo enviar notificación a Telegram: %s", exc)
            return False
