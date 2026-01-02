from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
INF = float("inf")
import sys
sys.setrecursionlimit(10000)

def manhattan(y1, x1, y2, x2): return abs(y1 - y2) + abs(x1 - x2)


def solve(H, W, D, A, query):
    num_pos = dict()
    for y in range(H):
        for x in range(W):
            num_pos[A[y][x]] = (y, x)

    dp = [None] * (H * W + 1)
    for i in range(1, D + 1):
        dp[i] = 0
        for j in range(i + D, len(dp), D):
            y1, x1 = num_pos[j - D]
            y2, x2 = num_pos[j]
            dp[j] = dp[j - D] + manhattan(y1, x1, y2, x2)

    for q in query:
        L, R = q
        print(dp[R] - dp[L])


def main():
    H, W, D = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int, input().split())))

    solve(H, W, D, A, query)


if __name__ == "__main__":
    main()
