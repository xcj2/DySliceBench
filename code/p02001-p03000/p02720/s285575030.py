# -*- coding: utf-8 -*-

import sys
from itertools import accumulate

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def bisearch_min(mn, mx, func):
    ok = mx
    ng = mn
    while ng+1 < ok:
        mid = (ok+ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def check(x):
    x = str(x)
    N = len(x)
    dp0 = list2d(N+1, 10, 0)
    dp1 = list2d(N+1, 10, 0)
    a = int(x[0])
    dp0[1][a] = 1
    for j in range(1, a):
        dp1[1][j] = 1
    for i in range(2, N+1):
        for j in range(1, 10):
            dp1[i][j] = 1
    for i, a in enumerate(x):
        a = int(a)
        for j in range(10):
            for k in range(10):
                if abs(j - k) >= 2:
                    continue
                if k > a:
                    dp1[i+1][k] += dp1[i][j]
                elif k == a:
                    dp0[i+1][k] += dp0[i][j]
                    dp1[i+1][k] += dp1[i][j]
                else:
                    dp1[i+1][k] += dp0[i][j]
                    dp1[i+1][k] += dp1[i][j]
    ans = sum(dp0[N]) + sum(dp1[N])
    return ans >= K

K = INT()

res = bisearch_min(0, 10**10, check)
print(res)
