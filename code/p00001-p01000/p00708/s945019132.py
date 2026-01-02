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
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    def D2(i,j):
        x1,y1,z1,r = p[i]
        x2,y2,z2,r = p[j]
        return (x1-x2)**2+(y1-y2)**2+(z1-z2)**2

    while 1:
        n = I()
        if n == 0:
            return
        p = [list(map(float, input().split())) for i in range(n)]
        d2 = [[D2(i,j) for j in range(i)] for i in range(n)]
        par = [i for i in range(n)]
        rank = [0]*n
        v = []
        for i in range(n):
            x,y,z,r1 = p[i]
            for j in range(i):
                x,y,z,r2 = p[j]
                d = r1+r2
                d2ij = d2[i][j]
                if d2ij > d**2:
                    v.append((d2ij**0.5-d,i,j))
                else:
                    unite(i,j)
        v.sort()
        ans = 0.0
        for c,a,b in v:
            if root(a) != root(b):
                ans += c
                unite(a,b)
        print("{:.3f}".format(round(ans,3)))
    return

#Solve
if __name__ == "__main__":
    solve()

