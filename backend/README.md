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
- `GET /api/v1/obsidian/note?path=...`
- `POST /api/v1/obsidian/note`
- `PUT /api/v1/obsidian/note` (supports `expected_modified_at` and `create_backup`)
- `GET /api/v1/nocodb/bases`
- `GET /api/v1/nocodb/bases/{base_id}/tables`
- `GET /api/v1/nocodb/tables/{table_id}/rows?base_id=...&limit=...&offset=...`
- `POST /api/v1/nocodb/tables/{table_id}/rows` (requires confirmation + writable table allowlist)
- `PATCH /api/v1/nocodb/tables/{table_id}/rows/{row_id}` (requires confirmation + writable table allowlist)
- `GET /api/v1/n8n/workflows`
- `GET /api/v1/n8n/executions`
- `POST /api/v1/n8n/workflows/{workflow_id}/activate`
- `POST /api/v1/n8n/workflows/{workflow_id}/deactivate`
- `POST /api/v1/perplexica/search`
- `POST /api/v1/perplexica/search-to-note`
- `GET /api/v1/openwebui/models`
- `POST /api/v1/openwebui/chat`
- `POST /api/v1/openwebui/chat-to-note`
- `GET /api/v1/admin/overview`
- `GET /api/v1/admin/diagnostics`
- `GET /api/v1/setup/state`
- `PUT /api/v1/setup/apply`

## Tests

```powershell
pip install -e ".[dev]"
pytest
```

NocoDB routes require `NOCODB_API_TOKEN`.
NocoDB write routes are disabled until `NOCODB_WRITABLE_TABLES` is configured.
