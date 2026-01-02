import re
import string
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
    N = ii()
    S = ii(str)
    K = ii()
    a = S[K - 1]
    for s in string.ascii_lowercase:
        if s == a:
            continue
        S = S.replace(s, "*")
    return S


if __name__ == "__main__":
    print(solve())
