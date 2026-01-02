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
    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b,c = LI()
        v[a].append((b,c))

    B = 1<<n
    dp = [[float("inf")]*n for i in range(B)]
    for i,c in v[0]:
        dp[1<<i][i] = c
    for b in range(B):
        for i in range(n):
            if not b&(1<<i):
                continue
            for j,c in v[i]:
                if b&(1<<j):
                    continue
                nb = b|(1<<j)
                nd = dp[b][i]+c
                if nd < dp[nb][j]:
                    dp[nb][j] = nd
    ans = dp[B-1][0]
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()

