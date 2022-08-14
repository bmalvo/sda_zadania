"""Wilson primes satisfy the following condition. Let P represent a prime number.

Then,

((P-1)! + 1) / (P * P)
should give a whole number.

Your task is to create a function that returns true if the given number is a Wilson prime."""
from math import factorial as ftrl


def am_i_wilson(n):
    return n > 2 and ((ftrl(n-1) + 1) / (n * n)).is_integer()


print(am_i_wilson(13))
