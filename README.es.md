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
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md"><strong>Español</strong></a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## El problema

**La paralelización está resuelta.** Claude Code, Codex, gstack, oh-my-claudecode — estas herramientas ya hacen que los agentes de IA individuales sean increíblemente productivos. Ejecutar 5 agentes en paralelo es un problema resuelto.

**La coordinación no lo está.** Cuando esos 5 agentes terminan su trabajo, ¿quién resuelve los conflictos? ¿Quién verifica la coherencia? ¿Quién evita que el Agente A sobreescriba las decisiones del Agente B? ¿Quién detiene la deriva de roles entre sesiones? Los frameworks multi-agente resuelven el *inicio* — Praxeology resuelve lo que viene después: **coordinación, seguimiento de estado, resolución de conflictos y alineación evolutiva.**

**Praxeology es la capa de gobernanza que faltaba.** Se sitúa por encima de tus herramientas de codificación, sin reemplazarlas — asegurando que tus agentes operen como una organización coherente en lugar de una colección de chatbots independientes.

---

## Prueba en producción

Esto no es teoría. [NeoMakes](https://neomakes.com) lo ejecuta cada día.

> **1 humano + 9 agentes de IA · 38 reglas de gobernanza · 7 departamentos**
> Tareas diarias → Revisiones semanales → Enmiendas mensuales
> Los agentes detectan brechas, proponen correcciones, evolucionan sus propios SOPs.

Cada agente tiene definidas **Speech Rules** (límites de oraciones, tono), **Anti-Patterns** (comportamientos prohibidos) y **Emotional Triggers** (cambios de respuesta según la situación) — asegurando un comportamiento consistente y distinguible entre los 9 agentes. NeoMakes es una instancia. La tuya se verá diferente.

---

## Cómo funciona

Una jerarquía de gobernanza de 4+1 niveles. Simple. Universal.

```
Estrategia (WHY) → Doctrina (WHAT) → Procedimiento (HOW) → Playbook (PATTERNS) → Ejecución (NOW)
```

Los niveles superiores siempre prevalecen sobre los inferiores. Sin excepciones. Los agentes resuelven decisiones recorriendo la jerarquía hacia arriba — deteniéndose en el primer nivel que cubre la situación.

---

## Qué lo hace diferente

No es una lista de características. Es un solucionador de problemas de coordinación.

| Tu problema | La respuesta de Praxeology |
|---|---|
| Los agentes se desvían de su rol entre sesiones | **ConstitutionalGuard** — Verificación de comportamiento de 4 capas |
| No hay forma de restringir las acciones de los agentes de forma segura | **SafetyGate** — Los niveles superiores bloquean reglas críticas que los niveles inferiores no pueden sobreescribir |
| Los agentes no pueden mejorar sus propios procesos | **SOP Evolution** — Bucle Learn-Compress-Apply. Descenso de gradiente para la gobernanza |
| Los cambios en un lugar rompen otro | **Review Cascade** — Propagación bidireccional (hacia arriba y hacia abajo en la jerarquía) |
| Los agentes no pueden señalar cuando las reglas son malas | **Proposal Flow** — Solicitudes de enmienda estructuradas de cualquier agente al fundador |
| Sin memoria institucional entre sesiones | **Work Cycle** — Brechas diarias → propuestas semanales → enmiendas mensuales → revisiones trimestrales |

---

## Inicio rápido

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # Asistente interactivo: nombre de organización, misión, departamentos, agentes
bash launch.sh   # Tu sistema de gobernanza está en marcha
```

> **¿Nuevo aquí?** Comienza con la [Guía de inicio rápido](docs/quickstart.md) y la [Guía de diseño de roles](docs/role-design.md).

---

## Sistema de diseño de agentes

Cada agente recibe un `CLAUDE.md` que define no solo *qué* hace, sino *cómo* se comporta:

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

Esto hace que los agentes sean **distinguibles, consistentes y acotados**. Un agente de QA suena diferente a un executor. Un planificador nunca escribe código. Un revisor nunca aprueba su propio trabajo. Consulta la [Guía de diseño de roles](docs/role-design.md) para la plantilla completa y estrategias de escalado (de 3 a 15+ agentes).

---

## Ejemplos

- [examples/solo-dev/](examples/solo-dev/) — Desarrollador independiente + 3 agentes (mínimo)
- [examples/tech-startup/](examples/tech-startup/) — Empresa de software en etapa inicial
- [examples/one-piece-crew/](examples/one-piece-crew/) — Tripulación ficticia con sistema de persona completo

---

<details>
<summary><strong>La teoría — Por qué funciona (El isomorfismo)</strong></summary>

La misma estructura de 4+1 niveles aparece en todos los dominios de la acción organizada:

| Nivel | Derecho nacional | Militar | Corporativo | Individual | Agente IA |
|------|-------------|----------|-----------|------------|----------|
| **1 Estrategia** | Constitución | Objetivo de campaña | Misión & Visión | Valores personales | System Prompt / Prime Directive |
| **2 Doctrina** | Ley estatutaria | Reglas de enfrentamiento | Política corporativa | Principios de vida | Directrices de comportamiento |
| **3 Procedimiento** | Reglamentos | Procedimientos operativos estándar | SOPs / Protocolos | Hábitos & Rutinas | Instrucciones de tareas |
| **4 Playbook** | Derecho consuetudinario / Precedente | Tácticas & Ejercicios | Mejores prácticas | Patrones aprendidos | Ejemplos few-shot |
| **Exec** | Orden ejecutiva | Órdenes de misión | Sprint / Plan de trabajo | Lista diaria | Contexto activo |

La gobernanza no es específica de un dominio. El patrón es universal. Un framework que funciona para una unidad militar funciona para una startup, un laboratorio de investigación o una flota de agentes de IA.

</details>

---

## Estructura de directorios

```
your-org/
├── CLAUDE.md                  # Contexto raíz para agentes de IA (generado)
├── launch.sh                  # Script de lanzamiento diario (generado)
├── _standard/                 # Documentos de gobernanza
│   ├── README.md              # Índice maestro de todos los artefactos de gobernanza
│   ├── {department}/          # Una carpeta por departamento
│   │   ├── STR-{NNN}.md      #   (ej. estrategia, operaciones, finanzas, ingeniería)
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Definiciones de agentes / miembros del equipo
│   ├── CLAUDE.md              # Reglas compartidas del equipo
│   └── {agent}/               # Subdirectorio por agente
│       ├── CLAUDE.md          # Contexto y persona del agente
│       └── sop.md             # SOPs del agente
├── _project/                  # Proyectos activos
├── _setting/                  # Configuración operacional
├── docs/                      # Documentación del framework
├── templates/                 # Plantillas de documentos reutilizables
└── examples/                  # Implementaciones de referencia
```

---

## Guías de integración

| Guía | Descripción |
|-------|-------------|
| [Integración Discord](docs/discord-integration.md) | Estructura de canales, menciones de bots, prevención de bucles |
| [Integración Google Drive](docs/drive-integration.md) | Configuración de enlaces simbólicos, almacenamiento de regulaciones, espacios de trabajo |
| [Panel Crew Manager](docs/crew-manager.md) | Panel web para monitoreo de sesiones |
| [Configuración Claude Code](docs/claude-code-setup.md) | Jerarquía CLAUDE.md, servidores MCP, sesiones por agente |
| [Work Cycle](docs/work-cycle.md) | Esquemas Todo/weekly, ciclo de reportes, flujo Standard Gap |

## Documentación

| Documento | Descripción |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Filosofía de diseño y mecanismos centrales |
| [docs/getting-started.md](docs/getting-started.md) | Requisitos previos, instalación, primeros pasos |
| [docs/standard-system.md](docs/standard-system.md) | El sistema documental de 4+1 niveles en profundidad |
| [docs/crew-system.md](docs/crew-system.md) | Gestión de agentes, auto-evolución de SOPs |
| [docs/tutorial.md](docs/tutorial.md) | Tutorial completo para construir un equipo de agentes gobernado |

---

## Origen

Construido por **[NeoMakes](https://neomakes.com)** — una empresa unipersonal que desarrolla IA en dispositivo para entornos extremos. El framework surgió de gobernar una flota de agentes de IA con el mismo rigor aplicado a las estructuras de mando militar.

El nombre proviene de la praxeología, el estudio de la acción humana. La acción intencionada tiene estructura. Esa estructura es universal. Hazla explícita y podrás gobernar cualquier cosa.

---

## Licencia

Licencia MIT — ver [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
