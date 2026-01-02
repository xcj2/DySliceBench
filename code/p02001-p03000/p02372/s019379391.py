#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    fl = defaultdict(lambda : 0)
    fr = defaultdict(lambda : 0)

    def dfs(x,hx):
        p = 0
        for y,c in v[x]:
            if hx < h[y]:
                continue
            fl[(x,y)] = p
            nh = h[y]+c
            if p < nh:
                p = nh
        p = 0
        for y,c in v[x][::-1]:
            if hx < h[y]:
                continue
            fr[(x,y)] = p
            nh = h[y]+c
            if p < nh:
                p = nh
        for y,c in v[x]:
            hy = h[y]
            if hx < hy:
                continue
            if ans[y]:continue
            nhx = max(fl[(x,y)],fr[(x,y)])
            ans[y] = nhy = max(h[y],nhx+c)
            h[x] = nhx
            dfs(y,nhy)
            h[x] = hx

    n = I()
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b,c = LI()
        v[a].append((b,c))
        v[b].append((a,c))
    q = [0]
    q2 = []
    h = [-1]*n
    h[0] = 0
    while q:
        x = q.pop()
        for y,c in v[x]:
            if h[y] < 0:
                h[y] = 0
                q.append(y)
                q2.append((y,x,c))
    while q2:
        y,x,c = q2.pop()
        nh = h[y]+c
        if h[x] < nh:
            h[x] = nh

    ans = [0]*n
    ans[0] = h[0]
    dfs(0,h[0])

    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()

