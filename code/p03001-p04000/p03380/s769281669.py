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

def solve(A):
    t = A[-1] / 2
    b = INF
    ans = -1
    for a in A:
        if abs(t - a) < b:
            b = abs(t - a)
            ans = a

    return A[-1], ans

def main():
    n = int(input())
    A = list(sorted(list(map(int, input().split()))))
    print(*solve(A))


if __name__ == '__main__':
    main()
