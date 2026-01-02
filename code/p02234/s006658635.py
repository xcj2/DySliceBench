#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    g = LIR(n)
    dp = [[float("inf")]*(n+1) for i in range(n)]
    for i in range(n):
        dp[i][i+1] = 0
    for k in range(1,n+1):
        for l in range(n):
            hl,wl = g[l]
            r = l+k
            if r > n:
                break
            hr,wr = g[r-1]
            nd = dp[l][r]
            for j in range(l+1,r):
                hj,wj = g[j-1]
                cost = hl*wj*wr
                nd = min(nd,dp[l][j]+dp[j][r]+cost)
            if nd < dp[l][r]:
                dp[l][r] = nd
    print(dp[0][n])
    return

#Solve
if __name__ == "__main__":
    solve()

