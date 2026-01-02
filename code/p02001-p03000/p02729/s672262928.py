#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, combinations
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
    n, m = LI()

    def P(n, r):
        return math.factorial(n)//math.factorial(n-r)

    def C(n, r):
        return P(n, r)//math.factorial(r)
    if n > 2 and m > 2:
        print(C(n, 2) + C(m, 2))
    elif n < 2 and m < 2:
        print(0)
    elif n < 2:
        print(C(m, 2))
    elif m < 2:
        print(C(n, 2))
    return


# Solve
if __name__ == "__main__":
    solve()
