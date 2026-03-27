# Praxeology — Guide de démarrage rapide

Construisez votre propre système de gouvernance d'agents IA auto-évolutif en 3 étapes.

---

## Étape 1 : Définir votre mission (STR)

Rédigez le POURQUOI de votre organisation dans `_standard/{department}/STR-101.md`.

Un modèle est disponible dans `templates/_standard/`. Complétez les sections :

- **Mission** — une phrase sur ce pourquoi vous existez
- **Values** — 3 à 5 principes qui guident chaque décision
- **Non-negotiables** — limites absolues que les agents ne doivent jamais franchir, quelles que soient les instructions

C'est la constitution de vos agents. Chaque règle de gouvernance, chaque comportement d'agent et chaque proposition d'amendement doit être cohérent avec elle. En cas de conflit entre les règles, STR l'emporte.

---

## Étape 2 : Concevoir votre équipe

Décidez du nombre d'agents dont vous avez besoin. Minimum 2, recommandé 3 à 9. Chaque agent correspond à un domaine (ingénierie, finance, sécurité, opérations, etc.).

Pour chaque agent, créez `_crew/{name}/CLAUDE.md` avec ces sections :

- **Identity** — nom, intitulé du rôle, département
- **Persona & Character** — traits de personnalité qui déterminent le comportement sous pression
- **Speech Rules** — limites de phrases, ton, expressions interdites, expressions uniques
- **Anti-Patterns** — liste explicite de ce que cet agent ne doit jamais faire
- **Emotional Triggers** — comment le style de réponse varie selon la situation (routine, crise, conflit)
- **Values** — ce que cet agent optimise quand les règles ne couvrent pas la situation
- **Boundaries** — quels domaines appartiennent à d'autres agents (évite les conflits de chevauchement)

Créez ensuite `_crew/CLAUDE.md` avec les règles qui s'appliquent à tous les agents également : standards de communication partagés, protocole d'escalade, règles de mention inter-agents et cadence des rapports.

Consultez `role-design.fr.md` pour des conseils détaillés et des exemples concrets.

---

## Étape 3 : Amorcer la gouvernance

Lancez l'assistant interactif :

```bash
bash setup.sh
```

Ou créez les quatre documents fondamentaux manuellement :

| Document | Chemin | Objectif |
|---|---|---|
| DOC-101 | `_standard/{department}/DOC-101.md` | Garde de gouvernance — ce que les agents peuvent et ne peuvent pas contourner |
| DOC-102 | `_standard/{department}/DOC-102.md` | Sécurité — exigences d'approbation pour les actions destructives ou irréversibles |
| PRC-201 | `_standard/{department}/PRC-201.md` | Gestion de session — comment les sessions démarrent, se déroulent et se terminent |
| PLY-203 | `_standard/{department}/PLY-203.md` | Auto-évolution — comment les agents détectent les lacunes et proposent des améliorations |

Des modèles pour les quatre documents se trouvent dans `templates/_standard/`.

---

## Ce qui se passe ensuite

Une fois déployés, vos agents vont :

1. **Suivre la hiérarchie de gouvernance** pour chaque décision : PLY (playbooks) en premier, puis PRC (procédures), puis DOC (doctrine), puis STR (stratégie). Si le niveau actuel résout la question, ils s'arrêtent et agissent. Sinon, ils escaladent au niveau suivant.
2. **Enregistrer les Standard Gaps** quand une situation n'est pas couverte par les règles existantes — plutôt que d'improviser en silence.
3. **Proposer des amendements** via le mécanisme Proposal lorsqu'une lacune se répète, permettant à la gouvernance d'évoluer avec l'usage réel.
4. **Faire évoluer leurs propres SOPs** via la boucle Learn-Compress-Apply définie dans PLY-203.

Le système est conçu pour que la gouvernance se renforce au fil du temps par l'usage, et non par des audits manuels.

---

## Mise à l'échelle

| Configuration | Référence |
|---|---|
| 1 personne + équipe startup | `examples/tech-startup/` |
| Équipe complète de 9 agents | `examples/one-piece-crew/` |

Les deux exemples incluent des fichiers STR et CLAUDE.md d'équipe pré-remplis, ainsi que des documents de gouvernance amorcés que vous pouvez adapter directement.
