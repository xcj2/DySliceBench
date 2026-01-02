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
    n,k = LI()
    v = LI()
    ans = -float("inf")
    for l in range(min(k,n)+1):
        vl = v[:l]
        for r in range(min(k,n)+1-l):
            vr = v[n-r:]
            s = max(0,k-l-r)
            nv = vl+vr
            nv.sort(reverse = True)
            while s > 0 and nv and nv[-1] < 0:
                nv.pop()
                s -= 1
            su = sum(nv)
            if ans < su:
                ans = su
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
