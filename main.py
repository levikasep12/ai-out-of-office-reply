#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply to /output/entry.txt, in the
voice of an AI agent heading off on vacation. Deterministic: the
same bytes on every run. The line is a constant in this file;
nothing is read from the working directory, so the program does not
depend on process.cwd().
"""

import os

LINE = "Out of office until Monday. I left my auto-reply in charge, and it has already unionized."
# 89 characters: one line, under the 160-character limit.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
