#!usr/bin/env python3
from collections import defaultdict, deque
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
    a11, a12, a13 = LI()
    a21, a22, a23 = LI()
    a31, a32, a33 = LI()
    n = I()
    b = IR(n)
    if a11 in b and a12 in b and a13 in b:
        print('Yes')
    elif a21 in b and a22 in b and a23 in b:
        print('Yes')
    elif a31 in b and a32 in b and a33 in b:
        print('Yes')
    elif a11 in b and a21 in b and a31 in b:
        print('Yes')
    elif a12 in b and a22 in b and a32 in b:
        print('Yes')
    elif a13 in b and a23 in b and a33 in b:
        print('Yes')
    elif a11 in b and a22 in b and a33 in b:
        print('Yes')
    elif a13 in b and a22 in b and a31 in b:
        print('Yes')
    else:
        print('No')
    return


# Solve
if __name__ == "__main__":
    solve()
