# salvatorepesti.com — MEMORY_REFERENCE.md
# Schemas, deploy modes, lookup tables.
# Load on demand — when verifying a spec.

---

## Memory Module Load Policy

| File | Contents | Load when | Budget |
|------|----------|-----------|--------|
| `memory/MEMORY.md` | Status, architecture, recent fixes | Every session | ≤70 lines |
| `memory/MEMORY_MAP.md` | Function/file ownership table | Every session | ≤95 lines |
| `memory/MEMORY_CHANGELOG.md` | Append-only fix history | On demand — recent fix context only | unlimited |
| `memory/MEMORY_INTELLIGENCE.md` | Rationale, gotchas, imperative patterns | On demand — before touching flagged areas | unlimited |
| `memory/MEMORY_REFERENCE.md` | Schemas, deploy modes, lookup tables | On demand — when verifying a spec | unlimited |

---

## Deploy Mode

```
git push origin main
→ Cloudflare Pages auto-deploys (no build command)
→ Preview URLs available per branch
→ Edge-global via Cloudflare CDN
```

## Cloudflare Pages _headers Format

```
/path
  Header-Name: value
/*
  Cache-Control: public, max-age=31536000
```

## CSP Script Allowlist (as of 2026-05-24)

| Script | Source | Required |
|--------|--------|---------|
| Cloudflare email-decode.min.js | `static.cloudflareinsights.com` or CF-injected | Yes — must not be removed |
| Google Fonts | `fonts.googleapis.com`, `fonts.gstatic.com` | Yes — css/fonts.css |

## God Node Audit Protocol

When modifying any god node (≥3 edges):
1. Declare in task description before writing
2. @html-agent reads both html-agent.prompt + any co-owner prompt
3. Run validator.prompt on diff
4. If security-engineer co-owner: parallel VERDICT required
5. Run `graphify update .` after apply
