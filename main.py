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
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
