#!/usr/bin/env python3
"""Small structural validator for Local Lead Intelligence."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "references/google-maps-and-data-use.md",
    "references/website-audit-rubric.md",
    "templates/lead-brief.md",
    "templates/outreach-draft.md",
    "templates/batch-report.md",
]
missing = [p for p in required if not (ROOT / p).is_file()]
if missing:
    print("Missing required files:", ", ".join(missing))
    sys.exit(1)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    print("SKILL.md must begin with YAML front matter")
    sys.exit(1)
front = skill.split("---\n", 2)[1]
for field in ("name:", "description:"):
    if field not in front:
        print(f"Missing front matter field: {field}")
        sys.exit(1)

if skill.count("---\n") < 2:
    print("SKILL.md front matter is not closed")
    sys.exit(1)

for phrase in (
    "Never bulk-scrape Google Maps",
    "No automatic outreach",
    "Ask for explicit approval before sending",
    "Quality gate",
    "Persist only independently verified records",
    "Do not bypass access controls",
):
    if phrase not in skill:
        print(f"Missing safeguard: {phrase}")
        sys.exit(1)

name = re.search(r"^name:\s*(.+)$", front, re.M)
print(f"OK: {name.group(1) if name else unnamed}")
print(f"OK: {len(required)} required files present")
print("OK: responsible research and approval safeguards present")
