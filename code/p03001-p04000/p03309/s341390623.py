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

def calc(b, A):
    ans = 0
    for i, a in enumerate(A, start=1):
        ans += abs(a - (b + i))
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(sorted([a - i for i, a in enumerate(A, start=1)]))

    ans = INF
    x = N // 2
    for i in range(max(0, x - 1), min(x + 1, N)):
        ans = min(ans, calc(B[i], A))
    print(ans)


if __name__ == '__main__':
    main()
