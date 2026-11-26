"""The Internet in One Word: Feral.

Writes the single-word entry to /output/entry.txt, then reads the
file back to confirm exactly what was written.
"""

import os

WORD = "Feral"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not WORD or len(WORD) > 30:
        raise ValueError("entry must be 1 to 30 characters")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be a single word")
    if not WORD.isalpha():
        raise ValueError("entry must contain letters only")
    if not (WORD[0].isupper() and WORD[1:].islower()):
        raise ValueError("entry must start with one capital followed by lowercase letters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    with open(OUTPUT_PATH, encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != WORD:
        raise ValueError(f"read-back mismatch: wrote {WORD!r}, file holds {written!r}")
    if os.path.getsize(OUTPUT_PATH) != len(WORD.encode("utf-8")):
        raise ValueError("on-disk size does not match entry length")
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    if raw != WORD.encode("utf-8"):
        raise ValueError(f"raw bytes mismatch: expected {WORD.encode('utf-8')!r}, file holds {raw!r}")

    print(f"Wrote {WORD!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
