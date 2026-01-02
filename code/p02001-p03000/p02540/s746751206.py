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
    return [LI()+[i] for i in range(n)]
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


    n = I()
    p = LIR(n)
    p.sort()
    par = list(range(n))
    rank = [0]*n
    q = []
    q2 = []
    for x,y,i in p:
        f = 0
        while q:
            yy,j = heappop(q)
            if y < yy:
                heappush(q,(yy,j))
                break
            f = 1
            unite(i,j)
            q2.append((yy,j))
        while q2:
            yy,j = q2.pop()
            heappush(q,(yy,j))
        if not f:
            heappush(q,(y,i))
    s = [0]*(n+1)
    for _,_,i in p:
        s[root(i)] += 1
    ans = [None]*n
    for _,_,i in p:
        ans[i] = s[root(i)]
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
