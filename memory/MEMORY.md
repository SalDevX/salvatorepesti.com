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
| CF config | `cloudflare.toml` | Pages name + build output dir |

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

*(populated by @memory-keeper after each commit)*

| Date | What | File |
|------|------|------|
| 2026-05-24 | holography framework installed | full agent layer |
| 2026-05-24 | memory-bootstrapper: filled human context in MEMORY.md | memory/MEMORY.md |
| 2026-05-24 | domain-agent-builder: created html-agent, tooling-agent, security-engineer prompts; updated AGENTS.md + dispatcher.prompt | agents/ |
| 2026-05-24 | refactor: single-file → multi-file; created index.html, css/main.css, css/fonts.css, js/main.js, _headers, _redirects, cloudflare.toml; removed 4 inline styles (→ .ext-arrow class); added CSP via _headers; updated all agent prompts + MEMORY_MAP.md | index.html, css/, js/, _headers |

