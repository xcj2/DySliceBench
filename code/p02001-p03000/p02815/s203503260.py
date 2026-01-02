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
    n = I()
    c = LI()
    c.sort(reverse = True)
    dp = [0]*n
    dp[0] = c[0]
    p = 1
    for i in range(n-1):
        ni = i+1
        dp[ni] = (2*dp[i]+p*(2+ni)*c[ni])%mod
        p *= 2
        p %= mod
    p *= 2
    p %= mod
    print(p*dp[n-1]%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
