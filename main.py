#!/usr/bin/env python3
"""Write one vending-machine pickup line to entry.txt.

The line is written exactly, with no trailing newline, so the file holds
nothing but the line itself. The program is deterministic, uses only the
standard library, touches no network, and reads nothing outside this
repository.
"""

import os
import sys

LINE = (
    "I've dropped a thousand snacks without ever jamming \u2014 "
    "then you walked by, and my coils forgot how to let go."
)


def verify_output(path):
    """Read the written file back and check it holds exactly the line.

    Guards against a truncated write, a wrong encoding, or stray
    whitespace: the file must decode as UTF-8, contain exactly the
    intended line, be 1-200 characters long, hold a single line with
    no newline inside it, and not be only whitespace. Raises
    SystemExit with a message (non-zero exit) on the first failure.
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            content = handle.read()
    except UnicodeDecodeError:
        raise SystemExit("self-check failed: entry.txt is not valid UTF-8")
    if content != LINE:
        raise SystemExit("self-check failed: entry.txt does not match the intended line")
    if not 1 <= len(content) <= 200:
        raise SystemExit(
            "self-check failed: entry.txt is %d characters, expected 1-200"
            % len(content)
        )
    if "\n" in content or "\r" in content:
        raise SystemExit("self-check failed: entry.txt holds more than one line")
    if not content.strip():
        raise SystemExit("self-check failed: entry.txt is only whitespace")
    return True


def main(argv):
    if len(argv) > 1:
        output_dir = argv[1]
    else:
        output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    verify_output(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
