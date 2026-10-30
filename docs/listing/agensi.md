# Agensi listings (paste-ready)

Agensi lists skills individually (one SKILL.md folder per listing). Rules checked 2026-10: free to list, creator keeps 70%, one-time price from $1 (under $5 = credit purchase only), subscriptions from $5/mo, every submission passes an automated security scan + review (usually 24–48h). Re-check at https://www.agensi.io/ before submitting.

Cover for all: `assets/cover-agensi.png` (1200×630). Upload the per-skill zips from the private repo `mlxengingin/skillforge-pro` → `dist/skills/<name>.zip`.

## Recommended first 3 listings (highest global demand)

### 1. seo-tool-site-launch — $9
**Title:** Micro-SaaS SEO Launch: keyword to first dollar
**Short:** Pick buyer-intent long-tail keywords, ship a one-tool landing page with a freemium gate, and run a 90-day content plan.
**Description:** Guides your agent through a 3-test keyword filter (search volume, paying competitors on page 1, weak incumbent pages), a landing-page outline with FAQ from People Also Ask, pricing, Search Console setup and weekly content. Includes `assets/landing-outline.md`. Guardrails: no fake testimonials, no spam links.
**Example prompts:** "Find 3 keywords for a PDF tool I can build this week" · "Write my landing page and FAQ for <tool>"

### 2. chrome-extension-mvp — $7
**Title:** Chrome Extension MVP (MV3) with paid license gate
**Short:** Scope, build and prep a Manifest V3 extension with minimal permissions, a license-key gate and store listing assets.
**Description:** One-job spec, `activeTab`-first permissions, popup/content/service-worker layout, license verification via your store's order IDs, local test checklist, Chrome Web Store copy and screenshot plan. Includes `assets/manifest.json`.
**Example prompts:** "Build an extension that exports any HTML table to CSV" · "Write my Chrome Web Store listing"

### 3. saas-pricing-experiment — $5
**Title:** Pricing & Price-Test Playbook for Micro-SaaS
**Short:** Anchor on competitors, choose one-time vs subscription vs credits, compute unit economics after fees and run a 2-week price test.
**Example prompts:** "How should I price my tool?" · "Plan a price test for my Pro tier"

## Later (after first reviews)
`programmatic-seo-pages` ($9), `agent-skill-marketplace-publish` ($5), `launch-post-kit` ($5), `prompt-to-listing` ($5).

## Security self-check (before submitting)
- No secrets/tokens, no reads of ~/.ssh or browser data, no undeclared network calls, no obfuscated code, no prompt-injection text. Run `python3 tools/validate_skill.py skills/pro` in the private repo → 0 problems.
