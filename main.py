"""Museum of the Year 3000 — entry program.

Writes a single museum label, as a museum in the year 3000 would place it
beside an ordinary object from today, to /output/entry.txt.

The label is a fixed string: no network, no randomness, no clock, no
environment input. The gate requires 1-200 characters of UTF-8 text, so
the program validates the length before writing. The label is one line:
a deadpan curator, centuries later, misreading a parking meter as a
machine citizens paid to rent the ground beneath their own vehicles.
"""

import os

LABEL = (
    "Parking meter, c. 2024. Citizens fed it coins to rent the ground "
    "beneath their own vehicles. No one remembers why the ground "
    "charged rent."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LABEL) <= MAX_CHARS:
        raise ValueError(
            "label must be 1-%d characters, got %d" % (MAX_CHARS, len(LABEL))
        )
    if LABEL != LABEL.strip() or not LABEL.strip():
        raise ValueError("label must not be blank or padded with whitespace")
    if "\n" in LABEL or "\r" in LABEL:
        raise ValueError("label must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
