"""EX03 - avoid_fifth function."""

__author__: str = "730404260"
vernacular: str = ""


def main() -> None:
    """Entrypoint of the program."""
    vernacular: str = input(str("Type any string: "))
    print(avoid_fifth(vernacular))


def avoid_fifth(e_sucks: str) -> str:
    randstr: str = ""
    """The function that offs the letter that shall not be named."""
    for character in e_sucks:
        if character.lower() != "e":
            randstr += character
    return randstr


if __name__ == "__main__":
    main()