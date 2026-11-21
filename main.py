"""A short poem about permission, written for the make.fun contest
"The poem about permission".

The poem's idea: permission is usually imagined as something handed
to you from outside — a knock at the door that someone else must
answer. Here the speaker turns that around: she knocks on her own
door, opens it herself, and realises the power to ask was never
taken from her — she had only forgotten it was hers. The poem is
about taking back the power to act, rather than waiting to be given it.
"""

import os
from pathlib import Path

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
