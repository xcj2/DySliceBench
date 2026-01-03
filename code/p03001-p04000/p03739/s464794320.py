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
    n = I()
    a = LI()
    ans = 0
    s = a[0]
    if s <= 0:
        ans += 1-a[0]
        s = 1
    f = 1
    for i in a[1:]:
        s += i
        if f and (s >= 0):
            ans += s+1
            s = -1
        if not f and (s <= 0):
            ans += 1-s
            s = 1
        f ^= 1
    m = ans
    ans = 0
    s = a[0]
    if s >= 0:
        ans += a[0]+1
        s = -1
    f = 0
    for i in a[1:]:
        s += i
        if f and (s >= 0):
            ans += s+1
            s = -1
        if not f and (s <= 0):
            ans += 1-s
            s = 1
        f ^= 1
    print(min(m,ans))
    return

#Solve
if __name__ == "__main__":
    solve()
