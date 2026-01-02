#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    if not n&1:
        dp = a[:2]
        for i in range(2,n)[::2]:
            nd = [-float("inf")]*2
            nd[0] = dp[0]+a[i]
            nd[1] = max(dp)+a[i+1]
            dp = [j for j in nd]
        print(max(dp))
        return
    dp = a[:3]
    dp[0] = a[0]
    dp[1] = a[1]
    dp[2] = a[2]
    for i in range(2,n-1)[::2]:
        nd = [-float("inf")]*3
        nd[0] = dp[0]+a[i]
        nd[1] = max(dp[0],dp[1])+a[i+1]
        nd[2] = max(dp)+a[i+2]
        dp = [j for j in nd]
    print(max(dp))
    return

#Solve
if __name__ == "__main__":
    solve()
