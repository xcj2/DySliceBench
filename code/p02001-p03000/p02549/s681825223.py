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
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 998244353

def solve():
    def add(i,x):
        while i < len(dp):
            dp[i] += x
            dp[i] %= mod
            i += i&-i
    def sum(i):
        res = 0
        while i:
            res += dp[i]
            res %= mod
            i -= i&-i
        return res

    n,k = LI()
    p = LIR(k)
    p.sort()
    dp = [0]*(n+2)
    add(1,1)
    add(2,-1)
    for i in range(1,n):
        dpi = sum(i)%mod
        for l,r in p:
            li = i+l
            if li > n:
                break
            ri = min(n,i+r)+1
            add(li,dpi)
            add(ri,-dpi)
    print(sum(n)%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
