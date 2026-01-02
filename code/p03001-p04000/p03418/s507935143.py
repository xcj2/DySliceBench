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

def solve(N, K):
    if K == 0:
        return N * N

    ans = 0
    for b in range(1, N + 1):
        now = K
        while K <= b and now <= N:
            ans += min(N, now + (b - K) - 1) - now + 1
            now += b
    return ans

def main():
    N, K = map(int, input().split())

    print(solve(N, K))

if __name__ == '__main__':
    main()
