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
    t = LI()
    a = LI()
    b = LI()
    a[0] -= b[0]
    a[1] -= b[1]
    if t[0]*a[0] == -t[1]*a[1]:
        print("infinity")
        return
    if a[0] < 0:
        a[0] *= -1
        a[1] *= -1
    if t[0]*a[0]+t[1]*a[1] > 0:
        print(0)
        return
    l = 0
    r = 10**100
    A = t[0]*a[0]+t[1]*a[1]
    while r-l > 1:
        m = (l+r) >> 1
        x = m*A
        y = x+t[0]*a[0]
        if x*y <= 0:
            l = m
        else:
            r = m
    ans = r*2-1
    if l*A+t[0]*a[0] == 0:
        ans -= 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
