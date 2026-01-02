from collections import defaultdict,deque
import numpy as np
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
lines = defaultdict(set)
for _ in range(N-1):
    x,y = inpl()
    x,y = x-1,y-1
    lines[x].add(y)
    lines[y].add(x)

lines2 = defaultdict(set)
visited = [False]*N
def dfs(s):
    visited[s] = True
    for t in lines[s]:
        if not visited[t]:
            lines2[s].add(t)
            dfs(t)
dfs(0)

dp = [[-1,-1] for _ in range(N)]
def solve(s,c):
    global dp

    if dp[s][c] != -1:
        return dp[s][c]

    ans = 1
    if c == 0:
        for t in lines2[s]:
            ans *= solve(t,0)+solve(t,1)
            ans %= mod
    else: # c == 1
        for t in lines2[s]:
            ans *= solve(t,0)
            ans %= mod

    dp[s][c] = ans
    return ans

print((solve(0,0)+solve(0,1))%mod)
