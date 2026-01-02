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
    n,m = LI()
    a = LI()
    b = LI()
    a.sort(reverse = True)
    b.sort(reverse = True)
    if len(set(a)) < n or len(set(b)) < m:
        print(0)
        return
    if a[0] != b[0]:
        print(0)
        return
    ans = 1
    s = 0
    for i in range(1,n*m+1)[::-1]:
        l = 0
        r = n
        while r-l > 1:
            mid = (l+r) >> 1
            if a[mid] >= i:
                l = mid
            else:
                r = mid
        x = l
        l = 0
        r = m
        while r-l > 1:
            mid = (l+r) >> 1
            if b[mid] >= i:
                l = mid
            else:
                r = mid
        y = l
        if a[x] == i:
            if b[y] == i:
                k = 1
            else:
                k = y+1
        else:
            if b[y] == i:
                k = x+1
            else:
                k = (x+1)*(y+1)-s
        ans *= k
        ans %= mod
        s += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
