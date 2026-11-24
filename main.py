#!/usr/bin/env python3
"""One-line office joke writer.

Writes exactly one office joke, a single line of at most 200
characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Standard library only, no network access.
"""

import os
import stat

JOKE = "HR sent a memo on work-life balance at 11:47 pm, from the office, with a read receipt."

MAX_CHARS = 200


def main():
    line = JOKE
    if not line or not line.strip():
        raise SystemExit("joke must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("joke must be exactly one line")
    if len(line) > MAX_CHARS:
        raise SystemExit("joke exceeds 200 characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: file content differs")
    if written.endswith("\n"):
        raise SystemExit("verification failed: trailing newline present")
    if stat.S_IMODE(os.stat(path).st_mode) != 0o644:
        raise SystemExit("verification failed: file mode is not 0644")


if __name__ == "__main__":
    main()
