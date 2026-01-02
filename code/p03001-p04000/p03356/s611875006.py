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
    f = [None]*n
    for i in range(n):
        p[i] -= 1
        f[p[i]] = i
    par = [i for i in range(n)]
    rank = [0]*n
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        if root(a) != root(b):
            unite(a,b)
    ans = 0
    for i in range(n):
        if root(f[i]) == root(i):
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
