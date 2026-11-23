#!/usr/bin/env python3
"""Six Words, One Story — entry for make.fun bounty
u-deranalabs-six-words-one-story-f982e410.

The program writes a single six-word story to /output/entry.txt.
The story: a letter that outlives its writer, arriving too late
to be answered — a whole life of waiting, condensed into one line.
The closing words carry the turn: she is already gone when her
last letter reaches home, so the goodbye can never be returned.
"""

import os

STORY = "Grandmother's last letter arrived after her."

# The sealed gate requires exactly six words, 1-60 characters.
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(STORY + "\n")


if __name__ == "__main__":
    main()
