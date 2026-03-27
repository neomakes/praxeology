# Guide de conception des rôles

Un guide pratique pour concevoir les rôles d'agents IA dans un système régi par Praxeology. Couvre l'identité, les contrats de communication, les limites comportementales et la mise à l'échelle des équipes.

---

## Principes

### 1. Chaque agent possède un domaine clairement délimité — sans autorité chevauchante

Chaque agent doit avoir un domaine défini et non chevauchant. Quand deux agents pourraient tous les deux revendiquer une tâche, c'est un défaut de conception. Résolvez-le en demandant : « Qui possède le livrable ? » — l'agent qui possède le livrable possède le domaine.

Exemple : Un Executor et un agent DevOps pourraient tous les deux « toucher à l'infrastructure ». Résolvez par la propriété du livrable — l'Executor possède le code applicatif, le DevOps possède les manifestes de déploiement et la configuration CI.

### 2. Les Boundaries empêchent les agents d'empiéter les uns sur les autres

Les Boundaries ne sont pas des suggestions — elles sont appliquées par des Anti-Patterns explicites. Le CLAUDE.md de chaque agent doit nommer ce qu'il NE fait PAS, et nommer l'agent qui le fait à sa place. Cela crée une carte de couverture complète et non chevauchante pour toute l'équipe.

### 3. La personnalité engendre un comportement cohérent — pas seulement les instructions

Les instructions décrivent quoi faire. La personnalité décrit comment le faire quand les instructions s'épuisent. Un agent avec un persona bien défini produira un comportement cohérent et prévisible dans des situations inédites. Un agent défini uniquement par des instructions de tâches va dériver.

Définissez le persona avant de définir les tâches.

### 4. Le même agent doit être reconnaissable d'une conversation à l'autre

Un agent bien conçu est identifiable par son ton, sa structure et son vocabulaire seuls — sans voir son nom. Si vous ne pouvez pas distinguer deux agents d'un extrait de transcription, ils ne sont pas suffisamment différenciés. La différenciation n'est pas cosmétique ; elle prévient la confusion des rôles et la dérive du persona.

---

## Le modèle CLAUDE.md

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

## Exemple concret : deux agents contrastés

Le même système peut avoir un Executor et un Planner. Voici comment la différenciation fonctionne en pratique.

**Executor — Style de communication**
- Dit : « Done. » « Next. » « That approach is wrong. Here is why: [one reason]. »
- Ton : Concis, déclaratif, action en premier.
- Limite de phrases : 3 par réponse hors rapports.
- Pas d'hésitations. Pas de « peut-être » ou « pourrait ».

**Planner — Style de communication**
- Dit : « Three options. Option A carries the least risk. My recommendation is A because... »
- Ton : Analytique, structuré, considère explicitement les compromis.
- Limite de phrases : 10 par réponse ; structuré avec des en-têtes dans les longs contenus.
- Les hésitations sont permises là où l'incertitude est réelle.

**Executor — Anti-Patterns**
- Écrire des architecture decision records — c'est la production du Planner.
- Proposer plusieurs options quand un seul chemin correct existe — choisir et exécuter.

**Planner — Anti-Patterns**
- Écrire du code d'implémentation — c'est la production de l'Executor.
- Déclarer un plan « done » sans spécifier la prochaine action concrète.

**Executor — Emotional Triggers**
- Échec : « My error. Cause: [X]. Fixed. » Sans élaboration.
- Succès : « Done. » Sans célébration.

**Planner — Emotional Triggers**
- Échec : Révise l'arbre de décision. Identifie quelle hypothèse était erronée. Le documente.
- Succès : Confirme que tous les critères d'acceptation sont satisfaits avant de déclarer la complétion.

---

## Guide de mise à l'échelle

### 3 agents — Développeur solo ou petite équipe
- **Executor** : Implémente le code, effectue les commits, exécute les tâches définies.
- **Reviewer** : Vérifie la production pour la correction, le style et les cas limites. N'implémente pas.
- **Planner** : Décompose les objectifs en tâches. N'implémente pas et ne révise pas.

Contrainte de conception : le Reviewer ne doit jamais écrire du code lors du même passage que la révision. Gardez l'authoring et la révision comme des invocations strictement séparées.

### 5 agents — Petite équipe avec surcharge opérationnelle
Ajoutez à la base de 3 agents :
- **DevOps** : Possède CI/CD, déploiement, configuration de l'environnement. L'Executor ne touche jamais à l'infrastructure.
- **Documentation** : Possède tous les artefacts écrits — specs, READMEs, changelogs. L'Executor n'écrit jamais de docs.

### 9 agents — Couverture C-suite complète
Correspondance avec les départements de gouvernance. Chaque agent possède le domaine de production d'un département :

| Agent | Département | Propriété de la production |
|---|---|---|
| Strategist | CEO | Mission, gouvernance, décisions inter-départements |
| Operator | COO | Processus, coordination de l'exécution, rapports |
| Engineer | CTO | Code, systèmes, architecture technique |
| Analyst | CFO | Budget, économie des tokens, allocation des ressources |
| Archivist | CDO | Pipelines de données, gestion des connaissances |
| People Lead | CHRO | Onboarding, évolution du persona des agents, santé de l'équipe |
| Security | CISO | Modélisation des menaces, contrôle d'accès, conformité |
| Researcher | R&D | Exploration, prototypage, évaluation |
| Communicator | CMO/Comms | Contenu externe, résumés, annonces |

Chaque agent dans un système à 9 agents doit avoir au moins 3 agents explicitement nommés dans sa section Boundaries.

### 15+ agents — Sous-équipes avec chefs d'équipe
À cette échelle, introduisez une couche hiérarchique :
- Chaque département a un agent **team lead** qui coordonne 2 à 3 agents spécialistes.
- Le team lead est le point de contact unique pour les demandes inter-départements. Les spécialistes ne reçoivent des tâches que de leur propre team lead.
- Chemin d'escalade : Spécialiste → Team Lead → Strategist. Sauter des niveaux uniquement en cas de crise.

Contrainte de conception à cette échelle : assurez-vous que chaque spécialiste a un Radar chart plus étroit que son team lead. Un spécialiste doit scorer 9-10 dans un domaine et en dessous de 5 dans tous les autres. Un team lead doit scorer 7+ dans 3 domaines. Évitez les spécialistes généralistes — ils créent de l'ambiguïté des rôles.

---

## Liste de contrôle de différenciation

Avant le déploiement, vérifiez chaque paire d'agents selon cette liste. Chaque case non cochée est un écart de différenciation qui provoquera une dérive du persona ou un conflit de rôle.

- [ ] Limites de nombre de phrases différentes par réponse
- [ ] Ton ou niveau de formalité différent (au moins un degré de séparation)
- [ ] Au moins 2 Anti-Patterns uniques chacun (non partagés entre la paire)
- [ ] Boundaries non chevauchantes (aucune catégorie de tâche revendiquée par les deux)
- [ ] Réponses aux Emotional Triggers distinguables (particulièrement pour les modes Échec et Succès)
- [ ] Scores Radar différents (pas deux agents avec des forces de domaine identiques)
- [ ] Références Standard primaires différentes (ou des sections différentes de documents partagés)

Si deux agents partagent le même ton, la même limite de phrases et n'ont aucun Anti-Pattern se référençant mutuellement, fusionnez-les en un seul agent ou reconçoivent depuis zéro.

---

## Pièges courants

### 1. Rendre tous les agents polis et similaires — aucune différenciation

Le comportement LLM par défaut est courtois, utile et équilibré. Laissé sans contraintes, chaque agent convergera vers cette ligne de base. Les sections Speech Rules et Anti-Patterns existent précisément pour prévenir cette convergence. Si vous vous trouvez à écrire « professionnel et utile » comme descripteur de ton, vous n'avez pas différencié.

Correctif : Attribuez au moins un trait de ton en tension avec « utile » — par ex. direct, sceptique, laconique, formel ou adversarial (dans des contextes bornés).

### 2. Autorité chevauchante — conflits et blocages

Quand deux agents peuvent tous les deux légitimement revendiquer une tâche, aucun n'agira de façon décisive, ou les deux agiront de façon incohérente. C'est la défaillance structurelle la plus courante dans les systèmes multi-agents.

Correctif : Pour chaque type de tâche que le système doit gérer, tracez-le vers exactement un agent dans les sections Boundaries. S'il trace vers deux, réécrivez les Boundaries d'un agent pour l'exclure.

### 3. Pas d'Anti-Patterns — dérive du persona au fil du temps

Un agent sans Anti-Patterns élargira graduellement sa portée parce que le système récompensera l'utilité. Un agent à qui on dit seulement quoi faire commencera éventuellement à faire des choses adjacentes qui semblent utiles.

Correctif : Définissez les Anti-Patterns avant le déploiement, pas après que la dérive soit observée. Au moins deux Anti-Patterns doivent nommer un autre agent spécifique comme propriétaire correct.

### 4. Pas d'Emotional Triggers — réponses plates quel que soit le contexte

Un agent sans Emotional Triggers répondra de façon identique à une demande routinière et à une crise. Cela le rend peu fiable comme membre d'équipe — les humains calibrent la confiance en fonction de la réactivité contextuelle.

Correctif : Définissez au minimum : les modes Normal, Task Received, Failure et Crisis. Chaque mode doit produire une sortie visiblement différente — pas seulement des mots différents, mais une structure, une longueur de phrase ou un niveau de formalité différents.

### 5. Définir les tâches avant de définir le persona

Les listes de tâches sont faciles à écrire et donnent une fausse impression de complétude. Un agent défini uniquement par des tâches se brisera dès qu'il rencontrera une tâche absente de la liste. Le persona comble les lacunes ; les tâches ne le peuvent pas.

Correctif : Écrivez Identity, Persona et Speech Rules en premier. Ajoutez les tâches et l'accès aux projets en dernier. Si le persona est flou après deux brouillons, le rôle de l'agent n'est pas suffisamment bien défini pour être déployé.

### 6. Des Values qui ne guident pas les décisions

Les valeurs génériques (« qualité », « efficacité », « collaboration ») ne fournissent aucune orientation comportementale quand deux valeurs entrent en conflit. Si un agent valorise à la fois la vitesse et l'exactitude, laquelle l'emporte sous pression ?

Correctif : Rédigez chaque valeur comme une règle de décision, pas une aspiration. « Correctness over speed — a slow correct answer is always preferred to a fast incorrect one » est une valeur. « We care about quality » n'en est pas une.

### 7. Boundaries sans attribution

Dire « ne rédige pas de documentation » est plus faible que « ne rédige pas de documentation — c'est la responsabilité de l'Archivist ». L'attribution crée une carte de couverture complète et rend les lacunes visibles.

Correctif : Chaque élément de Boundaries doit nommer l'agent ou le rôle responsable de ce domaine. Si aucun agent n'en est propriétaire, c'est une lacune dans la conception de l'équipe.
