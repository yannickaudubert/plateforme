from __future__ import annotations

from datetime import datetime, timezone
from threading import Lock
import time

import httpx

from app.models.system import ToolHealth


_HEALTH_CACHE: dict[tuple[str, str], tuple[float, ToolHealth]] = {}
_CACHE_LOCK = Lock()
_CACHE_TTL_SECONDS = 8.0


def _classify_http_status(tool: str, base_url: str, status_code: int, checked_at: str) -> ToolHealth:
    if 200 <= status_code < 400:
        return ToolHealth(
            tool=tool,
            status="ok",
            message=f"{tool} reachable at {base_url} (HTTP {status_code})",
            checked_at=checked_at,
        )

    if status_code in {401, 403}:
        return ToolHealth(
            tool=tool,
            status="degraded",
            message=f"{tool} reachable but unauthorized at {base_url} (HTTP {status_code})",
            checked_at=checked_at,
        )

    return ToolHealth(
        tool=tool,
        status="degraded",
        message=f"{tool} reachable but unhealthy at {base_url} (HTTP {status_code})",
        checked_at=checked_at,
    )


def probe_http_tool(tool: str, base_url: str, timeout_seconds: float = 3.0) -> ToolHealth:
    checked_at = datetime.now(timezone.utc).isoformat()
    if not base_url:
        return ToolHealth(
            tool=tool,
            status="degraded",
            message=f"{tool} base URL not configured",
            checked_at=checked_at,
        )

    cache_key = (tool, base_url)
    now = time.monotonic()
    with _CACHE_LOCK:
        cached = _HEALTH_CACHE.get(cache_key)
        if cached and now - cached[0] <= _CACHE_TTL_SECONDS:
            return cached[1]

    try:
        response = httpx.get(base_url, timeout=timeout_seconds, follow_redirects=True)
        health = _classify_http_status(tool, base_url, response.status_code, checked_at)
    except httpx.RequestError as exc:
        health = ToolHealth(
            tool=tool,
            status="degraded",
            message=f"{tool} unreachable at {base_url}: {exc.__class__.__name__}",
            checked_at=checked_at,
        )

    with _CACHE_LOCK:
        _HEALTH_CACHE[cache_key] = (now, health)
    return health
