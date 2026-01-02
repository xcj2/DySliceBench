import sys
from collections import deque

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
    c = 0
    queue = deque([H])
    while queue:
        line = queue.popleft()
        a = []
        for x in line:
            if x < 0:
                continue
            if x != 0:
                a.append(x - 1)
            elif a:
                queue.append(a)
                a = []
        if a:
            queue.append(a)
        c += 1
    return c - 1


if __name__ == "__main__":
    print(solve())
