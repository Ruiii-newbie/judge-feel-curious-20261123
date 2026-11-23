#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a small, quiet mystery --
a concrete image and an open question, in plain words, at an unhurried
pace. No network, standard library only.
"""

import os

TEXT = (
    "On the third floor, a door stands ajar. Behind it, a lamp "
    "burns in an empty room. A cup of tea steams beside a book left open "
    "at the middle page, and the chair is still warm. Nobody "
    "lives here. Somebody was just here. Who reads a book halfway -- and "
    "walks away before the ending?"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 280


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if len(text) > MAX_CODE_POINTS:
        raise SystemExit(
            f"entry text is {len(text)} code points, over the 280 limit"
        )
    return text


def main() -> None:
    text = validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, 1-280 code points.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
