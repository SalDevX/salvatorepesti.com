"""
tools/validator_rules.py — salvatorepesti.com
Project-specific validator rules. Overrides universal fallback rules in validator.py.
"""

import re

# -- helpers injected by validator.py: files_in_diff, files_touched_in_diff,
#    added_lines, added_lines_for_file, removed_lines, removed_lines_for_file, PROJECT_ROOT


def _rule_no_inline_styles(diff: str) -> tuple[bool, str]:
    """index.html must not gain inline style= attributes — use CSS classes instead."""
    for line in added_lines_for_file(diff, "index.html"):
        if re.search(r'\bstyle\s*=\s*["\']', line):
            return False, "Rule 1: inline style= added to index.html — use a CSS class in main.css"
    return True, ""


def _rule_email_protection_intact(diff: str) -> tuple[bool, str]:
    """Cloudflare email-decode.min.js script tag must not be removed from index.html."""
    touched = files_touched_in_diff(diff)
    if "index.html" not in touched:
        return True, ""
    for line in removed_lines_for_file(diff, "index.html"):
        if "email-decode.min.js" in line:
            return False, "Rule 2: Cloudflare email-decode.min.js removed from index.html — this breaks email obfuscation"
    return True, ""


def _rule_csp_not_weakened(diff: str) -> tuple[bool, str]:
    """_headers CSP must not gain unsafe-eval or wildcard script-src."""
    for line in added_lines_for_file(diff, "_headers"):
        if "unsafe-eval" in line or "script-src *" in line or "default-src *" in line:
            return False, "Rule 3: CSP weakened in _headers — unsafe-eval or wildcard src added"
    return True, ""


RULES = [
    _rule_no_inline_styles,
    _rule_email_protection_intact,
    _rule_csp_not_weakened,
]

RETRY_WITH = {
    "Rule 1": "claude-sonnet-4-6",
    "Rule 2": "human",
    "Rule 3": "human",
}
