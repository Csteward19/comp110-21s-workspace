"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730404260"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
import builtins
from random import randint


# Begin your solution here...
a: str = "Your fortune cookie says"
print(a)
b: int =  randint(0, 100)
if b > 75: 
    print("Many new changes are coming your way")
elif b > 50: 
    print("You will receive horrible news")
elif b > 25: 
    print("Love may be around the corner, or five blocks down")
else: 
    print("A bright spot is at the end of your tunnel")
c: str = "Now go spread positive vibes"
print(c)