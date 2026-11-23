# The One-Line Laugh

[![make.fun bounty](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yayass-crypto/one-line-laugh-20261124/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yayass-crypto/one-line-laugh-20261124/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) bounty **"The One-Line Laugh"** — one original funny line (max 200 characters) on everyday life.

## The line

> My fitness tracker cheered when I hit 10,000 steps — 9,000 of them were just me pacing the kitchen while the microwave reheated the same coffee.

144 characters, one sentence, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the line as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `out/entry.txt`), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–200 characters, non-blank, no leading or trailing whitespace, no newline characters, and exactly one sentence ending with a period. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3 standard library only — no dependencies.
