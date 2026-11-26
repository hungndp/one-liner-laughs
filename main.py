#!/usr/bin/env python3
"""One-Liner Laughs entry for make.fun.

Writes a single funny line to /output/entry.txt (or $ENTRY_OUTPUT).
No trailing newline: the gate counts every character.
"""

import os

# The joke, split so the landing lands last.
# Setup: a routine bar request. Punch: the "something strong" he hands
# over is not a drink at all.
SETUP = "I asked the bartender for something strong; he handed me his"
PUNCH = "resignation letter."


def build_line() -> str:
    """Assemble the one-liner from its setup and its punch."""
    return f"{SETUP} {PUNCH}".strip()


def output_path() -> str:
    """Where the line goes: $ENTRY_OUTPUT, else /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"


def write_entry(path: str) -> str:
    """Write the line with NO trailing newline; return what was written."""
    line = build_line()
    if not (1 <= len(line) <= 200):
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return line


def main() -> None:
    line = write_entry(output_path())
    print(line)


if __name__ == "__main__":
    main()
