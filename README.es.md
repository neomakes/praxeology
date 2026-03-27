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

## 🌐 Idiomas

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Español**

También disponible: [QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md))

---

## ¿Por qué Praxeology?

Herramientas como [gstack](https://github.com/gstack-io/gstack) y [oh-my-claudecode](https://github.com/anthropics/claude-code) son excelentes para hacer productivos a los agentes de IA individuales — navegación, codificación, pruebas, despliegue. Pero cuando se escala de **un agente** a **muchos agentes trabajando juntos**, surge un nuevo problema: la **gobernanza**.

Sin gobernanza, los agentes duplican trabajo, se contradicen, sobrepasan sus límites y se alejan con el tiempo de sus roles previstos. La ingeniería de prompts por sí sola no resuelve esto — se necesita una estructura que persista entre sesiones, evolucione con el uso y refleje cómo las organizaciones humanas más efectivas han gobernado la acción durante siglos.

Praxeology proporciona esa estructura. No es un reemplazo de sus herramientas de codificación — es la **capa constitucional** que se sitúa por encima de ellas, garantizando que sus agentes operen como una organización coherente en lugar de una colección de chatbots independientes.

---

## ¿Qué es esto?

**Praxeology** es un sistema operativo colaborativo humano–IA construido sobre una jerarquía de gobernanza universal de 4+1 niveles. Los humanos establecen la estrategia y los principios; la IA agéntica ejecuta dentro de esos límites, aprende de la experiencia y propone mejoras de vuelta. Captura la observación de que toda acción con propósito — desde naciones hasta agentes de IA — sigue el mismo patrón estructural.

```
Strategy (POR QUÉ) → Doctrine (QUÉ) → Procedure (CÓMO) → Playbook (PATRONES) → Execution (AHORA)
```

Los niveles superiores siempre prevalecen sobre los inferiores. Sin excepciones.

---

## El Isomorfismo

La misma estructura de 4+1 niveles aparece en todos los dominios de la acción organizada:

| Nivel | Derecho nacional | Militar | Corporativo | Individual | Agente IA |
|-------|-----------------|---------|-------------|------------|-----------|
| **1 Strategy** | Constitución | Objetivo de campaña | Misión y Visión | Valores personales | System Prompt / Prime Directive |
| **2 Doctrine** | Ley estatutaria | Reglas de enfrentamiento | Política corporativa | Principios de vida | Behavioral Guidelines |
| **3 Procedure** | Reglamentos | Standard Operating Procedures | SOPs / Protocolos | Hábitos y rutinas | Task Instructions |
| **4 Playbook** | Jurisprudencia / Precedente | Tácticas y ejercicios | Mejores prácticas | Patrones aprendidos | Few-shot Examples |
| **Exec Work Plan** | Decreto ejecutivo | Órdenes de misión | Sprint / Plan de trabajo | Lista diaria | Active Context |

Este isomorfismo es la tesis central: la gobernanza no es específica de un dominio. El patrón es universal. Un framework que funciona para una unidad militar funciona para una startup, un laboratorio de investigación o una flota de agentes de IA.

---

## Inicio rápido

**Paso 1 — Clonar**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**Paso 2 — Ejecutar la configuración**

```bash
bash setup.sh
```

El asistente interactivo solicita el nombre de su organización, misión, departamentos, agentes y proyectos. Genera la estructura de directorios completa y todos los documentos de arranque.

**Paso 3 — Lanzar**

```bash
bash launch.sh
```

Su sistema de gobernanza está activo. Abra `CLAUDE.md` en la raíz para ver el contexto generado para los agentes de IA.

> **¿Nuevo en Praxeology?** Comience con [docs/quickstart.md](docs/quickstart.md) para una guía de 3 pasos, y [docs/role-design.md](docs/role-design.md) para diseñar sus agentes.

---

## Características principales

| Característica | Descripción |
|----------------|-------------|
| **SafetyGate** | Los documentos de nivel superior pueden declarar límites estrictos que ningún documento de nivel inferior puede anular |
| **Proposal Flow** | Cualquier agente o miembro del equipo puede proponer una enmienda mediante el formato estructurado de Proposal |
| **SOP Evolution** | Los Procedures y Playbooks evolucionan a través de la Review Cascade antes de ser promovidos |
| **Review Cascade** | Los cambios se propagan hacia arriba: Playbook → Procedure → Doctrine → Strategy para verificaciones de coherencia |
| **Reverse Flow** | Los cambios de Strategy se propagan hacia abajo: todos los niveles inferiores se marcan para revisión |
| **Department Codes** | Departamentos con series de códigos numéricos (p. ej., 1xx–7xx en la instancia NeoMakes) con asignaciones de roles y personal |

---

## Estructura de directorios

```
your-org/
├── CLAUDE.md                  # Contexto raíz para agentes de IA (generado)
├── launch.sh                  # Script de lanzamiento diario (generado)
├── _standard/                 # Documentos de gobernanza
│   ├── README.md              # Índice principal de todos los artefactos de gobernanza
│   ├── {department}/          # Una carpeta por departamento (p. ej., strategy, operations, finance, ...)
│   │   ├── STR-{NNN}.md      #   La instancia NeoMakes usa: ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md      #   El tuyo puede ser cualquier nombre
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Definiciones de agentes / miembros del equipo
│   ├── CLAUDE.md              # Reglas compartidas del equipo
│   └── {agent}/               # Subdirectorio por agente
│       ├── CLAUDE.md          # Contexto y persona del agente
│       └── sop.md             # SOPs del agente
├── _project/                  # Proyectos activos
│   ├── .praxe/                # Fichas de proyecto (metadatos de gobernanza)
│   │   └── {project}.md       # Estado, prioridad, asignación de crew, hitos
│   └── {project}/             # Directorio de cada proyecto (código)
├── _setting/                  # Configuración operativa
│   ├── permissions.md         # Matriz de control de acceso
│   └── integrations.md        # Configuración de servicios externos
├── docs/                      # Documentación del framework
├── templates/                 # Plantillas de documentos reutilizables
└── examples/                  # Implementaciones de referencia
```

---

## Aplicaciones por dominio

### Corporativo

Asigne departamentos a roles organizativos. Cada departamento posee su pila de gobernanza. El documento Strategy de nivel superior es la constitución de la organización. (La instancia NeoMakes usa los departamentos CEO/COO/CFO/CTO/CDO/CHRO/CISO — el tuyo puede ser cualquier cosa.)

### Laboratorio de investigación

Asigne roles al PI, Director de Laboratorio, Responsable Financiero, Responsable de Sistemas, Alianzas, RRHH y Seguridad. Utilice la misma estructura de niveles. El documento Strategy captura la misión de investigación del laboratorio y sus restricciones éticas. Consulte [docs/tutorial.md](docs/tutorial.md) para un tutorial completo de laboratorio de investigación.

### Productividad personal

Una implementación para una sola persona. CEO = usted. Strategy = su misión de vida. Doctrine = sus elementos no negociables. Procedure = sus rituales semanales. Playbook = sus mejores prácticas acumuladas. Work Plan = su lista diaria.

### Equipo de agentes de IA

Cada agente de IA recibe un `_crew/{agent}/CLAUDE.md` que define su rol, nivel de autoridad y restricciones operativas. El `CLAUDE.md` raíz es la constitución compartida del equipo. Los documentos de nivel superior se anteponen a los contextos de los agentes antes de la ejecución.

---

## Documentación del framework

| Documento | Descripción |
|-----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Filosofía de diseño, mecanismos centrales y el patrón de gobernanza universal |
| [docs/getting-started.md](docs/getting-started.md) | Requisitos previos, instalación y primeros pasos |
| [docs/standard-system.md](docs/standard-system.md) | El sistema de documentos de 4+1 niveles en profundidad |
| [docs/crew-system.md](docs/crew-system.md) | Gestión de agentes, auto-evolución de SOPs y review cascade |
| [docs/tutorial.md](docs/tutorial.md) | Tutorial completo para construir un equipo de agentes de IA gobernado |

---

## Ejemplos

- [examples/solo-dev/](examples/solo-dev/) — Desarrollador en solitario + 3 agentes (configuración mínima)
- [examples/tech-startup/](examples/tech-startup/) — Empresa de software en etapa inicial
- [examples/one-piece-crew/](examples/one-piece-crew/) — Tripulación ficticia con sistema de persona completo (demostración)

---

## Uso en producción — NeoMakes (Una instancia)

Praxeology no es teórico. Hace funcionar una empresa real cada día. NeoMakes es una instancia de este framework — la suya será diferente.

**[NeoMakes, Inc.](https://neomakes.com)** opera como una empresa unipersonal con 9 agentes de IA gobernados por Praxeology:

| Métrica | Valor |
|---------|-------|
| Agentes | 9 (organizados en 7 departamentos C-level) |
| Regulaciones promulgadas | 38 (STR/DOC/PRC/PLY en todos los departamentos) |
| Operaciones diarias | Seguimiento de tareas, informes diarios, planificación semanal, revisiones mensuales |
| Integraciones | Claude Code + Discord (4 canales) + Google Drive + Notion + Calendar |
| Auto-evolución | Los agentes detectan Standard Gaps diariamente → Proposals semanales → Enmiendas mensuales |

Los agentes tienen personas definidas con **Speech Rules** (límites de frases, tono), **Anti-Patterns** (comportamientos prohibidos) y **Emotional Triggers** (cambios de respuesta según la situación) — garantizando un comportamiento coherente y distinguible en los 9 agentes.

### Guías de integración

| Guía | Descripción |
|------|-------------|
| [Discord Integration](docs/discord-integration.md) | Estructura de canales, menciones de bots, prevención de bucles, comunicación bot a bot |
| [Google Drive Integration](docs/drive-integration.md) | Configuración de symlinks, almacenamiento de regulaciones, espacios de trabajo por sala |
| [Crew Manager Dashboard](docs/crew-manager.md) | Panel web para monitoreo de sesiones, gestión de tareas, aprobación de permisos |
| [Claude Code Setup](docs/claude-code-setup.md) | Jerarquía CLAUDE.md, servidores MCP, configuración de sesión por agente |
| [Work Cycle](docs/work-cycle.md) | Esquemas weekly.json/todo.json, ciclo de informes, flujo inverso de Standard Gaps |

---

## Origen

Praxeology fue construido por **[NeoMakes](https://neomakes.com)** — una empresa unipersonal que desarrolla tecnología fundamental de interacción humano-IA para entornos extremos. El framework surgió de la necesidad de gobernar una flota creciente de agentes de IA con el mismo rigor aplicado a las organizaciones humanas.

El nombre proviene de la praxeología, el estudio de la acción humana. La intuición: la acción con propósito tiene estructura. Esa estructura es universal. Hágala explícita, y podrá gobernar cualquier cosa.

---

## Licencia

MIT License — ver [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
