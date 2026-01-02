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
    A = t[0]*a[0]+t[1]*a[1]
    k = t[0]*a[0]
    l = 0
    r = 10**20
    while r-l > 1:
        x = (l+r) >> 1
        if A*x+k > 0:
            l = x
        else:
            r = x
    ans = 2*l+1
    if A*r+k == 0:
        ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
