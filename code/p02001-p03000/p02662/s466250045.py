#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 998244353
inf = float("INF")

#solve
def solve():
    n, s = LI()
    a = LI()
    dp = [[0] * (3001) for _ in range(n)]
    dp[0][0] = 1
    dp[0][a[0]] = 1
    ans = 0
    for i in range(1, n):
        for si in range(a[i], 3001):
            dp[i][si] = dp[i - 1][si - a[i]] % mod
        dp[i][0] += 1
        dp[i][a[i]] += 1
        for si in range(3001):
            dp[i][si] = (dp[i][si] + dp[i - 1][si] * 2) % mod
        ans += dp[i][s]
    print(dp[-1][s] % mod)
    return


#main
if __name__ == '__main__':
    solve()
