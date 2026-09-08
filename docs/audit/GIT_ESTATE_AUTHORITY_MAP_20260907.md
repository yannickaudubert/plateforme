# BOOT-001 — Git Estate Authority Map

Date: 2026-09-07
Status: `STAGING / EVIDENCE-BASED / NOT-A-DELETION-AUTHORIZATION`

This map records the current best-supported architectural disposition. It must be amended by the fresh SandY probe before any destructive decision.

## Classification rules

- `KEEP` — active repository with a distinct durable role.
- `SALVAGE` — historically valuable code/semantics to reconcile into the current architecture; must not become a competing authority.
- `EXTERNAL_ANCHOR` — upstream/open-source resource that does not need a personal fork unless a maintained patchset requires one.
- `ARCHIVE` — historical evidence with no active runtime/product ownership.
- `REMOVE_CANDIDATE` — no durable role currently identified; removal still requires BOOT-001 gates.
- `NEEDS_EVIDENCE` — current evidence is insufficient or remote/local states conflict.

## Current map

| Repository | Plane / role | Disposition | Current evidence | Required next proof |
|---|---|---|---|---|
| `site` | PUBLIC / EXPERIENCE / CONSULTANT | KEEP | Active consultant, catalogue/Radar projection and publication work; substantial current branches/PRs. | Reconcile branches and retire superseded previews only after current site convergence. |
| `twinSIIAOS` | RADAR / TWIN / EXCHANGE | KEEP | Radar V4/V5, graph/lineage, SaaS augmentation and SandY bridge work exist. | Fresh SandY bridge/runtime probe; converge branch lineage before promotion. |
| `plateforme` | OPERATOR / EXPERIENCE / ADAPTER | KEEP | Admin Fabric proposal explicitly read-only; useful operator projection over existing authorities. | Contract freeze and API/adapter crosswalk; no second Core. |
| `mon_vault` | KNOWLEDGE PROJECTION / HANDOFF / RETEX | KEEP | Git handoff/contracts are a proposal projection; local archive is substantially larger. | Reconcile local canonical knowledge/vault ownership and sanitisation boundary. |
| `sandrine-loquet` | BUILDING / CLIENT VERTICAL | KEEP | Distinct Sandrine vertical and economic/catalogue work. | Fresh local/remote dependency inventory. |
| `universite-libre` | PEDAGOGICAL / PUBLIC KNOWLEDGE PROJECTION | KEEP | Distinct transmission/publication role in current portfolio. Exact originating conversation not recovered in this audit pass. | Recover lineage where possible; verify content and publication dependencies. |
| `siiaos-livre` | EDITORIAL / BOOK | NEEDS_EVIDENCE | README declares canonical manuscript, but GitHub `main` currently contains only README + `.gitattributes`. | Locate verified manuscript source; either restore canonical content or remove false authority claim. |
| `IrinA` | CORE/HERITAGE candidate | NEEDS_EVIDENCE | GitHub remote is empty while available local archive contains a substantial engineered system. | Fresh SandY repo/remote/head/worktree probe and architecture crosswalk. Protected from deletion. |
| `YanIA` | HERITAGE / SALVAGE | SALVAGE | Historical monorepo contains gateway/auth/control tower/capability policy/evidence/graph/persistence/workbench concepts. | Identify unique semantics/code still absent from current Core; import selectively, then archive or retain as heritage. |
| `AIfit` | MODEL/HARDWARE FIT heritage / upstream fork | NEEDS_EVIDENCE | Conversation on 2026-03-07 explicitly prepared a `llmfit` fork for the user's vision; intended hardening and abstraction work existed. GitHub authored-commit evidence is currently weak. | Probe local checkout for Codex changes/branches/patches; only then choose SALVAGE vs EXTERNAL_ANCHOR. |
| `Handy` | OSS resource | EXTERNAL_ANCHOR candidate | Personal fork; no Yannick-authored GitHub commits surfaced. | Prove no unpublished local patches or URL-bound automation. |
| `n8n` | OSS runtime/provider | EXTERNAL_ANCHOR candidate | Local operational relevance is real; personal fork shows no differentiated authored history in current audit. | Record actual local version/instance and any patches; prove fork URL not required. |
| `AppFlowy` | OSS runtime/provider | EXTERNAL_ANCHOR candidate | Historically deployed locally; personal fork has no differentiated authored history in current audit. | Record local version/instance and any patchset. |
| `Perplexica` | OSS runtime/provider | EXTERNAL_ANCHOR candidate | Historically deployed locally; personal fork has no differentiated authored history in current audit. | Record local version/instance and patchset/dependencies. |
| `n8n-workflows` | OSS/reference/workflow corpus | EXTERNAL_ANCHOR candidate | Personal fork; no differentiated authored GitHub history surfaced. | Check whether local workflow export/audit tooling references this fork or contains unique commits. |
| `agentdojo` | OSS research resource | EXTERNAL_ANCHOR candidate | Personal fork; no differentiated authored GitHub history surfaced. | Check local patches and research references. |
| `odysseus` | OSS agent/tool resource | EXTERNAL_ANCHOR candidate | Personal fork; no differentiated authored GitHub history surfaced. | Check local instance/patches and Registry/Radar role. |
| `searxng` | OSS search provider | EXTERNAL_ANCHOR candidate | Personal fork; no differentiated authored GitHub history surfaced. | Record local service/revision/config and prove fork URL not required. |
| `myplace` | UNKNOWN | REMOVE_CANDIDATE | GitHub remote empty since 2023; no durable SIIAOS role recovered in current audit. | Fresh local estate search + dependency search + conversation recovery. |
| `localsite` | UNKNOWN / abandoned bootstrap | REMOVE_CANDIDATE | GitHub empty; available local snapshot essentially only `.gitattributes`. | Fresh local estate and URL dependency search. |
| `appflowy-fullrest` | abandoned AppFlowy experiment candidate | REMOVE_CANDIDATE | GitHub empty, description `first steps`; no implementation found in available evidence. | Fresh local estate and dependency search. |
| `cockpit_d-velopement_territoriaux` | BUILDING prototype candidate | REMOVE_CANDIDATE | GitHub and available local snapshot contain essentially `.gitattributes` + licence. | Confirm no unpublished local branch; preserve territorial semantics as BuildingDefinition/Profile if needed. |

## Conversation provenance currently recovered

### AIfit / llmfit — 2026-03-07

Recovered conversation context states that the user was preparing a fork of `llmfit` to move toward his own vision. Subsequent assistant work described a preserve-first strategy: harden the original base before abstraction/extension, with concerns around diagnostics, download/cache safety, distinction between hardware facts and evaluation, and a more generic catalogue/core.

This is sufficient to prevent classifying `AIfit` as a disposable bookmark. It is not sufficient to prove the intended Codex changes were pushed to GitHub.

### Other repositories

For `myplace`, `localsite`, `appflowy-fullrest`, `IrinA`, `siiaos-livre`, `universite-libre` and `twinSIIAOS`, this audit pass did not recover a reliable exact conversation proving the creation action and intent. Git history and current contents may establish their present role, but causal claims about who created them or why remain `NEEDS_EVIDENCE` unless recovered later.

## Target urbanisation

```text
SIIAOS LOCAL AUTHORITY
  Core / Control / Registry / Policies / Missions / Evidence
  owned locally, observed through bridges

KNOWLEDGE
  governed local vault / knowledge fabric
  mon_vault = controlled projection + handoff, not a second truth

OPERATOR / EXPERIENCE
  plateforme

RADAR / DISCOVERY / LINEAGE
  twinSIIAOS
  existing Hyperveille staging/convergence only

PUBLIC
  site
  siiaos-livre
  universite-libre

BUILDINGS / VERTICALS
  sandrine-loquet
  territorial and other variants become definitions/instances unless unique code justifies a repo

HERITAGE / SALVAGE
  YanIA
  IrinA until reconciled
  AIfit if unique local work is proved

EXTERNAL ANCHORS
  n8n, AppFlowy, Perplexica, SearXNG, Odysseus, AgentDojo, Handy, etc.
  personal fork only when an explicit maintained patchset or workflow requires it
```

## Anti-patterns to eliminate

1. One GitHub repository per idea, persona, cockpit or software dependency.
2. A fork used as a bookmark when the Registry can hold upstream identity/version/licence/evidence.
3. README claiming canonical authority while the canonical data lives elsewhere.
4. Cloud projection being mistaken for local truth.
5. Local project existing without an explicit owner plane or remote policy.
6. Creating a new repository to resolve a naming/ownership ambiguity instead of reconciling the existing one.
7. Keeping historical monoliths alive as parallel authorities after their useful semantics are salvaged.

## Next state transition

No repository changes disposition to `REMOVE` until a fresh SandY observation has been compared with GitHub, Vercel/CI bindings, scripts/services and recovered conversation lineage, and the BOOT-001 human gate has been explicitly passed.
