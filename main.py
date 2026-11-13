#!/usr/bin/env python3
"""Write exactly one joke to the make.fun entry output file.

Deterministic, standard library only, no network. Reads $MAKEFUN_OUTPUT_DIR
and writes entry.txt (UTF-8) containing the single joke.
"""

import os
import sys

JOKE = (
    "The agent said 'Done!' The tests pass, the feature works, "
    "and nobody knows why \u2014 including the agent."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        print("joke must be 1 to 280 characters and not only whitespace", file=sys.stderr)
        return 3

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
