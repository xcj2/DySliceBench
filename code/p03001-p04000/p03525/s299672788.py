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

ans = 0
def gap(a,b):
    c = abs(a-b)
    return min(c,24-c)
def solve():
    global ans
    def dfs(f,i,k):
        global ans
        if i == n:
            ans = k
        else:
            nd = d[i]
            nk = min([gap(nd,j) for j in f])
            if nk > ans:
                nf = [i for i in f]+[nd]
                dfs(nf,i+1,min(k,nk))
            if d[i] != 12:
                nd = 24-d[i]
                nk = min([gap(nd,j) for j in f])
                if nk > ans:
                    nf = [i for i in f]+[nd]
                    dfs(nf,i+1,min(k,nk))

    n = I()
    d = LI()
    f = [0]
    dfs(f,0,float("inf"))
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
