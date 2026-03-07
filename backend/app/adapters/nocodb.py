from __future__ import annotations

from datetime import datetime, timezone

from app.models.system import ToolHealth


class NocoDBAdapter:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def health(self) -> ToolHealth:
        if not self.base_url:
            status = "degraded"
            message = "NocoDB base URL not configured"
        else:
            status = "ok"
            message = f"NocoDB endpoint configured: {self.base_url}"

        return ToolHealth(
            tool="nocodb",
            status=status,
            message=message,
            checked_at=datetime.now(timezone.utc).isoformat(),
        )
