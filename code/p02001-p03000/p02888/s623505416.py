# -*- coding: utf-8 -*-

import sys
from bisect import bisect_left

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
A = LIST()

A.sort()
ans = 0
for i in range(N):
    a = A[i]
    for j in range(i+1, N):
        # 小さい方2本a,bを決めておく(a < b)
        b = A[j]
        # 条件を満たすcの範囲は b < c < a+b の間
        k = bisect_left(A, a+b)
        ans += k - (j+1)
print(ans)
