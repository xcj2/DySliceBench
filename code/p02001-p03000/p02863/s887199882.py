import sys
from collections import deque
from functools import lru_cache
import bisect
import copy
import heapq
import itertools
import math
import random
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, T = read_values()
    P = sorted([tuple(read_values()) for _ in range(N)], key=lambda p: (p[0], -p[1]))

    dp = [[0] * (T + 2) for _ in range(N + 1)]

    for i, (a, b) in enumerate(P):
        for t in range(T + 1):
            if t < T:
                s = min(T, t + a)
                dp[i + 1][s] = max(dp[i + 1][s], dp[i][t] + b)
            dp[i + 1][t] = max(dp[i + 1][t], dp[i][t])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
