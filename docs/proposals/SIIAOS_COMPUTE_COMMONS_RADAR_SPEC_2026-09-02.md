# SIIAOS Compute Commons Radar — spécification v0.1

**Date :** 2026-09-02  
**Statut :** PROPOSAL

## 1. Principe

Un `ComputeProvider` est une offre de capacité ; un `Node` est une identité d'exécution enrôlée. HPC, cloud, notebook ou QPU distant ne deviennent pas des pseudo-nœuds locaux permanents. Ils sont qualifiés comme providers et deviennent des ExecutionTargets uniquement pour un job autorisé.

```text
Mission
→ compute requirements
→ data boundary
→ candidate providers
→ eligibility / entitlement / quota / queue
→ policy / jurisdiction / license
→ cost / performance / reproducibility
→ PlacementDecision
→ future bounded JobEnvelope
→ receipt / evidence
```

## 2. Classes

`local_node`, `remote_workstation`, `academic_hpc`, `public_hpc`, `cloud_free_tier`, `community_compute`, `remote_notebook`, `object_archive_storage`, `quantum_backend`.

## 3. ComputeProvider

Champs : provider/operator, classe, régions/juridiction, mécanisme d'accès, éligibilité, affiliation/projet requis, quota et période de renouvellement, prix/subvention/free tier, queue/scheduler, CPU/GPU/RAM/storage/network, runtimes/modules/containers, data classes autorisées/interdites, transfert/egress, rétention/destruction, terms/licence, observabilité/receipts, fenêtre/expiration, `last_verified_at`, confiance.

## 4. Observation distincte

`ComputeOfferObservation` sépare définition et vérité courante : observed_at, source, disponibilité, quota restant si accessible, queue si accessible, incidents/maintenance, inventory snapshot, confidence/TTL. Une page web ancienne ne devient jamais une disponibilité live après expiration du TTL.

## 5. PlacementDecision

Axes non compressés : data locality/privacy, tenant boundary, juridiction, capability fit, CPU/GPU/RAM/storage, queue/deadline, réseau/latence, coût, énergie/carbone si données fiables, reproductibilité, environnement logiciel, terms/licence, fiabilité, evidence et fallback. La décision conserve aussi les candidats rejetés et raisons.

## 6. Future JobEnvelope

Avant toute exécution externe : mission_id, tenant_id, principal/AgentInstance, capability, provider/target, inputs immuables ou hashes, classification données, ressources demandées, plafond temps/budget, environnement/container/lockfile, CredentialRefs injectées, idempotency key, outputs attendus, post-check, politique de rétention/destruction, cancel/STOP si disponible et receipt/evidence refs.

## 7. HPC France

Le modèle supporte les environnements par allocation : appels à projets, affiliation, fenêtres d'allocation, heures CPU/GPU, queues et règles de transfert. Une allocation devient `ComputeEntitlement`, pas une capacité permanente. GENCI/IDRIS/TGCC/CINES ou autres infrastructures sont cataloguées depuis des sources officielles ; le quota réel n'est considéré courant qu'après observation authentifiée.

## 8. Quantique

Un backend quantique fournit `quantum.execute` et/ou `quantum.simulate` avec technologie/backend, simulateur vs QPU, métadonnées qubits/connectivité/bruit lorsqu'exposées, limites de session/job, queue, quota shots/runtime, SDK, data/IP policy, coût/free allocation, calibration/result provenance. Le router préfère un simulateur local lorsque la mission n'exige pas un QPU réel.

## 9. Stockage externe

Un stockage ne se résume pas à des Go : durability class, juridiction, chiffrement/key ownership, protocole/API, egress, rétention, suppression, versioning, immutabilité et restore evidence doivent être qualifiés.

## 10. Lien avec Python Radar

Un package Python peut fournir un SDK/adapter vers un provider, mais ne prouve ni accès ni entitlement :

`PythonCapabilityArm → RemoteProviderAdapter → ComputeProvider → Entitlement → PlacementDecision`.

## 11. Sécurité

Pas de données client vers un provider non approuvé ; aucun credential dans le catalogue public ; revue des terms avant charge client/commerciale ; outputs distants non fiables avant vérification ; chaque remote environment est une trust zone distincte ; aucune UI publique ne peut soumettre une commande arbitraire.

## 12. Cockpit Compute

Affiche local-first, candidats externes, eligibility, entitlement/quota, fraîcheur availability/queue, compatibilité mission, coût/délai estimé, policy blockers, reproducibility package et explication du PlacementDecision.

## 13. Definition of Done

Le registre supporte toutes les classes ; au moins un exemple local, HPC, remote notebook/cloud et quantum sans credentials ; une demande de capability produit candidats + blockers ; les données publiques stale ne deviennent pas quota live ; aucun job ne part automatiquement ; toute proposition d'expérience enregistre environnement, policies, evidence attendue et cancel/rollback plan.
