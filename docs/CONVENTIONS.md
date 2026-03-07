# Repository Conventions

## Scope

- Keep the first milestone operational and explicit.
- Do not add deep integrations before health scaffolding is stable.

## Backend conventions

- Routers expose API endpoints only.
- Services contain business logic and orchestration.
- Adapters isolate external tool interactions.
- Models define typed API contracts.
- No secrets in logs.

## Frontend conventions

- Page components in `src/pages`.
- Reusable UI in `src/components`.
- API calls in `src/lib`.
- Type definitions in `src/types`.

## Safety conventions

- Obsidian file actions stay under allowed roots.
- Destructive actions require explicit confirmation (future iteration).
- Action journal is mandatory for operator-triggered operations.
