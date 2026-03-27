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
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md"><strong>Deutsch</strong></a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## Das Problem

**Parallelisierung ist gelöst.** Today's AI coding tools diese Tools machen einzelne KI-Agenten bereits unglaublich produktiv. Fünf Agenten parallel zu betreiben ist ein gelöstes Problem.

**Koordination ist es nicht.** Wenn diese 5 Agenten ihre Arbeit beendet haben, wer löst dann Konflikte? Wer überprüft die Konsistenz? Wer verhindert, dass Agent A die Entscheidungen von Agent B überschreibt? Wer stoppt Rollendrift zwischen Sessions? Multi-Agenten-Frameworks lösen den *Start* — Praxeology löst, was danach kommt: **Koordination, Zustandsverfolgung, Konfliktlösung und evolutionäre Ausrichtung.**

**Praxeology ist die fehlende Governance-Schicht.** Sie sitzt oberhalb deiner Coding-Tools, ersetzt sie nicht — sie stellt sicher, dass deine Agenten als kohärente Organisation agieren, nicht als Sammlung unabhängiger Chatbots.

---

## Produktionsbeweis

Das ist keine Theorie. [NeoMakes](https://neomakes.com) betreibt das täglich.

> **1 Mensch + 9 KI-Agenten · 38 Governance-Regeln · 7 Abteilungen**
> Tägliche Aufgaben → Wöchentliche Reviews → Monatliche Änderungen
> Agenten erkennen Lücken, schlagen Korrekturen vor, entwickeln ihre eigenen SOPs weiter.

Jeder Agent verfügt über definierte **Speech Rules** (Satzlimits, Ton), **Anti-Patterns** (verbotene Verhaltensweisen) und **Emotional Triggers** (situationsabhängige Reaktionsänderungen) — für konsistentes, unverwechselbares Verhalten über alle 9 Agenten hinweg. NeoMakes ist eine Instanz davon. Deine wird anders aussehen.

---

## So funktioniert es

Eine 4+1-Ebenen-Governance-Hierarchie. Einfach. Universal.

```
Strategie (WHY) → Doktrin (WHAT) → Verfahren (HOW) → Playbook (PATTERNS) → Ausführung (NOW)
```

Höhere Ebenen überschreiben stets niedrigere. Keine Ausnahmen. Agenten lösen Entscheidungen, indem sie die Hierarchie nach oben durchlaufen — und auf der ersten Ebene stoppen, die die Situation abdeckt.

---

## Was es auszeichnet

Keine Funktionsliste. Ein Löser für Koordinationsprobleme.

| Dein Problem | Praxeologys Antwort |
|---|---|
| Agenten driften zwischen Sessions von ihrer Rolle ab | **ConstitutionalGuard** — 4-schichtige Verhaltensverifizierung |
| Keine Möglichkeit, Agentenaktionen sicher einzuschränken | **SafetyGate** — Höhere Ebenen sperren kritische Regeln, die niedrigere Ebenen nicht überschreiben können |
| Agenten können ihre eigenen Prozesse nicht verbessern | **SOP Evolution** — Learn-Compress-Apply-Schleife. Gradientenabstieg für Governance |
| Änderungen an einem Ort brechen einen anderen | **Review Cascade** — Bidirektionale Ausbreitung (die Hierarchie hoch und runter) |
| Agenten können keine schlechten Regeln melden | **Proposal Flow** — Strukturierte Änderungsanträge von jedem Agenten an den Gründer |
| Kein institutionelles Gedächtnis zwischen Sessions | **Work Cycle** — Tägliche Lücken → wöchentliche Vorschläge → monatliche Änderungen → vierteljährliche Reviews |

---

## Schnellstart

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # Interaktiver Assistent: Organisationsname, Mission, Abteilungen, Agenten
bash launch.sh   # Dein Governance-System ist live
```

> **Neu hier?** Starte mit dem [Schnellstart-Leitfaden](docs/quickstart.md) und dem [Rollendesign-Leitfaden](docs/role-design.md).

---

## Agenten-Design-System

Jeder Agent erhält eine `CLAUDE.md`, die nicht nur *was* er tut definiert, sondern *wie* er sich verhält:

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

Das macht Agenten **unterscheidbar, konsistent und begrenzt**. Ein QA-Agent klingt anders als ein Executor. Ein Planer schreibt niemals Code. Ein Reviewer genehmigt niemals seine eigene Arbeit. Vollständige Vorlage und Skalierungsstrategien (3 bis 15+ Agenten) im [Rollendesign-Leitfaden](docs/role-design.md).

---

## Beispiele

- [examples/solo-dev/](examples/solo-dev/) — Solo-Entwickler + 3 Agenten (minimal)
- [examples/tech-startup/](examples/tech-startup/) — Frühphasiges Softwareunternehmen
- [examples/one-piece-crew/](examples/one-piece-crew/) — Fiktive Crew mit vollständigem Persona-System

---

<details>
<summary><strong>Die Theorie — Warum das funktioniert (Der Isomorphismus)</strong></summary>

Die gleiche 4+1-Ebenen-Struktur taucht in jedem Bereich organisierten Handelns auf:

| Ebene | Nationales Recht | Militär | Unternehmen | Individuum | KI-Agent |
|------|-------------|----------|-----------|------------|----------|
| **1 Strategie** | Verfassung | Feldzugsziel | Mission & Vision | Persönliche Werte | System Prompt / Prime Directive |
| **2 Doktrin** | Gesetzesrecht | Verhaltensregeln im Gefecht | Unternehmenspolitik | Lebensprinzipien | Verhaltensrichtlinien |
| **3 Verfahren** | Vorschriften | Standardbetriebsverfahren | SOPs / Protokolle | Gewohnheiten & Routinen | Aufgabenanweisungen |
| **4 Playbook** | Fallrecht / Präzedenz | Taktiken & Übungen | Best Practices | Erlernte Muster | Few-shot-Beispiele |
| **Ausführung** | Exekutivorder | Missionsaufträge | Sprint / Arbeitsplan | Tägliche Aufgaben | Aktiver Kontext |

Governance ist nicht domänenspezifisch. Das Muster ist universal. Ein Framework, das für eine militärische Einheit funktioniert, funktioniert für ein Startup, ein Forschungslabor oder eine KI-Agentenflotte.

</details>

---

## Verzeichnisstruktur

```
your-org/
├── CLAUDE.md                  # Stammkontext für KI-Agenten (generiert)
├── launch.sh                  # Tägliches Startskript (generiert)
├── _standard/                 # Governance-Dokumente
│   ├── README.md              # Hauptindex aller Governance-Artefakte
│   ├── {department}/          # Ein Ordner pro Abteilung
│   │   ├── STR-{NNN}.md      #   (z.B. Strategie, Betrieb, Finanzen, Engineering)
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Agenten- / Teammitglied-Definitionen
│   ├── CLAUDE.md              # Gemeinsame Crew-Regeln
│   └── {agent}/               # Unterverzeichnis pro Agent
│       ├── CLAUDE.md          # Agentenkontext und Persona
│       └── sop.md             # Agenten-SOPs
├── _project/                  # Aktive Projekte
├── _setting/                  # Betriebseinstellungen
├── docs/                      # Framework-Dokumentation
├── templates/                 # Wiederverwendbare Dokumentvorlagen
└── examples/                  # Referenzimplementierungen
```

---

## Integrationsleitfäden

| Leitfaden | Beschreibung |
|-------|-------------|
| [Discord-Integration](docs/discord-integration.md) | Kanalstruktur, Bot-Erwähnungen, Schleifen-Prävention |
| [Google Drive-Integration](docs/drive-integration.md) | Symlink-Einrichtung, Regelungsspeicherung, Arbeitsbereiche |
| [Crew Manager Dashboard](docs/crew-manager.md) | Web-Dashboard zur Session-Überwachung |
| [Claude Code-Einrichtung](docs/claude-code-setup.md) | CLAUDE.md-Hierarchie, MCP-Server, agentenspezifische Sessions |
| [Work Cycle](docs/work-cycle.md) | Todo/weekly-Schemata, Berichtszyklus, Standard-Gap-Fluss |

## Dokumentation

| Dokument | Beschreibung |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Designphilosophie und Kernmechanismen |
| [docs/getting-started.md](docs/getting-started.md) | Voraussetzungen, Installation, erste Schritte |
| [docs/standard-system.md](docs/standard-system.md) | Das 4+1-Ebenen-Dokumentensystem in der Tiefe |
| [docs/crew-system.md](docs/crew-system.md) | Agentenverwaltung, SOP-Selbstentwicklung |
| [docs/tutorial.md](docs/tutorial.md) | Vollständige Anleitung zum Aufbau eines regierten Agentensteams |

---

## Entstehung

Entwickelt von **[NeoMakes](https://neomakes.com)** — einem Einzelpersonenunternehmen, das KI für Extremumgebungen entwickelt. Das Framework entstand aus der Steuerung einer KI-Agentenflotte mit derselben Strenge, die auf militärische Kommandostrukturen angewendet wird.

Der Name kommt von der Praxeologie, der Wissenschaft vom menschlichen Handeln. Zielgerichtetes Handeln hat Struktur. Diese Struktur ist universal. Mach sie explizit, und du kannst alles regieren.

---

## Lizenz

MIT-Lizenz — siehe [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
