#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    def dijkstra(s):
        d = [float("inf")]*n
        p = [s]*n
        d[s] = 0
        q = [(0,s)]
        while q:
            dx,x = heappop(q)
            nd = dx+1
            for y in v[x]:
                if nd < d[y]:
                    d[y] = nd
                    p[y] = x
                    heappush(q,(nd,y))
        path = [[i] for i in range(n)]
        for i in range(1,n):
            pre = path[i][-1]
            while pre != s:
                path[i].append(p[pre])
                pre = path[i][-1]
            path[i] = path[i][::-1]
        return d,path

    n = I()
    v = [[] for i in range(n)]
    e = defaultdict(lambda : 0)
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        e[(a,b)] = i
        e[(b,a)] = i
    d = [[0]*n for i in range(n)]
    path = [[None]*n for i in range(n)]
    for i in range(n):
        D,p = dijkstra(i)
        d[i] = [j for j in D]
        path[i] = [j for j in p]
    m = I()
    l = LIR(m)
    for i in range(m):
        l[i][0] -= 1
        l[i][1] -= 1
    ans = 0
    B = [0]*m
    for j in range(m):
        x,y = l[j]
        for k in range(len(path[x][y])-1):
            a,b = path[x][y][k],path[x][y][k+1]
            B[j] |= 1<<e[(a,b)]
    for b in range(1,1<<m):
        f = bin(b).count("1")
        p = 0
        for j in range(m):
            if b&(1<<j):
                p |= B[j]
        s = bin(p).count("1")
        f &= 1
        k = 1<<(n-s-1)
        if f:
            ans += k
        else:
            ans -= k
    print((1<<(n-1))-ans)
    return

#Solve
if __name__ == "__main__":
    solve()
