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
inf = 1e10

#solve
def solve():
    n = II()
    t = LI()
    a = LI()[::-1]
    dt = [None] * n
    da = [None] * n
    ba = 0
    bt = 0
    for i in range(n):
        if bt < t[i]:
            dt[i] = (1, t[i])
            bt = t[i]
        else:
            dt[i] = (bt, bt)
    for i in range(n):
        if ba < a[i]:
            da[i] = (1, a[i])
            ba = a[i]
        else:
            da[i] = (ba, ba)
    da = da[::-1]
    ans = 1
    for i in range(n):
        f = True
        if da[i][0] == 1:
            if da[i][1] > dt[i][1]:
                print(0)
                return
            f &= 0
        if dt[i][0] == 1:
            if da[i][1] < dt[i][1]:
                print(0)
                return
            f &= 0
        if f:
            ans *= min(da[i][1], dt[i][1])
            ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
