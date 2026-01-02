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
mod = 10 ** 9 + 7 

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, M = read_values()
    S = read_list()
    T = read_list()

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1
    
    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - (dp[i][j] if S[i] != T[j] else 0)) % mod
    
    print(dp[N][M])


if __name__ == "__main__":
    main()

