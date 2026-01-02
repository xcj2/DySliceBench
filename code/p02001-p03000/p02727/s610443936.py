#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate
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


def main():
    X, Y, A, B, C = LI()
    p = LI()
    q = LI()
    r = LI()
    p = sorted(p, reverse=True)[:X]
    q = sorted(q, reverse=True)[:Y]
    heapify(p), heapify(q)

    for ri in r:
        if len(p) < X:
            heappush(p, ri)
        elif len(q) < Y:
            heappush(q, ri)
        else:
            ptop = p[0]
            qtop = q[0]
            if min(ptop, qtop, ri) == ri:
                continue
            if ptop <= qtop:
                heappop(p)
                heappush(p, ri)
            else:
                heappop(q)
                heappush(q, ri)

    print(sum(sorted(p, reverse=True)[:X]) +
          sum(sorted(q, reverse=True)[:Y]))


main()
