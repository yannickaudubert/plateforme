# Cockpit OS DSI Transverse

Cockpit OS DSI Transverse is a local-first operator layer above Windows.  
It unifies operational supervision and actions across:

- Obsidian (canonical documentation)
- NocoDB (structured transverse data)
- n8n (workflow orchestration)
- Perplexica (research and exploration)
- Open WebUI (operator AI interface)

Language versions:

- English: `README.md`
- Francais: `README.fr.md`

## Current status (v0.1 foundation)

This repository is now an executable and testable operator foundation:

- clean modular architecture (`frontend`, `backend`, `config`, `docs`, `scripts`)
- seven operator pages in React + TypeScript
- FastAPI backend with explicit adapters per tool
- action journaling persisted in SQLite and health status endpoints
- safe Obsidian read/write flows
- NocoDB read + safe write flows (bases, tables, rows, create/update) with auth and allowlist guardrails
- n8n operator controls (workflows, executions, activate/deactivate)
- Perplexica research actions with optional conversion to Obsidian note
- Open WebUI model/chat actions with optional conversion to Obsidian note
- bilingual setup wizard (French/English) for step-by-step user configuration

## Repository structure

- `frontend/` operator UI (React + TypeScript, Vite)
- `backend/` API, adapters, services, security rules, logging
- `config/` non-secret runtime config (`app.json`)
- `docs/` architecture and conventions
- `scripts/` local dev helpers
- `logs/` local action journal output (gitignored)

## Configuration model

Runtime value precedence:

1. `.env` environment variables
2. `config/app.json`
3. backend defaults (pydantic models)

Key variables in `.env`:

- `OBSIDIAN_VAULT_PATH` canonical vault root (default `D:/Yannick`)
- `OBSIDIAN_ALLOWED_ROOTS` allowed filesystem roots for Obsidian actions
- `NOCODB_WRITABLE_TABLES` comma-separated allowlist for NocoDB write operations
- `NOCODB_BASE_URL`, `N8N_BASE_URL`, `PERPLEXICA_BASE_URL`, `OPENWEBUI_BASE_URL`
- `NOCODB_API_TOKEN` required for NocoDB read endpoints

Start from:

```powershell
Copy-Item .env.example .env
```

## Local development

Prerequisites:

- Node.js 20+
- Python 3.11+
- Docker Desktop (optional)

Run frontend:

```powershell
Set-Location frontend
npm install
npm run dev
```

Run backend:

```powershell
Set-Location backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access points:

- Frontend: http://localhost:5173
- Backend docs: http://localhost:8000/docs
- Backend health: http://localhost:8000/health

## Setup Wizard (new)

The setup wizard is available in the UI at `/setup`.

Operator flow:

1. Choose language (`French` or `English`)
2. Fill runtime and Obsidian paths
3. Fill tool endpoints and NocoDB writable table scope
4. Optionally enter secrets
5. Review and apply

When you apply:

- `config/app.json` is updated
- `.env` is updated
- backend runtime caches are refreshed immediately

If you run full stack with docker compose, re-run `.\scripts\up.ps1` after major endpoint or secret changes to fully align all services.

## Docker compose (local dev)

```powershell
docker compose up --build
```

Compose includes:

- frontend: http://localhost:5173
- backend: http://localhost:8000

External services (NocoDB, n8n, Perplexica, Open WebUI) are expected to run separately on their configured URLs.

## Full stack deployment scripts

Use the operator scripts for a full local stack (backend, frontend, NocoDB, n8n, Open WebUI, optional Perplexica):

```powershell
.\scripts\bootstrap.ps1
.\scripts\up.ps1
.\scripts\status.ps1
.\scripts\down.ps1
```

To include Perplexica:

```powershell
.\scripts\up.ps1 -WithPerplexica
.\scripts\status.ps1 -WithPerplexica
```

The full compose definition is in `docker-compose.full.yml`.

## Implemented operator capabilities

Home:

- consolidated tool health status
- recent action journal display

Obsidian Workspace:

- list notes (excluding `.obsidian`)
- read note content and frontmatter
- create note with path guardrails
- update note with optimistic locking (`expected_modified_at`)
- atomic writes and automatic backups in `.cockpit-backups/`

NocoDB Control:

- list bases
- list tables in a selected base
- read rows from a selected table
- create/update rows with explicit confirmation
- write guardrails via `NOCODB_WRITABLE_TABLES` allowlist
- explicit error handling for auth, missing resources, and upstream failures

n8n Orchestrator:

- list workflows
- list recent executions
- activate/deactivate workflows with confirmation

Perplexica Research:

- execute research query
- inspect answer and sources
- convert search result to Obsidian note

Open WebUI Operator:

- list available models
- run chat completion
- convert chat result to Obsidian note

Setup Wizard:

- guided multi-step setup forms
- language choice French/English
- runtime, paths, tools, and secret inputs
- writes `config/app.json` and `.env` through backend API
- applies changes immediately by refreshing runtime dependency caches

## API surface (current)

System and admin:

- `GET /health`
- `GET /api/v1/system/status`
- `GET /api/v1/admin/overview`
- `GET /api/v1/admin/diagnostics`
- `GET /api/v1/setup/state`
- `PUT /api/v1/setup/apply`

Obsidian:

- `GET /api/v1/obsidian/notes`
- `GET /api/v1/obsidian/note?path=...`
- `POST /api/v1/obsidian/note`
- `PUT /api/v1/obsidian/note`

NocoDB:

- `GET /api/v1/nocodb/bases`
- `GET /api/v1/nocodb/bases/{base_id}/tables`
- `GET /api/v1/nocodb/tables/{table_id}/rows?base_id=...&limit=...&offset=...`
- `POST /api/v1/nocodb/tables/{table_id}/rows`
- `PATCH /api/v1/nocodb/tables/{table_id}/rows/{row_id}`

n8n:

- `GET /api/v1/n8n/workflows?limit=...`
- `GET /api/v1/n8n/executions?limit=...`
- `POST /api/v1/n8n/workflows/{workflow_id}/activate`
- `POST /api/v1/n8n/workflows/{workflow_id}/deactivate`

Perplexica:

- `POST /api/v1/perplexica/search`
- `POST /api/v1/perplexica/search-to-note`

Open WebUI:

- `GET /api/v1/openwebui/models`
- `POST /api/v1/openwebui/chat`
- `POST /api/v1/openwebui/chat-to-note`

## Safety and security notes

- `.obsidian` is blocked from business content operations.
- relative traversal and out-of-root paths are rejected.
- secrets are never returned by API, only boolean flags in admin overview.
- journal sanitizes keys containing `secret`, `token`, or `key`.
- journal persistence uses local SQLite (`logs/actions.sqlite3`).
- NocoDB read APIs return `401` when `NOCODB_API_TOKEN` is missing/invalid.
- NocoDB writes are disabled by default until `NOCODB_WRITABLE_TABLES` is configured.

## Validation and tests

Backend:

```powershell
Set-Location backend
.\.venv\Scripts\Activate.ps1
pytest -q
python -m compileall app
```

Frontend:

```powershell
Set-Location frontend
npm run build
```

## Current limitations

- n8n scope currently focuses on workflow listing/execution visibility and activate/deactivate (no run payload orchestration yet).
- Perplexica and Open WebUI integrations currently expose single-query/chat actions plus note conversion, not full session/history control.
- NocoDB writes depend on upstream API compatibility and explicit table allowlist configuration.
