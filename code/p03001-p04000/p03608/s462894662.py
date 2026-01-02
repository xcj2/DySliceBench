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
def S(): return list(sys.stdin.readline())[:-1]
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
    n,m,R = LI()
    r = LI()
    for i in range(R):
        r[i] -= 1
    v = [[float("inf")]*n for i in range(n)]
    for i in range(m):
        a,b,c = LI()
        a -= 1
        b -= 1
        v[a][b] = c
        v[b][a] = c
    l = 1<<R
    for k in range(n):
        for i in range(n):
            for j in range(n):
                nv = v[i][k]+v[j][k]
                if nv < v[i][j]:
                    v[i][j] = nv
    dp = [[float("inf")]*R for i in range(l)]
    for i in range(R):
        dp[1<<i][i] = 0
    for b in range(l):
        for i in range(R):
            if not (1<<i)&b:
                continue
            x = r[i]
            for j in range(R):
                bj = 1<<j
                if bj&b:
                    continue
                y = r[j]
                nd = dp[b][i]+v[x][y]
                nb = b|bj
                if nd < dp[nb][j]:
                    dp[nb][j] = nd
    print(min(dp[-1]))
    return

#Solve
if __name__ == "__main__":
    solve()
