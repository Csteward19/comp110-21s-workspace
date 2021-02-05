"""An exercise in remainders and boolean logic."""

__author__ = "730404260"


# Begin your solution here...
a = int(input("Enter an int: "))
print(a)
if a % 2 == 0 and a % 7 == 0:
    print("TAR HEELS")
else:
    if a % 2 == 0:
        print("TAR")
    else:
        if a % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
