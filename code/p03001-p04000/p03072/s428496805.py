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
    N = ii()
    H = il()
    first = H[0]
    count = 1
    for h in H[1:]:
        if first <= h:
            count += 1
            first = h
    return count


if __name__ == "__main__":
    print(solve())