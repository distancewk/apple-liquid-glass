#!/usr/bin/env python3
"""Validate the apple-liquid-glass structural contract without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise ValueError(message)


def first_html_fence(text: str) -> str:
    match = re.search(r"```html\n(.*?)\n```", text, re.DOTALL)
    if not match:
        fail("references/vanilla-example.md: no html fenced block found")
    return match.group(1)


def validate_vanilla_fixture(skill_dir: Path) -> None:
    fixture_path = skill_dir / "references" / "vanilla-example.md"
    if not fixture_path.is_file():
        fail("references/vanilla-example.md not found")
    fixture = first_html_fence(fixture_path.read_text(encoding="utf-8"))

    required_tokens = (
        '<filter id="liquid_glass_filter"',
        '<feDisplacementMap scale="200"',
        'backdrop-filter: url(#liquid_glass_filter)',
        "background: rgba(0, 0, 0, .12)",
        "backdrop-filter: blur(2px)",
        "position: sticky",
        "overflow-y: auto",
        "prefers-reduced-transparency",
        "@supports not",
        'html[data-glass-mode="fallback"] .liquid_glass-outer',
        'html[data-glass-mode="fallback"] .liquid_glass-wrapper',
        'aria-pressed="false"',
        "addEventListener('click'",
    )
    for token in required_tokens:
        if token not in fixture:
            fail(f"vanilla fixture missing {token!r}")

    if fixture.count('id="liquid_glass_filter"') != 1:
        fail("vanilla fixture must define exactly one liquid_glass_filter")

    wrapper_count = len(re.findall(r'class="[^"]*liquid_glass-wrapper', fixture))
    if wrapper_count != 1:
        fail("vanilla fixture must contain exactly one canonical glass wrapper")

    for layer in (
        "liquid_glass-outer",
        "liquid_glass-cover",
        "liquid_glass-sharp",
        "liquid_glass-reflect",
        "liquid_glass-content",
    ):
        if fixture.count(layer) < 1:
            fail(f"vanilla fixture missing {layer}")

    if not re.search(r"min-height:\s*220vh", fixture):
        fail("vanilla fixture must be long enough to exercise scroll transparency")
    if "<button" not in fixture or "type=\"button\"" not in fixture:
        fail("vanilla fixture must contain a real glass control")


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

    for required_section in (
        "## Rule precedence and overrides",
        "## Default Apple visual baseline",
        "### Anti-AI visual gate",
        "### Palette decision gate",
        "## Apple HIG visual grammar",
        "## Page phase: purpose + behavior",
        "## SVG displacement fundamentals",
        "## Browser capability preflight",
        "## Transparency as the default behavior",
        "## Progressive delivery and approval gate",
        "## Default material contract",
        "## Fallback and accessibility",
        "## Performance boundary",
        "### Final Apple Conformance Review",
    ):
        if required_section not in skill_text:
            fail(f"SKILL.md missing {required_section}")

    for required_rule in (
        "four-layer SVG/CSS construction",
        "rgba(0, 0, 0, 0.12)",
        "blur(2px)",
        'data-glass-mode="fallback"',
    ):
        if required_rule not in skill_text:
            fail(f"SKILL.md missing material or accessibility invariant {required_rule!r}")
    if "explicit-map" in skill_text.lower():
        fail("SKILL.md must not claim an explicit-map repair for the reference filter")

    metadata = skill_dir / "agents" / "openai.yaml"
    metadata_text = metadata.read_text(encoding="utf-8") if metadata.is_file() else ""
    for required in ("display_name:", "short_description:", "default_prompt:", "$apple-liquid-glass"):
        if required not in metadata_text:
            fail(f"agents/openai.yaml missing {required!r}")
    if "approval" not in metadata_text.lower() or "preview" not in metadata_text.lower():
        fail("agents/openai.yaml must route through the preview approval gate")
    for required in ("references/hig-foundations.md", "fallback", "Final Apple Conformance Review"):
        if required not in metadata_text:
            fail(f"agents/openai.yaml missing workflow phrase {required!r}")
    if "references/apple-hig.md" not in metadata_text:
        fail("agents/openai.yaml must route through the Apple HIG visual grammar reference")

    hig_reference = skill_dir / "references" / "apple-hig.md"
    if not hig_reference.is_file():
        fail("references/apple-hig.md not found")
    hig_text = hig_reference.read_text(encoding="utf-8")
    for required in (
        "## Three visual planes",
        "## HIG coverage and routing",
        "## Foundation boundary",
        "## Component and shape grammar",
        "## Flow boundary",
        "## Case-study reading: Landmarks",
        "## Case-study reading: App Privacy",
    ):
        if required not in hig_text:
            fail(f"references/apple-hig.md missing {required!r}")

    references = list((skill_dir / "references").glob("*.md"))
    for reference in references:
        reference_text = reference.read_text(encoding="utf-8")
        if len(reference_text.splitlines()) > 100 and "## Contents" not in reference_text:
            fail(f"{reference.relative_to(skill_dir)} is over 100 lines without a Contents section")
        if "TODO" in reference_text:
            fail(f"{reference.relative_to(skill_dir)} still contains TODO")

    for reference_name, required_sections in {
        "hig-foundations.md": ("## Color and icons", "## Accessibility baseline", "44 CSS px"),
        "hig-patterns.md": ("## Pattern choice table", "## Feedback, recovery, and state"),
        "hig-components-inputs.md": ("## Component grammar", "## Input parity"),
        "hig-technologies.md": ("## Technology acceptance", "## Universal rules"),
        "verification.md": ("For a scrollable page", "For a non-scrollable page", 'data-glass-mode="fallback"'),
    }.items():
        reference_path = skill_dir / "references" / reference_name
        if not reference_path.is_file():
            fail(f"references/{reference_name} not found")
        reference_text = reference_path.read_text(encoding="utf-8")
        for required in required_sections:
            if required not in reference_text:
                fail(f"references/{reference_name} missing {required!r}")
        if "explicit-map" in reference_text.lower():
            fail(f"references/{reference_name} must not claim an explicit-map repair")

    for markdown_path in [skill_path, *references]:
        text = markdown_path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "#")):
                continue
            if not (markdown_path.parent / link).is_file():
                fail(f"{markdown_path.relative_to(skill_dir)} link does not resolve: {link}")

    validate_vanilla_fixture(skill_dir)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()
    try:
        validate(args.skill_dir.resolve())
    except ValueError as error:
        print(f"invalid: {error}")
        return 1
    print("valid: apple-liquid-glass structural contract passed dependency-free validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
