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
    def root(x):
        if par[x] == x:
            return par[x]
        s[par[x]] += s[x]
        s[x] = 0
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
            s[y] += s[x]
            s[x] = 0
        else:
            par[y] = x
            s[x] += s[y]
            s[y] = 0
            if rank[x] == rank[y]:
                rank[x] += 1

    n,m = LI()
    v = []
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v.append((a,b))
    par = [i for i in range(n)]
    rank = [0]*n
    s = [1]*n
    su = n*(n-1) >> 1
    ans = [su]
    for i,j in v[1:][::-1]:
        ri = root(i)
        rj = root(j)
        if ri != rj:
            su -= s[ri]*s[rj]
            unite(i,j)
        ans.append(su)
    for i in ans[::-1]:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
