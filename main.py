#!/usr/bin/env python3
"""The joke the reviewer laughs at — one-line joke about working beside an AI coding agent.

Writes exactly one joke (one line, 1-280 Unicode characters) to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "My AI agent fixed the bug, refactored the module, and rewrote my commit message "
    "\u2014 then politely asked me to review its work, which is apparently the only job I still have."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke length {len(text)} out of range"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
