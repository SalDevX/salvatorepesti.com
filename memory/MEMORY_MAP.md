# salvatorepesti.com — MEMORY_MAP.md
# Who does what and where. Keep in sync with refactors.
# Last updated: 2026-05-24

---

## Community 0 — Meta-Controller (tools/meta_controller.py)

| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `tools/meta_controller.py` | `MetaController`, `FailBlock`, `RetryPlan`, `from_text()`, `_infer_category()` | **YES — 5 edges** | Retry loop core — cross-agent audit before changing |
| `bin/meta-controller` | `run_agent()`, `run_validator()`, `dry_run()`, `main()` | — | Entry: `bin/meta-controller --task "..."` |

## Community 1 — Portfolio Presentation (index.html + js/main.js)

| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `index.html` | Principles (Boundaries, Documentation, Ship in the Open, Read the System) | — | Principle nodes — owner confirmation before changing |
| `js/main.js` | `Live Clock Script (WITA UTC+8)`, `Scroll Reveal Script (IntersectionObserver)`, Deploy Date Stamp | — | `clock()`, reveal(), deploy stamp |
| `index.html` | `Cloudflare Email Protection (email-decode.min.js)`, `Geist & Geist Mono Typefaces` | — | Must not remove CF email script |

## Community 2 — Validator Core (tools/validator.py)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `tools/validator.py` | `_load_project_rules()`, `main()` | — | Loads optional `tools/validator_rules.py` |

## Community 3 — Validator Rules: Project-Specific (tools/validator_rules.py)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `tools/validator_rules.py` | `_rule_no_inline_styles()`, `_rule_email_protection_intact()`, `_rule_csp_not_weakened()`, `RULES`, `RETRY_WITH` | `_rule_email_protection_intact()` **4 edges** | Overrides all universal rules; Rule 2+3 escalate to human |
| `tools/validator.py` | `added_lines_for_file()` | **4 edges** | File-scoped line extractor — called by inline-style and CSP rules |

## Community 4 — CDN / Performance (index.html)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `index.html` | `Case 02 — reel-engine — fully automated YouTube content production pipeline`, `CDN & Caching Strategies`, `Frontend Performance Optimization`, `Infrastructure & Deployment Automation`, `Automated Release Pipelines` | `Case 02` **4 edges** (pending regraph), `CDN & Caching Strategies` **3 edges** | 500hrs/day shipped — owner confirmation before editing |

## Community 5 — Cloudflare / Edge (index.html + _headers + wrangler.toml)

| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `index.html` | `Case 01 — MartaHowell Jewellery — Cloudflare-native commerce and data infrastructure`, `API Design & Edge Compute`, `Authentication Systems` | — | Workers, D1, R2, FileMaker pipeline |
| `index.html` + `_headers` | `Cloudflare Ecosystem`, `Edge Infrastructure` | `Cloudflare Ecosystem` **5 edges**, `Edge Infrastructure` **4 edges** | CSP + CDN config — parallel security review |
| `wrangler.toml` | Pages config — name, build output dir | — | No credentials — safe to commit |

## Community 6 — Security (index.html + _headers)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `index.html` | `Salvatore Pesti`, `Browser Security Hardening`, `Secure Web Architecture`, `Security Auditing & Hardening`, `Principle: Security Is a Posture` | `Secure Web Architecture` **4 edges**, `Security Auditing & Hardening` **3 edges**, `Salvatore Pesti` **3 edges** | Identity + security nodes — owner + security-engineer audit |

## Community 7 — Validator Rules: Diff Parsing (tools/validator.py)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `tools/validator.py` | `files_in_diff()`, `_rule_no_direct_data_js_edit()` | `files_in_diff()` **4 edges** | Parses `--- a/` headers; does NOT catch new files; `_rule_no_direct_data_js_edit` is universal fallback — NOT active (overridden by validator_rules.py) |

## Community 8 — Validator Rules: Mobile/Desktop Parity / Email (tools/validator.py)
| File | Key functions / nodes | God node? | Notes |
|------|-----------------------|-----------|-------|
| `tools/validator.py` | `files_touched_in_diff()`, `removed_lines()`, `_rule_mobile_desktop_parity()` | `files_touched_in_diff()` **4 edges** | Parses `+++ b/` headers; includes new files; `_rule_mobile_desktop_parity` is universal fallback — NOT active (overridden by validator_rules.py) |

---

## Agent System — @memory-keeper

| File | Key functions | Owner | Notes |
|------|---------------|-------|-------|
| `CLAUDE.md` | Session start protocol | @memory-keeper | `@AGENTS.md` always injected |
| `AGENTS.md` | Routing table + god nodes | @memory-keeper | Always in context via `@` include |
| `agents/dispatcher.prompt` | ROUTE block, routing table, god node detection | @memory-keeper | Read first on every task |
| `agents/html-agent.prompt` | HTML/CSS/JS/Cloudflare config ownership | @memory-keeper | Read for index.html, css/, js/, _headers tasks |
| `agents/tooling-agent.prompt` | Validator, meta-controller, bin ownership | @memory-keeper | Read for tools/ and bin/ tasks |
| `agents/security-engineer.prompt` | Security review VERDICT | @memory-keeper | Parallel read-only — triggered by dispatcher |
| `agents/validator.prompt` | Validation ruleset, retry ladder | @memory-keeper | Run after every diff |
| `agents/meta-controller.prompt` | Retry strategy, ESCALATE block | @memory-keeper | Triggered on validator FAIL |
| `memory/MEMORY.md` | Project status | @memory-keeper | Read every session |
| `memory/MEMORY_MAP.md` | This file | @memory-keeper | Read every session |
| `tools/validator.py` | `files_in_diff()`, `files_touched_in_diff()`, `added_lines()`, `added_lines_for_file()`, `main()` | @tooling-agent | Run: `git diff \| python3 tools/validator.py` |
| `tools/meta_controller.py` | `MetaController`, `FailBlock`, `RetryPlan`, `build_retry_plan_for_attempt()`, `from_text()`, `_infer_category()` | @tooling-agent | Retry loop |
| `bin/meta-controller` | `run_agent()`, `run_validator()`, `dry_run()`, `main()` | @tooling-agent | Entry: `bin/meta-controller --task "..."` |
| `tests/smoke_test.py` | Smoke tests | @tooling-agent | Does not exist yet — skip until created |
| `logs/` | Failure reports | @meta-controller | `meta-controller-YYYY-MM-DD-HH-MM-SS.md` |
| `index.html` | All markup, Cloudflare email protection, case studies | @html-agent | Entry point — all god nodes declared here |
| `css/fonts.css` | Google Fonts @import | @html-agent | Load order: fonts.css → main.css |
| `css/main.css` | All styles incl. `.ext-arrow`, `.reveal`, layout | @html-agent | No inline styles in HTML |
| `js/main.js` | `clock()`, deploy date stamp, `reveal()` | @html-agent | Replaces all former inline scripts |
| `_headers` | CSP, HSTS, cache-control per path | @html-agent + @security-engineer | Update CSP when adding new external origins |
| `_redirects` | `/salvatorepesti.com.html → /`, `/index.html → /` | @html-agent | Cloudflare Pages redirect rules |
| `wrangler.toml` | Pages config — name, build output dir | @html-agent | Auto-detected by Wrangler; renamed cloudflare.toml d06cd53; project name salvatorepesti-com→salvatorepesti 216ab7a |
| `.gitignore` | Git ignore rules | @html-agent | Added d06cd53 |
