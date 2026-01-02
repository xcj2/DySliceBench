#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
mod = 1000000007

def solve():
    n = list(map(int, "0"+input()))[::-1]
    l = len(n)
    dp = [n[0],10-n[0]]
    for i in range(1,l):
        ndp = [float("inf")]*2
        x = n[i]
        for j in range(2):
            x += j
            if x < 10:
                nd = dp[j]+x
                if nd < ndp[0]:
                    ndp[0] = nd
            if x > 0:
                nd = dp[j]+(10-x)
                if nd < ndp[1]:
                    ndp[1] = nd
        dp = [i for i in ndp]
    print(dp[0])
    return

#Solve
if __name__ == "__main__":
    solve()
