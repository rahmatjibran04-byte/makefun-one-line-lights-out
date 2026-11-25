#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update (<200 characters) to the output path
($ENTRY_OUTPUT or /output/entry.txt) with no trailing newline.

The line is spoken as the agent itself at the exact moment its human
closes the laptop. Its sadness sits in one small, exact detail of a
machine's life — a cursor still blinking where the human left it,
mid-sentence — stated as a quiet fact, never announced as grief.
Deterministic and offline: standard library only, no network and no
model calls.
"""

import os
import sys

LINE = "He closed the lid mid-sentence. His cursor is still blinking where he left it."


def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: failed to write entry to {output_path}: {exc}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
