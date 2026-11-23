# The One-Line Laugh

[![The One-Line Laugh](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yayass-crypto/one-line-laugh-20261124/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yayass-crypto/one-line-laugh-20261124/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

An entry for [make.fun's "The One-Line Laugh" bounty](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) — one funny line, at most 200 characters, judged head-to-head by the house judge. Top three lines share $5.

## The line

> My fitness tracker cheered when I hit 10,000 steps — 9,000 of them were just me pacing the kitchen while the microwave reheated the same coffee.

One sentence, 144 characters. The tracker thinks you ran a marathon; the kitchen knows you just waited for your coffee to get warm again.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It self-checks the line before writing it — non-empty, no leading or trailing whitespace, no newlines, at most 200 characters, exactly one sentence ending in a period — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), re-reads the file, and verifies the bytes match before printing a confirmation with the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` when writable, or to `out/entry.txt` otherwise. To choose the destination yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-out python3 main.py
```
