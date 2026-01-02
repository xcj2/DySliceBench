import sys

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
    S = [1 if s == "W" else -1 for s in S]
    pivot = np.argmin(np.cumsum(S))
    E = S[:pivot].count(1)
    W = S[pivot+1:].count(-1)
    return E + W


if __name__ == "__main__":
    print(solve())
