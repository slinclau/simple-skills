# simple-skills

Practical skills for LLM agents. Works with any AI tool that accepts a system prompt — coding agents, chat assistants, API integrations, and more.

---

## Skills

| Skill | Description |
|---|---|
| `research-quality` | Rigorous research and writing discipline — no invented facts, minimal footprint, explicit confidence levels |

---

## Install

### Claude Code (coding agent)

```
/install-plugin github:slinclau/simple-skills
```

Skills are then available as `simple-skills:research-quality` via the `Skill` tool.

### Claude.ai Projects

Open your Project → **Project instructions** → paste the contents of [`skills/research-quality/SKILL.md`](skills/research-quality/SKILL.md). All conversations in that project will follow the skill rules.

### ChatGPT

**Custom instructions** (applies to all chats): Settings → Personalization → Custom Instructions → paste skill content in "How would you like ChatGPT to respond?".

**GPT builder**: System prompt → paste skill content.

**Per-conversation**: paste skill content at the start of any chat.

### Gemini (CLI)

Copy `GEMINI.md` to your project root, or add this line to your existing `GEMINI.md`:

```
@https://raw.githubusercontent.com/slinclau/simple-skills/main/skills/research-quality/SKILL.md
```

### Gemini (web / Gems)

Open a Gem → **Instructions** → paste the contents of `skills/research-quality/SKILL.md`.

### Cursor / Windsurf / Copilot / Codex / other coding agents

Copy `AGENTS.md` to your project root. Most coding agents auto-read this file. Alternatively paste the skill content into your agent's rules file (`.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`, etc.).

### API / custom integrations

Paste the skill content into your system prompt:

```python
system_prompt = open("skills/research-quality/SKILL.md").read()
```

Works with OpenAI, Anthropic, Google, Mistral, or any API that accepts a system prompt.

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

After adding a skill, reference it in `GEMINI.md` and `AGENTS.md`, and add a row to the Skills table above.
