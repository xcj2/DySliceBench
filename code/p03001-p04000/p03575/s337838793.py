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
    v = LIR(m)
    for i in range(m):
        v[i][0] -= 1
        v[i][1] -= 1
    ans = 0
    for i in range(m):
        par = [i for i in range(n)]
        rank = [0]*n
        s = 1
        for j in range(m):
            if i == j:
                continue
            a,b = v[j]
            if root(a) != root(b):
                s += 1
                if s >= n:
                    break
                unite(a,b)
        else:
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
