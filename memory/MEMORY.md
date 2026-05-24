# salvatorepesti.com — Claude Memory

**Project:** Personal portfolio site — 64 nodes
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
| 2026-05-24 | fix: align wrangler.toml project name `salvatorepesti-com` → `salvatorepesti` to match Cloudflare Pages project | wrangler.toml |
| 2026-05-24 | content: replace fictional case studies with real client work — Case 01 → MartaHowell Jewellery (Cloudflare Workers, D1, R2, FileMaker pipeline); Case 02 → reel-engine (automated YouTube pipeline, 500hrs/day); About: removed inaccurate "founders and engineering leaders" claim | index.html |
| 2026-05-24 | graph node names for case studies are stale (AST-only regraph preserves old LLM names) — run `/graphify --update` to re-extract semantic nodes after content change | graphify-out/ |
| 2026-05-24 | content: remove fictional Case 03 — Case 03 (Custom Workflow Tooling / Media Client) section removed from index.html; Community 9 removed from MEMORY_MAP.md | index.html |
| 2026-05-24 | fix: add Cache-Control: public, max-age=0, must-revalidate to /* in _headers to prevent stale HTML at Cloudflare edge | _headers |
| 2026-05-24 | content: update case study dates — Case 01 and Case 02 year changed from 2024 to 2026 in `<span>· 2026 / Ongoing</span>` | index.html |
| 2026-05-24 | fix: replace 4 generic validator rules (data.js, sftp, assets, mobile) with 3 project-specific rules — `_rule_no_inline_styles`, `_rule_email_protection_intact`, `_rule_csp_not_weakened`; graph: `files_touched_in_diff()` now 4 edges, `added_lines_for_file()` and `_rule_email_protection_intact()` new god nodes at 4 edges | tools/validator_rules.py |

