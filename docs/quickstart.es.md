# Praxeology — Guía de inicio rápido

Construya su propio sistema de gobernanza de agentes IA auto-evolutivo en 3 pasos.

---

## Paso 1: Definir su misión (STR)

Escriba el POR QUÉ de su organización en `_standard/{department}/STR-101.md`.

Hay una plantilla disponible en `templates/_standard/`. Complete:

- **Mission** — una frase sobre el propósito de su existencia
- **Values** — 3 a 5 principios que guían cada decisión
- **Non-negotiables** — límites absolutos que los agentes nunca deben cruzar independientemente de las instrucciones

Esta es la constitución de sus agentes. Cada regla de gobernanza, cada comportamiento de agente y cada propuesta de enmienda debe ser coherente con ella. Cuando las reglas entren en conflicto, STR prevalece.

---

## Paso 2: Diseñar su equipo

Decida cuántos agentes necesita. Mínimo 2, recomendado 3 a 9. Cada agente corresponde a un dominio (ingeniería, finanzas, seguridad, operaciones, etc.).

Para cada agente, cree `_crew/{name}/CLAUDE.md` con estas secciones:

- **Identity** — nombre, título del rol, departamento
- **Persona & Character** — rasgos de personalidad que determinan el comportamiento bajo presión
- **Speech Rules** — límites de oraciones, tono, frases prohibidas, expresiones únicas
- **Anti-Patterns** — lista explícita de lo que este agente nunca debe hacer
- **Emotional Triggers** — cómo varía el estilo de respuesta según la situación (rutina, crisis, conflicto)
- **Values** — qué optimiza este agente cuando las reglas no cubren la situación
- **Boundaries** — qué dominios pertenecen a otros agentes (evita conflictos por solapamiento)

Luego cree `_crew/CLAUDE.md` con las reglas que aplican a todos los agentes por igual: estándares de comunicación compartidos, protocolo de escalada, reglas de mención entre agentes y cadencia de reportes.

Consulte `role-design.es.md` para orientación detallada y ejemplos trabajados.

---

## Paso 3: Inicializar la gobernanza

Ejecute el asistente interactivo:

```bash
bash setup.sh
```

O cree los cuatro documentos fundamentales manualmente:

| Documento | Ruta | Propósito |
|---|---|---|
| DOC-101 | `_standard/{department}/DOC-101.md` | Guardia de gobernanza — qué pueden y no pueden anular los agentes |
| DOC-102 | `_standard/{department}/DOC-102.md` | Seguridad — requisitos de aprobación para acciones destructivas o irreversibles |
| PRC-201 | `_standard/{department}/PRC-201.md` | Gestión de sesiones — cómo inician, transcurren y terminan las sesiones |
| PLY-203 | `_standard/{department}/PLY-203.md` | Auto-evolución — cómo los agentes detectan brechas y proponen mejoras |

Las plantillas para los cuatro documentos están en `templates/_standard/`.

---

## Qué sucede a continuación

Una vez desplegados, sus agentes:

1. **Seguirán la jerarquía de gobernanza** en cada decisión: PLY (playbooks) primero, luego PRC (procedimientos), luego DOC (doctrina), luego STR (estrategia). Si el nivel actual resuelve la pregunta, se detienen y actúan. Si no, escalan al siguiente nivel.
2. **Registrarán Standard Gaps** cuando una situación no esté cubierta por las reglas existentes — en lugar de improvisar en silencio.
3. **Propondrán enmiendas** a través del mecanismo Proposal cuando una brecha se repita, permitiendo que la gobernanza evolucione con el uso real.
4. **Evolucionarán sus propios SOPs** a través del bucle Learn-Compress-Apply definido en PLY-203.

El sistema está diseñado para que la gobernanza se refuerce con el tiempo mediante el uso, no mediante auditorías manuales.

---

## Escalado

| Configuración | Referencia |
|---|---|
| 1 persona + equipo startup | `examples/tech-startup/` |
| Equipo completo de 9 agentes | `examples/one-piece-crew/` |

Ambos ejemplos incluyen archivos STR y CLAUDE.md de equipo pre-completados, así como documentos de gobernanza inicializados que puede adaptar directamente.
