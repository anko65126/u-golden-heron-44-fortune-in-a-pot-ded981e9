"""Entry point for the Fortune in a Pot bounty.

Writes one kind, funny fortune for a houseplant to /output/entry.txt.
The line is at most 120 characters, deterministic, and needs no
network access. The joke is the plant's quiet revenge: growth the
human cannot keep up with, and watering finally done on time.
"""
from pathlib import Path

LINE = (
    "This week you will be repotted, praised, and — for once — watered before you have to ask."
)

TARGET = Path("/output/entry.txt")


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
