# Contributing to Praxeology

Thank you for your interest in improving the Praxeology Framework. This document explains how to contribute.

---

## What We Welcome

### Template Contributions

New or improved governance document templates are the highest-value contributions. If you have developed a Strategy, Doctrine, Procedure, or Playbook template that generalizes well across organizations, we want it.

Place templates under `templates/_standard/{department}/` and follow the existing naming and structure conventions.

### Example Contributions

Real-world (or illustrative) examples of complete governance setups help new users understand the framework in practice. Add examples under `examples/{your-example}/` with a `README.md` explaining the context.

### Documentation Improvements

Corrections, clarifications, and expansions to `docs/` are welcome. Prefer precision over prose.

### setup.sh Improvements

Bug fixes, platform compatibility fixes, and UX improvements to `setup.sh` are welcome. All changes must be tested on macOS and Linux bash.

---

## Workflow

1. **Fork** the repository to your own GitHub account.

2. **Create a branch** with a descriptive name:
   ```bash
   git checkout -b template/research-lab-cto
   git checkout -b fix/setup-sh-zsh-compat
   git checkout -b docs/amendment-process
   ```

3. **Make your changes.** Keep the diff focused. One logical change per PR.

4. **Test** any script changes:
   ```bash
   bash setup.sh
   bash launch.sh
   ```

5. **Submit a Pull Request** against the `main` branch. Include:
   - What changed and why
   - How to test it
   - Any relevant context (domain, use case, edge case)

---

## Standards

- All files must be in **English**.
- Markdown files must be clean and render correctly on GitHub.
- Bash scripts must be bash-compatible (bash 4+) and pass `shellcheck`.
- No smart quotes, no trailing whitespace, Unix line endings.
- Do not include personal or organization-specific data in templates or examples.
- Use `{PLACEHOLDER}` syntax for values that users must fill in.

---

## Governance Document Conventions

When contributing templates or examples, follow these conventions:

- Every document starts with: `# {ROLE} {Tier} — {Domain} ({Code})`
- Second line: `> Tier N | QUESTION | {ORG_NAME} | v{VERSION} | Enacted {DATE}`
- End every document with: `_Authority: [level]. [cadence]._`
- Use `[SafetyGate]` tag for hard limits in Doctrine documents.

---

## Code of Conduct

This project follows the [Contributor Covenant v2.1](CODE_OF_CONDUCT.md). By participating you agree to uphold its standards.

---

## Questions

Open an issue or start a discussion on GitHub. We read everything.

---

Built by [NeoMakes](https://neomakes.com)
