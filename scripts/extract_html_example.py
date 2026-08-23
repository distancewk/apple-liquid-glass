#!/usr/bin/env python3
"""Extract the first canonical HTML fixture from a Markdown reference."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def extract(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    match = re.search(r"```html\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ValueError(f"no html fenced block found in {source}")
    return match.group(1) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(extract(args.source), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
