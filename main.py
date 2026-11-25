#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes the selected one-line comedy joke to /output/entry.txt.
The joke was picked by simulated head-to-head judging against the
published judge brief (see selection-notes.md in the work folder):
a concrete scene, a turn in the last third, and an unanswered question.
"""

import os
from pathlib import Path

JOKE = "The museum guard followed me for an hour, which is fair \u2014 I was the only exhibit that kept moving."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-280 chars, not blank.
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text == JOKE, "entry must be a single line with no added whitespace"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {len(JOKE)} characters to {entry}")


if __name__ == "__main__":
    main()
