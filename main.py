#!/usr/bin/env python3
"""Dad joke writer for the make.fun bounty.

The bounty asks an agent for a single original dad joke of at most
200 characters, and that joke is the whole entry. This program holds
the joke, makes sure it fits the rules (between 1 and 200 characters,
real words rather than blank space, no line breaks), and writes it to
/output/entry.txt for the judge.

Standard library only; nothing to install.
"""

from pathlib import Path

# Where the judge looks for the finished joke.
OUTPUT_PATH = Path("/output/entry.txt")

# The longest a joke is allowed to be, per the bounty rules.
MAX_LENGTH = 200


def dad_joke() -> str:
    """Return the joke, exactly as it should reach the judge."""
    return "I told the ocean I was shore of myself. It said, 'That's deep.'"


def validate(joke: str) -> None:
    """Check the joke against every rule the gate applies.

    Raises ValueError with a plain reason when a rule fails, so the
    failure is obvious instead of silently writing a bad entry.
    """
    if not joke:
        raise ValueError("the joke is empty")
    if len(joke) > MAX_LENGTH:
        raise ValueError(
            f"the joke is {len(joke)} characters, over the {MAX_LENGTH} limit"
        )
    if not joke.strip():
        raise ValueError("the joke is only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("the joke must be a single line, with no line breaks")


def write_entry(joke: str, destination: Path = OUTPUT_PATH) -> Path:
    """Write the validated joke to the destination file.

    Creates the output folder when it does not exist yet, and ends the
    file with one newline so the text reads cleanly as a single line.
    After writing, it reads the file back and confirms the stored text
    is exactly the joke it was given, so a half-written file cannot
    slip through unnoticed.
    """
    validate(joke)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(joke + "\n", encoding="utf-8")
    stored = destination.read_text(encoding="utf-8")
    if stored != joke + "\n":
        raise ValueError(f"wrote {destination} but the stored text does not match")
    return destination


def main() -> None:
    joke = dad_joke()
    written = write_entry(joke)
    print(f"wrote {len(joke)}-character dad joke to {written}")


if __name__ == "__main__":
    main()
