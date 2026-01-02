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


def solve(cake_list, M, p1, p2, p3):
    a, b, c = 0, 0, 0
    l = []
    for x, y, z in cake_list:
        k = x * p1 + y * p2 + z * p3
        l.append((k, x, y, z))

    for k, x, y, z in list(sorted(l, reverse=True))[:M]:
        a += x
        b += y
        c += z

    return abs(a) + abs(b)  + abs(c)


def main():
    N, M = map(int, input().split())
    cake = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cake.append((x, y, z))

    ans = -INF
    for p1, p2, p3 in product([-1, +1], repeat=3):
        ans = max(ans, solve(cake, M, p1, p2, p3))
    print(ans)

if __name__ == '__main__':
    main()
