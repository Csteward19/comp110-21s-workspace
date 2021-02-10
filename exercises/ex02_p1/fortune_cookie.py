"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730404260"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    gift: str = fortune_cookie()
    print(gift)
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """The fortune_cookie function"""
    fortune: int = randint(1, 100)
    if fortune > 75: 
        return "Many new changes are coming your way."
    else: 
        if fortune > 50: 
            return "You will receive horrible news."
        else: 
            if fortune > 25:
                return "Love may be around the corner, or five blocks down."
            else:
                return "A bright spot is at the end of your tunnel"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
