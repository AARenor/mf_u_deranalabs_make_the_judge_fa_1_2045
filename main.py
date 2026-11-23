"""Write the one-line entry for make.fun bounty u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
