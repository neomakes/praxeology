# Praxeology — Schnellstartanleitung

Bauen Sie in 3 Schritten Ihr eigenes selbstevolvierendes KI-Agenten-Governance-System.

---

## Schritt 1: Ihre Mission definieren (STR)

Schreiben Sie das WARUM Ihrer Organisation in `_standard/{department}/STR-101.md`.

Eine Vorlage finden Sie unter `templates/_standard/`. Füllen Sie aus:

- **Mission** — ein Satz darüber, wozu Sie existieren
- **Values** — 3–5 Grundsätze, die jede Entscheidung leiten
- **Non-negotiables** — harte Grenzen, die Agenten unabhängig von Anweisungen niemals überschreiten dürfen

Dies ist die Verfassung Ihrer Agenten. Jede Governance-Regel, jedes Agentenverhalten und jeder Änderungsvorschlag muss damit vereinbar sein. Bei Regelkonflikten gewinnt STR.

---

## Schritt 2: Ihr Team zusammenstellen

Entscheiden Sie, wie viele Agenten Sie benötigen. Mindestens 2, empfohlen 3–9. Jeder Agent ist einem Bereich zugeordnet (Engineering, Finanzen, Sicherheit, Betrieb usw.).

Erstellen Sie für jeden Agenten `_crew/{name}/CLAUDE.md` mit diesen Abschnitten:

- **Identity** — Name, Rollenbezeichnung, Abteilung
- **Persona & Character** — Persönlichkeitsmerkmale, die das Verhalten unter Druck bestimmen
- **Speech Rules** — Satzlimits, Ton, verbotene Formulierungen, einzigartige Ausdrücke
- **Anti-Patterns** — explizite Liste dessen, was dieser Agent niemals tun darf
- **Emotional Triggers** — wie sich der Antwortstil je nach Situation verändert (Routine, Krise, Konflikt)
- **Values** — was dieser Agent optimiert, wenn Regeln die Situation nicht abdecken
- **Boundaries** — welche Bereiche anderen Agenten gehören (verhindert Überschneidungskonflikte)

Erstellen Sie dann `_crew/CLAUDE.md` mit Regeln, die für alle Agenten gleichermaßen gelten: gemeinsame Kommunikationsstandards, Eskalationsprotokoll, agentenübergreifende Erwähnungsregeln und Berichtsrhythmus.

Ausführliche Anleitungen und ausgearbeitete Beispiele finden Sie in `role-design.de.md`.

---

## Schritt 3: Governance aufsetzen

Starten Sie den interaktiven Assistenten:

```bash
bash setup.sh
```

Oder erstellen Sie die vier Kerndokumente manuell:

| Dokument | Pfad | Zweck |
|---|---|---|
| DOC-101 | `_standard/{department}/DOC-101.md` | Governance-Wächter — was Agenten überschreiben können und was nicht |
| DOC-102 | `_standard/{department}/DOC-102.md` | Sicherheit — Genehmigungsanforderungen für destruktive oder irreversible Aktionen |
| PRC-201 | `_standard/{department}/PRC-201.md` | Sitzungsverwaltung — wie Sitzungen starten, laufen und enden |
| PLY-203 | `_standard/{department}/PLY-203.md` | Selbstentwicklung — wie Agenten Lücken erkennen und Verbesserungen vorschlagen |

Vorlagen für alle vier Dokumente befinden sich in `templates/_standard/`.

---

## Was als nächstes passiert

Nach der Bereitstellung werden Ihre Agenten:

1. **Der Governance-Hierarchie folgen** für jede Entscheidung: PLY (Playbooks) zuerst, dann PRC (Verfahren), dann DOC (Doktrin), dann STR (Strategie). Wenn die aktuelle Ebene die Frage löst, handeln sie. Andernfalls eskalieren sie zur nächsten Ebene.
2. **Standard Gaps protokollieren**, wenn eine Situation nicht durch bestehende Regeln abgedeckt ist — anstatt stillschweigend zu improvisieren.
3. **Änderungen vorschlagen** über den Proposal-Mechanismus, wenn eine Lücke wiederholt auftritt, sodass die Governance mit dem realen Einsatz wächst.
4. **Ihre eigenen SOPs weiterentwickeln** über die Learn-Compress-Apply-Schleife, definiert in PLY-203.

Das System ist so konzipiert, dass Governance durch Nutzung enger wird — nicht durch manuelle Audits.

---

## Skalierung

| Konfiguration | Referenz |
|---|---|
| 1 Person + Startup-Team | `examples/tech-startup/` |
| Vollständiges Team mit 9 Agenten | `examples/one-piece-crew/` |

Beide Beispiele enthalten vorausgefüllte STR- und CLAUDE.md-Dateien sowie vorgefertigte Governance-Dokumente, die Sie direkt anpassen können.
