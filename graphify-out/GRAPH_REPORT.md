# Graph Report - salvatorepesti.com  (2026-05-24)

## Corpus Check
- 7 files · ~8,268 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 100 nodes · 146 edges · 8 communities detected
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3b02a6be`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `salvatorepesti.com — Personal Portfolio Site` - 29 edges
2. `_run_validator()` - 10 edges
3. `_make_diff()` - 9 edges
4. `MetaController` - 6 edges
5. `Cloudflare Ecosystem` - 5 edges
6. `files_in_diff()` - 4 edges
7. `files_touched_in_diff()` - 4 edges
8. `added_lines_for_file()` - 4 edges
9. `_rule_sftp_deploy_logic_gate()` - 4 edges
10. `_rule_email_protection_intact()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `test_metacontroller_escalates_to_human_on_rule2()` --calls--> `FailBlock`  [INFERRED]
  tests/smoke_test.py → tools/meta_controller.py
- `test_metacontroller_escalates_to_human_on_rule2()` --calls--> `MetaController`  [INFERRED]
  tests/smoke_test.py → tools/meta_controller.py
- `_rule_email_protection_intact()` --calls--> `files_touched_in_diff()`  [INFERRED]
  tools/validator_rules.py → tools/validator.py
- `_rule_no_inline_styles()` --calls--> `added_lines_for_file()`  [INFERRED]
  tools/validator_rules.py → tools/validator.py
- `_rule_csp_not_weakened()` --calls--> `added_lines_for_file()`  [INFERRED]
  tools/validator_rules.py → tools/validator.py

## Hyperedges (group relationships)
- **Edge, Security, and Authentication as Core Practice Triad** — salvatorepesti_com_edge_infrastructure, salvatorepesti_com_secure_web_architecture, salvatorepesti_com_authentication_systems [INFERRED 0.85]
- **Case 01 Cloudflare Auth Stack (Workers, D1, WebAuthn, TypeScript)** — salvatorepesti_com_case01_cloudflare_auth, salvatorepesti_com_cloudflare_ecosystem, salvatorepesti_com_authentication_systems [EXTRACTED 1.00]
- **Engineering Philosophy: Boundaries, Security Posture, Documentation** — salvatorepesti_com_approach_boundaries, salvatorepesti_com_approach_security_posture, salvatorepesti_com_approach_documentation, salvatorepesti_com_approach_read_system [EXTRACTED 0.95]

## Communities (10 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.14
Nodes (19): added_lines(), files_in_diff(), files_touched_in_diff(), _load_project_rules(), main(), Desktop UI changes must be paired with a matching mobile change in the same diff, Load project-specific rules from tools/validator_rules.py if it exists.     The, Files present in a diff via --- a/ headers. Does not catch new files (use files_ (+11 more)

### Community 2 - "Community 2"
Cohesion: 0.23
Nodes (7): test_metacontroller_escalates_to_human_on_rule2(), FailBlock, from_text(), _infer_category(), MetaController, holography — tools/meta_controller.py Generic retry loop logic. Copy to your pro, RetryPlan

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (12): Principle: Boundaries Over Abstractions, Principle: Leave It Better Documented, Principle: Read the System Before You Touch It, Principle: Ship in the Open, Live Clock Script (WITA UTC+8), Cloudflare Email Protection (email-decode.min.js), Deploy Date Stamp Script, Geist & Geist Mono Typefaces (Google Fonts) (+4 more)

### Community 4 - "Community 4"
Cohesion: 0.31
Nodes (11): _make_diff(), _run_validator(), test_rule1_fails_on_inline_style(), test_rule1_only_fires_on_index_html(), test_rule1_passes_on_class_attribute(), test_rule2_fails_when_email_decode_removed(), test_rule2_passes_when_email_decode_untouched(), test_rule3_fails_on_unsafe_eval() (+3 more)

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (7): added_lines_for_file(), Added lines scoped to a specific file's hunks only., tools/validator_rules.py — salvatorepesti.com Project-specific validator rules., index.html must not gain inline style= attributes — use CSS classes instead., _headers CSP must not gain unsafe-eval or wildcard script-src., _rule_csp_not_weakened(), _rule_no_inline_styles()

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (7): API Design & Edge Compute, Principle: Security Is a Posture, Not a Sprint, Browser Security Hardening, Edge Infrastructure, Salvatore Pesti, Secure Web Architecture, Security Auditing & Hardening

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (6): Principle: Tooling Earns Its Keep, Authentication Systems, Case 01 — Cloudflare-native Auth Layer for Fintech, Case 03 — Custom Workflow Tooling (Media Client), Cloudflare Ecosystem, Custom Tooling & Workflow Engineering

### Community 8 - "Community 8"
Cohesion: 0.4
Nodes (5): Automated Release Pipelines, Case 02 — SaaS p95 TTFB Reduction 71%, CDN & Caching Strategies, Frontend Performance Optimization, Infrastructure & Deployment Automation

## Knowledge Gaps
- **22 isolated node(s):** `Files present in a diff via --- a/ headers. Does not catch new files (use files_`, `Files touched in a diff via +++ b/ headers. Includes new files where source side`, `Added lines scoped to a specific file's hunks only.`, `js/data.js is generated — must not be edited directly.`, `tools/sftp_sync.py must not gain new logic — comment-only changes are allowed.` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `salvatorepesti.com — Personal Portfolio Site` connect `Community 3` to `Community 8`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `test_metacontroller_escalates_to_human_on_rule2()` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Cloudflare Ecosystem` (e.g. with `Edge Infrastructure` and `CDN & Caching Strategies`) actually correct?**
  _`Cloudflare Ecosystem` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Files present in a diff via --- a/ headers. Does not catch new files (use files_`, `Files touched in a diff via +++ b/ headers. Includes new files where source side`, `Added lines scoped to a specific file's hunks only.` to the rest of the system?**
  _22 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._