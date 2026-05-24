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
