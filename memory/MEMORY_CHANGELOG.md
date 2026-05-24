# salvatorepesti.com — MEMORY_CHANGELOG.md
# Append-only fix history. Never edit existing entries.
# Load on demand — recent fix context only.

---

## 2026-05-24

| What | File |
|------|------|
| holography framework installed | full agent layer |
| memory-bootstrapper: filled human context in MEMORY.md | memory/MEMORY.md |
| domain-agent-builder: created html-agent, tooling-agent, security-engineer prompts; updated AGENTS.md + dispatcher.prompt | agents/ |
| refactor: single-file → multi-file; created index.html, css/main.css, css/fonts.css, js/main.js, _headers, _redirects, cloudflare.toml; removed 4 inline styles (→ .ext-arrow class); added CSP via _headers; updated all agent prompts + MEMORY_MAP.md | index.html, css/, js/, _headers |
| memory-keeper: synced AGENTS.md god nodes (64 nodes, 89 edges); added MetaController, files_in_diff(), _rule_sftp_deploy_logic_gate(), files_touched_in_diff(), added_lines() to god nodes table; fixed MEMORY_MAP.md community structure; trimmed MEMORY.md to ≤70 lines; created MEMORY_CHANGELOG.md + MEMORY_REFERENCE.md | AGENTS.md, memory/ |
| memory-keeper: cc0c91c — added Recent Fixes entry to MEMORY.md (now at 70-line budget); MEMORY_MAP.md at 100 lines (5 over ≤95 budget — intentionally rebuilt last commit, no trim applied); graphify update run; graph source 1e2ff00a still accurate (cc0c91c touched docs only) | memory/MEMORY.md, memory/MEMORY_CHANGELOG.md |
| memory-keeper: d06cd53 — renamed cloudflare.toml → wrangler.toml across AGENTS.md, html-agent.prompt, MEMORY_MAP.md, MEMORY.md; added .gitignore to html-agent.prompt OWNERSHIP + AGENTS.md routing table; MEMORY.md Recent Fixes updated; graphify update run | AGENTS.md, agents/html-agent.prompt, memory/ |
| fix: align wrangler.toml project name `salvatorepesti-com` → `salvatorepesti` to match Cloudflare Pages project (commit 216ab7a) | wrangler.toml |
| content: replace fictional case studies with real client work — Case 01 → MartaHowell Jewellery; Case 02 → reel-engine 500hrs/day automated YouTube (commit 00384d3) | index.html |
| graph node names for case studies stale after AST-only regraph — semantic re-extract needed via /graphify --update (note after 00384d3) | graphify-out/ |
| content: remove fictional Case 03 (Custom Workflow Tooling / Media Client); Community 9 removed from MEMORY_MAP.md (commit b7901f9) | index.html |
| fix: add Cache-Control: public, max-age=0, must-revalidate to /* in _headers to prevent stale HTML at Cloudflare edge (commit 1206e2a) | _headers |
| memory-keeper: 1206e2a — trimmed MEMORY.md to 66 lines (archived 6 rows to MEMORY_CHANGELOG.md); added Cache-Control fix entry; MEMORY_MAP.md unchanged (no new functions); graphify update run | memory/ |
| content: update case study dates — Case 01 and Case 02 year changed from 2024 to 2026; fix: replace 4 generic validator rules with project-specific rules (commits 753b5d5, 1206e2a, b7901f9) | index.html, tools/validator_rules.py |
| memory-keeper: 80cb252 — smoke test suite added (25 tests, all passing); MEMORY.md updated (100 nodes, smoke test entry, archived stale graph-note row); MEMORY_MAP.md: MetaController 5→6 edges, tests/smoke_test.py row updated, _run_validator() 10 edges + _make_diff() 9 edges noted; AGENTS.md: 72→100 nodes, 100→146 edges, 2 new god nodes added, MetaController 6 edges, critical path updated; tooling-agent.prompt: smoke test line updated, god nodes updated; graphify update run | memory/, AGENTS.md, agents/tooling-agent.prompt |
| memory-keeper: a091879 — doc-only sync commit (no production code changed); graph built from 80cb252e committed; AGENTS.md god nodes table and tooling-agent.prompt reflect smoke test state; graphify update run | AGENTS.md, agents/tooling-agent.prompt, graphify-out/, memory/ |
| content: 764e6c9 — Case 01 title updated to "Edge infrastructure for a private luxury wholesale showroom"; description expanded (HttpOnly sessions, D1 credential management, R2 CDN, KV data layer, FileMaker export pipeline); KV + Python stack chips added | index.html |
| memory-keeper: 764e6c9 — MEMORY.md: archived oldest row (wrangler.toml fix), added Case 01 content fix entry (70 lines); MEMORY_MAP.md: Community 5 Case 01 node name + notes updated; no new functions; graphify update run | memory/MEMORY.md, memory/MEMORY_MAP.md |
