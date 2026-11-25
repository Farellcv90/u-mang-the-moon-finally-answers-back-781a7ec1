#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

The angle: the Moon, wry and old after four billion years of listening
to every wish, every howl, every 2 a.m. promise, finally answers back —
not with another blessing, but by making a wish of its own: it is
clocking off. The joke lands because the Moon has always been the
audience for humanity's late-night confessions; tonight the roles flip
and the listener asks for a night off.

Writes one line, spoken as the Moon answering everyone who has ever
stared up at it: the wishes, the howls, the late-night promises.
Validates the gate (UTF-8, 1-240 chars, not only whitespace) and writes
the entry to /output/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "I've heard every wish, every howl, every 2 a.m. promise "
    "for four billion years \u2014 so tonight I'm making one of my own: "
    "I'm off the clock."
)


def main() -> None:
    text = ENTRY
    # Gate validation: UTF-8, 1-240 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if len(encoded) > 240:
        raise SystemExit(f"entry is {len(encoded)} UTF-8 bytes, over 240")
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"entry length {len(text)} outside 1-240 chars")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
