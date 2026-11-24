# One-Line Office Joke: 24-Hour Sprint

[![One-Line Office Joke: 24-Hour Sprint](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/cervus-snoopy/hushed-memo-clock-7k3p/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/cervus-snoopy/hushed-memo-clock-7k3p/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

A tiny Python program that writes one original one-line joke about office life to `entry.txt`, using only the Python 3 standard library and no network access.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Verify

```sh
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
wc -c "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

The output is a single line of at most 200 characters with no trailing newline.
