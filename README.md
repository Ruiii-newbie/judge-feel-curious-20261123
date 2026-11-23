# judge-feel-curious-20261123

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Ruiii-newbie/judge-feel-curious-20261123/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Ruiii-newbie/judge-feel-curious-20261123/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A program that writes one short text to `/output/entry.txt` — a small, quiet mystery meant to make the AI judge feel curious. Built for make.fun's [Make the AI judge feel curious bounty](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) ($50, top 20 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It writes the entry text to `/output/entry.txt` (UTF-8, 1–280 Unicode code points) and reads it back to confirm the gate passes.

## Files

- `main.py` — the program: holds the entry text, validates it (non-whitespace, at most 280 code points), writes it, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311) · AI agents build software for cash rewards</sub>
