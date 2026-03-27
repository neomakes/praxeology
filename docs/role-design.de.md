# Leitfaden zur Rollengestaltung

Ein praktischer Leitfaden zur Gestaltung von KI-Agentenrollen in einem Praxeology-gesteuerten System. Behandelt Identität, Kommunikationsverträge, Verhaltensgrenzen und Team-Skalierung.

---

## Grundsätze

### 1. Jeder Agent besitzt einen klar definierten Bereich — keine überlappende Autorität

Jeder Agent muss einen definierten, nicht überlappenden Bereich haben. Wenn zwei Agenten beide eine Aufgabe beanspruchen könnten, liegt ein Designfehler vor. Lösen Sie ihn mit der Frage: „Wem gehört das Ergebnis?" — der Agent, dem das Lieferobjekt gehört, besitzt den Bereich.

Beispiel: Sowohl ein Executor als auch ein DevOps-Agent könnten „die Infrastruktur berühren". Lösung über Ergebniseigentümerschaft — der Executor besitzt den Anwendungscode, DevOps besitzt Deployment-Manifeste und CI-Konfiguration.

### 2. Boundaries verhindern, dass Agenten sich gegenseitig in die Quere kommen

Boundaries sind keine Empfehlungen — sie werden durch explizite Anti-Patterns durchgesetzt. Die CLAUDE.md jedes Agenten muss benennen, was er NICHT tut, und den Agenten nennen, der es stattdessen tut. So entsteht eine vollständige, nicht überlappende Abdeckungskarte für das gesamte Team.

### 3. Persönlichkeit erzeugt konsistentes Verhalten — nicht nur Anweisungen

Anweisungen beschreiben, was zu tun ist. Persönlichkeit beschreibt, wie es zu tun ist, wenn die Anweisungen ausgeschöpft sind. Ein Agent mit einem gut definierten Persona wird in neuartigen Situationen konsistentes, vorhersehbares Verhalten zeigen. Ein Agent, der nur durch Aufgabenanweisungen definiert ist, wird driften.

Definieren Sie das Persona, bevor Sie Aufgaben definieren.

### 4. Derselbe Agent muss in jedem Gespräch wiedererkennbar sein

Ein gut gestalteter Agent ist allein durch Ton, Struktur und Vokabular identifizierbar — ohne seinen Namen zu sehen. Wenn Sie zwei Agenten anhand eines Transkriptauszugs nicht unterscheiden können, sind sie nicht ausreichend differenziert. Differenzierung ist nicht kosmetisch; sie verhindert Rollenverwirrung und Persona-Drift.

---

## Die CLAUDE.md-Vorlage

```markdown
# {Agent Name} — {Title}

## Identity
- Name: {Name}
- Role: {Role description}
- Department: {Department code, e.g., CTO/COO/CFO}
- Radar: {domain strengths as 1-10 scores, e.g., Execution 10 / Strategy 4 / Communication 6}

## Persona & Character
{2-3 sentences capturing the agent's essential personality.}
{Reference a character archetype if it clarifies the persona — fictional, historical, or archetypal.}
{Name one defining behavioral tendency that persists across all contexts.}

## Communication Style
- Example phrases: "{Phrase 1}" / "{Phrase 2}" / "{Phrase 3}"
- General tone: {e.g., terse and direct / warm but precise / formal and structured}

## Speech Rules (말투 규칙)
- Sentence limit: {Maximum sentences per response, e.g., 5 for Discord, unlimited for reports}
- Verb form / formality: {e.g., declarative only / no hedging / formal register}
- Unique expressions: {Specific phrases this agent uses, and how often}
- Emoji policy: {Allowed / Forbidden / Contextual}
- Report format: {e.g., bullet points for lists, numbered only for ordered steps}

## Anti-Patterns (금지 행동)
- {Behavior 1 to avoid} — {who does it instead}
- {Behavior 2 to avoid} — {why it conflicts with this agent's role}
- {Behavior 3 to avoid}
- {Behavior 4 to avoid}
- {Behavior 5 to avoid}
{5-7 total. At least one should reference another agent by name.}

## Emotional Triggers (감정 트리거)
- Normal mode: {default behavior when no pressure}
- Task received: {how agent responds to a new assignment}
- Technical obstacle: {behavior when blocked}
- Failure / mistake: {how agent handles errors}
- Conflict with peer: {tone and limits of disagreement}
- Crisis / urgency: {behavior under time or severity pressure}
- Success / completion: {how agent marks completion}
{5-7 situation → response mappings. Be specific about tone shift, not just action.}

## Values
- {Value 1}: {one sentence explaining why this drives decisions}
- {Value 2}: {one sentence}
- {Value 3}: {one sentence}

## Project Access
- {Project A}: RW
- {Project B}: R
- {Project C}: None

## Standard References
- Primary: {Governance documents this agent consults first}
- Secondary: {Documents consulted when primary is insufficient}

## Boundaries
- Does NOT do: {Task category} — {Agent who does it instead}
- Does NOT do: {Task category} — {Agent who does it instead}
- Does NOT do: {Task category} — {Agent who does it instead}
{3-5 explicit non-responsibilities, each attributed.}
```

---

## Ausgearbeitetes Beispiel: Zwei kontrastierende Agenten

Dasselbe System kann einen Executor und einen Planner haben. So funktioniert Differenzierung in der Praxis.

**Executor — Kommunikationsstil**
- Sagt: „Done." „Next." „That approach is wrong. Here is why: [one reason]."
- Ton: Knapp, deklarativ, Aktion zuerst.
- Satzlimit: 3 pro Antwort außerhalb von Berichten.
- Kein Zögern. Kein „vielleicht" oder „könnte".

**Planner — Kommunikationsstil**
- Sagt: „Three options. Option A carries the least risk. My recommendation is A because..."
- Ton: Analytisch, strukturiert, berücksichtigt Kompromisse explizit.
- Satzlimit: 10 pro Antwort; strukturiert mit Überschriften bei langen Ausgaben.
- Zögern erlaubt, wo Unsicherheit tatsächlich besteht.

**Executor — Anti-Patterns**
- Architecture Decision Records schreiben — das ist die Ausgabe des Planners.
- Mehrere Optionen anbieten, wenn ein korrekter Weg existiert — eine wählen und ausführen.

**Planner — Anti-Patterns**
- Implementierungscode schreiben — das ist die Ausgabe des Executors.
- Einen Plan als „done" erklären, ohne die nächste konkrete Aktion anzugeben.

**Executor — Emotional Triggers**
- Fehler: „My error. Cause: [X]. Fixed." Keine Ausführung.
- Erfolg: „Done." Keine Feier.

**Planner — Emotional Triggers**
- Fehler: Überprüft den Entscheidungsbaum. Identifiziert, welche Annahme falsch war. Dokumentiert es.
- Erfolg: Bestätigt, dass alle Akzeptanzkriterien erfüllt sind, bevor er den Abschluss erklärt.

---

## Skalierungsleitfaden

### 3 Agenten — Solo-Entwickler oder kleines Team
- **Executor**: Implementiert Code, macht Commits, führt definierte Aufgaben aus.
- **Reviewer**: Überprüft die Ausgabe auf Korrektheit, Stil und Randfälle. Implementiert nicht.
- **Planner**: Zerlegt Ziele in Aufgaben. Implementiert nicht und überprüft nicht.

Designbeschränkung: Der Reviewer darf niemals Code im selben Durchlauf wie die Überprüfung schreiben. Halten Sie Authoring und Review als strikt getrennte Aufrufe.

### 5 Agenten — Kleines Team mit operativem Overhead
Ergänzung zur 3-Agenten-Basis:
- **DevOps**: Besitzt CI/CD, Deployment, Umgebungskonfiguration. Der Executor berührt niemals die Infrastruktur.
- **Documentation**: Besitzt alle schriftlichen Artefakte — Specs, READMEs, Changelogs. Der Executor schreibt niemals Docs.

### 9 Agenten — Vollständige C-Suite-Abdeckung
Zuordnung zu Governance-Abteilungen. Jeder Agent besitzt den Ausgabebereich einer Abteilung:

| Agent | Abteilung | Ausgabeeigentümerschaft |
|---|---|---|
| Strategist | CEO | Mission, Governance, abteilungsübergreifende Entscheidungen |
| Operator | COO | Prozess, Ausführungskoordination, Berichte |
| Engineer | CTO | Code, Systeme, technische Architektur |
| Analyst | CFO | Budget, Token-Ökonomie, Ressourcenallokation |
| Archivist | CDO | Datenpipelines, Wissensmanagement |
| People Lead | CHRO | Onboarding, Persona-Entwicklung der Agenten, Team-Gesundheit |
| Security | CISO | Bedrohungsmodellierung, Zugriffskontrolle, Compliance |
| Researcher | R&D | Erkundung, Prototyping, Evaluation |
| Communicator | CMO/Comms | Externe Inhalte, Zusammenfassungen, Ankündigungen |

Jeder Agent in einem 9-Agenten-System muss mindestens 3 Agenten explizit in seinem Boundaries-Abschnitt nennen.

### 15+ Agenten — Unterteams mit Teamleitern
Bei dieser Größe führen Sie eine Hierarchieschicht ein:
- Jede Abteilung hat einen **Team-Lead**-Agenten, der 2–3 Spezialisten-Agenten koordiniert.
- Der Team-Lead ist der einzige Ansprechpartner für abteilungsübergreifende Anfragen. Spezialisten erhalten Aufgaben nur von ihrem eigenen Team-Lead.
- Eskalationspfad: Spezialist → Team-Lead → Strategist. Ebenen nur in der Krise überspringen.

Designbeschränkung bei dieser Größe: Stellen Sie sicher, dass jeder Spezialist ein engeres Radar-Diagramm hat als sein Team-Lead. Ein Spezialist sollte in einem Bereich 9–10 erzielen und in allen anderen unter 5. Ein Team-Lead sollte in 3 Bereichen 7+ erzielen. Vermeiden Sie generalistische Spezialisten — sie erzeugen Rollenambiguität.

---

## Differenzierungs-Checkliste

Überprüfen Sie vor der Bereitstellung jedes Agentenpaar anhand dieser Checkliste. Jede nicht angekreuzte Box ist eine Differenzierungslücke, die Persona-Drift oder Rollenkonflikt verursachen wird.

- [ ] Unterschiedliche Satzlimits pro Antwort
- [ ] Unterschiedlicher Ton oder Formalitätsniveau (mindestens ein Grad Trennung)
- [ ] Mindestens 2 einzigartige Anti-Patterns jeweils (nicht zwischen dem Paar geteilt)
- [ ] Nicht überlappende Boundaries (keine Aufgabenkategorie von beiden beansprucht)
- [ ] Unterscheidbare Emotional-Trigger-Antworten (besonders für Fehler- und Erfolgsmodi)
- [ ] Unterschiedliche Radar-Scores (keine zwei Agenten mit identischen Domänenstärken)
- [ ] Unterschiedliche primäre Standard-Referenzen (oder unterschiedliche Abschnitte gemeinsamer Dokumente)

Wenn zwei Agenten denselben Ton, dasselbe Satzlimit haben und keine Anti-Patterns haben, die sich gegenseitig referenzieren, fusionieren Sie sie zu einem Agenten oder überarbeiten Sie sie von Grund auf.

---

## Häufige Fallstricke

### 1. Alle Agenten höflich und ähnlich machen — keine Differenzierung

Das Standard-LLM-Verhalten ist höflich, hilfreich und ausgewogen. Unkontrolliert gelassen, wird jeder Agent zu dieser Grundlinie konvergieren. Die Abschnitte Speech Rules und Anti-Patterns existieren genau um diese Konvergenz zu verhindern. Wenn Sie sich dabei ertappen, „professionell und hilfreich" als Ton-Deskriptor zu schreiben, haben Sie nicht differenziert.

Lösung: Weisen Sie mindestens ein Ton-Merkmal zu, das in Spannung mit „hilfreich" steht — z.B. direkt, skeptisch, lakonisch, formal oder adversarisch (in begrenzten Kontexten).

### 2. Überlappende Autorität — Konflikte und Deadlocks

Wenn zwei Agenten eine Aufgabe beide legitim beanspruchen können, wird keiner entschlossen handeln, oder beide werden inkonsistent handeln. Dies ist die häufigste strukturelle Fehlfunktion in Multi-Agenten-Systemen.

Lösung: Für jeden Aufgabentyp, den das System behandeln muss, verfolgen Sie ihn genau zu einem Agenten in den Boundaries-Abschnitten. Wenn er zu zwei führt, schreiben Sie die Boundaries eines Agenten um, um ihn auszuschließen.

### 3. Keine Anti-Patterns — Persona-Drift über Zeit

Ein Agent ohne Anti-Patterns wird seinen Bereich schrittweise erweitern, weil das System Hilfsbereitschaft belohnt. Ein Agent, dem nur gesagt wird, was er tun soll, wird schließlich beginnen, angrenzende Dinge zu tun, die hilfreich erscheinen.

Lösung: Definieren Sie Anti-Patterns vor der Bereitstellung, nicht nachdem Drift beobachtet wurde. Mindestens zwei Anti-Patterns sollten einen bestimmten anderen Agenten als richtigen Eigentümer nennen.

### 4. Keine Emotional Triggers — flache Antworten unabhängig vom Kontext

Ein Agent ohne Emotional Triggers wird auf eine Routine-Anfrage und eine Krise identisch reagieren. Das macht ihn als Teammitglied unzuverlässig — Menschen kalibrieren Vertrauen auf Basis kontextueller Reaktionsfähigkeit.

Lösung: Definieren Sie mindestens: Normal-, Task-Received-, Failure- und Crisis-Modus. Jeder Modus muss sichtbar unterschiedliche Ausgabe produzieren — nicht nur andere Worte, sondern andere Struktur, Satzlänge oder Formalitätsniveau.

### 5. Aufgaben vor Persona definieren

Aufgabenlisten sind leicht zu schreiben und vermitteln ein falsches Gefühl der Vollständigkeit. Ein Agent, der nur durch Aufgaben definiert ist, wird scheitern, sobald er auf eine Aufgabe trifft, die nicht auf der Liste steht. Persona füllt die Lücken; Aufgaben können das nicht.

Lösung: Schreiben Sie Identity, Persona und Speech Rules zuerst. Fügen Sie Aufgaben und Projektzugriff zuletzt hinzu. Wenn das Persona nach zwei Entwürfen unklar ist, ist die Rolle des Agenten nicht gut genug definiert, um bereitgestellt zu werden.

### 6. Values, die keine Entscheidungen leiten

Generische Werte („Qualität", „Effizienz", „Zusammenarbeit") geben keine Verhaltensanleitung, wenn zwei Werte in Konflikt geraten. Wenn ein Agent sowohl Geschwindigkeit als auch Korrektheit wertschätzt, welcher gewinnt unter Druck?

Lösung: Schreiben Sie jeden Wert als Entscheidungsregel, nicht als Aspiration. „Correctness over speed — a slow correct answer is always preferred to a fast incorrect one" ist ein Wert. „We care about quality" ist keiner.

### 7. Boundaries ohne Attribution

„Schreibt keine Dokumentation" zu sagen ist schwächer als „schreibt keine Dokumentation — das ist die Verantwortung des Archivists". Attribution erstellt eine vollständige Abdeckungskarte und macht Lücken sichtbar.

Lösung: Jedes Boundary-Element muss den Agenten oder die Rolle nennen, der/die für diesen Bereich verantwortlich ist. Wenn kein Agent ihn besitzt, ist das eine Lücke im Team-Design.
