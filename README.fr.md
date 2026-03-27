<p align="center">
  <img src="assets/banner.svg" alt="Praxeology — The governance layer that keeps your AI agent team aligned, evolving, and accountable." width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.fr.md"><strong>Français</strong></a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## Le problème

**La parallélisation est résolue.** Today's AI coding tools ces outils rendent déjà les agents IA individuels incroyablement productifs. Faire tourner 5 agents en parallèle est un problème résolu.

**La coordination, non.** Quand ces 5 agents ont terminé leur travail, qui résout les conflits ? Qui vérifie la cohérence ? Qui empêche l'agent A d'écraser les décisions de l'agent B ? Qui arrête la dérive de rôle entre les sessions ? Les frameworks multi-agents résolvent le *démarrage* — Praxeology résout ce qui vient après : **la coordination, le suivi d'état, la résolution de conflits et l'alignement évolutif.**

**Praxeology est la couche de gouvernance manquante.** Elle se place au-dessus de vos outils de codage, sans les remplacer — en s'assurant que vos agents fonctionnent comme une organisation cohérente plutôt qu'une collection de chatbots indépendants.

---

## Preuve en production

Ce n'est pas de la théorie. [NeoMakes](https://neomakes.com) fait tourner cela chaque jour.

> **1 humain + 9 agents IA · 38 règles de gouvernance · 7 départements**
> Tâches quotidiennes → Revues hebdomadaires → Amendements mensuels
> Les agents détectent les lacunes, proposent des corrections, font évoluer leurs propres SOP.

Chaque agent dispose de **Speech Rules** (limites de phrases, ton), d'**Anti-Patterns** (comportements interdits) et d'**Emotional Triggers** (changements de réponse selon la situation) — garantissant un comportement cohérent et distinctif entre les 9 agents. NeoMakes est une instance. La vôtre sera différente.

---

## Comment ça fonctionne

Une hiérarchie de gouvernance à 4+1 niveaux. Simple. Universel.

```
Stratégie (WHY) → Doctrine (WHAT) → Procédure (HOW) → Playbook (PATTERNS) → Exécution (NOW)
```

Les niveaux supérieurs priment toujours sur les niveaux inférieurs. Sans exception. Les agents résolvent les décisions en remontant la hiérarchie — s'arrêtant au premier niveau qui couvre la situation.

---

## Ce qui le distingue

Pas une liste de fonctionnalités. Un résolveur de problèmes de coordination.

| Votre problème | La réponse de Praxeology |
|---|---|
| Les agents dérivent de leur rôle entre les sessions | **ConstitutionalGuard** — Vérification comportementale à 4 couches |
| Aucun moyen de contraindre les actions des agents en toute sécurité | **SafetyGate** — Les niveaux supérieurs verrouillent les règles critiques que les niveaux inférieurs ne peuvent pas écraser |
| Les agents ne peuvent pas améliorer leurs propres processus | **SOP Evolution** — Boucle Learn-Compress-Apply. Descente de gradient pour la gouvernance |
| Les changements à un endroit cassent un autre | **Review Cascade** — Propagation bidirectionnelle (en montant et descendant la hiérarchie) |
| Les agents ne peuvent pas signaler quand les règles sont mauvaises | **Proposal Flow** — Demandes d'amendement structurées de tout agent vers le fondateur |
| Pas de mémoire institutionnelle entre les sessions | **Work Cycle** — Lacunes quotidiennes → propositions hebdomadaires → amendements mensuels → revues trimestrielles |

---

## Démarrage rapide

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # Assistant interactif : nom d'organisation, mission, départements, agents
bash launch.sh   # Votre système de gouvernance est en ligne
```

> **Nouveau ?** Commencez par le [Guide de démarrage rapide](docs/quickstart.md) et le [Guide de conception des rôles](docs/role-design.md).

---

## Système de conception des agents

Chaque agent reçoit un `CLAUDE.md` qui définit non seulement *ce qu'il fait*, mais *comment il se comporte* :

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

Cela rend les agents **distinguables, cohérents et bornés**. Un agent QA sonne différemment d'un exécuteur. Un planificateur n'écrit jamais de code. Un réviseur n'approuve jamais son propre travail. Voir le [Guide de conception des rôles](docs/role-design.md) pour le modèle complet et les stratégies de mise à l'échelle (de 3 à 15+ agents).

---

## Exemples

- [examples/solo-dev/](examples/solo-dev/) — Développeur solo + 3 agents (minimal)
- [examples/tech-startup/](examples/tech-startup/) — Entreprise logicielle en phase initiale
- [examples/one-piece-crew/](examples/one-piece-crew/) — Équipage fictif avec système de persona complet

---

<details>
<summary><strong>La théorie — Pourquoi ça fonctionne (L'isomorphisme)</strong></summary>

La même structure à 4+1 niveaux apparaît dans tous les domaines de l'action organisée :

| Niveau | Droit national | Militaire | Entreprise | Individu | Agent IA |
|------|-------------|----------|-----------|------------|----------|
| **1 Stratégie** | Constitution | Objectif de campagne | Mission & Vision | Valeurs personnelles | System Prompt / Prime Directive |
| **2 Doctrine** | Loi statutaire | Règles d'engagement | Politique d'entreprise | Principes de vie | Directives comportementales |
| **3 Procédure** | Réglementations | Procédures opérationnelles standard | SOP / Protocoles | Habitudes & Routines | Instructions de tâches |
| **4 Playbook** | Droit jurisprudentiel / Précédent | Tactiques & Exercices | Meilleures pratiques | Modèles appris | Exemples few-shot |
| **Exec** | Ordonnance exécutive | Ordres de mission | Sprint / Plan de travail | Liste quotidienne | Contexte actif |

La gouvernance n'est pas spécifique à un domaine. Le modèle est universel. Un framework qui fonctionne pour une unité militaire fonctionne pour une startup, un laboratoire de recherche ou une flotte d'agents IA.

</details>

---

## Structure des répertoires

```
your-org/
├── CLAUDE.md                  # Contexte racine pour les agents IA (généré)
├── launch.sh                  # Script de lancement quotidien (généré)
├── _standard/                 # Documents de gouvernance
│   ├── README.md              # Index principal de tous les artefacts de gouvernance
│   ├── {department}/          # Un dossier par département
│   │   ├── STR-{NNN}.md      #   (ex. stratégie, opérations, finance, ingénierie)
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Définitions des agents / membres d'équipe
│   ├── CLAUDE.md              # Règles d'équipe partagées
│   └── {agent}/               # Sous-répertoire par agent
│       ├── CLAUDE.md          # Contexte et persona de l'agent
│       └── sop.md             # SOP de l'agent
├── _project/                  # Projets actifs
├── _setting/                  # Paramètres opérationnels
├── docs/                      # Documentation du framework
├── templates/                 # Modèles de documents réutilisables
└── examples/                  # Implémentations de référence
```

---

## Guides d'intégration

| Guide | Description |
|-------|-------------|
| [Intégration Discord](docs/discord-integration.md) | Structure des canaux, mentions de bots, prévention des boucles |
| [Intégration Google Drive](docs/drive-integration.md) | Configuration des liens symboliques, stockage des règlements, espaces de travail |
| [Tableau de bord Crew Manager](docs/crew-manager.md) | Tableau de bord Web pour la surveillance des sessions |
| [Configuration Claude Code](docs/claude-code-setup.md) | Hiérarchie CLAUDE.md, serveurs MCP, sessions par agent |
| [Work Cycle](docs/work-cycle.md) | Schémas Todo/weekly, cycle de reporting, flux Standard Gap |

## Documentation

| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Philosophie de conception et mécanismes fondamentaux |
| [docs/getting-started.md](docs/getting-started.md) | Prérequis, installation, premières étapes |
| [docs/standard-system.md](docs/standard-system.md) | Le système documentaire à 4+1 niveaux en profondeur |
| [docs/crew-system.md](docs/crew-system.md) | Gestion des agents, auto-évolution des SOP |
| [docs/tutorial.md](docs/tutorial.md) | Tutoriel complet pour construire une équipe d'agents gouvernée |

---

## Origine

Construit par **[NeoMakes](https://neomakes.com)** — une entreprise unipersonnelle développant une IA embarquée pour les environnements extrêmes. Le framework est né de la gouvernance d'une flotte d'agents IA avec la même rigueur appliquée aux structures de commandement militaire.

Le nom vient de la praxéologie, l'étude de l'action humaine. L'action intentionnelle a une structure. Cette structure est universelle. Rendez-la explicite, et vous pouvez gouverner n'importe quoi.

---

## Licence

Licence MIT — voir [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
