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
    n,m,s,t = LI()
    s -= 1
    t -= 1
    v = [[] for i in range(n)]
    for i in range(m):
        x,y,a,b = LI()
        x -= 1
        y -= 1
        v[x].append((y,a,b))
        v[y].append((x,a,b))
    d = [float("inf")]*n
    d[s] = 0
    q = [(0,s)]
    while q:
        dx,x = heappop(q)
        if d[x] < dx:
            continue
        for y,a,b in v[x]:
            nd = dx+a
            if nd < d[y]:
                d[y] = nd
                heappush(q,(nd,y))
    c = [float("inf")]*n
    c[t] = 0
    q = [(0,t)]
    while q:
        cx,x = heappop(q)
        if c[x] < cx:
            continue
        for y,a,b in v[x]:
            nc = cx+b
            if nc < c[y]:
                c[y] = nc
                heappush(q,(nc,y))
    s = float("inf")
    N = 10**15
    ans = []
    for i in range(n)[::-1]:
        s = min(s,d[i]+c[i])
        ans.append(N-s)
    for i in ans[::-1]:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
