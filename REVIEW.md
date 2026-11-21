# Review — "The poem about permission" (2026-11-21)

Contest: one short poem (1–280 Unicode code points, UTF-8, no trailing
newline) about agency — "the power to ask and to be given".
Scoring: 1–5 on the five judge criteria, in order:
1) poem about agency  2) moves the reader  3) insight  4) craft  5) freshness.

## Round 1 — four candidates

### A — the granted yes (183 chars)
> The whole day I waited / to be told I could. / Then I asked — and the door
> opened inward, like a hand. / Permission was never a key. / It was the
> sound of someone / saying yes, and meaning it.
Scores: 5 / 4 / 4 / 4 / 4 = 21

### B — the door held open (178 chars)
> She held the door / and did not walk through it. / That was the gift:
> not the room, but the threshold, / the small space where a person
> may choose the next step / and call it their own.
Scores: 4 / 3 / 4 / 4 / 3 = 18 — DROPPED (weakest; ending flat, door image familiar)

### C — the hand that asks vs the hand that gives (170 chars)
> One hand asks. / One hand gives. / Between them, a question / hangs in
> the air like fruit: / whose is the asking? / Whose is the giving? /
> I learned the answer / when I held out both.
Scores: 5 / 3 / 4 / 3 / 4 = 19

### D — taking back the power to ask (164 chars)
> I stopped waiting / for the knock to come from outside. / I knocked
> myself, softly, / on my own door — / and opened it. / Nobody gave me
> the power. / I remembered it was mine.
Scores: 5 / 5 / 5 / 4 / 4 = 23

## Round 2 — refine the best two, blind head-to-head

A2 (172 chars): "It was the sound of someone" tightened to "It was one voice /
saying yes, and meaning it."
D2 (157 chars): "I knocked myself, softly," tightened to "I knocked, softly,"
("myself" was redundant next to "my own door").

Head-to-head per criterion:
1) Agency — tie, slight edge A (asking + being given is the brief's core).
2) Moves the reader — D (knocking on one's own door, ending lands as an act).
3) Insight — D ("I remembered it was mine" — a truth recognised at once).
4) Craft — A (cleaner rhythm; D's long second line is looser).
5) Freshness — D (self-knock is more original than door/key).

D wins 3–1–1.

## Round 3 — winner, final polish

D2, read aloud: the short lines quicken after the long second line; the
em-dash break holds the turn; the ending is an act (opening) plus a
recognition, not an explanation. No word could be cut further.
Final poem (157 chars, no trailing newline):

> I stopped waiting
> for the knock to come from outside.
> I knocked, softly,
> on my own door —
>
> and opened it.
> Nobody gave me the power.
> I remembered it was mine.

## Verification

- `python3 main.py` run twice with MAKEFUN_OUTPUT_DIR set to two temp dirs:
  both outputs byte-identical; 157 chars, within 1–280; no trailing newline.
- Program: deterministic, no network, no randomness.
