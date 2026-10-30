---
name: github-pages-product-ship
description: Ship a static product demo on GitHub Pages with pricing and one-action payment stub.
---

# GitHub Pages Product Ship

## When to use
Need a public demo URL today without cloud accounts beyond GitHub.

## Workflow
1. Put a static site in /docs or /web.
2. Add pricing section + config.js payment URL stub.
3. Enable GitHub Pages from main branch.
4. Add USER_ONE_ACTION.md listing the single owner step.
5. Verify demo URL loads generator and download works.

## Guardrails
- Do not wait for Stripe if a placeholder checkout path exists.
- Keep PII out of client logs.

