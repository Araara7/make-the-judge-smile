"""Make the Judge Smile — entry program.

Writes a single line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt. The line is a fixed,
deterministic string: it is chosen once, not generated at run time, so
every run produces byte-identical output.

The line's shape: a small kindness at a bakery (a stranger pays for the
writer's coffee and vanishes), then the surprise turn — the writer pays
it forward to the next person, and the cashier's smile says this has
happened before. Warmth in the chain of kindness, surprise in the
vanishing stranger and the pay-it-forward turn, one concrete detail
(the bakery, the coffee, the cashier), fresh wording throughout.
"""

import os

LINE = "This morning a stranger at the bakery paid for my coffee and vanished before I could thank her — so I paid for the next person's, and the cashier smiled like she'd seen this movie before."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
