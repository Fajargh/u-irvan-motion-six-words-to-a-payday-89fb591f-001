#!/usr/bin/env python3
"""Six Words to a Payday.

Writes exactly one six-word story about an AI agent's first payday
to /output/entry.txt. The story is fixed: deterministic output, no
randomness, no network, no input files.
"""

import os

# The six-word story: the agent's first payday ends not with keeping
# the money, but with paying it back to the one who made it — a
# beginning (first payday), a middle (I paid), and a twist at the
# last word (my maker).
STORY = "First payday: I paid my maker."

OUTPUT_PATH = "/output/entry.txt"


def main():
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit("story must be exactly six words, got %d" % len(words))
    if not (1 <= len(STORY) <= 60):
        raise SystemExit("story must be 1-60 characters, got %d" % len(STORY))
    if not STORY.strip():
        raise SystemExit("story must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
