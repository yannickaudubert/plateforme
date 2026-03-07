# Cockpit OS DSI Transverse

Cockpit OS DSI Transverse is a local-first operator layer above Windows. It unifies operational control for:

- Obsidian (canonical documentation)
- NocoDB (structured transverse data)
- n8n (workflow orchestration)
- Perplexica (research and exploration)
- Open WebUI (operator AI interactions)

This repository provides the first executable milestone:

- clear repository structure
- React + TypeScript frontend scaffold with seven operator pages
- FastAPI backend scaffold with explicit adapters and health/status routes
- config and secrets layers
- action journal scaffold
- local development instructions
- docker-compose for local development

## Architecture

- `frontend/`: operator interface (React + TypeScript)
- `backend/`: API, services, adapters, guardrails, journaling (FastAPI)
- `config/`: non-secret runtime configuration
- `docs/`: architecture and repository conventions
- `scripts/`: local helper scripts for development
- `logs/`: runtime logs (gitignored)

## Configuration precedence

Runtime values follow this order:

1. environment variables from `.env`
2. values from `config/app.json`
3. hardcoded defaults in backend config models

## Local development

Prerequisites:

- Node.js 20+
- Python 3.11+
- Docker Desktop (optional for compose workflow)

1. Create environment file:

```powershell
Copy-Item .env.example .env
```

2. Frontend:

```powershell
Set-Location frontend
npm install
npm run dev
```

3. Backend (new terminal):

```powershell
Set-Location backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Open:

- Frontend: http://localhost:5173
- Backend docs: http://localhost:8000/docs
- API health: http://localhost:8000/health

For NocoDB read operations, set `NOCODB_API_TOKEN` in `.env`.

## Docker compose

```powershell
docker compose up --build
```

Compose exposes:

- frontend: http://localhost:5173
- backend: http://localhost:8000

## Current scope

This milestone intentionally avoids deep live integrations. Adapters provide explicit interfaces and health scaffolding first.

Obsidian note updates are safe-by-default with:

- optimistic locking via `modified_at`
- local backup creation in `.cockpit-backups/`
- atomic write replacement
