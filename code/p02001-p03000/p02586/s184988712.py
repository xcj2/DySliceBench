import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    R, C, K = read_values()
    V = [0] * (R * C)
    for _ in range(K):
        r, c, v = read_values()
        r -= 1
        c -= 1
        V[r * C + c] = v
    
    dp = [0 for _ in range(R * C * 4)]
    for i in range(R * C):
        r = i // C
        c = i % C
        if c + 1 < C:
            # not take
            for k in range(4):
                dp[4 * (i + 1) + k] = max(dp[4 * (i + 1) + k], dp[4 * i + k])

            # take 
            for k in range(3):
                dp[4 * (i + 1) + k + 1] = max(dp[4 * (i + 1) + k + 1], dp[4 * i + k] + V[i])

        # next r
        if r + 1 < R:
            for k in range(4):
                dp[4 * (i + C)] = max(dp[4 * (i + C)], dp[4 * i + k] + (V[i] if k < 3 else 0))

    res = 0
    for k in range(4):
        res = max(res, dp[4 * (R * C - 1) + k] + (V[-1] if k < 3 else 0))

    print(res)


if __name__ == "__main__":
    main()
