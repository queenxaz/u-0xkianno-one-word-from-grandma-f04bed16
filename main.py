"""One Word From Grandma — entry program.

Writes the single word a grandma would text about AI to /output/entry.txt.
No network, no randomness, no arguments: the word is fixed.
"""

import os

WORD = "Alexa"  # Grandma's whole idea of AI is the Alexa in her kitchen.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
