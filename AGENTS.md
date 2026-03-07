# AGENTS.md

## Product name

Cockpit OS DSI Transverse

## Product intent

This repository builds a local-first operator platform above Windows for a consultant DSI transverse workflow.

This is not:
- a generic dashboard
- a fake operating system
- a replacement for Windows
- a toy demo

This is:
- an operator cockpit
- a transverse control layer
- a production and supervision interface
- a unification layer above several specialized tools

## Core tools to integrate

The cockpit must be designed around these tools:

- Obsidian
- NocoDB
- n8n
- Perplexica
- Open WebUI when needed

## Source of truth

### Documentation
The canonical knowledge base is the Obsidian vault at:

`D:\Yannick`

Markdown notes are the canonical documentary source.

### Structured data
NocoDB is the main structured transverse database.

### Automation
n8n is the main orchestration engine.

### Research
Perplexica is used for research and exploration.

### AI operator layer
Open WebUI is used when conversational or tool-assisted AI interaction is relevant.

## Design rules

- local-first
- modular
- explicit adapters
- safe writes
- auditability
- progressive industrialization
- functionality must be useful before being fancy

## Required app sections

- Home
- Obsidian Workspace
- NocoDB Control
- n8n Orchestrator
- Perplexica Research
- Open WebUI Operator
- Administration

## Repository architecture goals

Use a clean separation such as:

- `/apps`
- `/backend`
- `/frontend`
- `/packages`
- `/docs`
- `/config`
- `/scripts`

Or any equivalent structure that keeps concerns separate.

## Backend expectations

Backend should:
- expose a clean API
- encapsulate adapters
- manage configuration and secrets
- journal actions
- enforce guardrails
- orchestrate inter-tool flows

## Frontend expectations

Frontend should:
- be operator-oriented
- prioritize actionability
- show status, errors, and useful commands
- avoid decorative complexity
- expose direct actions per tool

## Tool adapters

Create explicit adapters for:
- Obsidian vault filesystem operations
- NocoDB API
- n8n API
- Perplexica access layer
- Open WebUI access layer

## Security and safety

Must include:
- explicit config layer
- secrets layer
- masked secrets in UI
- no secret exposure in logs
- action journal
- path whitelisting for filesystem actions
- confirmations for destructive actions
- clear error handling

## Build strategy

Always prefer:
1. structure
2. configuration
3. minimum executable product
4. adapters
5. operator views
6. safe actions
7. tests
8. polish

## First milestone

Create a bootable repository with:
- repo structure
- README
- SPEC
- config system
- secrets system
- backend scaffold
- frontend scaffold
- docker-compose for local dev
- empty adapters
- initial operator views
- action journal scaffold
- health endpoints

## Notes for Codex

Do not overbuild early.
Do not create fake integrations.
Do not add heavy abstractions without current need.
Prefer explicit code over magical frameworks.
Prefer clear interfaces over speculative complexity.