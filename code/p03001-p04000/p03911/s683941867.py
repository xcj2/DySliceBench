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
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    n,m = LI()
    N = n+m
    par = [i for i in range(N)]
    rank = [0]*N
    for i in range(n):
        l = LI()
        for j in l[1:]:
            unite(j-1,i+m)
    r = set([root(i) for i in range(m,N)])
    if len(r) == 1:
        print("YES")
    else:
        print("NO")
    return


#Solve
if __name__ == "__main__":
    solve()
