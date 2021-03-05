"""EX03 - palindromify function."""

__author__: str = "730404260"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("han", True))
    print(palindromify("race", False))
def palindromify(pal: str, possible: bool) -> str:
    """Whether the word can be palindromified."""
    sample_str: str = pal
    if possible == True:
        i: int = len(pal) - 1
    else:
        i: int = len(pal) - 2
    while i >= 0:
        sample_str += pal[i]
        i -= 1
    return sample_str
if __name__ == "__main__":
    main()