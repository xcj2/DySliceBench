import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from collections import *
import math
from bisect import *
import functools
INF = float('inf')
mod = 10**9+7

N = int(input())
es = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(lambda x: int(x)-1, input().split())
    es[x].append(y)
    es[y].append(x)
depth = [None] * N
def dfs(v, p, d):
    depth[v] = d
    for u in es[v]:
        if u != p:
            dfs(u, v, d+1)
dfs(0, -1, 0)
dp = [[1] * 2 for i in range(N)]
@functools.lru_cache(maxsize=None)
def rec(v):
    d = depth[v]
    for u in es[v]:
        if d < depth[u]:
            w, b = rec(u)
            dp[v][0] *= w+b
            dp[v][1] *= w
    dp[v][0] %= mod
    dp[v][1] %= mod
    return dp[v][0], dp[v][1]
w, b = rec(0)
print((w+b)%mod)
