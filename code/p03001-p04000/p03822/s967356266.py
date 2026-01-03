#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import *
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(2147483647)
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10
input=lambda:sys.stdin.readline().rstrip()
#solve
def solve():

    n = int(input())
    edg = [[] for _ in range(n)]
    dp = [None] * n
    for i in range(1,n):
        u = int(input()) - 1
        edg[u].append(i)
        edg[i].append(u)

    def dfs(v,p=-1)->int:
        if (dp[v] is not None): return dp[v]
        if (edg[v] == [p]):
            dp[v] = 0
            return 0
        tmp = []
        for nv in edg[v]:
            if (nv == p): continue
            tmp.append(dfs(nv,v))
        dp[v] = max(1 + i + x for i, x in enumerate(sorted(tmp, reverse=1)))
        return dp[v]
    
    print(dfs(0))
    return


#main
if __name__ == '__main__':
    solve()
