# Graph Report - salvatorepesti.com  (2026-05-24)

## Corpus Check
- 5 files · ~6,702 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 64 nodes · 89 edges · 11 communities detected
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d06cd53c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 11|Community 11]]

## God Nodes (most connected - your core abstractions)
1. `salvatorepesti.com — Personal Portfolio Site` - 29 edges
2. `MetaController` - 5 edges
3. `Cloudflare Ecosystem` - 5 edges
4. `files_in_diff()` - 4 edges
5. `_rule_sftp_deploy_logic_gate()` - 4 edges
6. `Edge Infrastructure` - 4 edges
7. `Secure Web Architecture` - 4 edges
8. `Case 02 — SaaS p95 TTFB Reduction 71%` - 4 edges
9. `files_touched_in_diff()` - 3 edges
10. `added_lines()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Cloudflare Ecosystem` --conceptually_related_to--> `CDN & Caching Strategies`  [INFERRED]
  salvatorepesti.com.html → salvatorepesti.com.html  _Bridges community 4 → community 6_
- `_rule_sftp_deploy_logic_gate()` --calls--> `files_in_diff()`  [EXTRACTED]
  tools/validator.py → tools/validator.py  _Bridges community 8 → community 3_
- `salvatorepesti.com — Personal Portfolio Site` --references--> `Salvatore Pesti`  [EXTRACTED]
  salvatorepesti.com.html → salvatorepesti.com.html  _Bridges community 1 → community 5_
- `salvatorepesti.com — Personal Portfolio Site` --references--> `Edge Infrastructure`  [EXTRACTED]
  salvatorepesti.com.html → salvatorepesti.com.html  _Bridges community 1 → community 4_
- `salvatorepesti.com — Personal Portfolio Site` --references--> `CDN & Caching Strategies`  [EXTRACTED]
  salvatorepesti.com.html → salvatorepesti.com.html  _Bridges community 1 → community 6_

## Hyperedges (group relationships)
- **Edge, Security, and Authentication as Core Practice Triad** — salvatorepesti_com_edge_infrastructure, salvatorepesti_com_secure_web_architecture, salvatorepesti_com_authentication_systems [INFERRED 0.85]
- **Case 01 Cloudflare Auth Stack (Workers, D1, WebAuthn, TypeScript)** — salvatorepesti_com_case01_cloudflare_auth, salvatorepesti_com_cloudflare_ecosystem, salvatorepesti_com_authentication_systems [EXTRACTED 1.00]
- **Engineering Philosophy: Boundaries, Security Posture, Documentation** — salvatorepesti_com_approach_boundaries, salvatorepesti_com_approach_security_posture, salvatorepesti_com_approach_documentation, salvatorepesti_com_approach_read_system [EXTRACTED 0.95]

## Communities (12 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.24
Nodes (6): FailBlock, from_text(), _infer_category(), MetaController, holography — tools/meta_controller.py Generic retry loop logic. Copy to your pro, RetryPlan

### Community 1 - "Community 1"
Cohesion: 0.18
Nodes (12): Principle: Boundaries Over Abstractions, Principle: Leave It Better Documented, Principle: Read the System Before You Touch It, Principle: Ship in the Open, Live Clock Script (WITA UTC+8), Cloudflare Email Protection (email-decode.min.js), Deploy Date Stamp Script, Geist & Geist Mono Typefaces (Google Fonts) (+4 more)

### Community 2 - "Community 2"
Cohesion: 0.5
Nodes (3): _load_project_rules(), main(), Load project-specific rules from tools/validator_rules.py if it exists.     The

### Community 3 - "Community 3"
Cohesion: 0.4
Nodes (5): added_lines(), tools/sftp_sync.py must not gain new logic — comment-only changes are allowed., Asset filenames referenced in diffs must exist on disk in assets/., _rule_asset_path_consistency(), _rule_sftp_deploy_logic_gate()

### Community 4 - "Community 4"
Cohesion: 0.4
Nodes (5): API Design & Edge Compute, Authentication Systems, Case 01 — Cloudflare-native Auth Layer for Fintech, Cloudflare Ecosystem, Edge Infrastructure

### Community 5 - "Community 5"
Cohesion: 0.4
Nodes (5): Principle: Security Is a Posture, Not a Sprint, Browser Security Hardening, Salvatore Pesti, Secure Web Architecture, Security Auditing & Hardening

### Community 6 - "Community 6"
Cohesion: 0.4
Nodes (5): Automated Release Pipelines, Case 02 — SaaS p95 TTFB Reduction 71%, CDN & Caching Strategies, Frontend Performance Optimization, Infrastructure & Deployment Automation

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (4): files_touched_in_diff(), Desktop UI changes must be paired with a matching mobile change in the same diff, Files touched in a diff via +++ b/ headers. Includes new files where source side, _rule_mobile_desktop_parity()

### Community 8 - "Community 8"
Cohesion: 0.5
Nodes (4): files_in_diff(), Files present in a diff via --- a/ headers. Does not catch new files (use files_, js/data.js is generated — must not be edited directly., _rule_no_direct_data_js_edit()

### Community 9 - "Community 9"
Cohesion: 0.67
Nodes (3): Principle: Tooling Earns Its Keep, Case 03 — Custom Workflow Tooling (Media Client), Custom Tooling & Workflow Engineering

## Knowledge Gaps
- **19 isolated node(s):** `Files present in a diff via --- a/ headers. Does not catch new files (use files_`, `Files touched in a diff via +++ b/ headers. Includes new files where source side`, `Added lines scoped to a specific file's hunks only.`, `js/data.js is generated — must not be edited directly.`, `tools/sftp_sync.py must not gain new logic — comment-only changes are allowed.` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `salvatorepesti.com — Personal Portfolio Site` connect `Community 1` to `Community 9`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.193) - this node is a cross-community bridge._
- **Why does `files_in_diff()` connect `Community 8` to `Community 2`, `Community 3`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Why does `_rule_sftp_deploy_logic_gate()` connect `Community 3` to `Community 8`, `Community 2`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Cloudflare Ecosystem` (e.g. with `Edge Infrastructure` and `CDN & Caching Strategies`) actually correct?**
  _`Cloudflare Ecosystem` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Files present in a diff via --- a/ headers. Does not catch new files (use files_`, `Files touched in a diff via +++ b/ headers. Includes new files where source side`, `Added lines scoped to a specific file's hunks only.` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._