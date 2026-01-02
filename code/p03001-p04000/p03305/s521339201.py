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
    n,m,s,t = LI()
    s -= 1
    t -= 1
    v = [[] for i in range(n)]
    v2 = [[] for i in range(n)]
    for i in range(m):
        a,b,c,d = LI()
        a -= 1
        b -= 1
        v[a].append((b,c))
        v[b].append((a,c))
        v2[a].append((b,d))
        v2[b].append((a,d))
    d = [float("inf")]*n
    d[s] = 0
    q = [(0,s)]
    while q:
        dx,x = heappop(q)
        for y,c in v[x]:
            nd = dx+c
            if nd < d[y]:
                d[y] = nd
                heappush(q,(nd,y))
    d2 = [float("inf")]*n
    d2[t] = 0
    q = [(0,t)]
    while q:
        dx,x = heappop(q)
        for y,c in v2[x]:
            nd = dx+c
            if nd < d2[y]:
                d2[y] = nd
                heappush(q,(nd,y))
    ans = [10**15-(d[i]+d2[i]) for i in range(n)]
    for i in range(n-1)[::-1]:
        if ans[i+1] > ans[i]:
            ans[i] = ans[i+1]
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
