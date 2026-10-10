# SIIAOS — Archéologie des capacités sur 12 semaines

**Fenêtre principale :** 2026-W24 à 2026-W35, avec delta courant 2026-W36  
**Statut :** PROPOSAL / reconstruction de provenance  
**Branche :** `proposal/siiaos-admin-fabric-20260902`  
**Règle :** ce document ne vaut ni promotion canonique, ni preuve d'installation. Il distingue conception, artefact, test, runtime et usage réel.

## 1. Méthode de vérité

Pour chaque capacité, conserver séparément :

- `design_state` : idée, doctrine, spécification, ratification ;
- `artifact_state` : code, package, schéma, workflow, config, dépôt ;
- `test_state` : non testé, smoke, test ciblé, suite automatisée, validation ;
- `runtime_state` : inconnu, arrêté, actif, dégradé, en erreur ;
- `usage_state` : démonstration, usage ponctuel, intégré, production ;
- `authority_state` : référence, legacy, candidate, canon, superseded ;
- `provenance` : source, date, hash/commit si disponible, niveau de confiance.

Une capacité n'est déclarée « perdue » que si une preuve montre qu'une fonction auparavant opérée n'est plus disponible. Sinon employer : `AT_RISK`, `NOT_PORTED`, `DORMANT`, `UNKNOWN_CURRENT_RUNTIME` ou `SUPERSEDED`.

## 2. Delta longitudinal W24 → W35

### W24 — 8 au 14 juin : du cockpit au système nerveux distribué

Acquis : SIIAOS multi-profils, logique territoriale distribuée, local-first, cockpit comme point de contrôle plutôt que simple chat.

Gain : transversalité organisation/territoire.  
Risque ultérieur : les interfaces spécialisées se multiplient sans foyer opérateur unique.

### W25 — 15 au 21 juin : premier noyau réellement opérable

Acquis : ARAGORN micro-SI local-first, CLI SIIAOS, boucle `scan → diagnostic → recommandation → preuve → cockpit`, probes, tests, GitOps et bootstrap d'infrastructure.

Gain : passage doctrine → exécution instrumentée.  
Gain d'expertise opérée : infrastructure, diagnostic, preuves et rollback commencent à devenir des comportements système.

### W26 — 22 au 28 juin : agents gouvernés et Immeuble opérant

Acquis : cockpit agentique, handoffs, registres proposal-first, V1 read-only, modes admin/business/client, Immeuble/Building, Agent Core et premiers contrats d'autorité.

Gain : gouvernance de l'action et lisibilité spatiale du SI.  
Régression structurelle apparue : prolifération des versions et branches de Building/runtime.

### W27 — 29 juin au 5 juillet : continuité et consolidation insuffisante

Pas de jalon majeur distinct confirmé. La valeur est dans la continuité des probes, preuves, Building et handoffs.

Risque : l'absence de promotion canonique claire laisse des fonctionnalités dans plusieurs lignées.

### W28 — 6 au 12 juillet : Data/Office Factory et benchmark ouvert

Acquis : données structurées, PostgreSQL/Grist/NocoDB comme familles évaluées, Office Factory multi-format et benchmark systématique des alternatives libres/ouvertes.

Gain : passage de « logiciels » à `providers` évaluables et remplaçables.  
Gain de transversalité : documents, données, souveraineté, licences et interopérabilité deviennent des capacités communes à tous les métiers.

### W29 — 13 au 19 juillet : infrastructures publiques et délibération sectorielle

Acquis : cartographie DSI/DSN/HPC/réseaux/capacités publiques ; banque de questions de gouvernance de filière.

Gain : ouverture du SIIAOS vers ressources externes mutualisables et décision collective.  
Dette non fermée : aucun `External Compute Provider Registry` n'est encore prouvé comme runtime canonique.

### W30 — 20 au 26 juillet : continuité Data/Office/alternatives

Pas de jalon distinct suffisamment prouvé ; conserver la période comme continuité sans fabriquer de fonctionnalité.

### W31 — 27 juillet au 2 août : Hyperveille scientifique gouvernée

Acquis : doctrine Hyperveille avec sources primaires, déduplication, provenance, evidence ledger, staging, anti-prompt-injection, tests, rollback, séparation faits/hypothèses/interprétations et pilotes métacognitifs.

Gain d'expertise opérée : science/recherche devient un domaine gouverné, pas une simple recherche Web.  
Gain : `NO_SIGNIFICANT_CHANGE`, critique contradictoire, calibration et fraîcheur deviennent des sorties légitimes.

### W32 — 3 au 9 août : Git comme ancre de version et démonstration publique

Acquis : `siiaos-livre`, `twinSIIAOS`, canon Git/Obsidian pour les corpus concernés, terrain de démonstration Resource Radar.

Gain : passage de bundles isolés à des ancres Git versionnées.  
Attention : un dépôt ou Vercel reste un `ExternalAnchor`, jamais l'autorité globale du système.

### W33 — 10 au 16 août : fédération AgorIA et séparation des domaines de confiance

Acquis : représentation AgorIA/SIIAOS/ARAGORN, industrialisation au cas par cas, cloisonnement membre/client/projet, début de SandY comme nouvelle lignée de laboratoire.

Gain : transversalité fédérée sans fusion des données privées.

### W34 — 17 au 23 août : explosion des cas réels et des artefacts

Acquis majeurs : Sandrine Vault/cockpit/BDD/n8n, PASS étudiant, Neurocampus Graphify/RAG scientifique, Organizational Fabric Hermes, 257 chantiers, Cartographie Maître/Capability Graph, LM Studio Companion, Immeuble v0.1→v0.7.1.2, Capability Core, Agent Core, Authority Trace, archiviste Library et salvage/généalogie.

Gain : expertise métier opérée sur plusieurs domaines : commerce/plantes, pédagogie, recherche CNRS, territoire, conseil, création.  
Régression : le nombre de packs et versions augmente plus vite que leur promotion vers une lignée canonique unique.

### W35 — 24 au 30 août : convergence, preuves et fabric

Acquis : Knowledge Fabric, Context Graph, Memory Experiment, Mission Runtime, Agent Model Runtime, ModelOps, Git Fabric, Control Plane, Machine File Ledger, SI Discovery, Resource Planner, Machine Evidence, Drift Guard, Science→Méthodes→Ateliers→Applications, AgorIA fédéré, Node Registry/External Anchors, Resource Commons, Ephemeral Interface Factory, Companion, SwarmUI/Image Studio.

Alpha9 apporte un saut qualitatif : SQLite durable, 120 tâches canoniques, 257 historiques comme preuves/généalogie, EvidenceGraph, pré-revue de convergence, tests Go/JSON/smoke et `host_mutation_disabled`.

Gain : le système commence à savoir distinguer **ce qu'il sait**, **ce qu'il possède**, **ce qu'il peut faire** et **ce qu'il est autorisé à faire**.

Régression/opérationnel : certaines couches autrefois actives ou expérimentées (n8n général, OpenWebUI, observabilité) ne sont pas actuellement prouvées actives sur SandY ; elles doivent être classées DORMANT/UNKNOWN plutôt qu'ABSENT.

## 3. Delta courant W36 — 31 août au 2 septembre

Éléments déjà observés : audit réel Docker SandY, 22 conteneurs, LiteLLM/Forgejo/Odysseus/router/workers/NATS/SearXNG/ChromaDB/ntfy actifs, SEO en restart-loop, stack observabilité et plusieurs UI IA dormantes. Travail en cours sur Galaxy/Sandrine, SIIAOS Audio Watch, Tool/Experience Hub, Agent Operator Fabric, Radar évolutif, GrowthBook, inventaire des solutions Windows/WSL/Git et reconstruction globale SandY.

Le delta W36 doit rester ouvert jusqu'à fin de semaine.

## 4. Gains transversaux réels

Le progrès principal n'est pas le nombre d'outils. Les capacités qui deviennent transversales sont :

- preuve/provenance/lineage ;
- registre d'actifs/services/capacités/providers ;
- mission/mandat/autorité/human gate ;
- knowledge/context/evidence fabric ;
- Node/ExternalAnchor/placement ;
- Tool/Experience Hub ;
- Organizational Fabric et équipes d'agents ;
- machine evidence/resource planning/drift ;
- science/research governance ;
- benchmark/radar/admission ;
- données et production documentaire ;
- segmentation organisation/client/projet/donnée.

## 5. Capacités à risque ou en régression opérationnelle

1. **Cockpit opérateur unifié** : plusieurs générations et démos existent, mais aucun backoffice unique n'est encore prouvé comme point d'entrée quotidien permanent.
2. **Workflow général** : n8n existe dans le patrimoine et dans des cas métier, mais son runtime général n'est pas confirmé actif sur SandY au 02/09.
3. **Observabilité** : Prometheus/Grafana/Loki/Tempo/OTel/MLflow sont présents mais dormants dans le snapshot Docker.
4. **Building/Immeuble** : riche fonctionnalité juin/août, mais risque de non-portage vers le runtime le plus récent.
5. **Multi-tenant fail-closed** : architecture forte, preuve end-to-end encore à produire.
6. **Secrets + backup/restore global** : briques et pratiques existent, mais capacité transverse de production non encore prouvée.
7. **External compute/HPC/quantum** : intention et cartographie présentes ; provider registry et placement automatisé non prouvés.
8. **Radar Python** : manque structurel confirmé dans le modèle actuel de Resource Radar.

## 6. Règle de reprise

Chaque nouvelle consolidation doit chercher d'abord : `REUSE → SALVAGE/PORT → COMPOSE → REBUILD → CREATE`.

Une fonction historique ne doit jamais être supprimée de la cible uniquement parce qu'elle n'apparaît plus dans le dernier prototype. Elle doit recevoir une décision explicite : `KEEP`, `PORT`, `SUPERSEDE`, `ARCHIVE`, `DEPRECATE` ou `REJECT`, avec preuve et justification.
