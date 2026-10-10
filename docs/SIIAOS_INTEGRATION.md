# Intégration au puzzle SIIAOS

```yaml
siiaos_puzzle_version: "2026-09-25"
integration_status: "CONVERGENCE"
truth_status: "CODED"
authority: "none by default"
canonical_reference: "yannickaudubert/twinSIIAOS/docs/SIIAOS_PUZZLE.md"
```

## Rôle dans le SIIAOS

Cockpit opérateur transverse local. Cette plateforme fournit une surface et des adapters vers des outils spécialisés ; elle ne définit pas seule le canon SIIAOS.

## Ce que cette brique implique

- Obsidian, NocoDB, n8n, Perplexica et Open WebUI sont des implémentations/capacités remplaçables, pas des autorités.
- Les écritures doivent rester bornées, journalisées et réversibles.
- Le cockpit doit afficher DesiredState et ObservedState sans les confondre.

## Ce qui peut l'impliquer

- operator workflows
- mission execution
- knowledge operations
- administration

## Capabilities fournies

- operator UI
- tool adapters
- health/status views
- safe write surfaces
- action journal

## Capabilities consommées

- canonical identities/authorities/policies
- capability metadata
- tool endpoints
- knowledge/data references
- Evidence requirements

## Interfaces et contrats

Les interfaces propres au dépôt restent valides dans leur périmètre, mais elles doivent pouvoir se rattacher aux objets SIIAOS pertinents : Identity, Authority, Mandate, Policy, NeedSpec, ContextPack, Capability, Mission, Decision, OperationRecord, Evidence, DesiredState, ObservedState et ChangeSet.

Aucune interface locale ne doit créer silencieusement une seconde source de vérité.

## Données, autorité et confidentialité

- Les accès sont explicitement bornés par identité, rôle, autorité, mandat et policy.
- `Identity != Role != Authority`.
- Les données client, personnelles, confidentielles ou secrètes restent dans leur périmètre d'autorité.
- Source originale, index, RAG, synthèse, interface et canon sont distincts.
- Une capacité technique ne crée jamais une permission.

## Evidence attendue

- health checks
- action journal
- adapter errors
- write confirmations
- runtime probes

Une capacité ne doit être déclarée opérationnelle qu'après preuve adaptée au risque.

## Non-rôles

- système d'exploitation Windows
- canon unique
- orchestrateur souverain
- preuve que les outils externes sont prêts

## Truth gates

Toujours distinguer :

`PROPOSÉ != CODÉ != TESTÉ != DÉPLOYÉ != OBSERVÉ != PROUVÉ`

et :

`DesiredState != ObservedState`

Les états runtime doivent être reliés à une preuve datée.

## Conditions de promotion

Une intégration peut progresser de CANDIDATE/CONVERGENCE vers ACTIVE lorsque ses contrats, permissions, données autorisées, tests, preuves, mécanismes de repli et conditions de retrait sont explicites et vérifiés.

## Retrait / rollback

La brique doit pouvoir être remplacée ou retirée sans perdre les sources, décisions, Evidence, provenance et capacité de reprise.

## Référence canonique

Le puzzle complet et le contrat documentaire commun vivent dans `twinSIIAOS/docs/`. Cette fiche locale explique uniquement la place de ce dépôt et ne remplace pas le document canonique.
