<p align="center">
  <img src="assets/banner.svg" alt="praxeology — Human–AI Collaborative Governance for Purposeful Action" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

---

## 🌐 Langues

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [中文](README.zh.md) · **Français** · [Deutsch](README.de.md) · [Español](README.es.md)

Également disponible : [QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md))

---

## Pourquoi Praxeology ?

Des outils comme [gstack](https://github.com/gstack-io/gstack) et [oh-my-claudecode](https://github.com/anthropics/claude-code) excellent à rendre les agents IA individuels productifs — navigation, codage, test, déploiement. Mais lorsque vous passez d'**un seul agent** à **plusieurs agents travaillant ensemble**, un nouveau problème émerge : la **gouvernance**.

Sans gouvernance, les agents dupliquent le travail, se contredisent, outrepassent leurs limites et s'éloignent progressivement de leurs rôles définis. L'ingénierie de prompt seule ne résout pas ce problème — il faut une structure qui persiste entre les sessions, évolue avec l'usage et reflète la façon dont les organisations humaines les plus efficaces ont gouverné l'action pendant des siècles.

Praxeology fournit cette structure. Ce n'est pas un remplacement de vos outils de codage — c'est la **couche constitutionnelle** qui se situe au-dessus d'eux, garantissant que vos agents fonctionnent comme une organisation cohérente plutôt que comme une collection de chatbots indépendants.

---

## Qu'est-ce que c'est ?

**Praxeology** est un système d'exploitation collaboratif humain–IA, fondé sur une hiérarchie de gouvernance universelle à 4+1 niveaux. Les humains définissent la stratégie et les principes ; l'IA agentique exécute dans ces limites, apprend de l'expérience et propose des améliorations en retour. Il capture l'observation que toute action intentionnelle — des nations aux agents IA — suit le même schéma structurel.

```
Strategy (POURQUOI) → Doctrine (QUOI) → Procedure (COMMENT) → Playbook (PATTERNS) → Execution (MAINTENANT)
```

Les niveaux supérieurs prévalent toujours sur les niveaux inférieurs. Sans exception.

---

## L'Isomorphisme

La même structure à 4+1 niveaux apparaît dans tous les domaines de l'action organisée :

| Niveau | Droit national | Militaire | Entreprise | Individu | Agent IA |
|--------|---------------|-----------|------------|----------|----------|
| **1 Strategy** | Constitution | Objectif de campagne | Mission & Vision | Valeurs personnelles | System Prompt / Prime Directive |
| **2 Doctrine** | Loi statutaire | Règles d'engagement | Politique d'entreprise | Principes de vie | Behavioral Guidelines |
| **3 Procedure** | Règlements | Standard Operating Procedures | SOPs / Protocoles | Habitudes & Routines | Task Instructions |
| **4 Playbook** | Jurisprudence | Tactiques & Exercices | Meilleures pratiques | Patterns appris | Few-shot Examples |
| **Exec Work Plan** | Décret exécutif | Ordres de mission | Sprint / Plan de travail | Liste quotidienne | Active Context |

Cet isomorphisme est la thèse centrale : la gouvernance n'est pas spécifique à un domaine. Le schéma est universel. Un cadre qui fonctionne pour une unité militaire fonctionne pour une startup, un laboratoire de recherche ou une flotte d'agents IA.

---

## Démarrage rapide

**Étape 1 — Cloner**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**Étape 2 — Lancer la configuration**

```bash
bash setup.sh
```

L'assistant interactif demande le nom de votre organisation, sa mission, les départements, les agents et les projets. Il génère la structure de répertoires complète et tous les documents d'amorçage.

**Étape 3 — Lancer**

```bash
bash launch.sh
```

Votre système de gouvernance est opérationnel. Ouvrez `CLAUDE.md` à la racine pour voir le contexte généré pour les agents IA.

> **Nouveau sur Praxeology ?** Commencez par [docs/quickstart.md](docs/quickstart.md) pour un guide en 3 étapes, et [docs/role-design.md](docs/role-design.md) pour concevoir vos agents.

---

## Fonctionnalités clés

| Fonctionnalité | Description |
|----------------|-------------|
| **SafetyGate** | Les documents de niveau supérieur peuvent déclarer des limites absolues qu'aucun document de niveau inférieur ne peut outrepasser |
| **Proposal Flow** | Tout agent ou membre d'équipe peut proposer un amendement via le format Proposal structuré |
| **SOP Evolution** | Les Procedures et Playbooks évoluent via la Review Cascade avant promotion |
| **Review Cascade** | Les modifications se propagent vers le haut : Playbook → Procedure → Doctrine → Strategy pour des vérifications de cohérence |
| **Reverse Flow** | Les modifications de Strategy cascadent vers le bas : tous les niveaux inférieurs sont signalés pour révision |
| **Department Codes** | Départements avec séries de codes numériques (ex. : 1xx–7xx dans l'instance NeoMakes) avec attributions de rôles |

---

## Structure des répertoires

```
your-org/
├── CLAUDE.md                  # Contexte racine pour les agents IA (généré)
├── launch.sh                  # Script de lancement quotidien (généré)
├── _standard/                 # Documents de gouvernance
│   ├── README.md              # Index principal de tous les artefacts de gouvernance
│   ├── {department}/          # Un dossier par département (ex. : strategy, operations, finance, ...)
│   │   ├── STR-{NNN}.md      #   L'instance NeoMakes utilise : ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md      #   Le vôtre peut être n'importe quoi
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Définitions des agents / membres d'équipe
│   ├── CLAUDE.md              # Règles communes de l'équipe
│   └── {agent}/               # Sous-répertoire par agent
│       ├── CLAUDE.md          # Contexte et persona de l'agent
│       └── sop.md             # SOPs de l'agent
├── _project/                  # Projets actifs
│   ├── .praxe/                # Fiches projet (métadonnées de gouvernance)
│   │   └── {project}.md       # Statut, priorité, affectation, jalons
│   └── {project}/             # Répertoire de chaque projet (code)
├── _setting/                  # Paramètres opérationnels
│   ├── permissions.md         # Matrice de contrôle d'accès
│   └── integrations.md        # Configuration des services externes
├── docs/                      # Documentation du framework
├── templates/                 # Modèles de documents réutilisables
└── examples/                  # Implémentations de référence
```

---

## Applications par domaine

### Entreprise

Associez les départements aux rôles organisationnels. Chaque département possède sa pile de gouvernance. Le document Strategy de premier niveau est la constitution de l'organisation. (L'instance NeoMakes utilise les départements CEO/COO/CFO/CTO/CDO/CHRO/CISO — le vôtre peut être n'importe quoi.)

### Laboratoire de recherche

Associez les rôles au PI, au responsable de laboratoire, au responsable financier, au responsable systèmes, aux partenariats, aux RH et à la sécurité. Utilisez la même structure de niveaux. Le document Strategy capture la mission de recherche du laboratoire et ses contraintes éthiques. Voir [docs/tutorial.md](docs/tutorial.md) pour un tutoriel complet de laboratoire de recherche.

### Productivité personnelle

Une implémentation pour une seule personne. CEO = vous. Strategy = votre mission de vie. Doctrine = vos non-négociables. Procedure = vos rituels hebdomadaires. Playbook = vos meilleures pratiques accumulées. Work Plan = votre liste quotidienne.

### Équipe d'agents IA

Chaque agent IA reçoit un `_crew/{agent}/CLAUDE.md` définissant son rôle, son niveau d'autorité et ses contraintes opérationnelles. Le `CLAUDE.md` racine est la constitution partagée de l'équipe. Les documents de niveau supérieur sont ajoutés en tête des contextes des agents avant exécution.

---

## Documentation du framework

| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Philosophie de conception, mécanismes centraux et schéma de gouvernance universel |
| [docs/getting-started.md](docs/getting-started.md) | Prérequis, installation et premiers pas |
| [docs/standard-system.md](docs/standard-system.md) | Le système de documents à 4+1 niveaux en profondeur |
| [docs/crew-system.md](docs/crew-system.md) | Gestion des agents, auto-évolution des SOP et review cascade |
| [docs/tutorial.md](docs/tutorial.md) | Tutoriel complet pour construire une équipe d'agents IA gouvernée |

---

## Exemples

- [examples/solo-dev/](examples/solo-dev/) — Développeur solo + 3 agents (configuration minimale)
- [examples/tech-startup/](examples/tech-startup/) — Startup logicielle en phase initiale
- [examples/one-piece-crew/](examples/one-piece-crew/) — Équipage fictif avec système de persona complet (démonstration)

---

## Utilisation en production — NeoMakes (Une instance)

Praxeology n'est pas théorique. Il fait tourner une vraie entreprise chaque jour. NeoMakes est une instance de ce framework — la vôtre sera différente.

**[NeoMakes, Inc.](https://neomakes.com)** opère comme une entreprise à 1 personne avec 9 agents IA gouvernés par Praxeology :

| Métrique | Valeur |
|----------|--------|
| Agents | 9 (organisés sur 7 départements C-level) |
| Règlements en vigueur | 38 (STR/DOC/PRC/PLY sur tous les départements) |
| Opérations quotidiennes | Suivi des tâches, rapports journaliers, planification hebdomadaire, revues mensuelles |
| Intégrations | Claude Code + Discord (4 canaux) + Google Drive + Notion + Calendar |
| Auto-évolution | Les agents détectent les Standard Gaps quotidiennement → Proposals hebdomadaires → Amendements mensuels |

Les agents ont des personas définis avec des **Speech Rules** (limites de phrases, ton), des **Anti-Patterns** (comportements interdits) et des **Emotional Triggers** (changements de réponse selon la situation) — garantissant un comportement cohérent et distinctif pour chacun des 9 agents.

### Guides d'intégration

| Guide | Description |
|-------|-------------|
| [Discord Integration](docs/discord-integration.md) | Structure des canaux, mentions de bots, prévention des boucles, communication bot-à-bot |
| [Google Drive Integration](docs/drive-integration.md) | Configuration des symlinks, stockage des règlements, espaces de travail par room |
| [Crew Manager Dashboard](docs/crew-manager.md) | Tableau de bord web pour le suivi des sessions, gestion des tâches, approbation des permissions |
| [Claude Code Setup](docs/claude-code-setup.md) | Hiérarchie CLAUDE.md, serveurs MCP, configuration de session par agent |
| [Work Cycle](docs/work-cycle.md) | Schémas weekly.json/todo.json, cycle de reporting, flux inverse des Standard Gaps |

---

## Origine

Praxeology a été construit par **[NeoMakes](https://neomakes.com)** — une entreprise à une seule personne développant des technologies fondamentales d'interaction humain-IA pour les environnements extrêmes. Le framework est né du besoin de gouverner une flotte croissante d'agents IA avec la même rigueur que celle appliquée aux organisations humaines.

Le nom vient de la praxéologie, l'étude de l'action humaine. L'intuition fondatrice : l'action intentionnelle a une structure. Cette structure est universelle. Rendez-la explicite, et vous pouvez tout gouverner.

---

## Licence

MIT License — voir [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
