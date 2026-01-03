import math
from functools import reduce

N = int(input())
T = [int(input()) for i in range(N)]

# def gcd(numbers):  # "numbers" is list
#     return reduce(math.gcd, numbers)

# def lcm_base(x, y):
#     return (x * y) // math.gcd(x, y)


#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


#a,bの最小公倍数
def lcm_base(a, b):
    return a * b // gcd(a, b)


def lcm(numbers):  # "numbers" is list
    return reduce(lcm_base, numbers,
                  1)  # [third argument] return 1 if "numbers" is empty


print(lcm(T))