"""EX03 - prime functions."""

__author__: str = "730404260"


def main() -> None:
    """Entrypoint of the program."""
    print("If true, number is prime. If false, number is composite.")
    print(is_prime(5))
    print(list_primes(2, 10))
    

def is_prime(num: int) -> bool:
    """Determines if a number is prime."""
    if num > 1:
        for specific in range(2,100):
            if num % specific == 0 and num != specific:
                return False
            else:
                return True
    else:
        return False
    

def list_primes(param1: int, param2: int) -> list[int]:
    """Will return all primes between two numbers."""
    to_be_returned: list[int] = []
    for step in range(param1, param2):
        if is_prime(step) is True:
            to_be_returned.append(step)
    return to_be_returned
    

if __name__ == "__main__":
    main()