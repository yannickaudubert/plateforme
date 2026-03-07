# Backend

Minimal FastAPI API scaffold for Cockpit OS DSI Transverse.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Main routes

- `GET /health`
- `GET /api/v1/system/status`
- `GET /api/v1/obsidian/notes`
- `GET /api/v1/admin/overview`
