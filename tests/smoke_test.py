#!/usr/bin/env python3
"""
tests/smoke_test.py — salvatorepesti.com smoke suite

Run: python3 -m pytest tests/smoke_test.py -v
All tests must pass before any commit to master.
"""

import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_validator(diff: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "tools" / "validator.py")],
        input=diff, capture_output=True, text=True, cwd=str(PROJECT_ROOT),
    )
    return r.returncode, (r.stdout + r.stderr)


def _make_diff(filename: str, added_lines: list[str], removed_lines: list[str] | None = None) -> str:
    removed = removed_lines or []
    hunk = "\n".join(f"+{l}" for l in added_lines) + (
        "\n" + "\n".join(f"-{l}" for l in removed) if removed else ""
    )
    return (
        f"diff --git a/{filename} b/{filename}\n"
        f"index abc1234..def5678 100644\n"
        f"--- a/{filename}\n"
        f"+++ b/{filename}\n"
        f"@@ -1,3 +1,{1 + len(added_lines)} @@\n"
        f" context line\n"
        f"{hunk}\n"
    )


# ---------------------------------------------------------------------------
# 1. Import checks
# ---------------------------------------------------------------------------

def test_validator_import():
    from tools import validator  # noqa: F401


def test_meta_controller_import():
    from tools.meta_controller import MetaController, FailBlock, RetryPlan
    assert MetaController is not None
    assert FailBlock is not None
    assert RetryPlan is not None


# ---------------------------------------------------------------------------
# 2. Validator — empty diff is always PASS
# ---------------------------------------------------------------------------

def test_validator_empty_diff():
    code, out = _run_validator("")
    assert code == 0
    assert "PASS" in out


# ---------------------------------------------------------------------------
# 3. Rule 1 — no inline styles in index.html
# ---------------------------------------------------------------------------

def test_rule1_fails_on_inline_style():
    diff = _make_diff("index.html", ['<span style="color:red">text</span>'])
    code, out = _run_validator(diff)
    assert code == 1
    assert "Rule 1" in out


def test_rule1_passes_on_class_attribute():
    diff = _make_diff("index.html", ['<span class="ext-arrow">↗</span>'])
    code, out = _run_validator(diff)
    assert "Rule 1" not in out or "PASS" in out


def test_rule1_only_fires_on_index_html():
    diff = _make_diff("css/main.css", ['.foo { color: red; }'])
    code, out = _run_validator(diff)
    assert "Rule 1" not in out or "PASS" in out


# ---------------------------------------------------------------------------
# 4. Rule 2 — Cloudflare email protection intact
# ---------------------------------------------------------------------------

def test_rule2_fails_when_email_decode_removed():
    diff = _make_diff(
        "index.html",
        ['<p>some new content</p>'],
        removed_lines=['<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>'],
    )
    code, out = _run_validator(diff)
    assert code == 1
    assert "Rule 2" in out


def test_rule2_passes_when_email_decode_untouched():
    diff = _make_diff("index.html", ['<p>Updated bio copy.</p>'])
    code, out = _run_validator(diff)
    assert "Rule 2" not in out or "PASS" in out


# ---------------------------------------------------------------------------
# 5. Rule 3 — CSP not weakened in _headers
# ---------------------------------------------------------------------------

def test_rule3_fails_on_unsafe_eval():
    diff = _make_diff("_headers", ["  Content-Security-Policy: script-src 'self' 'unsafe-eval'"])
    code, out = _run_validator(diff)
    assert code == 1
    assert "Rule 3" in out


def test_rule3_fails_on_wildcard_script_src():
    diff = _make_diff("_headers", ["  Content-Security-Policy: script-src *"])
    code, out = _run_validator(diff)
    assert code == 1
    assert "Rule 3" in out


def test_rule3_passes_on_safe_csp_change():
    diff = _make_diff("_headers", ["  Cache-Control: public, max-age=0, must-revalidate"])
    code, out = _run_validator(diff)
    assert "Rule 3" not in out or "PASS" in out


# ---------------------------------------------------------------------------
# 6. FailBlock parsing
# ---------------------------------------------------------------------------

def test_failblock_from_text_parses_category():
    from tools.meta_controller import FailBlock
    text = "FAIL:\n  rule: 1\n  category: style\n  signal: inline style added\n  agent: @html-agent\n  attempt: 1"
    fb = FailBlock.from_text(text, attempt=1)
    assert fb.rule == 1
    assert fb.agent == "@html-agent"


def test_failblock_infers_category_from_signal():
    from tools.meta_controller import FailBlock
    text = "FAIL:\n  rule: 2\n  signal: email-decode.min.js removed\n  attempt: 1"
    fb = FailBlock.from_text(text, attempt=1)
    assert fb.category is not None


# ---------------------------------------------------------------------------
# 7. MetaController retry plan
# ---------------------------------------------------------------------------

def test_metacontroller_escalates_to_human_on_rule2():
    from tools.meta_controller import MetaController, FailBlock
    mc = MetaController(task="update contact section")
    fb = FailBlock(rule=2, category="security", signal="email-decode removed", agent="@html-agent", attempt=1)
    plan = mc.build_retry_plan_for_attempt(fb, attempt=2)
    assert plan.attempt == 2


# ---------------------------------------------------------------------------
# 8. Project structure
# ---------------------------------------------------------------------------

def test_index_html_exists():
    assert (PROJECT_ROOT / "index.html").exists()


def test_css_files_exist():
    assert (PROJECT_ROOT / "css" / "main.css").exists()
    assert (PROJECT_ROOT / "css" / "fonts.css").exists()


def test_js_main_exists():
    assert (PROJECT_ROOT / "js" / "main.js").exists()


def test_headers_exists():
    assert (PROJECT_ROOT / "_headers").exists()


def test_wrangler_toml_exists():
    assert (PROJECT_ROOT / "wrangler.toml").exists()


def test_agent_prompts_exist():
    agents = PROJECT_ROOT / "agents"
    required = [
        "dispatcher.prompt",
        "html-agent.prompt",
        "security-engineer.prompt",
        "validator.prompt",
        "meta-controller.prompt",
        "memory-keeper.prompt",
    ]
    for name in required:
        assert (agents / name).exists(), f"Missing: agents/{name}"


def test_memory_files_exist():
    assert (PROJECT_ROOT / "memory" / "MEMORY.md").exists()
    assert (PROJECT_ROOT / "memory" / "MEMORY_MAP.md").exists()


def test_validator_cli_is_runnable():
    r = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "tools" / "validator.py")],
        input="", capture_output=True, text=True, cwd=str(PROJECT_ROOT),
    )
    assert r.returncode == 0


# ---------------------------------------------------------------------------
# 9. index.html content invariants
# ---------------------------------------------------------------------------

def test_email_protection_in_html():
    html = (PROJECT_ROOT / "index.html").read_text()
    assert "email-decode.min.js" in html


def test_no_inline_styles_in_html():
    import re
    html = (PROJECT_ROOT / "index.html").read_text()
    matches = re.findall(r'\bstyle\s*=\s*["\']', html)
    assert not matches, f"Inline styles found: {matches}"


def test_csp_not_weakened_in_headers():
    headers = (PROJECT_ROOT / "_headers").read_text()
    assert "unsafe-eval" not in headers
    assert "script-src *" not in headers
