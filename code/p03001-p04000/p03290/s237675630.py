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
    D, G = read_values()
    P = [0] * D
    C = [0] * D
    for i in range(D):
        P[i], C[i] = read_values()
        
    dp = [0] * (sum(P) + 1)
    for i in range(2 ** D):
        A = [0 if (i >> k) & 1 else P[k] - 1 for k in range(D)]
        r = sum(P[k] if (i >> k) & 1 else 0 for k in range(D))
        t = sum(C[k] + P[k] * (k + 1) * 100 if (i >> k) & 1 else 0 for k in range(D))
        dp[r] = max(dp[r], t)
        for j in range(D - 1, - 1, -1):
            for k in range(1, A[j] + 1):
                r += 1
                t += (j + 1) * 100
                dp[r] = max(dp[r], t)
    for i in range(len(dp) - 1):
        dp[i + 1] = max(dp[i +1], dp[i])
    # print(dp)
    print(bisect.bisect_left(dp, G))


if __name__ == "__main__":
    main()
