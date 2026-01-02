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
mod = 998244353

def solve():
    n,s = LI()
    a = LI()
    dp = [0]*(s+1)
    dp[0] = pow(2,n,mod)
    inv = pow(2,mod-2,mod)
    for i in a:
        for k in range(s)[::-1]:
            nk = k+i
            if nk > s:
                continue
            dp[nk] += dp[k]*inv%mod
            dp[nk] %= mod
    print(dp[s])
    return

#Solve
if __name__ == "__main__":
    solve()
