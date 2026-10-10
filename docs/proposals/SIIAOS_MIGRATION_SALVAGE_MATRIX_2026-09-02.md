# SIIAOS — Matrice de migration / salvage / supersession

**Date :** 2026-09-02  
**Statut :** PROPOSAL — aucune suppression ni promotion automatique

## 1. Décisions autorisées

`PRESERVE_AUTHORITY`, `ADMIT_UNDER_TESTS`, `SALVAGE_PATTERN`, `KEEP_SERVICE`, `RECONCILE`, `ARCHIVE_REFERENCE`, `QUARANTINE`, `SUPERSEDE_AFTER_PROOF`.

Une ancienne lignée n'est jamais supprimée parce qu'un objet plus récent semble équivalent. Une supersession exige source, commit/hash, mapping fonctionnel, tests, preuve de migration, archive et rollback.

## 2. Matrice initiale

| Lignée / actif | Valeur | Décision | Destination | Gate manquant |
|---|---|---|---|---|
| v0.7.2-C | Agent Core, Capability Core, Authority & Trace, OperationRecord, Convergence Core, STOP, migration safety | PRESERVE_AUTHORITY | Canonical/Control/Evidence | G0 reproduction exacte |
| alpha9 | Task Fabric, EvidenceGraph, Project/Artifact/Portfolio, Knowledge Pack, observations read-only, SQLite, UI | ADMIT_UNDER_TESTS | Project/Evidence/Knowledge/State | tests objet par objet |
| plateforme | React, FastAPI, admin diagnostics, safe adapters, SQLite journal | SALVAGE_PATTERN | SIIAOS Admin / Adapter Layer | tenancy + authority bridge |
| Resource Radar V3 | discovery, artifacts, local bridge, manifest, Vercel | SALVAGE_PATTERN | Radar Fabric / External Anchor | lineage repo/deployment |
| knowledge-index-local | index/search/provenance | KEEP_SERVICE / RECONCILE | Knowledge provider | rights-before-index / tenancy |
| IrinA | graph/timeline/evidence/durable state patterns | SALVAGE_PATTERN | Evidence/Decision/Knowledge | schema comparison |
| si-local-admin | machine/service observation patterns | SALVAGE_PATTERN | Node/Service Registry | fresh probes |
| `_siaos` audits/proposals | historical architecture/audits | ARCHIVE_REFERENCE / RECONCILE | Provenance / decisions | classify proposal vs implemented |
| historical Immeuble/Building | BuildingState, modes, UI/Godot patterns | SALVAGE_PATTERN | Building/Experience Registry | ViewSpec crosswalk |
| Hyperveille staging | source/signal/evidence/decision pipeline | RECONCILE_EXISTING | Hyperwatch/Radar | staging promotion decision |
| SIIAOS v1 bundle | package lineage, SBOM/tests/rebuild evidence | RECONCILE | Deployment/VersionLineage | SandY live acceptance separate |
| SandY Docker | live/dormant services, compose, ports | OBSERVE_NOT_CANON | Node/Service/Port | fresh probes + Git lineage |
| Windows/WSL footprints | native tools/runtimes/apps | OBSERVE_NOT_CANON | Asset/Service/Capability | separate Windows/Ubuntu probes |

## 3. Crosswalk obligatoire

```text
legacy id/path
→ source lineage
→ hash/commit/version
→ semantic object type
→ canonical target id
→ field mapping
→ lost/unknown fields
→ authority change? yes/no
→ fixtures/tests
→ PREPARED / MIGRATED / VERIFIED / PASS
→ rollback/archive location
```

Une valeur reconstruite n'est pas présentée comme fait historique sans preuve d'origine. Employer `unknown` ou `derived_at_migration`.

## 4. Anti-compression

Ne pas fusionner :

- Role / Persona / AgentProfile / AgentInstance / Team / TeamDeck ;
- Skill / Capability / Tool / Provider / Adapter / RuntimeHarness / Model ;
- Project / Mission / Task / Operation / Evidence / Artifact ;
- Service definition / deployment / instance / runtime observation ;
- AuthoritySource / Interpretation / Policy / Control / Test / Evidence ;
- BuildingDefinition / BuildingInstance / ViewSpec / InterfaceInstance ;
- Node / ComputeProvider / ExternalAnchor ;
- source document / derived note / chunk / index / RAG answer.

## 5. Supersession

`SUPERSEDED` n'est possible que si le remplaçant démontre une couverture égale ou meilleure des contrats requis et conserve la lineage. Une fonction non portée devient un gap/risque de régression, jamais une disparition silencieuse.

## 6. Ordre de réconciliation

1. authority et identity ;
2. OperationRecord / evidence ;
3. truth facets / observations ;
4. project/mission/task ;
5. specialized registries ;
6. knowledge lineage ;
7. Experience / ViewSpec ;
8. radars ;
9. Agent Operator Gateway ;
10. bounded execution après les gates.
