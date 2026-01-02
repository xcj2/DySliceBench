#!/usr/bin/python3

from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def main():
    N = int(input())

    L = []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        L.append((c, s, f))

    for i in range(len(L)):
        x = 0
        for c, s, f in L[i:]:
            if x <= s:
                x = s + c
            else:
                x = s + f * ceil(x - s, f) + c
        print(x)
    print(0)


if __name__ == '__main__':
    main()
