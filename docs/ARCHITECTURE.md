# Architecture

Cockpit OS DSI Transverse follows a modular split:

- UI layer (`frontend`) for operator workflows and status visibility
- API layer (`backend`) for orchestration, guardrails, and adapters
- Adapter layer (`backend/app/adapters`) for each integrated tool
- Config layer (`config`) for non-secret settings
- Secrets layer (`.env`) for credentials and API keys
- Journal layer (`logs` + backend logging service) for action traceability

Design principles:

- local-first
- explicit interfaces
- safe-by-default actions
- progressive integration depth
- no hidden magic
