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
mod = 1000000007
inf = float("INF")

#solve
def solve():
    def dfs(x):
        ans[x] = bisect_left(dp, inf)
        for e in edg[x]:
            if d[e]:
                d[e] = 0
                i = bisect_left(dp, a[e])
                p = dp[i]
                dp[i] = a[e]
                dfs(e)
                dp[i] = p
    n = II()
    a = LI()
    dp = [inf] * n
    edg = [[] for i in range(n)]
    for _ in range(n - 1):
        u, v = LI_()
        edg[u].append(v)
        edg[v].append(u)
    d = [1] * n
    ans = [1] * n
    d[0] = 0
    dp[0] = a[0]
    dfs(0)
    for a in ans:
        print(a)
    return


#main
if __name__ == '__main__':
    solve()
