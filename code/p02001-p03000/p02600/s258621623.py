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
    x = I()
    if 599 >= x >= 400:
        print(8)
    elif 799 >= x >= 600:
        print(7)
    elif 999 >= x >= 800:
        print(6)
    elif 1199 >= x >= 1000:
        print(5)
    elif 1399 >= x >= 1200:
        print(4)
    elif 1599 >= x >= 1400:
        print(3)
    elif 1799 >= x >= 1600:
        print(2)
    elif 1999 >= x >= 1800:
        print(1)
    return


# Solve
if __name__ == "__main__":
    solve()
