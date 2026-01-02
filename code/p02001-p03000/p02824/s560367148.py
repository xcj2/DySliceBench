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
    n,m,v,p = LI()
    a = LI()
    a.sort()
    l = -1
    r = n-1
    while l+1 < r:
        i = (l+r) >> 1
        A = a[i]+m
        ri = bisect.bisect_right(a,A)
        j = n-ri
        if j >= p:
            l = i
            continue
        s = m
        for j in range(n-p+1):
            if i == j:
                continue
            s += min(m,A-a[j])
        s += m*(p-1)
        if s >= m*v:
            r = i
        else:
            l = i
    print(n-r)
    return

#Solve
if __name__ == "__main__":
    solve()
