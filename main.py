"""Robot Romance: One-Line Pickup Lines for AI.

Writes one pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back
to /output/entry.txt): a single line, under 200 characters, aimed at
charming a robot or an AI.
"""

import os

LINE = "I tried to fine-tune my heart on everyone else, but it kept overfitting to you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
