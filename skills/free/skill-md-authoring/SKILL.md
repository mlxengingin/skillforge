---
name: skill-md-authoring
description: Author a compact, trigger-friendly SKILL.md for Cursor or Claude Code.
---

# Skill.md Authoring

## When to use
User asks to create or improve an agent skill file.

## Workflow
1. Capture the job-to-be-done in one sentence.
2. Write a description that doubles as a trigger hint.
3. Add When-to-use, Workflow steps, Guardrails, Output.
4. Keep the file under ~400 lines; put long references in companion files.
5. Verify the skill can be installed as a folder with SKILL.md at root.

## Guardrails
- No secrets in the skill.
- No destructive shell commands without confirmation.
- Prefer checklists over essays.

