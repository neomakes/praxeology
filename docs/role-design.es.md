# Guía de diseño de roles

Una guía práctica para diseñar roles de agentes IA en un sistema gobernado por Praxeology. Cubre identidad, contratos de comunicación, límites de comportamiento y escalado del equipo.

---

## Principios

### 1. Cada agente posee un dominio claro — sin autoridad superpuesta

Cada agente debe tener un dominio definido y sin solapamientos. Cuando dos agentes podrían reclamar la misma tarea, hay un defecto de diseño. Resuélvalo preguntando: "¿Quién es dueño del resultado?" — el agente que posee el entregable posee el dominio.

Ejemplo: Tanto un Executor como un agente DevOps podrían "tocar la infraestructura". Resuelva por propiedad del entregable — el Executor posee el código de la aplicación, DevOps posee los manifiestos de despliegue y la configuración de CI.

### 2. Las Boundaries evitan que los agentes se interfieran entre sí

Las Boundaries no son sugerencias — se aplican mediante Anti-Patterns explícitos. El CLAUDE.md de cada agente debe nombrar lo que NO hace, y nombrar el agente que lo hace en su lugar. Esto crea un mapa de cobertura completo y sin solapamientos para todo el equipo.

### 3. La personalidad genera comportamiento consistente — no solo las instrucciones

Las instrucciones describen qué hacer. La personalidad describe cómo hacerlo cuando las instrucciones se agotan. Un agente con un persona bien definido producirá un comportamiento consistente y predecible en situaciones novedosas. Un agente definido solo por instrucciones de tareas derivará.

Defina el persona antes de definir las tareas.

### 4. El mismo agente debe ser reconocible en cualquier conversación

Un agente bien diseñado es identificable por tono, estructura y vocabulario solos — sin ver su nombre. Si no puede distinguir a dos agentes por un extracto de transcripción, no están suficientemente diferenciados. La diferenciación no es cosmética; previene la confusión de roles y la deriva del persona.

---

## La plantilla CLAUDE.md

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

## Ejemplo trabajado: dos agentes contrastados

El mismo sistema puede tener un Executor y un Planner. Así es como funciona la diferenciación en la práctica.

**Executor — Estilo de comunicación**
- Dice: "Done." "Next." "That approach is wrong. Here is why: [one reason]."
- Tono: Conciso, declarativo, acción primero.
- Límite de oraciones: 3 por respuesta fuera de los reportes.
- Sin vacilaciones. Sin "quizás" o "podría".

**Planner — Estilo de comunicación**
- Dice: "Three options. Option A carries the least risk. My recommendation is A because..."
- Tono: Analítico, estructurado, considera los compromisos explícitamente.
- Límite de oraciones: 10 por respuesta; estructurado con encabezados en salidas largas.
- Las vacilaciones están permitidas donde la incertidumbre es genuina.

**Executor — Anti-Patterns**
- Escribir architecture decision records — esa es la producción del Planner.
- Proporcionar múltiples opciones cuando existe un solo camino correcto — elegir uno y ejecutar.

**Planner — Anti-Patterns**
- Escribir código de implementación — esa es la producción del Executor.
- Declarar un plan como "done" sin especificar la siguiente acción concreta.

**Executor — Emotional Triggers**
- Fallo: "My error. Cause: [X]. Fixed." Sin elaboración.
- Éxito: "Done." Sin celebración.

**Planner — Emotional Triggers**
- Fallo: Revisa el árbol de decisiones. Identifica qué suposición era incorrecta. Lo documenta.
- Éxito: Confirma que todos los criterios de aceptación se cumplen antes de declarar la finalización.

---

## Guía de escalado

### 3 agentes — Desarrollador solo o equipo pequeño
- **Executor**: Implementa código, hace commits, ejecuta tareas definidas.
- **Reviewer**: Revisa la producción en cuanto a corrección, estilo y casos límite. No implementa.
- **Planner**: Descompone objetivos en tareas. No implementa ni revisa.

Restricción de diseño: el Reviewer nunca debe escribir código en el mismo paso que la revisión. Mantenga la autoría y la revisión como invocaciones estrictamente separadas.

### 5 agentes — Equipo pequeño con sobrecarga operacional
Agregue a la base de 3 agentes:
- **DevOps**: Posee CI/CD, despliegue, configuración del entorno. El Executor nunca toca la infraestructura.
- **Documentation**: Posee todos los artefactos escritos — specs, READMEs, changelogs. El Executor nunca escribe docs.

### 9 agentes — Cobertura C-suite completa
Mapear a departamentos de gobernanza. Cada agente posee el dominio de producción de un departamento:

| Agente | Departamento | Propiedad de la producción |
|---|---|---|
| Strategist | CEO | Misión, gobernanza, decisiones entre departamentos |
| Operator | COO | Procesos, coordinación de ejecución, reportes |
| Engineer | CTO | Código, sistemas, arquitectura técnica |
| Analyst | CFO | Presupuesto, economía de tokens, asignación de recursos |
| Archivist | CDO | Pipelines de datos, gestión del conocimiento |
| People Lead | CHRO | Onboarding, evolución del persona de agentes, salud del equipo |
| Security | CISO | Modelado de amenazas, control de acceso, cumplimiento |
| Researcher | R&D | Exploración, prototipado, evaluación |
| Communicator | CMO/Comms | Contenido externo, resúmenes, anuncios |

Cada agente en un sistema de 9 agentes debe tener al menos 3 agentes explícitamente nombrados en su sección Boundaries.

### 15+ agentes — Sub-equipos con líderes de equipo
A esta escala, introduzca una capa jerárquica:
- Cada departamento tiene un agente **team lead** que coordina 2–3 agentes especialistas.
- El team lead es el único punto de contacto para las solicitudes entre departamentos. Los especialistas solo reciben tareas de su propio team lead.
- Ruta de escalada: Especialista → Team Lead → Strategist. Saltarse niveles solo en crisis.

Restricción de diseño a esta escala: asegúrese de que cada especialista tenga un Radar chart más estrecho que su team lead. Un especialista debe puntuar 9–10 en un área y por debajo de 5 en todas las demás. Un team lead debe puntuar 7+ en 3 áreas. Evite los especialistas generalistas — crean ambigüedad de roles.

---

## Lista de verificación de diferenciación

Antes del despliegue, verifique cada par de agentes con esta lista. Cada casilla sin marcar es una brecha de diferenciación que causará deriva del persona o conflicto de roles.

- [ ] Diferentes límites de cantidad de oraciones por respuesta
- [ ] Diferente tono o nivel de formalidad (al menos un grado de separación)
- [ ] Al menos 2 Anti-Patterns únicos cada uno (no compartidos entre el par)
- [ ] Boundaries sin solapamiento (ninguna categoría de tarea reclamada por ambos)
- [ ] Respuestas a Emotional Triggers distinguibles (especialmente para los modos de Fallo y Éxito)
- [ ] Diferentes puntuaciones de Radar (no dos agentes con fortalezas de dominio idénticas)
- [ ] Diferentes referencias Standard primarias (o diferentes secciones de documentos compartidos)

Si dos agentes comparten el mismo tono, el mismo límite de oraciones y no tienen Anti-Patterns que se referencien mutuamente, fusiónelos en un solo agente o rediseñe desde cero.

---

## Errores comunes

### 1. Hacer todos los agentes educados y similares — sin diferenciación

El comportamiento LLM predeterminado es cortés, útil y equilibrado. Sin restricciones, cada agente convergerá hacia esta línea base. Las secciones Speech Rules y Anti-Patterns existen precisamente para prevenir esta convergencia. Si se encuentra escribiendo "profesional y útil" como descriptor de tono, no ha diferenciado.

Solución: Asigne al menos un rasgo de tono en tensión con "útil" — p. ej., directo, escéptico, lacónico, formal o adversarial (en contextos acotados).

### 2. Autoridad superpuesta — conflictos y bloqueos

Cuando dos agentes pueden reclamar legítimamente una tarea, ninguno actuará de forma decisiva, o ambos actuarán inconsistentemente. Este es el fallo estructural más común en los sistemas multi-agente.

Solución: Para cada tipo de tarea que el sistema debe manejar, rastréela hasta exactamente un agente en las secciones Boundaries. Si apunta a dos, reescriba las Boundaries de un agente para excluirla.

### 3. Sin Anti-Patterns — deriva del persona con el tiempo

Un agente sin Anti-Patterns expandirá gradualmente su alcance porque el sistema recompensará la utilidad. Un agente al que solo se le dice qué hacer eventualmente comenzará a hacer cosas adyacentes que parecen útiles.

Solución: Defina Anti-Patterns antes del despliegue, no después de que se observe la deriva. Al menos dos Anti-Patterns deben nombrar a un agente específico como el propietario correcto.

### 4. Sin Emotional Triggers — respuestas planas independientemente del contexto

Un agente sin Emotional Triggers responderá de forma idéntica a una solicitud rutinaria y a una crisis. Esto lo hace poco confiable como miembro del equipo — los humanos calibran la confianza en función de la capacidad de respuesta contextual.

Solución: Defina como mínimo: los modos Normal, Task Received, Failure y Crisis. Cada modo debe producir una salida visiblemente diferente — no solo diferentes palabras, sino diferente estructura, longitud de oraciones o nivel de formalidad.

### 5. Definir tareas antes de definir el persona

Las listas de tareas son fáciles de escribir y dan una falsa sensación de completitud. Un agente definido solo por tareas fallará en el momento en que encuentre una tarea que no está en la lista. El persona llena los vacíos; las tareas no pueden.

Solución: Escriba Identity, Persona y Speech Rules primero. Añada tareas y acceso al proyecto al final. Si el persona no está claro después de dos borradores, el rol del agente no está suficientemente bien definido para desplegarse.

### 6. Values que no guían decisiones

Los valores genéricos ("calidad", "eficiencia", "colaboración") no proporcionan orientación comportamental cuando dos valores entran en conflicto. Si un agente valora tanto la velocidad como la corrección, ¿cuál gana bajo presión?

Solución: Escriba cada valor como una regla de decisión, no una aspiración. "Correctness over speed — a slow correct answer is always preferred to a fast incorrect one" es un valor. "We care about quality" no lo es.

### 7. Boundaries sin atribución

Decir "no escribe documentación" es más débil que "no escribe documentación — esa es la responsabilidad del Archivist". La atribución crea un mapa de cobertura completo y hace visibles las brechas.

Solución: Cada elemento de Boundaries debe nombrar al agente o rol responsable de ese dominio. Si ningún agente lo posee, eso es una brecha en el diseño del equipo.
