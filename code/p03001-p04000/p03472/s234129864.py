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


def solve(N, H, A, B):
    a_max = max(A)
    ans = 0
    for b in sorted(B, reverse=True):
        if H <= 0:
            break

        if b > a_max:
            H -= b
            ans += 1
        else:
            break
    if H > 0:
        ans += ceil(H, a_max)
    return ans


def main():
    N, H = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(solve(N, H, A, B))


if __name__ == '__main__':
    main()
