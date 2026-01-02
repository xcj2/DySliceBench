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
    def lca(x,y):
        k = depth[x] - depth[y]
        while k > 0:
            x = par[x][int(math.log(k,2))]
            k = depth[x] - depth[y]
        k = -k
        while k > 0:
            y = par[y][int(math.log(k,2))]
            k = depth[y] - depth[x]
        if x == y:
            return x
        for i in range(17)[::-1]:
            if par[x][i] != par[y][i]:
                x = par[x][i]
                y = par[y][i]
        return par[x][0]
    n,s,t = LI()
    s -= 1
    t -= 1
    v = [[] for i in range(n)]
    f = [0]*n
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        f[a] += 1
        f[b] += 1
    l = []
    for i in range(n):
        if f[i] == 1:
            l.append(i)
    par = [[] for i in range(n)]
    par[t].append(t)
    depth = [-1]*n
    depth[t] = 0
    q = deque([t])
    while q:
        x = q.popleft()
        for y in v[x]:
            if depth[y] < 0:
                depth[y] = depth[x]+1
                q.append(y)
                par[y].append(x)
    d = [-1]*n
    d[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in v[x]:
            if d[y] < 0:
                d[y] = d[x]+1
                q.append(y)
    for i in range(16):
        for x in range(n):
            par[x].append(par[par[x][i]][i])
    l.sort(key = lambda x:-depth[x])
    for i in l:
        x = lca(i,s)
        if d[x] < depth[x]:
            break
    print(depth[i]-1)
    return

#Solve
if __name__ == "__main__":
    solve()
