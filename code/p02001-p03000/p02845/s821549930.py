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
    d = [0,0,0]
    ans = 1
    for i in a:
        s = 0
        for k in d:
            if k == i:
                s += 1
        if not s:
            print(0)
            return
        ans *= s
        ans %= mod
        for k in range(3):
            if d[k] == i:
                d[k] += 1
                break
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
