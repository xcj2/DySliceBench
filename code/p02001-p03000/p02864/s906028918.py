#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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
    n,k = LI()
    h = LI()
    h.insert(0,0)
    dp = [[float("inf")]*(n+1) for i in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        ni = i+1
        hi = h[ni]
        for s in range(n):
            ns = s+1
            for j in range(ni):
                hj = h[j]
                nd = dp[j][s]+max(0,hi-hj)
                if nd < dp[ni][ns]:
                    dp[ni][ns] = nd
    ans = min([dp[i][n-k] for i in range(n+1)])
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
