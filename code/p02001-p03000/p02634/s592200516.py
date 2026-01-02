import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    A, B, C, D = read_values()

    dp = [[0 for _ in range(D - B + 1)] for _ in range(C - A + 1)]
    dp[0][0] = 1

    for i in range(C - A):
        dp[i + 1][0] = dp[i][0] * B % mod
    for j in range(D - B):
        dp[0][j + 1] = dp[0][j] * A % mod

    for i in range(1, C - A + 1):
        for j in range(1, D - B + 1):
            dp[i][j] = (dp[i - 1][j] * (B + j)) % mod + (dp[i][j - 1] * (A + i)) % mod - (dp[i - 1][j - 1] * (A + i - 1) * (B + j - 1)) % mod
            dp[i][j] %= mod

    print(dp[C - A][D - B] % mod)


if __name__ == "__main__":
    main()

