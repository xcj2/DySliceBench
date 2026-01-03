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

N, K = MAP()
A = LIST()

B = [0] * N
for i, a in enumerate(A):
    if a > 0:
        B[i] = a

acc = [0] + list(accumulate(A))
acc2 = [0] + list(accumulate(B))
acc2rev = [0] + list(accumulate(B[::-1]))[::-1] + [0]

ans = -INF
for i in range(1, N-K+2):
    cnt = max(acc[i+K-1] - acc[i-1], 0)
    cnt += acc2[i-1] + acc2rev[i+K]
    ans = max(ans, cnt)
print(ans)
