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

d = defaultdict(lambda : -1)
def solve():
    global d
    def dfs(x,pre,k,m):
        global d
        p = 1
        if pre != -1:
            if x < pre:
                d[(x,pre)] = k
            else:
                d[(pre,x)] = k
        for y in v[x]:
            if p == k:
                p += 1
            if m[y]:continue
            m[y] = 1
            dfs(y,x,p,m)
            p += 1
    n = I()
    v = [[] for i in range(n)]
    e = []
    f = [0]*n
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        e.append((a,b))
        f[a] += 1
        f[b] += 1
    if n == 2:
        print(1)
        print(1)
        return
    m = [0]*n
    m[0] = 1
    dfs(0,-1,0,m)
    print(max(f))
    for x,y in e:
        print(d[(x,y)])
    return

#Solve
if __name__ == "__main__":
    solve()
