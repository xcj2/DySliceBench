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
    m = 61
    d = [0]*m
    ans = 0
    p = [pow(2,j,mod) for j in range(m)]
    for i in range(n):
        ai = a[i]
        for j in range(m):
            if ai&(1<<j):
                ans += (i-d[j])*p[j]%mod
                ans %= mod
                d[j] += 1
            else:
                ans += d[j]*p[j]%mod
                ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
