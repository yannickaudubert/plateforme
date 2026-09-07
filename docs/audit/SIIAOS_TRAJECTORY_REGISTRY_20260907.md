# SIIAOS — Trajectory Registry

Date: 2026-09-07
Status: `STAGING / RECONSTRUCTION / NO-DELETION-AUTHORITY`
Scope: prototypes, POCs, MVPs, local preproduction, GitHub branches, Vercel previews, inherited systems and repeated architectural experiments.

## Purpose

The goal is not to declare the newest implementation the winner. The goal is to reconstruct the lineage of SIIAOS work so that each earlier experiment can be classified as:

- `ANCESTOR` — useful historical experiment whose semantics survive elsewhere;
- `SALVAGE` — contains unique code/contracts/knowledge still worth importing;
- `CURRENT` — active owner of a durable role;
- `PROJECTION` — interface/publication of another authority;
- `STAGING` — controlled convergence area, not canonical truth;
- `EXTERNAL_ANCHOR` — upstream/open-source resource represented in Registry/Radar rather than owned as a SIIAOS core;
- `ARCHIVE_CANDIDATE` — useful history after salvage;
- `REMOVE_CANDIDATE` — no durable role yet proven, subject to BOOT-001 gates;
- `NEEDS_EVIDENCE` — lineage or current state is not sufficiently proved.

Two dimensions are kept separate throughout this document:

1. historical intent: what a conversation/README/plan said the object should become;
2. observed execution: what files, code, branches, tests, deployments or archives actually exist.

A conceptual resemblance is not by itself proof of technical migration.

---

# 1. Executive reconstruction

The SIIAOS estate is not a collection of unrelated projects. Most of the apparent proliferation comes from repeated attempts to solve the same durable problems:

1. sovereign/local foundation;
2. operator cockpit and control plane;
3. registries and capability routing;
4. knowledge/vault capitalisation;
5. agents/operators and human gates;
6. local AI/model/runtime qualification;
7. resource radar/hyperveille/discovery;
8. public and consultant surfaces;
9. client/building verticals;
10. continuity, heritage and reconstruction.

The repeated POCs should therefore be converged by **architectural lineage**, not merely deleted by repository name.

Current target ownership proposed by the evidence available today:

```text
CONTROL / AUTHORITY
  local SIIAOS authority on SandY/ARAGORN
  policies + missions + registry + evidence + admission

KNOWLEDGE
  governed local vault/knowledge fabric
  mon_vault = professional source/projection according to validated boundaries
  first = technical/operator/archive role according to validated boundaries
  indexes remain rebuildable derivatives

OPERATOR / EXPERIENCE
  plateforme

RADAR / DISCOVERY / LINEAGE
  twinSIIAOS Resource Radar V5
  + existing _siiaos_hyperveille_staging as ingestion/staging

AGENT / OPERATOR FABRIC
  common gateway/contract layer over Hermes, Codex, OpenClaw, PicoClaw, n8n and future operators

PUBLIC / CONSULTANT
  site

PUBLIC KNOWLEDGE
  siiaos-livre
  universite-libre

BUILDINGS / VERTICALS
  sandrine-loquet and explicit BuildingDefinition/BuildingInstance objects

HERITAGE / SALVAGE
  YanIA
  IrinA until authority is resolved
  older cockpit/control-plane implementations
  SIIAOS-vpoc if fresh local evidence proves content
```

---

# 2. Chronological spine

## 2026-03 — first explicit product/system experiments

### 2026-03-01 — Demo Cockpit Sandbox

Historical conversation evidence describes a frontend-only SIIAOS demo cockpit with:

- global cockpit;
- role/capability explorer;
- ReactFlow pipeline builder;
- impact twin;
- archive view;
- localStorage persistence;
- URL-hash deep links;
- MCP approval simulation;
- simulated runner/jobs/logs;
- execution tab and tracing;
- compute budgets/RBAC/notifications/cost estimates in a V2 attempt.

Observed status from the historical record: interactive UI prototype, not runtime authority. Some final UI patching attempts failed.

Disposition: `ANCESTOR`.

Surviving semantics:

- capability-centred UI;
- pipeline/mission visualisation;
- human approvals;
- execution evidence/logs;
- cost/compute awareness;
- twin/impact views.

Current destination: `plateforme` Experience/Operator plane + common Mission/Capability/Evidence contracts.

### 2026-03-05 — Sovereign SIIAOS / Citadelle baseline

SIIAOS was explicitly framed as `Système d’Information d’Intelligence Augmentée Orienté Souveraineté`; a Citadelle is a specialised instance.

Initial technical stack proposed around Docker/Compose, Ollama, Obsidian, Qdrant, LlamaIndex, n8n, PostgreSQL, Trivy and Grafana/Loki, with local-only exposure and profiles for core/action/observe/devsecops.

Disposition: `ANCESTOR / DOCTRINE`.

Surviving semantics:

- local-first;
- open/reversible;
- explicit profiles and resource limits;
- internal core network;
- secrets separated from code;
- security/observability as structural layers.

The exact Compose V1 should not be treated as present runtime truth without a fresh machine probe.

### 2026-03-07 to 2026-03-10 — YanIA gateway and Vercel experiments

Vercel project `yan-ia-gateway` was created on 2026-03-09 and linked to GitHub repo `YanIA`.

Observed Vercel history contains early branches and commits around:

- Vercel preview preparation;
- MCP layered strategy and bootstrap scripts;
- governed Pinokio local runtime APIs;
- repo stabilisation;
- deployment simplification and CI gates.

The recorded deployments are ERROR states, including early production-targeted deployments. Later attempts also include developer-watch and agentic benchmark branches.

The local/Git structure later visible for YanIA is much richer than a simple gateway: `apps/gateway`, `apps/web`, migrations, tests, admin/API surfaces, packages, services and workers.

Disposition: `SALVAGE / HERITAGE`.

Reason: YanIA proved many integration ideas early, but it must not become a parallel current Core merely because it is broad.

Unique candidates to salvage:

- gateway/auth and compatibility patterns;
- capability surfaces;
- evidence/citation and persistence patterns;
- admin/workbench UX;
- agentic benchmark material;
- provider/runtime integration learnings.

Current destination: common Control/Agent Gateway/Experience contracts after object-by-object comparison.

### 2026-03-07 — AIfit / llmfit fork trajectory

Historical conversation evidence shows that the `llmfit` fork was intentionally prepared to evolve toward the user's local AI/model fit vision, with a preserve-first doctrine before abstraction.

Snapshot evidence on 2026-08-30 shows a substantial local tree:

- `llmfit-core`;
- `llmfit-desktop`;
- `llmfit-tui`;
- data;
- scripts;
- skills;
- desktop capability metadata.

This contradicts any simplistic classification of AIfit as a disposable GitHub bookmark.

Disposition: `NEEDS_EVIDENCE -> likely SALVAGE / MODELOPS COMPONENT`.

Gate: fresh checkout/branch/unpushed-commit probe before deciding whether the personal GitHub fork remains necessary.

Potential current destination: Model Registry / Fit Assessment / Runtime Qualification component of SIIAOS, not Core authority.

### SIIAOS-vpoc

Historical conversation confirms `SIIAOS-vpoc` as an early experimental SIIAOS version. The 2026-08-30 filesystem snapshot still contains `C:\GitHub\SIIAOS-vpoc`, but no child tree is visible in that snapshot and the repository is not among the 22 current GitHub repositories surfaced by the connected account.

Disposition: `NEEDS_EVIDENCE / HERITAGE TRACE`.

Do not revive or delete it based on name. BOOT-001 must determine whether it is empty, untracked, disconnected, or still contains unique commits locally.

---

# 3. Knowledge / archive trajectory

## 2026-04-24 — local AI observer + archive/RAG direction

Historical work framed a minimal local observer producing lightweight state/events/metrics/RAG trace files before Prometheus/Grafana and heavier observability tooling.

Recommended technical evolution at that point was:

`Python explorer MVP -> Go durable local agent/API -> later deep TUI`.

Disposition: `ANCESTOR`.

This is important because the current architecture should preserve the principle: inexpensive machine-readable observation first, heavier observability later.

## 2026-05-04 to 2026-06-05 — dual-vault doctrine

The stable architecture was progressively clarified:

- `mon_vault` = professional knowledge, missions, methods, offers, deliverables, consultant activity twin;
- `first` = technical/operator/archive/system evidence role;
- controlled membranes and stable IDs;
- no raw bidirectional synchronisation;
- derived views/indexes should be rebuildable.

A BrowserOS/OpenAI archive project was later visible under `C:\first\_codex\projects\openai-browseros-dual-vault-archive` with skills, workflows, data, docs, prompts, scripts and tests.

Disposition: `CURRENT DOCTRINE + ANCESTOR IMPLEMENTATIONS`.

The BrowserOS-specific implementation is not current authority. The dual-vault boundary is a durable constraint.

## 2026-06-25 — knowledge benchmark and index experiments

Historical work moved through Vault Savoir Exchange / Capsule Savoir Ledger concepts and a local Python knowledge benchmark, later recommending Go for efficient large-vault scanning.

Current local archive `knowledge-index-local.rar` proves a substantial later indexing engine exists with:

- corpus/allowlist/threshold config;
- source, extraction, chunk, lineage, evidence and test schemas;
- SQLite code index;
- extraction, chunking, indexing, semantic/search/evaluation modules;
- security and ZIP quarantine;
- ground-truth query set;
- tests for evaluation/index/search/security/ZIP handling.

Disposition: `SALVAGE -> CURRENT KNOWLEDGE-FABRIC DERIVATIVE ENGINE`.

Critical boundary: index/search databases are rebuildable derivatives, never the source of professional or technical truth.

## mon_vault

Local archive is large and materially richer than its GitHub projection. GitHub currently carries a succession/handoff proposal and contracts, while the local vault includes broader historical/professional material.

Disposition: `CURRENT KNOWLEDGE SOURCE/PROJECTION BOUNDARY TO RECONCILE`.

Do not collapse `mon_vault` into `plateforme`, Radar or GitHub merely for convenience.

---

# 4. Cockpit / Operator / Control trajectory

## 2026-06-15 — Go backend core

Historical record describes a Go backend with local JSON persistence and REST objects/endpoints for actors, projects, tasks, signals, opportunities and agent runs, health/summary tested, PostgreSQL deferred.

Disposition: `ANCESTOR / SALVAGE semantics`.

It established an important shift from UI simulation toward an operable local core.

## 2026-06-22 — siiaos-agentic-cockpit MVP

Historical output built an MVP package with:

- FastAPI backend;
- React/Vite admin UI;
- SQLite;
- monitoring;
- kanban;
- clients/projects/missions/tasks;
- agents/tools/deliverables/validations;
- audit scripts;
- planned specialist branches for backend/frontend/machine/LM Studio/Hermes/n8n/deliverables/monitoring.

A second alpha added read-only discovery/convergence of existing Vaults, Markdown, scripts, existing AI cockpits, Git repos/configs/tools/pipelines, with `discovery.json`, reports and integration candidates.

Disposition: `ANCESTOR`.

This is a direct conceptual ancestor of the present Operator/Experience plane.

## 2026-06-23 to 2026-06-25 — Building V0.3 / V1 / V1.3

Historical record:

- V0.3 adapted to ARAGORN around read-only audit of machine/Docker/services/ports;
- V1 delivered a local Go cockpit, read-only governance, registries, machine/Docker/process/task scans, Hermes/Odysseus preparation without execution, localhost port 8790 and five launch scripts;
- V1.3 added context/onboarding audit, machine maturity, proposed teams/capabilities/stacks and audit rooms, still read-only.

Disposition: `ANCESTOR / HIGH-VALUE SALVAGE`.

Durable semantics to preserve:

- observe before mutate;
- local state and capability registry;
- distinction installed/running/healthy/authorised/mission-ready;
- operator rooms/views;
- external agent preparation without automatic execution.

## `C:\first\20_derives\cockpits\systeme_operant_mvp`

The 2026-08-30 filesystem snapshot proves a real derived MVP still exists with:

- Python backend;
- separate Go backend;
- web assets;
- data and scripts;
- hypergrille docs;
- Go `grist-sync` command/internal package;
- Grist integration.

Disposition: `SALVAGE / ARCHIVE_CANDIDATE AFTER CROSSWALK`.

This is not a new current Core. Its useful integration logic should be compared with `plateforme`, Registry and Knowledge/Graph contracts.

## `si-local-admin`

Local archive proves a compact but mature operator/control experiment containing:

- `CAPABILITY_REGISTRY.yaml`;
- `CURRENT_STATE_AUDIT.md`;
- `OPERABILITY_MATRIX.md`;
- `SERVICE_ALLOWLIST.yaml`;
- risk/approval gates;
- machine inventory reports;
- MCP, model, Docker, Git, ports, Vault and process scans;
- Hermes config and 24h loop proposal;
- Aragorn queues/risk registers;
- controlled service invocation PowerShell.

Disposition: `SALVAGE / DIRECT ANCESTOR OF ADMIN FABRIC`.

This object is especially important for Contract Freeze because it already expresses capability/service/operability concepts that reappear later.

## `_siaos` June/July convergence workspace

The `_siaos` archive contains multiple generations rather than one product:

- machine/Vault/Docker audits;
- global inventory and local tools reports;
- GitHub cartography;
- Observable Building study;
- Office Factory dry-run spec/contract;
- Open Source Radar study;
- Skill/Runtime audit;
- first/mon_vault inventories;
- local control-plane proposal;
- `proposals-v2` and `proposals-v3`;
- agent/service/vault/mission/port/risk/data-classification registries;
- backup/client-instance/cockpit-depth/Dyad MVP docs;
- runtime state;
- skill drafts for runtime observer, agent delegation, office factory and browser supervision.

Disposition: `STAGING / HERITAGE / SALVAGE`.

It must not remain an implicit second source of authority. Its surviving contracts belong in the current Control/Registry/Knowledge/Agent layers. Historical proposal generations can then be archived.

## `SIIAOS-v1`

The local archive proves a structured control/governance implementation with 126 entries including:

- Hermes role contracts/teams/reports;
- archive classification;
- human validation gates;
- control flags;
- production/repository safety;
- Codex economy/discovery budget policy;
- machine feedback protocol;
- service registry;
- activation contracts;
- tool-control schema/policy;
- routing and decision schemas;
- staged reports from drive discovery through control UI generation;
- startup/launch audit and validation reports;
- a generated local UI.

Disposition: `SALVAGE / GOVERNANCE-HARNESS ANCESTOR`.

Do not keep a parallel SIIAOS-v1 authority. Preserve the useful policy/contract vocabulary in Contract Freeze and archive the old implementation once coverage is proved.

## `plateforme`

Current repo and local archive prove a real implementation, not only documentation:

- FastAPI backend/adapters;
- React frontend;
- SQLite/action/health model;
- Obsidian/NocoDB/n8n/Perplexica/OpenWebUI integrations;
- security/path/secret/logging protections;
- operator pages and scripts.

The 2026-09-02 Admin Fabric proposal correctly narrows its role: read-only operator foundation/projection/adapters, preserving earlier authority kernels and blocking execution/production on identity/tenant/durability gates.

Disposition: `CURRENT — OPERATOR / EXPERIENCE / ADAPTER PLANE`.

This is the correct destination for cockpit UX; it must not absorb canonical Registry/Knowledge/Agent authority by convenience.

---

# 5. Radar / Hyperveille / Resource discovery trajectory

## 2026-05-02 — Capabilities Radar concept

The territorial work introduced a generalised capability-radar pattern: tools/resources classified by role and maturity, with progression from observed/identified toward qualified/connectable/activatable/integrated/pilotable.

This was already a conceptual shift away from a simple software catalogue.

Disposition: `ANCESTOR`.

## 2026-07 — `_siaos` Open Source Radar and Hyperveille staging

`_siaos` contains an explicit Open Source Radar study dated 2026-07-10.

The separate `_siiaos_hyperveille_staging` archive proves an actual staging implementation with:

- source configuration;
- SearXNG queries;
- RSSHub routes;
- classification config;
- prompts for extraction/scoring/resume;
- Docker/SearXNG config;
- exports, reports and logs;
- a manual Hyperveille sample dated 2026-07-07.

Disposition: `CURRENT STAGING / INGESTION`.

Architectural invariant: do not create a second Hyperveille. Consolidate this staging and promote only after comparison, with intended promotion target `D:\SIIAOS\hyperveille` rather than inventing a new `_siaos\hyperveille` tree.

## 2026-08-27 — Resource Radar cloud demonstration sequence

Vercel records three separate radar project names created the same day:

- `siiaos-resource-radar`;
- `siiaos-resource-radar-v2`;
- `siiaos-resource-radar-v3-preview`.

Observed deployments:

- base Radar: six READY production-targeted deployments on 2026-08-27;
- V2: two READY production-targeted deployments;
- V3 preview: one READY production-targeted deployment.

These are **versions/previews of one capability**, not three durable products.

Disposition: `PROJECTION / PREVIEW HISTORY`.

Vercel project count must not drive architectural project count.

## Resource Radar V3

V3 introduced a useful functional surface:

- live external search across several sources;
- artifact resolution;
- persistent mirror queue;
- cross-OS command generation;
- JSON manifest export;
- localhost dependency-free bridge;
- token/hash protections;
- separation between download and install/activation.

Disposition: `ANCESTOR / FUNCTIONAL MVP`.

## Resource Radar V4

V4 made the architecture explicit:

`Sources -> Hyperveille -> observations -> SandY Radar Core -> publication gate -> public radar/consultant site`.

It added canonical concepts for resources, capabilities, models, agents, runtimes, sources, signals, gaps, benchmarks, evidence and decisions, plus explicit maturity states and champion/challenger/candidate positions.

Disposition: `ANCESTOR -> DIRECT PREDECESSOR OF V5`.

## Resource Radar V5 graph

V5 changes the model from a list to a living provenance/lineage/dependency/evidence/execution/use graph. It introduces lineage edges and observations as first-class contracts and a Model Lineage Passport concept.

Disposition: `CURRENT TARGET — RADAR CORE CONTRACT FAMILY`, subject to Contract Freeze with the wider SIIAOS registry.

## V5 SaaS augmentation

The SaaS augmentation ADR extends the same graph rather than creating another catalogue. Proprietary SaaS can be used/augmented/interfaced/mirrored/archived/hybridised/replaced/kept exit-ready, with official mechanisms preferred before userscripts/DOM hooks.

Disposition: `CURRENT DESIGN`.

## SandY harness branch

The V5 SandY harness adds preflight/start/smoke scripts for the local bridge.

Disposition: `POC / NEEDS RUNTIME PROOF`.

Presence of scripts is not proof that the bridge has successfully run on the live machine.

---

# 6. Agent / Operator Fabric trajectory

The agent layer repeatedly appears across early and later prototypes:

- Hermes role contracts and teams in SIIAOS-v1;
- OpenClaw/PicoClaw and other installed agent systems noted during early convergence;
- Hermes/Odysseus preparation in Building V1;
- agent/tool/deliverable/validation objects in agentic cockpit;
- Aragorn queues and Hermes loop in `si-local-admin`;
- `_siaos` agent/mission registries and skill drafts;
- YanIA gateway/provider experiments;
- current need for interchangeable Hermes/OpenClaw/PicoClaw/Codex/n8n operators.

Disposition: `UNFINISHED DURABLE LINEAGE`.

The correct convergence is not to pick one old harness as the winner. It is to establish a common Agent Gateway / Operator Fabric contract with:

- capabilities;
- permissions;
- sandbox;
- quotas;
- human gates;
- operation records;
- evidence;
- STOP/rollback;
- locality/node selection;
- provider substitution.

Older harnesses then become adapters, fixtures or heritage.

---

# 7. Model / local AI runtime trajectory

This line starts with local model/runtime experimentation rather than a single repo:

- sovereign local stack doctrine;
- AIfit/llmfit compatibility/fit work;
- local-ai-observer concept;
- LM Studio/Ollama/OpenWebUI/LocalAI/vLLM etc. in catalogues and machine inventories;
- YanIA runtime/MCP experiments;
- current SandY ModelOps/Router requirement;
- WSL2 selected as preferred Linux runtime for Linux-native components such as vLLM and streaming Qwen3-ASR.

Disposition: `CURRENT CAPABILITY FAMILY, NOT YET ONE CANONICAL PRODUCT`.

Target components:

- Model Registry;
- Fit Assessment;
- Runtime Probe;
- Model/Provider Router;
- evidence-backed benchmarks;
- hardware/node-aware placement;
- local/external provider substitution.

AIfit is a likely reusable component after fresh local evidence.

---

# 8. Public site / consultant / Surface Fabric trajectory

## 2026-03-07 — Vercel consultant project

Vercel project `yannick-audubert-consultant`, linked to GitHub `site`, was created on 2026-03-07.

## 2026-06-04 — client-space direction

Historical work proposed a secured `/client` area with authentication, request intake, dashboards and exports toward Vault/GitHub/AppFlowy/CRM. This should be treated as a product/surface idea, not evidence that the full client system was delivered.

## 2026-09 — current preproduction/convergence branches

Current branches establish several distinct experiments:

- `stack-radar-convergence-v1` — Catalogue V2, Radar projection, premium/Pass and security/SEO work;
- `preprod` — Heritage Hub, Mission Registry seed, Surface Fabric and local Git bootstrap docs/scripts;
- `refonte-consultant-v3` — public positioning and proof pages;
- `refonte-graphique-consultant-v1` — deeper Cabinet/Experience visual experiment;
- `sandbox/cabinet-admin-v0.1` — same head as graphical branch at the observed point.

The week produced a large number of Vercel preview deployments, but production remained on the older May 27 deployment. The latest graphical preview had a localised TypeScript type-check failure; compilation itself succeeded.

Disposition:

- `site` = `CURRENT PUBLIC/CONSULTANT PROJECTION`;
- weekly branches = `PREPROD / EXPERIMENTS`, not independent authorities;
- `preprod` contains some Control/Heritage contracts that should be moved/crosswalked to their canonical owner rather than letting site become a control repository.

The future site should consume safe projections from Radar/Knowledge/Control, not own their source data.

---

# 9. Building / client / territorial trajectory

## Territorial cockpit

Earlier France Territoriale work explicitly aimed to integrate territorial knowledge/capabilities into SIIAOS rather than clone the wiki or build a separate monolith.

A Git/local repo `cockpit_d-velopement_territoriaux` exists, but both GitHub and the available local archive are essentially a skeleton (`.gitattributes` + licence).

Disposition: `REMOVE_CANDIDATE as repo / PRESERVE semantics as BuildingDefinition`.

The territorial capability family remains useful; the empty repository does not.

## DSI innovation / organisation cockpit

Local archive contains a small but deliberate project skeleton:

- product vision;
- coding guidance;
- expertises;
- SI/data governance;
- 90-day roadmap;
- initial backlog;
- web/API/shared package placeholders.

Disposition: `DESIGN PROTOTYPE / BUILDING PROFILE`.

Unless unique executable code appears in the fresh probe, this should become a Building/Profile definition and reusable Experience configuration rather than a standalone product repo.

## Sandrine

`sandrine-loquet` has a current explicit Building/economic/catalogue trajectory and is not equivalent to the empty cockpit prototypes.

Disposition: `CURRENT CLIENT/BUILDING VERTICAL`.

Rule: client-specific data, authority and operational constraints must remain separate from the generic SIIAOS core.

---

# 10. IrinA trajectory

GitHub currently shows `IrinA` as an empty private repository, but the available local archive contains roughly 380 non-Git files and represents one of the most substantial SIIAOS implementations in the estate.

Observed components include:

- constitution/canon/change control;
- architecture principles and roadmap;
- decisions on capability model, signed projections, machine-state immunity, secrets/runtime, federative anti-centralisation, economic engine and graph/timeline contracts;
- backend graph/timeline JSON contracts;
- SQLite local persistence contract;
- local demo databases;
- minimal local runtime Python package;
- audit reports;
- founder cockpit UX grammar;
- smoke scripts;
- product scope;
- domains/governance/ops/runbooks.

Disposition: `NEEDS AUTHORITY RESOLUTION / HIGH-PRIORITY SALVAGE`.

IrinA may contain the cleanest implementation of several canonical concepts, but the current evidence does not prove that it was intentionally designated as the final SIIAOS Core or that every later contract family derives from it.

Required crosswalk:

- IrinA Capability model <-> Admin Fabric Registry <-> Radar V5 Capability/Resource graph <-> Handoff contracts;
- IrinA graph/timeline <-> Evidence/Knowledge/Operation lineage;
- IrinA machine-state immunity <-> current runtime probe/truth-facet doctrine;
- IrinA signed projection model <-> current public/site/Radar projection gates.

Do not delete, blindly merge, or silently crown it as canonical before this comparison.

---

# 11. Secondary POCs / labs / derivative artifacts

The 2026-08-30 filesystem snapshot also shows experimental objects that should not become architecture owners merely because they contain code:

- `C:\first\labs\headroom-codex-vscode-poc` — lab/benchmark tooling; keep under Labs/Experiments if useful;
- `C:\first\20_derives\public\preaudit_entree_mvp` — derived/public MVP; classify by deliverable use, not Core role;
- `C:\first\20_derives\cockpits\gouvernance-210j-420h` — derived cockpit/planning asset;
- `C:\first\tools\dyad` and `_siaos` Dyad proposals — UI/development experience experiments, not authority;
- generated infographics and target-interface folders — communication/design artifacts only.

Disposition: `LAB / DERIVED / ARCHIVE according to use`.

These are precisely the objects that the future Repository/Artifact Registry must prevent from being mistaken for first-class systems.

---

# 12. What actually supersedes what

The following lineage is supported strongly enough for working urbanisation decisions:

```text
Demo Cockpit Sandbox
   -> siiaos-agentic-cockpit MVP
   -> Building V0.3/V1/V1.3 + systeme_operant_mvp + si-local-admin
   -> _siaos control-plane proposals / SIIAOS-v1 governance harness
   -> plateforme Admin Fabric
```

Meaning: the old cockpit implementations are not current competitors. They are ancestors/salvage sources for `plateforme` + common contracts.

```text
Capabilities Radar concept
   -> _siaos Open Source Radar
   -> _siiaos_hyperveille_staging ingestion
   -> Resource Radar V2/V3 cloud MVP
   -> Radar V4 explicit local-master architecture
   -> Radar V5 lineage/supply-chain graph + SaaS augmentation
```

Meaning: V2/V3/V4 are version history, not separate products. Hyperveille is an upstream ingestion/staging component and must not be duplicated.

```text
Cognitive archive / local observer
   -> dual-vault BrowserOS/archive work
   -> Vault benchmark / knowledge exchange experiments
   -> knowledge-index-local
   -> current Knowledge Fabric / Evidence / RETEX target
```

Meaning: search/index implementations are subordinate to governed source material and stable IDs.

```text
early local model fit/runtime experiments
   -> AIfit/llmfit + YanIA runtime/gateway experiments
   -> current ModelOps / Runtime Probe / Router target
```

Meaning: no single old runtime experiment owns the present model layer.

```text
public consultant/client experiments
   -> site Vercel project
   -> client-space ideas
   -> stack/radar convergence
   -> consultant V3 / cabinet graphical preprod
   -> future Surface Fabric consuming canonical projections
```

Meaning: site remains a surface, not a hidden control plane.

---

# 13. What is NOT yet proven as a supersession

The following relationships remain explicitly unproven:

1. `IrinA -> current Core`: plausible and important, but authority designation is not yet proved.
2. `SIIAOS-vpoc -> Building/plateforme`: conceptual ancestry is plausible, direct code lineage is not yet proved.
3. `YanIA -> current Agent Gateway`: it clearly contains predecessor ideas, but not every current contract derives from it.
4. `SIIAOS-v1 -> _siaos proposals -> IrinA`: chronology/semantic overlap exists, but file-level migration has not been established.
5. `systeme_operant_mvp -> plateforme`: strong conceptual overlap, but direct code reuse must be checked before claiming technical inheritance.
6. `knowledge-index-local -> mon_vault`: wrong framing; the index is a derived engine, not a replacement for the vault.

These uncertainty markers must survive the cleanup process.

---

# 14. Preproduction debt to eliminate

## Git branch debt

### `site`

Current branch family should be converged into explicit owners:

- public experience/consultant changes -> site canonical branch;
- mission/control contracts currently living in `preprod` -> Control/Registry owner;
- Heritage Hub semantics -> Heritage/Knowledge owner;
- Radar catalogue/projection material -> Radar source + generated safe projection;
- abandoned/superseded cabinet branches -> archive/delete only after diff and proof.

### `twinSIIAOS`

Branch family represents sequential Radar generations and SandY harness work. Required state:

- V5 graph contract as candidate source;
- V5 SaaS augmentation folded into same candidate;
- SandY harness validated or marked failed/not-proven;
- V4/V3 code retained only as compatibility/salvage history;
- no permanent V2/V3/V4/V5 product split.

### `plateforme`

Keep Admin Fabric convergence proposal as current operator direction. Fold BOOT-001 audit only after review. Avoid resurrecting earlier independent authority inside the cockpit.

## Vercel project debt

Current Vercel estate includes separate Radar V2, V3 preview and base Radar projects created on 2026-08-27. They should eventually be reduced to the minimum number of publication/preview projects required by the chosen Surface/Radar delivery model.

Do not remove them until current URLs/dependencies/rollback requirements are inventoried.

YanIA Vercel is historical failed-deployment evidence and should not be interpreted as a healthy current hosted service.

---

# 15. Proposed canonical object model for trajectory cleanup

Every historical artifact/repo/branch/project should receive a machine-readable record with at least:

```yaml
id:
name:
kind: repo|branch|deployment|local_project|archive|poc|mvp|prototype|projection
lineage_id:
stage: idea|prototype|poc|mvp|preprod|production|heritage|archive
first_observed_at:
last_observed_at:
historical_intent:
observed_execution:
authority_role:
plane:
current_destination:
disposition:
confidence:
unique_assets:
dependencies:
successor_refs:
evidence_refs:
unknowns:
removal_gates:
```

The important addition is `lineage_id`: multiple repos/deployments/branches can belong to one architectural trajectory without becoming multiple current products.

---

# 16. First lineage IDs

Proposed stable lineage identifiers for the next audit pass:

- `LIN-CONTROL-001` — SIIAOS control/registry/governance;
- `LIN-OPERATOR-001` — cockpit/operator/experience;
- `LIN-KNOWLEDGE-001` — vault/knowledge/evidence/index;
- `LIN-RADAR-001` — resource radar/hyperveille/discovery;
- `LIN-AGENT-001` — agent/operator gateway/fabric;
- `LIN-MODELOPS-001` — local model/runtime/fit/router;
- `LIN-SURFACE-001` — consultant/public/client surfaces;
- `LIN-BUILDING-001` — building/client/territorial verticals;
- `LIN-HERITAGE-001` — succession/reconstruction/legacy salvage;
- `LIN-LABS-001` — bounded experiments and disposable POCs.

Repos are not the lineages. They are artifacts attached to lineages.

---

# 17. Immediate next actions

## A. Fresh machine truth

Run BOOT-001 read-only probe on SandY and attach every detected local repo/project to a lineage.

## B. Contract Freeze crosswalk

Compare the four major overlapping contract families:

1. `plateforme` Admin Fabric registry;
2. site/preprod Mission Registry seed;
3. Radar V5 contracts;
4. mon_vault succession/handoff contracts;
5. additionally IrinA contracts/decisions because current evidence shows they are too substantial to ignore.

## C. File-level salvage manifests

For each ancestor (`SIIAOS-v1`, `_siaos`, `si-local-admin`, `systeme_operant_mvp`, YanIA, IrinA), produce:

- unique concepts;
- unique executable code;
- unique schemas/contracts;
- duplicated concepts already represented better elsewhere;
- tests worth retaining;
- configuration that is machine-specific/stale;
- secrets/sensitive material exclusions;
- successor file/object.

## D. Preprod cleanup plan

Do not delete branches yet. Build a matrix of branch -> unique diff -> current owner -> successor -> archive/remove gate.

## E. Golden journey

After Contract Freeze, prove one end-to-end path:

`Need -> Mission -> Capability -> Provider/Tool -> HumanGate -> Operation -> Evidence -> Admission -> Knowledge/RETEX -> Operator projection -> safe public/Radar projection`.

Use one real local component first, then repeat.

---

# 18. Working conclusion

The main error accumulated over the past months was not excessive experimentation. The experiments produced many useful ideas and working code. The debt comes from **not closing the lineage after an experiment succeeded or failed**.

The new rule is therefore:

> A POC is allowed to proliferate temporarily, but it must terminate by either promotion into an existing lineage owner, salvage into canonical contracts, or explicit archive/removal. It must not silently become another authority.

This registry is the first reconstruction pass. It is intentionally conservative where direct lineage is not proven and will be updated from fresh SandY evidence before destructive cleanup.
