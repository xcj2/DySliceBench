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
def S(): return list(sys.stdin.readline())[:-1]
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

#A
def A():
    def root(x):
        if par[x] == x:
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
    p = LI()
    for i in range(n):
        p[i] -= 1
    par = [i for i in range(n)]
    rank = [0]*n
    for i in range(m):
        x,y = LI()
        x -= 1
        y -= 1
        if root(x) != root(y):
            unite(x,y)
    ans = 0
    for i in range(n):
        if root(p[i]) == root(i):
            ans += 1
    print(ans)
    return

#B
def B():

    return

#C
def C():

    return

#D
def D():

    return

#E
def E():

    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    A()
