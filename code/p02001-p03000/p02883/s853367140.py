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
    a = LI()
    f = LI()
    a.sort()
    f.sort(reverse = True)
    M = 0
    for i in range(n):
        M = max(M,a[i]*f[i])
    l = -1
    r = M
    while r-l > 1:
        m = (l+r)>>1
        s = 0
        for i in range(n):
            p = m//f[i]
            s += max(0,a[i]-p)
            if s > k:
                l = m
                break
        else:
            r = m
    print(r)
    return

#Solve
if __name__ == "__main__":
    solve()
