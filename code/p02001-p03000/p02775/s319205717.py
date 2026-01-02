# -*- coding: utf-8 -*-

import sys

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

S = input()
S = S[::-1]
N = len(S)

dp0 = [INF] * (N+1)
dp1 = [INF] * (N+1)
dp0[0] = 0
for i, s in enumerate(S):
    s = int(s)
    dp0[i+1] = min(dp0[i+1], dp0[i] + s)
    dp1[i+1] = min(dp1[i+1], dp0[i] + 10-s)
    dp0[i+1] = min(dp0[i+1], dp1[i] + (s+1))
    dp1[i+1] = min(dp1[i+1], dp1[i] + 10-(s+1))
ans = min(dp0[N], dp1[N]+1)
print(ans)
