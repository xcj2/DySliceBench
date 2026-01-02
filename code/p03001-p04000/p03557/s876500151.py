# -*- coding: utf-8 -*-

import sys
from bisect import bisect_right
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
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
A = sorted(LIST())
B = sorted(LIST())
C = sorted(LIST())

dp1 = [1] * (N+1)
dp2 = [0] * (N+1)
dp3 = [0] * (N+1)

for i1, a in enumerate(A):
    i2 = bisect_right(B, a)
    dp2[i2] += dp1[i1]
dp2 = list(accumulate(dp2))
for i2, b in enumerate(B):
    i3 = bisect_right(C, b)
    dp3[i3] += dp2[i2]
dp3 = list(accumulate(dp3))
print(sum(dp3[:N]))
