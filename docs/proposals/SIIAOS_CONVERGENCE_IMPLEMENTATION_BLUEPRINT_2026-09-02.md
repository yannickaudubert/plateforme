# SIIAOS — Blueprint de convergence détaillée

**Date :** 2026-09-02  
**Statut :** PROPOSAL / implementation slice read-only  
**Branche :** `proposal/siiaos-admin-fabric-20260902`

## 0. Décision

La convergence suit **OPTION-C** : `v0.7.2-C` reste le noyau d'autorité et `v0.8.0-alpha9` une branche de contribution admise objet par objet sous tests. `plateforme` est salvagée comme projection opérateur et bibliothèque de patterns d'adapters ; Resource Radar V3 est salvagé comme provider de découverte/projection publique. Aucun de ces éléments ne devient l'autorité canonique par simple intégration.

Invariants : pas de second Agent Core ; pas de second Capability Core ; `OperationRecord` et Authority & Trace conservés ; Convergence Core consultatif/read-only ; STOP global conservé ; unknown first-class ; UI = projection ; provider = implémentation remplaçable ; aucun host executor dans ce slice.

## 1. Les neuf plans

1. **Canonical Plane** — identité, tenant, client, projet, mission, tâche, mandat, rôle, agent profile, capability, policy, requirement, decision et lineage.
2. **Registry Plane** — registres spécialisés et crosswalks, sans `registry.json` monolithique comme autorité.
3. **Knowledge Plane** — source, classification, rights-before-index, staging, promotion humaine, lineage et index dérivés.
4. **Control Plane** — mission, routing, policy, HumanGate, node placement et décision.
5. **Evidence Plane** — observations, OperationRecord, EvidenceGraph, tests, receipts, freshness et drift.
6. **Adapter Plane** — traduction vers outils/protocoles/providers sans autorité de policy.
7. **Execution Plane** — exécution bornée future ; désactivée ici.
8. **Projection Plane** — web, Godot, client rooms, mobile, Vercel/public.
9. **Federation Plane** — SandY, ARAGORN, Galaxy, nœuds futurs, external anchors et compute providers.

Le flux cible :

```text
WorkIntent
→ JobClassifier / MethodResolver
→ Mission + RequiredCapabilities + KnowledgeRequirements
→ TeamRecipe
→ ProviderCandidateSet
→ Policy / readiness / cost / quality / locality
→ NodePlacement
→ HumanGate si requis
→ Operation / Human Handoff
→ Artifact + Evidence + RETEX
```

## 2. Registres spécialisés

### P0

Building, Node, External Anchor, Service, Capability, Provider/Adapter, Agent/Persona/Team, Project/Mission/Task, Knowledge/Source/Promotion, Evidence Index, Deployment/VersionLineage, Port/Endpoint, Experience, Domain/Compliance, Regulatory, Improvement/Experiment/Drift.

### P1

Model, Skill/Tool enrichi, License, Expert, Dataset/Data, Research/Method/Protocol et Cost/Resource observations.

Chaque objet devra porter un identifiant stable, version de schéma, tenant, provenance/origin, lifecycle, evidence refs, timestamps, principal/source et classification. Une vue d'agrégation ne devient jamais une deuxième autorité.

## 3. SIIAOS Admin = ville industrielle

Le backoffice est le système de production quotidien, pas un tableau de containers. Il doit d'abord répondre : qu'est-ce qui requiert mon attention, quelle mission est bloquée, quelle preuve justifie l'état, quelles capacités/équipes/ressources sont mobilisables ?

### Navigation opérateur

- Aujourd'hui / Command Center
- Dossiers, Missions & Projets
- Analyser & Concevoir
- Produire
- Intelligence & Savoirs
- SI, Outils & Experiences
- Clients & Engagements
- Organisation Agentique
- IA / ModelOps / Compute
- Radars & Admission
- Gouvernance / Réglementaire / Risques
- Amélioration / Expérimentation
- Administration SIIAOS

### Global Context Ribbon

`Building · Tenant/Client · Project · Mission · Lens · Data Boundary · Team · Knowledge Pack · Execution posture`

Toutes les vues doivent utiliser ce contexte pour filtrer données, agents, tools et capabilities. Le frontend ne décide jamais lui-même des droits.

## 4. Immeubles / cockpits

Un cockpit est une projection de la même ville :

```text
BuildingDefinition
+ tenant
+ maturity
+ topology
+ domain/compliance packs
+ capability set
+ team recipes
+ surface policy
= BuildingInstance
```

Profils initiaux : DSI/Innovation/IA/Open Source/GitOps, Consulting, Science/Open Science, Territoires/communs, OSINT, Data/Open Data, Dev/DevOps/AgentOps, Infra/Compute/HPC/Quantum, Multimodal/Audio, Knowledge/ArchiveOps, Sandrine/Ferme aux Fleurs, AgorIA, Neurocampus, PASS/éducation.

Ils ne dupliquent pas les registres transversaux. Ils ajoutent contexte métier, tenant/data boundary, DomainPacks, équipes, méthodes et ViewSpecs.

## 5. Organisation agentique

Les objets restent séparés :

`Role → Persona → AgentProfile → AgentInstance → Team → TeamDeck`

et transversalement :

`Skill → Capability → Tool → Provider → RuntimeHarness → Model`.

Les pôles virtuels sont des **TeamDecks dormants** : Audit transverse, Architecture, Programme, Product/PO, Sécurité/Droit/Conformité, Data/IA, Prospective/Hyperveille, Science/Recherche, Code Foundry, Livrable critique. Une mission active les instances nécessaires seulement après résolution contexte, connaissances autorisées, capabilities, operator gateway, modèle/provider, nœud, budget et policy.

Hermes, Codex, OpenClaw, PicoClaw, Qwen Code, Kimi Code, Claude Code et futurs harnesses restent des opérateurs interchangeables derrière Agent Gateway.

## 6. Project / Mission / Task Fabric

Les 120 tâches canoniques et les 257 chantiers historiques ne deviennent pas deux backlogs concurrents. Le modèle cible sépare Portfolio, Project, Mission, WorkItem/Task, Dependency, Milestone, Mandate, Decision, RAID, Artifact/Deliverable, Evidence, RETEX et ImprovementProposal.

Tout workstream historique entre d'abord avec source/date/confiance. Il n'est promu en tâche canonique qu'après réconciliation.

## 7. Knowledge, Science, OSINT, Hyperveille

Knowledge Fabric conserve : source → classification → rights-before-index → staging → review → promotion → index dérivé → réponse avec lineage. `first`, `mon_vault`, Vaults clients et archives ne sont pas physiquement fusionnés.

Science/Open Science ajoute ResearchProject, ResearchQuestion, Protocol, Experiment, Dataset, LiteratureItem, Claim, CounterClaim, Disagreement, Confidence, Replication, Publication et MethodPack.

OSINT sépare source publique, fait, inférence, hypothèse, entités, chronologie et preuve ; minimisation et provenance restent explicites.

Hyperveille conserve le pipeline `source → signal → qualification → preuve → impact candidate → experiment proposal → human review → promote/reject/archive`. Un signal ne modifie jamais automatiquement une production ou une politique.

## 8. Radar Fabric

Grammaire commune :

```text
Discovery
→ provenance/freshness
→ licence/security
→ compatibility
→ capability arms
→ benchmark/evidence
→ alternatives
→ ExperimentProposal
→ human decision
→ admit/reject/watch/archive
```

Familles : Resource, OSS/Application, Python, Compute Commons, Model/Dataset, Open Science, Regulatory Freshness, API/MCP/Protocols, Interface/Experience.

Le **Python Radar** transforme package→versions→dependencies→interfaces→functional arms→node fit→bounded experiment. Aucun `pip install` automatique.

Le **Compute Commons Radar** traite local nodes, remote workstations, HPC, free/cloud/community compute, notebooks, stockage et quantum backends comme providers avec entitlement, quota, queue, juridiction, data classes, coût et evidence.

## 9. Regulatory / Governance Fabric

Ne jamais confondre :

1. `AuthoritySource` — texte officiel/guidance/version ;
2. `Interpretation/Applicability` — analyse contextualisée et revue ;
3. `MachineControl` — politique/contrôle/test interne traçable.

Objets : AuthoritySource, AuthorityVersion, Requirement, ApplicabilityRule, Interpretation, Policy, Control, ControlTest, EvidenceExpectation, ComplianceAssessment, Exception, Risk, RegulatoryImpactCandidate.

`UNKNOWN`, `POSSIBLY_APPLICABLE` et `EXTERNAL_REVIEW_REQUIRED` sont des sorties normales. Une évolution réglementaire crée un ImpactCandidate, jamais une mutation silencieuse.

## 10. Tool / Experience Hub

Un même outil peut offrir API/action, MCP, deep-link, controlled embed, local reverse proxy, API-native mini-view, native app, SIIAOS projection ou headless workflow.

`Experience` porte contexte, audience, provider/tool, integration mode, endpoint/deeplink, auth method, data boundary, actions, permissions, readiness, fallback, lifecycle et evidence.

Règle : **une capability → un contrat → plusieurs implémentations et expériences**.

## 11. GitHub et Vercel

GitHub porte code, schémas, migrations, ADR/docs, manifests, fixtures non sensibles, tests et release lineage. Les modifications passent branche/PR.

Vercel peut exposer docs, Resource Radar, previews et surfaces publiques sans secrets. Il ne reçoit ni le canon privé, ni données client, ni shell local, ni droits hôte. Tout projet/déploiement Vercel devient un ExternalAnchor relié à commit/deployment/freshness/surface policy.

## 12. Slice CS-C01 implémenté ici

- `config/convergence/registry.v0.1.json`
- modèles Pydantic stricts
- loader read-only
- routes GET `/api/v1/convergence/*`
- tests d'invariants et de non-mutation
- vue React `SIIAOS Fabric`

Cette tranche **voit et explique** la convergence. Elle ne lance, n'installe, n'active, n'arrête et ne supprime rien.

## 13. Séquence suivante

- **CS-C02** Crosswalk & lineage importer : 0.7.2-C, alpha9, Building, plateforme, Resource Radar, knowledge-index, Hyperveille, historique.
- **CS-C03** Truth & Observation Contract : facettes, freshness, Machine/Service/NodeObservation, drift.
- **CS-C04** Identity/Tenant/DataBoundary/HumanGate avec negative isolation tests.
- **CS-C05** Durable Registry Store : SQLite migrations checksummées, WAL, backup/restore drill, integrity.
- **CS-C06** Project/Mission/Task + Evidence bridge : alpha9 objet par objet, sans duplicate authority.
- **CS-C07** Experience Registry et ViewSpec read-only compiler.
- **CS-C08** Regulatory/Domain/Compliance source→requirement→control→evidence.
- **CS-C09** Radar adapters : Resource, Python, Compute, Regulatory.
- **CS-C10** Agent Organization + Team Composer + Operator Gateway.
- **CS-C11** Capability→provider→node placement simulation expliquée, `effective_executable=false`.
- **CS-C12** Bounded Executor Lab uniquement après identity/tenancy/durability/trace/STOP.
- **CS-C13** Distributed Hall, Client Rooms, AgorIA après maturité M3.

## 14. Acceptance du premier vrai jalon

Le jalon est atteint quand l'opérateur peut ouvrir le Hall, sélectionner client/projet/mission, voir états facettés et preuves, composer une équipe dormante, comprendre les capabilities et providers candidats, ouvrir l'outil dans le meilleur mode sans céder l'autorité, simuler un run plan avec gates, livrer un artefact relié aux preuves et revenir au Hall sans duplication de vérité.

## 15. Non-objectifs actuels

Pas de déploiement Vercel du backoffice privé ; pas de Docker mutation ; pas d'activation n8n ; pas de migration Vault ; pas de secret nouveau ; pas de host executor ; pas de fédération de données AgorIA ; pas de statut production-ready.
