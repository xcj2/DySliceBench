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
    depth = [-1]*n
    depth[t] = 0
    q = deque([t])
    while q:
        x = q.popleft()
        for y in v[x]:
            if depth[y] < 0:
                depth[y] = depth[x]+1
                q.append(y)
    d = [-1]*n
    d[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in v[x]:
            if d[y] < 0:
                d[y] = d[x]+1
                q.append(y)
    l.sort(key = lambda x:-depth[x])
    for i in l:
        if d[i] < depth[i]:
            break
    print(depth[i]-1)
    return

#Solve
if __name__ == "__main__":
    solve()
