from __future__ import annotations

from datetime import datetime, timezone

from app.models.system import ToolHealth


class N8nAdapter:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def health(self) -> ToolHealth:
        if not self.base_url:
            status = "degraded"
            message = "n8n base URL not configured"
        else:
            status = "ok"
            message = f"n8n endpoint configured: {self.base_url}"

        return ToolHealth(
            tool="n8n",
            status=status,
            message=message,
            checked_at=datetime.now(timezone.utc).isoformat(),
        )
