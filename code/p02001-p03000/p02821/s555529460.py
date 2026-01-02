#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    n,m = LI()
    a = LI()
    a.sort()
    l = 0
    r = 2*a[-1]
    while r-l > 1:
        x = (l+r) >> 1
        s = 0
        for i in a:
            j = bisect.bisect_left(a,x-i)
            s += n-j
        if s <= m:
            r = x
        else:
            l = x
    s = [0]*n
    s[-1] = a[-1]
    for i in range(n-1)[::-1]:
        s[i] = s[i+1]+a[i]
    res = m
    ans = 0
    for i in a:
        j = bisect.bisect_left(a,r-i)
        if res < n-j:
            j = n-res
        if j < n:
            ans += min(res,(n-j))*i
            ans += s[j]
            res -= n-j
            if res < 0:
                res = 0
    print(ans+res*l)
    return

#Solve
if __name__ == "__main__":
    solve()
