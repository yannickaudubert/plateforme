# SPEC.md

## 1. Product definition

Cockpit OS DSI Transverse is a local-first operator platform above Windows.

It centralizes:
- knowledge operations
- structured data operations
- workflow orchestration
- research capture
- AI-assisted operator actions

## 2. Core integrated systems

### 2.1 Obsidian
Role:
- canonical documentary knowledge base

Expected cockpit capabilities:
- browse vault
- open notes
- create notes
- edit Markdown
- inspect frontmatter
- route notes to knowledge pipelines
- prepare future RAG exports

### 2.2 NocoDB
Role:
- structured transverse data layer

Expected cockpit capabilities:
- list bases and tables
- inspect schema
- read rows
- create/update rows safely
- connect structured records with notes and deliverables

### 2.3 n8n
Role:
- orchestration engine

Expected cockpit capabilities:
- list workflows
- see statuses
- trigger workflows
- inspect recent executions
- surface failures

### 2.4 Perplexica
Role:
- research and exploration interface

Expected cockpit capabilities:
- launch research queries
- store useful research traces
- convert results into notes
- link results to projects or missions

### 2.5 Open WebUI
Role:
- conversational AI operator layer

Expected cockpit capabilities:
- choose model
- choose context
- trigger cockpit tools
- interact with knowledge and other system layers

## 3. Product architecture

### Frontend
Recommended:
- React
- TypeScript
- operator-oriented UI

### Backend
Recommended:
- Python
- FastAPI
- explicit adapters
- clean service boundaries

### Local configuration
- YAML or JSON for non-secret config
- `.env` for secrets
- project-level config files when needed

### Logging
- structured action log
- no secret leakage
- per-tool error traces

## 4. Mandatory functional areas

### 4.1 Home
- global status
- alerts
- recent actions
- recent failures
- quick navigation

### 4.2 Obsidian Workspace
- tree
- note details
- frontmatter
- edit actions
- knowledge export hooks

### 4.3 NocoDB Control
- tables
- schemas
- row operations
- record links

### 4.4 n8n Orchestrator
- workflows
- runs
- failures
- manual triggers

### 4.5 Perplexica Research
- query
- history
- project tagging
- convert to note

### 4.6 Open WebUI Operator
- model selection
- context selection
- cockpit tool invocation
- safe operator mode

### 4.7 Administration
- config
- secrets
- health
- logs
- paths
- environment

## 5. Non-functional requirements

- local-first
- modular
- safe-by-default
- auditable
- evolvable
- explicit
- useful

## 6. First implementation milestone

The first delivery must provide:
- executable frontend
- executable backend
- health checks
- config loading
- secrets loading
- adapter stubs
- operator navigation
- filesystem-safe Obsidian integration scaffold
- NocoDB/n8n/Perplexica/Open WebUI adapter scaffolds
- journal scaffold
- local dev run instructions

## 7. Definition of done for any feature

A feature is only considered valid if:
- it runs on the target local environment
- it has a clear user action
- it produces a visible useful result
- it handles errors
- it is logged
- it does not break source systems
- it saves time or improves quality in real usage