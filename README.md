# SkillForge

**Free SKILL.md generator + 13 spec-compliant Pro Agent Skills for Cursor, Claude Code and Codex.**

Live: https://mlxengingin.github.io/skillforge/ (zh / en)

## Repo layout
- `index.html`, `config.js` — the static site (GitHub Pages, root of `main`). Checkout link lives only in `config.js`.
- `skills/free/` — 3 free skills (MIT)
- Pro skills (13) live in the private repo `mlxengingin/skillforge-pro` (paid content; single source + build tools there)
- `tools/validate_skill.py` — Agent Skills spec validator (`python3 tools/validate_skill.py skills`)
- `tools/make_covers.py` — generates `assets/og.png` and store covers
- `docs/listing/` — paste-ready listings for 爱发电, Gumroad, Agensi
- `docs/launch/` — launch post drafts (not published)
- `docs/USER_ONE_ACTION.md` — the one step left to start selling

## Spec
Skills follow https://agentskills.io/specification: `name` = folder name (lowercase, hyphens, ≤64), `description` ≤1024 chars with "Use when …", body < 500 lines, extras in `references/`, `assets/`, `scripts/`.

## License
Site, free skills and tools: MIT. Pro skills: `LICENSE-PRO.md`.
