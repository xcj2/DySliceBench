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
    n = II()
    a = [(i, j) for (i, j) in zip(LI(), range(n))]
    a.sort(reverse=True)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + a[i][0] * abs(a[i][1] - i)
        dp[0][i + 1] = dp[0][i] + a[i][0] * abs(a[i][1] - (n - (i + 1)))
        for l in range(1, i + 1):
            r = i - l + 1
            dp[l][r] = max(dp[l - 1][r] + a[i][0] * abs(a[i][1] - (l - 1)),
                            dp[l][r - 1] + a[i][0] * abs(a[i][1] - (n - r)))
    ans = 0
    for r in range(n + 1):
        l = n - r
        ans = max(ans, dp[l][r])
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
