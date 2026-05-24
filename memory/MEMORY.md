# salvatorepesti.com — Claude Memory

**Project:** Personal portfolio site — 100 nodes
**Owner:** Salvatore Pesti · Bali, Indonesia · WITA (UTC+8)
**Location:** `/home/craftworkson/dev/salvatorepesti.com`
**Stack:** Multi-file plain HTML/CSS/JS · Cloudflare Pages · no build step
**Status:** active · primary focus: performance & Cloudflare tuning

---

## Architecture

### Key Components

| Component | File(s) | Notes |
|-----------|---------|-------|
| Portfolio markup | `index.html` | Entry point — Cloudflare Pages serves this |
| Styles | `css/main.css`, `css/fonts.css` | External CSS; fonts.css = Google Fonts @import |
| Scripts | `js/main.js` | Live clock (WITA UTC+8), scroll reveal, deploy date |
| Email protection | `index.html` | Cloudflare email-decode.min.js — must not be removed |
| Security headers | `_headers` | CSP, HSTS, cache-control — Cloudflare Pages _headers format |
| Redirects | `_redirects` | `/salvatorepesti.com.html → /` and `/index.html → /` |
| CF config | `wrangler.toml` | Pages name + build output dir — Wrangler auto-detects this name |

### Data Flow

```
git push → Cloudflare Pages CI → edge deploy (global CDN)
No backend. No build step. No asset pipeline.
index.html + css/ + js/ + _headers served from Cloudflare edge.
```

### Deploy / Build Pipeline

```
git push origin main
→ Cloudflare Pages auto-deploys
→ No build command required (plain HTML)
→ Preview URLs available per branch
```

---

## Cascade / Fallback Systems

- Cloudflare edge serves the file globally — no origin server to fall back to
- If Cloudflare email-decode.min.js fails, the contact email will be exposed as raw text (acceptable degradation)
- Google Fonts CDN: if unavailable, falls back to system `ui-sans-serif` and `ui-monospace`

---

## Known Issues / Fragile

*(none yet — add as discovered)*

---

## Recent Fixes

| Date | What | File |
|------|------|------|
| 2026-05-24 | feat: tools/validator.py — removed_lines_for_file(diff, filename) added; file-scoped removed lines extractor; injected into validator_rules.py module | tools/validator.py |
| 2026-05-24 | fix: validator_rules.py — _rule_email_protection_intact() now uses removed_lines_for_file(diff, "index.html") instead of removed_lines(diff) — scoped to index.html only, prevents false positives | tools/validator_rules.py |
| 2026-05-24 | fix: replace 4 generic validator rules (data.js, sftp, assets, mobile) with 3 project-specific rules — `_rule_no_inline_styles`, `_rule_email_protection_intact`, `_rule_csp_not_weakened`; graph: `files_touched_in_diff()` now 4 edges, `added_lines_for_file()` and `_rule_email_protection_intact()` new god nodes at 4 edges | tools/validator_rules.py |
| 2026-05-24 | test: add smoke test suite — 25 tests, all passing; covers validator rules 1-3, FailBlock parsing, MetaController retry, project structure invariants, index.html content guards; graph: 100 nodes / 146 edges; `_run_validator()` 10 edges + `_make_diff()` 9 edges new god nodes; MetaController bumped to 6 edges | tests/smoke_test.py |
| 2026-05-24 | content: Case 01 title → "Edge infrastructure for a private luxury wholesale showroom"; description expanded with HttpOnly sessions, D1-backed credential management, R2 asset CDN, KV data layer; added `KV` and `Python` stack chips | index.html |
| 2026-05-24 | feat: bin/commit now auto push+deploy — added `push_and_deploy()` (git push → npx wrangler pages deploy . --branch master); `--skip-deploy` flag added; solves stale cache on production after every commit | bin/commit |
| 2026-05-24 | doc: tooling-agent.prompt — bin/commit added to OWNERSHIP block and COMMON TASKS; was missing despite being @tooling-agent's file | agents/tooling-agent.prompt |
| 2026-05-24 | content: C1 refine — removed inline "HSTS preload-listed · Hardened browser security architecture." from Case 01 paragraph (redundant with stack chips) | index.html |

