"""The Dog Ate My Homework: Funniest Excuse.

Writes one line -- the excuse a dog gives after being caught eating the
homework, in the dog's own voice -- to /output/entry.txt.

The chosen line plays on the homework's own instruction ("show your work"):
the dog reads it literally and answers with its teeth. No embarrassment,
no apology, no stock excuse -- just a dog who believes it did nothing wrong.
"""

import os

LINE = "It said 'show your work.' I showed it my teeth. Case closed."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the chosen excuse to /output/entry.txt, enforcing the gate.

    The gate is asserted before any write, so a bad line can never reach
    the file: length 1-200 chars, exactly one line, not only whitespace.
    The file is written with a single trailing newline, which the gate
    scorer strips when counting characters.
    """
    # Gate: UTF-8 text, 1-200 characters, single line, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
