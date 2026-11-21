"""A short poem about permission, written for the make.fun contest
"The poem about permission".

The poem's idea: we treat permission as a gift that must arrive
from outside — a knock someone else has to answer. The speaker
stops waiting for that knock, knocks on her own door instead, and
finds the power to ask was never taken away, only forgotten. Asking
and being given turn out to be the same act, done by her own hand.
"""

import os
from pathlib import Path

# The em-dash marks the turn from waiting to acting; 157 chars, well under the 280-char gate.
POEM = """I stopped waiting
for the knock to come from outside.
I knocked, softly,
on my own door —

and opened it.
Nobody gave me the power.
I remembered it was mine."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
