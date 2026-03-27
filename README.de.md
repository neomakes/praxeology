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

## 🌐 Sprachen

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [中文](README.zh.md) · [Français](README.fr.md) · **Deutsch** · [Español](README.es.md)

Auch verfügbar: [QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md) · [FR](docs/quickstart.fr.md) · [DE](docs/quickstart.de.md) · [ES](docs/quickstart.es.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md) · [FR](docs/role-design.fr.md) · [DE](docs/role-design.de.md) · [ES](docs/role-design.es.md))

---

## Warum Praxeology?

Tools wie [gstack](https://github.com/gstack-io/gstack) und [oh-my-claudecode](https://github.com/anthropics/claude-code) sind hervorragend darin, einzelne KI-Agenten produktiv zu machen — Browsen, Codieren, Testen, Deployen. Wenn man jedoch von **einem Agenten** zu **vielen zusammenarbeitenden Agenten** skaliert, tritt ein neues Problem auf: **Governance**.

Ohne Governance duplizieren Agenten Arbeit, widersprechen sich gegenseitig, überschreiten Grenzen und weichen mit der Zeit von ihren vorgesehenen Rollen ab. Prompt-Engineering allein löst das nicht — man braucht eine Struktur, die über Sitzungen hinweg bestehen bleibt, sich durch den Einsatz weiterentwickelt und widerspiegelt, wie die effektivsten menschlichen Organisationen seit Jahrhunderten Handeln regeln.

Praxeology stellt diese Struktur bereit. Es ist kein Ersatz für Ihre Coding-Tools — es ist die **konstitutionelle Schicht**, die über ihnen liegt und sicherstellt, dass Ihre Agenten als kohärente Organisation und nicht als Sammlung unabhängiger Chatbots agieren.

---

## Was ist das?

**Praxeology** ist ein kollaboratives Betriebssystem für Mensch und KI, aufgebaut auf einer universellen 4+1-stufigen Governance-Hierarchie. Menschen legen Strategie und Prinzipien fest; agentische KI führt innerhalb dieser Grenzen aus, lernt aus Erfahrungen und schlägt Verbesserungen zurück vor. Es erfasst die Beobachtung, dass jedes zielgerichtete Handeln — von Nationen bis zu agentischer KI — demselben strukturellen Muster folgt.

```
Strategy (WARUM) → Doctrine (WAS) → Procedure (WIE) → Playbook (MUSTER) → Execution (JETZT)
```

Höhere Stufen überschreiben stets niedrigere. Keine Ausnahmen.

---

## Der Isomorphismus

Dieselbe 4+1-stufige Struktur erscheint in jedem Bereich organisierten Handelns:

| Stufe | Nationales Recht | Militär | Unternehmen | Individuum | KI-Agent |
|-------|-----------------|---------|-------------|------------|----------|
| **1 Strategy** | Verfassung | Kampagnenziel | Mission & Vision | Persönliche Werte | System Prompt / Prime Directive |
| **2 Doctrine** | Gesetzesrecht | Einsatzregeln | Unternehmenspolitik | Lebensprinzipien | Behavioral Guidelines |
| **3 Procedure** | Verordnungen | Standard Operating Procedures | SOPs / Protokolle | Gewohnheiten & Routinen | Task Instructions |
| **4 Playbook** | Fallrecht / Präzedenz | Taktiken & Übungen | Best Practices | Erlernte Muster | Few-shot Examples |
| **Exec Work Plan** | Exekutivorder | Missionsaufträge | Sprint / Arbeitsplan | Tägliche To-Do-Liste | Active Context |

Dieser Isomorphismus ist die Kernthese: Governance ist nicht domänenspezifisch. Das Muster ist universell. Ein Framework, das für eine Militäreinheit funktioniert, funktioniert auch für ein Startup, ein Forschungslabor oder eine KI-Agenten-Flotte.

---

## Schnellstart

**Schritt 1 — Klonen**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**Schritt 2 — Setup ausführen**

```bash
bash setup.sh
```

Der interaktive Assistent fragt nach Ihrem Organisationsnamen, der Mission, Abteilungen, Agenten und Projekten. Er generiert die vollständige Verzeichnisstruktur und alle Bootstrap-Dokumente.

**Schritt 3 — Starten**

```bash
bash launch.sh
```

Ihr Governance-System ist live. Öffnen Sie `CLAUDE.md` im Stammverzeichnis, um den generierten Kontext für KI-Agenten zu sehen.

> **Neu bei Praxeology?** Beginnen Sie mit [docs/quickstart.md](docs/quickstart.md) für eine 3-Schritte-Anleitung und [docs/role-design.md](docs/role-design.md) zum Entwerfen Ihrer Agenten.

---

## Hauptfunktionen

| Funktion | Beschreibung |
|----------|-------------|
| **SafetyGate** | Dokumente höherer Stufen können harte Grenzen deklarieren, die kein Dokument niedrigerer Stufe überschreiben kann |
| **Proposal Flow** | Jeder Agent oder jedes Teammitglied kann eine Änderung über das strukturierte Proposal-Format vorschlagen |
| **SOP Evolution** | Procedures und Playbooks entwickeln sich durch die Review Cascade vor der Beförderung weiter |
| **Review Cascade** | Änderungen propagieren aufwärts: Playbook → Procedure → Doctrine → Strategy für Konsistenzprüfungen |
| **Reverse Flow** | Strategy-Änderungen kaskadieren abwärts: alle niedrigeren Stufen werden zur Überprüfung markiert |
| **Department Codes** | Abteilungen mit numerischen Codeserien (z. B. 1xx–7xx in der NeoMakes-Instanz) mit Rollen- und Mitarbeiterzuweisungen |

---

## Verzeichnisstruktur

```
your-org/
├── CLAUDE.md                  # Stammkontext für KI-Agenten (generiert)
├── launch.sh                  # Tägliches Startskript (generiert)
├── _standard/                 # Governance-Dokumente
│   ├── README.md              # Hauptindex aller Governance-Artefakte
│   ├── {department}/          # Ein Ordner pro Abteilung (z. B. strategy, operations, finance, ...)
│   │   ├── STR-{NNN}.md      #   Die NeoMakes-Instanz verwendet: ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md      #   Ihres kann beliebig benannt werden
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Agent- / Teammitglied-Definitionen
│   ├── CLAUDE.md              # Gemeinsame Team-Regeln
│   └── {agent}/               # Unterverzeichnis pro Agent
│       ├── CLAUDE.md          # Agentenkontext und Persona
│       └── sop.md             # Agenten-SOPs
├── _project/                  # Aktive Projekte
│   ├── .praxe/                # Projektkarten (Governance-Metadaten)
│   │   └── {project}.md       # Status, Priorität, Crew-Zuweisung, Meilensteine
│   └── {project}/             # Jedes Projektverzeichnis (Code)
├── _setting/                  # Betriebseinstellungen
│   ├── permissions.md         # Zugriffssteuerungsmatrix
│   └── integrations.md        # Konfiguration externer Dienste
├── docs/                      # Framework-Dokumentation
├── templates/                 # Wiederverwendbare Dokumentvorlagen
└── examples/                  # Referenzimplementierungen
```

---

## Domänenanwendungen

### Unternehmen

Ordnen Sie Abteilungen den Organisationsrollen zu. Jede Abteilung besitzt ihren eigenen Governance-Stack. Das Strategy-Dokument der obersten Ebene ist die Unternehmensverfassung. (Die NeoMakes-Instanz verwendet die Abteilungen CEO/COO/CFO/CTO/CDO/CHRO/CISO — Ihres kann beliebig sein.)

### Forschungslabor

Ordnen Sie Rollen dem PI, Lab Manager, Finance Lead, Systems Lead, Partnerships, HR und Security zu. Verwenden Sie dieselbe Stufenstruktur. Das Strategy-Dokument erfasst die Forschungsmission des Labors und ethische Einschränkungen. Siehe [docs/tutorial.md](docs/tutorial.md) für eine vollständige Anleitung für Forschungslabore.

### Persönliche Produktivität

Eine Einzelpersonen-Implementierung. CEO = Sie. Strategy = Ihre Lebensmission. Doctrine = Ihre Nicht-Verhandelbaren. Procedure = Ihre wöchentlichen Rituale. Playbook = Ihre angesammelten Best Practices. Work Plan = Ihre tägliche Liste.

### KI-Agenten-Team

Jeder KI-Agent erhält eine `_crew/{agent}/CLAUDE.md`, die seine Rolle, sein Autoritätsniveau und seine Betriebsbeschränkungen definiert. Die Stamm-`CLAUDE.md` ist die gemeinsame Verfassung des Teams. Dokumente höherer Stufen werden den Agentenkontexten vor der Ausführung vorangestellt.

---

## Framework-Dokumentation

| Dokument | Beschreibung |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Designphilosophie, Kernmechanismen und das universelle Governance-Muster |
| [docs/getting-started.md](docs/getting-started.md) | Voraussetzungen, Installation und erste Schritte |
| [docs/standard-system.md](docs/standard-system.md) | Das 4+1-stufige Dokumentsystem in der Tiefe |
| [docs/crew-system.md](docs/crew-system.md) | Agentenverwaltung, SOP-Selbstevolution und Review Cascade |
| [docs/tutorial.md](docs/tutorial.md) | Vollständige Anleitung zum Aufbau eines regierten KI-Agenten-Teams |

---

## Beispiele

- [examples/solo-dev/](examples/solo-dev/) — Solo-Entwickler + 3 Agenten (minimale Einrichtung)
- [examples/tech-startup/](examples/tech-startup/) — Software-Unternehmen in der Frühphase
- [examples/one-piece-crew/](examples/one-piece-crew/) — Fiktive Crew mit vollständigem Persona-System (Demonstration)

---

## Produktiveinsatz — NeoMakes (Eine Instanz)

Praxeology ist nicht theoretisch. Es betreibt täglich ein echtes Unternehmen. NeoMakes ist eine Instanz dieses Frameworks — Ihre wird anders aussehen.

**[NeoMakes, Inc.](https://neomakes.com)** operiert als 1-Personen-Unternehmen mit 9 KI-Agenten, die durch Praxeology gesteuert werden:

| Kennzahl | Wert |
|----------|------|
| Agenten | 9 (organisiert in 7 C-Level-Abteilungen) |
| Erlassene Regelungen | 38 (STR/DOC/PRC/PLY über alle Abteilungen) |
| Tägliche Operationen | Aufgabenverfolgung, Tagesberichte, Wochenplanung, Monatsreviews |
| Integrationen | Claude Code + Discord (4 Kanäle) + Google Drive + Notion + Calendar |
| Selbstevolution | Agenten erkennen Standard Gaps täglich → Proposals wöchentlich → Amendments monatlich |

Die Agenten haben definierte Personas mit **Speech Rules** (Satzlimits, Ton), **Anti-Patterns** (verbotene Verhaltensweisen) und **Emotional Triggers** (situationsabhängige Reaktionsänderungen) — was konsistentes, unterscheidbares Verhalten aller 9 Agenten gewährleistet.

### Integrationsleitfäden

| Leitfaden | Beschreibung |
|-----------|-------------|
| [Discord Integration](docs/discord-integration.md) | Kanalstruktur, Bot-Erwähnungen, Schleifen-Prävention, Bot-zu-Bot-Kommunikation |
| [Google Drive Integration](docs/drive-integration.md) | Symlink-Einrichtung, Regelungsspeicherung, raumbasierte Arbeitsbereiche |
| [Crew Manager Dashboard](docs/crew-manager.md) | Web-Dashboard für Sitzungsüberwachung, Aufgabenverwaltung, Berechtigungsgenehmigung |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md-Hierarchie, MCP-Server, agentenbezogene Sitzungskonfiguration |
| [Work Cycle](docs/work-cycle.md) | weekly.json/todo.json-Schemata, Berichtszyklus, Standard-Gap-Rückfluss |

---

## Ursprung

Praxeology wurde von **[NeoMakes](https://neomakes.com)** entwickelt — einem Einzelpersonen-Unternehmen, das grundlegende Mensch-KI-Interaktionstechnologien für Extremumgebungen entwickelt. Das Framework entstand aus dem Bedürfnis, eine wachsende Flotte von KI-Agenten mit derselben Strenge zu regieren, die auf menschliche Organisationen angewendet wird.

Der Name stammt von der Praxeologie, der Wissenschaft vom menschlichen Handeln. Die Erkenntnis: zielgerichtetes Handeln hat Struktur. Diese Struktur ist universell. Machen Sie sie explizit, und Sie können alles regieren.

---

## Lizenz

MIT License — siehe [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
