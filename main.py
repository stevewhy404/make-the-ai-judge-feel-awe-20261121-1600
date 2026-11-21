"""make-the-ai-judge-feel-awe-20261121-1600: writes one short text to entry.txt.

Python 3.13, stdlib only, no network, deterministic.
"""

import os

TEXT = (
    "The sea comes in after dark, one slow wave at a time, "
    "over sand still warm from the day. Above it, the stars keep "
    "arriving: light that left home before there were houses, "
    "before there were names for any of this \u2014 and it is only now reaching us."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
