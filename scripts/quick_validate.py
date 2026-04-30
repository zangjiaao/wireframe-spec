#!/usr/bin/env python3
"""Quick validation script for local skill repositories.

Validates:
1) SKILL.md frontmatter shape and allowed keys
2) Required core files for this skill repo
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64

ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}

# Project-local required files for wireframe-spec.
REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "scripts/quick_validate.py",
    "agents/openai.yaml",
    "references/wireframe-standards.md",
    "references/templates/mobile-layout-template.html",
    "references/templates/desktop-layout-template.html",
]


def validate_frontmatter(skill_md: Path) -> tuple[bool, str]:
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        return False, f"Invalid YAML in frontmatter: {exc}"

    if not isinstance(frontmatter, dict):
        return False, "Frontmatter must be a YAML dictionary"

    unexpected = set(frontmatter.keys()) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        allowed = ", ".join(sorted(ALLOWED_FRONTMATTER_KEYS))
        bad = ", ".join(sorted(unexpected))
        return False, f"Unexpected frontmatter key(s): {bad}. Allowed: {allowed}"

    for required_key in ("name", "description"):
        if required_key not in frontmatter:
            return False, f"Missing '{required_key}' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, "Name should be hyphen-case (lowercase letters, digits, hyphens)"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, "Name cannot start/end with hyphen or contain consecutive hyphens"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"Name is too long ({len(name)}), max is {MAX_SKILL_NAME_LENGTH}"

    desc = frontmatter.get("description", "")
    if not isinstance(desc, str):
        return False, f"Description must be a string, got {type(desc).__name__}"
    desc = desc.strip()
    if "<" in desc or ">" in desc:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(desc) > 1024:
        return False, f"Description too long ({len(desc)}), max is 1024"

    return True, "Frontmatter is valid"


def validate_required_files(skill_dir: Path) -> tuple[bool, str]:
    missing = [rel for rel in REQUIRED_FILES if not (skill_dir / rel).exists()]
    if missing:
        return False, "Missing required file(s): " + ", ".join(missing)
    return True, "Required files are present"


def validate_skill(skill_dir: Path) -> tuple[bool, list[str]]:
    messages: list[str] = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, ["SKILL.md not found"]

    ok, msg = validate_frontmatter(skill_md)
    messages.append(msg)
    if not ok:
        return False, messages

    ok, msg = validate_required_files(skill_dir)
    messages.append(msg)
    if not ok:
        return False, messages

    messages.append("Skill is valid!")
    return True, messages


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/quick_validate.py <skill_directory>")
        return 1

    skill_dir = Path(sys.argv[1]).expanduser().resolve()
    ok, messages = validate_skill(skill_dir)
    for message in messages:
        print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
