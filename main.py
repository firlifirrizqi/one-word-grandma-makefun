#!/usr/bin/env python3
"""One Word From Grandma: the single word a grandma would text about AI.

The word is "AIYOH" -- the warm, baffled exclamation a Southeast Asian
grandma types when her grandchild shows her a talking robot. It carries
the AI right in its first two letters, and the rest is pure grandma:
a little startled, a little delighted, and instantly readable.
"""

import os

WORD = "AIYOH"


def main() -> None:
    # Self-check the gate: one word, 1-30 UTF-8 characters, not blank.
    word = WORD.strip()
    assert 1 <= len(word.encode("utf-8")) <= 30 and word.split() == [word]
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
