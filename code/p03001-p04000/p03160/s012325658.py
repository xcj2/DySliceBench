#!usr/bin/env python3
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


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
    h = LI()
    dp = [0]*n
    dp[1] = abs(h[0] - h[1])
    for i in range(2, n):
        dp[i] = min(abs((h[i] - h[i-1])) + dp[i-1],
                    abs((h[i] - h[i-2])) + dp[i-2])
    print(dp[n-1])
    return


# Solve
if __name__ == "__main__":
    solve()
