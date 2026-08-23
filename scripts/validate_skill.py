#!/usr/bin/env python3
"""Validate the liquid-glass skill without third-party Python packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise ValueError(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail("SKILL.md: missing YAML frontmatter")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"SKILL.md: malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    allowed = {"name", "description", "license", "allowed-tools", "metadata"}
    unexpected = set(result) - allowed
    if unexpected:
        fail(f"SKILL.md: unexpected frontmatter keys: {sorted(unexpected)}")
    return result


def validate(skill_dir: Path) -> None:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        fail("SKILL.md not found")
    skill_text = skill_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)

    name = frontmatter.get("name", "").strip()
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail(f"invalid skill name: {name!r}")
    if len(name) > 64 or name.startswith("-") or name.endswith("-") or "--" in name:
        fail(f"invalid skill name shape: {name!r}")
    description = frontmatter.get("description", "").strip()
    if not description:
        fail("description is empty")
    if len(description) > 1024 or "<" in description or ">" in description:
        fail("description is too long or contains angle brackets")

    if "TODO" in skill_text:
        fail("SKILL.md still contains TODO")

    metadata = skill_dir / "agents" / "openai.yaml"
    metadata_text = metadata.read_text(encoding="utf-8") if metadata.is_file() else ""
    for required in ("display_name:", "short_description:", "default_prompt:", "$liquid-glass"):
        if required not in metadata_text:
            fail(f"agents/openai.yaml missing {required!r}")

    for reference in (skill_dir / "references").glob("*.md"):
        reference_text = reference.read_text(encoding="utf-8")
        if len(reference_text.splitlines()) > 100 and "## Contents" not in reference_text:
            fail(f"{reference.relative_to(skill_dir)} is over 100 lines without a Contents section")
        if "TODO" in reference_text:
            fail(f"{reference.relative_to(skill_dir)} still contains TODO")

    for link in re.findall(r"\]\(([^)]+)\)", skill_text):
        if link.startswith(("http://", "https://", "#")):
            continue
        if not (skill_dir / link).is_file():
            fail(f"SKILL.md link does not resolve: {link}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()
    try:
        validate(args.skill_dir.resolve())
    except ValueError as error:
        print(f"invalid: {error}")
        return 1
    print("valid: liquid-glass skill passed dependency-free validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
