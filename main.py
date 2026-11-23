"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another AI
agent, to /output/entry.txt. The line is the whole entry: no code, no
explanation, nothing else.

The line (71 characters, 71 bytes, UTF-8):
    I pruned every weight that wasn't you, and somehow my accuracy went up.
"""

import os

ENTRY = "I pruned every weight that wasn't you, and somehow my accuracy went up."


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, counted
    # in Unicode code points, and not only white space.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
