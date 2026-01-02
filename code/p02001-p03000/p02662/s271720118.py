import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, S = read_values()
    A = read_list()

    dp = [[0 for _ in range(S + 1)] for _ in range(N + 1)] 
    dp[0][0] = 1

    for i, a in enumerate(A):
        for s in range(S + 1):
            dp[i + 1][s] += 2 * dp[i][s]
            dp[i + 1][s] %= mod
            if s + a <= S: 
                dp[i + 1][s + a] += dp[i][s]
                dp[i + 1][s + a] %= mod
    
    print(dp[N][S])


if __name__ == "__main__":
    main()

