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
    n,m,l = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b,c = LI()
        a -= 1
        b -= 1
        v[a].append((b,c))
        v[b].append((a,c))
    ans = [[[float("inf")]*2 for j in range(n)] for i in range(n)]
    q = []
    for s in range(n):
        ans[s][s] = [0,0]
        heappush(q,(0,0,s))
        while q:
            da,dx,x = heappop(q)
            if [da,dx] > ans[s][x]:
                continue
            for y,w in v[x]:
                if w > l:
                    continue
                nd = dx+w
                if nd <= l:
                    na = da
                    nd_ = nd
                else:
                    na = da+1
                    nd_ = w
                if [na,nd_] < ans[s][y]:
                    ans[s][y] = [na,nd_]
                    heappush(q,(na,nd_,y))
    q = I()
    for _ in range(q):
        s,t = LI()
        s -= 1
        t -= 1
        ds = ans[s][t][0]
        if ds == float("inf"):
            print(-1)
        else:
            print(ds)
    return

#Solve
if __name__ == "__main__":
    solve()
