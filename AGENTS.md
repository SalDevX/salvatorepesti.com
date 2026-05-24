# salvatorepesti.com — AGENTS.md
# Specialized agent team for 72 nodes.
# Last updated: 2026-05-24 (5d985fa)

---

## Routing — which file to read

| Task | Read this file |
|------|----------------|
| ALL tasks — entry point (read first) | `agents/dispatcher.prompt` |
| Edit `index.html`, `css/`, `js/`, `_headers`, `_redirects`, `wrangler.toml`, `.gitignore` | `agents/html-agent.prompt` |
| Edit `tools/validator.py`, `tools/validator_rules.py`, `tools/meta_controller.py`, `bin/` | `agents/tooling-agent.prompt` |
| Doc sync after commit / MEMORY.md / MEMORY_MAP.md | `agents/memory-keeper.prompt` |
| Security review — auth, I/O, external scripts, credentials | `agents/security-engineer.prompt` |
| Validate any output before applying to disk | `agents/validator.prompt` |
| FAIL escalation from any agent — retry loop | `agents/meta-controller.prompt` |

Cross-agent task: read both relevant prompt files. No others.

---

## Memory load policy

| File | Load when | Line budget |
|------|-----------|-------------|
| `memory/MEMORY.md` | Every session | ≤70 lines |
| `memory/MEMORY_MAP.md` | Every session | ≤95 lines |
| `memory/MEMORY_CHANGELOG.md` | On demand — recent fix context only | unlimited |
| `memory/MEMORY_INTELLIGENCE.md` | On demand — before touching flagged areas | unlimited |
| `memory/MEMORY_REFERENCE.md` | On demand — when verifying a spec | unlimited |

---

## Global invariants — apply to every task, every agent

**Hard rules — never break:**
- Never modify god nodes without declaring in task description: `salvatorepesti.com — Personal Portfolio Site` (index.html, 29 edges), `Cloudflare Ecosystem` (index.html + _headers, 5 edges), `Edge Infrastructure` (index.html + _headers + wrangler.toml, 4 edges)
- Run `graphify update .` after every code change (zero API cost — AST only)

**After every code change:**
1. `graphify update .`
2. `python3 tools/refresh_god_nodes.py` — patches god nodes table in AGENTS.md
3. Update `memory/MEMORY.md` with today's date
4. Update `memory/MEMORY_MAP.md` if new functions added
5. `python3 -m pytest tests/smoke_test.py -v` — all tests must pass

**Agent ownership — apply to every task, every agent:**
- Each agent may ONLY modify files listed in its `## AGENT OWNERSHIP` block
- God Nodes require full cross-agent audit before any change — declare in task description before writing

**Strict output mode — apply to every agent response:**
- Return ONLY diff or complete file
- No explanation unless `--explain` is appended to the request
- No prose preamble or postamble

**Validator gate — required before any diff is applied:**
- Run `agents/validator.prompt` on every code diff before writing to disk
- FAIL → retry with escalated model (see validator.prompt retry ladder)
- 2× FAIL same rule → escalate to human, do NOT auto-apply

---

## God Nodes — never touch without full cross-agent audit

Graph source: `graphify-out/GRAPH_REPORT.md` · 72 nodes · 100 edges · last run 2026-05-24

| Node | Edges | File | Owner | Notes |
|------|-------|------|-------|-------|
| `salvatorepesti.com — Personal Portfolio Site` | 29 | `index.html + css/ + js/` | @html-agent | Full cross-agent audit required |
| `MetaController` | 5 | `tools/meta_controller.py` | @tooling-agent | Retry loop core — changes cascade to bin/meta-controller |
| `Cloudflare Ecosystem` | 5 | `index.html + _headers` | @html-agent | Verify Cloudflare scripts intact |
| `files_in_diff()` | 4 | `tools/validator.py` | @tooling-agent | Used by validator rules — signature change breaks all |
| `files_touched_in_diff()` | 4 | `tools/validator.py` | @tooling-agent | Includes new files — used by _rule_email_protection_intact |
| `added_lines_for_file()` | 4 | `tools/validator.py` | @tooling-agent | File-scoped line extractor — used by inline-style and CSP rules |
| `_rule_sftp_deploy_logic_gate()` | 4 | `tools/validator.py` | @tooling-agent | Universal fallback — NOT active (overridden by validator_rules.py) |
| `_rule_email_protection_intact()` | 4 | `tools/validator_rules.py` | @tooling-agent + @html-agent | Prevents removal of CF email-decode.min.js — Rule 2: human review |
| `Edge Infrastructure` | 4 | `index.html + _headers + wrangler.toml` | @html-agent | Cache/CDN config must not regress |
| `Secure Web Architecture` | 4 | `index.html + _headers` | @html-agent + @security-engineer | Parallel security review required |
| `Case 02 — reel-engine — fully automated YouTube content production pipeline` | 4 | `index.html` | @html-agent | Owner confirmation before changing metrics |
| `added_lines()` | 3 | `tools/validator.py` | @tooling-agent | All added lines (not file-scoped) — used by universal fallback rules |
| `Salvatore Pesti` | 3 | `index.html` | @html-agent | Owner confirmation before changing bio/identity |
| `CDN & Caching Strategies` | 3 | `index.html` | @html-agent | Performance claims — verify before editing |
| `Security Auditing & Hardening` | 3 | `index.html` | @html-agent + @security-engineer | Parallel security review required |

### Critical Path

`salvatorepesti.com — Personal Portfolio Site` (index.html + css/ + js/) has 29 edges — changes cascade across the graph.
`MetaController` (tools/meta_controller.py) has 5 edges — retry loop core; changes cascade to bin/meta-controller.
Declare in task description before writing. Full cross-agent audit required.
