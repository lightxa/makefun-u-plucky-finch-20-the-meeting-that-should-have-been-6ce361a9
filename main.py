"""The Meeting That Should Have Been an Email.

Writes one original one-line joke about a meeting that should have
been an email to /output/entry.txt. Pure standard library, fully
deterministic, no network access, no input read from anywhere.
"""

from pathlib import Path

ENTRY = (
    "We held a meeting to discuss the email about the meeting, "
    "then scheduled a follow-up to discuss the meeting about the email."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the single-line entry, exactly as it will be written."""
    return ENTRY


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
