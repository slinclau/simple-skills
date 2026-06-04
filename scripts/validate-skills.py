#!/usr/bin/env python3
"""Validates skill files and checks sync with AGENTS.md / GEMINI.md."""

import os
import sys
import re

SKILLS_DIR = "skills"
AGENTS_FILE = "AGENTS.md"
GEMINI_FILE = "GEMINI.md"
REQUIRED_FRONTMATTER = ["name", "description"]

errors = []


def parse_frontmatter(path):
    with open(path) as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    block = content[3:end]
    fields = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def read_file(path):
    with open(path) as f:
        return f.read()


# Collect skill directories
skill_dirs = [
    d for d in os.listdir(SKILLS_DIR)
    if os.path.isdir(os.path.join(SKILLS_DIR, d))
]

for skill in sorted(skill_dirs):
    skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")

    # Check SKILL.md exists
    if not os.path.exists(skill_path):
        errors.append(f"[{skill}] Missing SKILL.md")
        continue

    # Check required frontmatter fields
    fm = parse_frontmatter(skill_path)
    for field in REQUIRED_FRONTMATTER:
        if field not in fm or not fm[field]:
            errors.append(f"[{skill}] SKILL.md missing frontmatter field: '{field}'")

    # Check sync with AGENTS.md
    agents_content = read_file(AGENTS_FILE)
    if skill not in agents_content:
        errors.append(f"[{skill}] Not referenced in {AGENTS_FILE}")

    # Check sync with GEMINI.md
    gemini_content = read_file(GEMINI_FILE)
    if skill not in gemini_content:
        errors.append(f"[{skill}] Not referenced in {GEMINI_FILE}")

    print(f"  ok  {skill}")

if errors:
    print("\nErrors:")
    for e in errors:
        print(f"  ✗ {e}")
    sys.exit(1)

print(f"\n{len(skill_dirs)} skill(s) valid.")
