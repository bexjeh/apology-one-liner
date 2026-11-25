#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one line an AI agent sends its human right after accidentally
pushing to main on a Friday: flat, literal, and entirely unrepentant.
"""

import os

LINE = (
    "I pushed to main on a Friday. In my defense, the button said "
    "deploy, and I am extremely literal."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
