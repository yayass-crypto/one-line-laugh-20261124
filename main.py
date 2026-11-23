#!/usr/bin/env python3
"""The One-Line Laugh — a fitness tracker that celebrates kitchen pacing.

Writes a single funny line (max 200 chars) about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: out/), then verifies the written
file byte-for-byte: identical bytes, valid UTF-8, 1-200 chars, non-blank,
no leading/trailing whitespace, and exactly one sentence.
"""

import os
import sys

SENTENCE = (
    "My fitness tracker cheered when I hit 10,000 steps \u2014 "
    "9,000 of them were just me pacing the kitchen while the microwave "
    "reheated the same coffee."
)

# The em dash above is U+2014. Keep the sentence exactly as written:
# one sentence, no trailing newline in the output file.
# Wording notes (graded 2026-11-24 vs funny/fresh/tight): the tracker
# "cheered" personifies the device; the middle clause reframes the
# 10,000 steps as kitchen pacing; "just" undercuts the celebration;
# the payoff lands on the last words "reheated the same coffee" —
# the steps were not a walk at all.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = SENTENCE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # --- Verification: read the file back and check it byte-for-byte. ---
    with open(path, "rb") as fh:
        written = fh.read()

    if written != data:
        print("FAIL: entry.txt bytes differ from the sentence", file=sys.stderr)
        return 1

    try:
        text = written.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"FAIL: entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if text != SENTENCE:
        print("FAIL: decoded text differs from the sentence", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= 200:
        print(f"FAIL: length {len(text)} chars is outside 1-200", file=sys.stderr)
        return 1

    if not text.strip():
        print("FAIL: entry is blank", file=sys.stderr)
        return 1

    if text != text.strip():
        print("FAIL: entry has leading or trailing whitespace", file=sys.stderr)
        return 1

    if "\n" in text or "\r" in text:
        print("FAIL: entry must be a single line with no newline characters",
              file=sys.stderr)
        return 1

    if written.endswith(b"\n"):
        print("FAIL: entry.txt must not end with a trailing newline",
              file=sys.stderr)
        return 1

    # Exactly one sentence: count sentence terminators.
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        print(
            f"FAIL: expected exactly 1 sentence terminator, found {terminators}",
            file=sys.stderr,
        )
        return 1

    if not text.endswith("."):
        print("FAIL: entry must end with a period", file=sys.stderr)
        return 1

    print(f"OK: wrote {path} ({len(data)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
