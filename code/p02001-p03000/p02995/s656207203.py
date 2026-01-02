import sys
from collections import Counter, deque, defaultdict
from itertools import accumulate, permutations, combinations, takewhile, compress, cycle
from functools import reduce
from math import ceil, floor, log10, log2, factorial
from pprint import pprint

sys.setrecursionlimit(1000000)
# MOD = 10 ** 9 + 7
# N = int(input())
# A = [int(x) for x in input().split()]
# V = [[0] * 100 for _ in range(100)]
# A = [int(input()) for _ in range(N)]

A, B, C, D = [int(x) for x in input().split()]


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def f(a, b, c):
    if a % c == 0:
        a1 = a // c
    else:
        a1 = a // c + 1
    b1 = b // c
    r = b1 - a1 + 1
    return r


# c = (B - A + 1) // C
# d = (B - A + 1) // D
# cd = (B - A + 1) // (C * D)

c = f(A, B, C)
d = f(A, B, D)
cd = f(A, B, lcm(C, D))

n = B - A + 1
print(n - c - d + cd)
