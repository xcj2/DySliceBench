#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    def dfs(x,dp):
        ans[x] = bisect.bisect_left(dp, float("inf"))
        for y in v[x]:
            if d[y]:
                d[y] = 0
                i = bisect.bisect_left(dp,a[y])
                p = dp[i]
                dp[i] = a[y]
                dfs(y,dp)
                dp[i] = p

    n = I()
    a = LI()
    v = [[] for i in range(n)]
    for _ in range(n-1):
        x,y = LI()
        x -= 1
        y -= 1
        v[x].append(y)
        v[y].append(x)
    dp = [float("inf")]*n
    dp[0] = a[0]
    d = [1]*n
    d[0] = 0
    ans = [0]*n
    dfs(0,dp)
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
