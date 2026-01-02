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
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#solve
def solve():
    n = II()
    ab = LIR(n)
    ab.sort()
    if n & 1:
        ans = ab[n // 2][0]
    else:
        ans = ab[n // 2 - 1][0] + ab[n // 2][0]
        ans /= 2
    ab = list(map(lambda x: x[1], ab))
    ab.sort()
    if n & 1:
        print((ab[n // 2] - ans) + 1)
    else:
        print(int(((ab[n // 2 - 1] + ab[n // 2]) / 2 - ans) * 2 + 1))
    return


#main
if __name__ == '__main__':
    solve()
