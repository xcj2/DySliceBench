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
    n,m,r = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b,c = LI()
        v[a].append((b,c))
    d = [float("inf")]*n
    d[r] = 0
    q = [(0,r)]
    while q:
        dx,x = heappop(q)
        for y,c in v[x]:
            nd = dx+c
            if nd < d[y]:
                d[y] = nd
                heappush(q,(nd,y))
    for i in d:
        if i == float("inf"):
            print("INF")
        else:
            print(i)
    return

#Solve
if __name__ == "__main__":
    solve()

