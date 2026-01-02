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


def dev(a):
    d = {}
    for i in (2, 5):
        r = 0
        while a % i == 0:
            r += 1
            a //= i
        d[i] = min(18, r)
    return d


def main():
    N = int(input())
    A = []
    for _ in range(N):
        s = input().strip().split(".")
        a = int(s[0]) * (10 ** 9)
        if len(s) > 1:
            t = s[1] + "0" * (9 - len(s[1]))
            a += int(t)
            # a += int(float("0." + s[1]) * (10 ** 9))
        # a = int(float(input()) * (10 ** 9))
        # print(a)
        A.append(dev(a))
    # print(A)
    S = [[0] * 19 for _ in range(19)]
    dp = [[0] * 20 for _ in range(20)]
    for a in A:
        S[a[2]][a[5]] += 1

    # print(S)
    for i in range(19):
        for j in range(19):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + S[i][j]
    
    # print(dp[-1])
    res = 0
    for a in A:
        s = 18 - a[2]
        t = 18 - a[5]
        
        r = N - dp[-1][t] - dp[s][-1] + dp[s][t]
        if a[2] >= 9 and a[5] >= 9:
            r -= 1
        # print(a, r)
        res += r
    print(res // 2)
    
if __name__ == "__main__":
    main()