# simple-skills

Practical skills for LLM coding agents.

---

## Skills

| Skill | Description |
|---|---|
| `research-quality` | Rigorous research and writing discipline — no invented facts, minimal footprint, explicit confidence levels |

---

## Install

### Claude Code

```
/install-plugin github:slinclau/simple-skills
```

Skills are then available as `simple-skills:research-quality` via the `Skill` tool.

### Gemini CLI

Copy `GEMINI.md` to your project root, or add this line to your existing `GEMINI.md`:

```
@https://raw.githubusercontent.com/slinclau/simple-skills/main/skills/research-quality/SKILL.md
```

### Codex / Copilot / Cursor / Windsurf / other agents

Copy `AGENTS.md` to your project root, or paste the contents of the relevant `skills/*/SKILL.md` file into your agent's system prompt or rules file.

### Any LLM (manual)

Paste the contents of `skills/research-quality/SKILL.md` directly into your system prompt.

---

## Adding skills

Each skill lives in `skills/<skill-name>/SKILL.md` with a YAML frontmatter block:

```markdown
---
name: your-skill-name
description: One or two sentences describing when the agent should invoke this skill.
---

# Skill content here
```

After adding a skill, reference it in `GEMINI.md` and `AGENTS.md`.
