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
    s = S()
    n = len(s)
    s1 = s[:(n-1)//2]
    s2 = s[((n+3)//2)-1:][::-1]
    if len(s1) % 2 == 0:
        s11 = s1[:len(s1)//2]
    else:
        s11 = s1[:(len(s1)-1)//2]
    s12 = s1[((len(s1)+3)//2)-1:][::-1]
    if s1 == s2 and s11 == s12:
        print('Yes')
    else:
        print('No')
    return


# Solve
if __name__ == "__main__":
    solve()
