import re
import sys
from itertools import product

import numpy as np

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


def solve():
    S = ii(str)
    a = 0
    b = 0
    for i, s in enumerate(S):
        if i % 2 == 0:
            if s == "0":
                a += 1
            else:
                b += 1
        else:
            if s == "0":
                b += 1
            else:
                a += 1
    return min(a, b)


if __name__ == "__main__":
    print(solve())