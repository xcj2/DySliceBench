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
    n,m = LI()
    v = [[] for i in range(n)]
    for _ in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    q = [(0,0)]
    d = [float("inf")]*n
    d[0] = 0
    pre = [None]*n
    while q:
        dx,x = heappop(q)
        nd = dx+1
        for y in v[x]:
            if nd < d[y]:
                d[y] = nd
                pre[y] = x
                heappush(q,(nd,y))
    if float("inf") in d:
        print("No")
        return
    print("Yes")
    for i in pre[1:]:
        print(i+1)
    return

#Solve
if __name__ == "__main__":
    solve()
