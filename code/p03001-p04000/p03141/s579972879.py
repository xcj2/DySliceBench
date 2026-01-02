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
    AB = iml(N)
    ll = []
    for a, b in AB:
        ll.append(a + b)
    ind = np.argsort(ll)[::-1]
    t = [AB[i][0] for i in ind[::2]]
    a = [AB[i][1] for i in ind[1::2]]
    return sum(t) - sum(a)


if __name__ == "__main__":
    print(solve())
