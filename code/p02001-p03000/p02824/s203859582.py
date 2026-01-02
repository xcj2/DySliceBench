#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt


def LI(): return list(map(int, input().split()))


def LF(): return list(map(float, input().split()))


def LI_(): return list(map(lambda x: int(x)-1, input().split()))


def II(): return int(input())


def IF(): return float(input())


def LS(): return list(map(list, input().split()))


def S(): return list(input().rstrip())


def IR(n): return [II() for _ in range(n)]


def LIR(n): return [LI() for _ in range(n)]


def FR(n): return [IF() for _ in range(n)]


def LFR(n): return [LI() for _ in range(n)]


def LIR_(n): return [LI_() for _ in range(n)]


def SR(n): return [S() for _ in range(n)]


def LSR(n): return [LS() for _ in range(n)]


mod = 1000000007
inf = 1e10

#solve


def solve():
    n, m, v, p = LI()
    a = LI()
    a.sort(reverse=True)
    ok = p - 1
    ng = n
    def f(x):
        tmp = (p - 1) * m + (n - x) * m
        t = a[x] + m
        if t < a[p - 1]:
            return False
        for i in range(p - 1, x):
            tmp += t - a[i]
        return tmp >= m * v
        
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok + 1)
    return


#main
if __name__ == '__main__':
    solve()
