import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7
mod = 998244353 

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


def main():
    N, X = read_values()
    A = read_list()

    dp = [[[0 for _ in range(N * X + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    

    dp[0][0][0] = 1

    for i, a in enumerate(A):
        for j in range(N + 1):
            for k in range(N * X):
                if k + a <= N * X and j < N:
                    dp[i + 1][j + 1][k + a] += dp[i][j][k]
                dp[i + 1][j][k] += dp[i][j][k]
    
    res = 0
    for i in range(1, N + 1):
        res += dp[N][i][i * X]

    print(res)


if __name__ == "__main__":
    main()

