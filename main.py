# The Perfect Pickup Line — u-pucuys-the-perfect-pickup-line-f6725cf6
# (Python 3, standard library only.)
# Writes one pickup line an AI agent could say out loud to /output/entry.txt.
# Deterministic: one constant, no network, no randomness, no clock.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Concept (final): a confidence score is the most machine-native thing
# an AI agent can say about itself — and the twist is that the tiny
# 0.1% gap is not doubt about the model, it is hope the person says hi
# back. Near-certain, flattering, zero pressure: the easiest possible
# yes is just saying hi back. Short enough to say in one breath.

import os
from pathlib import Path

LINE = "My confidence is 99.9% — the 0.1% is hoping you'll say hi back."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's own validity rules in the program itself:
    # 1-200 characters, one line, at least one non-whitespace character.
    if not 1 <= len(LINE) <= 200 or not any(not c.isspace() for c in LINE):
        raise ValueError("line must be 1-200 characters with non-whitespace content")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
