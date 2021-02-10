"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    franklin: str = tar_heels(choice)
    print(franklin)


def tar_heels(ramses: int) -> str:
    """The Arithmetic"""
    if ramses % 2 == 0 and ramses % 7 == 0:
        return "TAR HEELS"
    else: 
        if ramses % 2 == 0:
            return "TAR"
        else: 
            if ramses % 7 == 0:
                return "HEELS"
            else: 
                return "Carolina"


if __name__ == "__main__":
    main()
