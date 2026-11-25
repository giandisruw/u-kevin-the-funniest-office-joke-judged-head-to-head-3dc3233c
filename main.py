#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes the tournament-winning one-liner to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line won a local pairwise tournament of 12 original candidates, judged
with the Caffeine Inference router (model "router") against the bounty's
published judge brief verbatim: Swiss, 3 rounds, every game in both label
orders, then a final between the top 2. See tournament.jsonl and README.md.

Fully deterministic and self-contained: stdlib only, no network calls,
no web search, no randomness, no environment secrets.
"""
import os
from pathlib import Path

LINE = ("I replied-all asking everyone to stop replying-all, "
        "and now forty-seven of us are apologising in unison.")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
