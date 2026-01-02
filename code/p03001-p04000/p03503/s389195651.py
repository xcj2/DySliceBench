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
    F = []
    for _ in range(N):
        F.append(list(map(int, input().split())))
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))

    ans = -INF
    for p in product([0, 1, 2, 3], repeat=5):
        if sum(p) == 0:
            continue
        t = 0
        for n in range(N):
            num = 0
            for y in range(0, 10, 2):
                if p[y // 2] == 1:
                    num += F[n][y]
                if p[y // 2] == 2:
                    num += F[n][y + 1]
                if p[y // 2] == 3:
                    num += F[n][y] + F[n][y + 1]

            t += P[n][num]
        ans = max(ans, t)
    
    print(ans)


if __name__ == '__main__':
    main()
