#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
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
inf = float('INF')
from copy import deepcopy

#solve
def solve():
    n, k = LI()
    h = [0] + LI()
    d = defaultdict(int)
    d[(0, 0)] = 0
    for i in range(1, n + 1):
        nd = defaultdict(lambda: inf)
        for key, value in d.items():
            a, b = key
            if nd[(i, b)] > value + (h[i] - h[a] if h[i] > h[a] else 0):
                nd[(i, b)] = value + (h[i] - h[a] if h[i] > h[a] else 0)
            if b + 1 > k:
                continue
            if nd[(a, b + 1)] > value:
                nd[(a, b + 1)] = value
        d = nd
    ans = inf
    for i in range(n + 1):
        for j in range(k + 1):
            ans = min(ans, d[(i, j)])
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
