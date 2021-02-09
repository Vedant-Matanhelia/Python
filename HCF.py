# A Program to return the hcf of numbers in a list
import math
from functools import reduce

math.gcd()


def gcd(num1: int, num2: int) -> int:
    hcf = 0
    if num1 > num2:
        mn = num2
    else:
        mn = num1

    for i in range(1, mn + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf


def gcd_list(numbers: list) -> int:
    hcf = reduce(lambda x, y: gcd(x, y), numbers)
    return hcf


print(gcd_list([25, 125]))
