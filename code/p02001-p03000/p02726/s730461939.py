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

N, x, y = MAP()
x -= 1; y -= 1

G = list2d(N, N, 0)
for i in range(N):
    for j in range(i+1, N):
        G[i][j] = min(j - i, abs(i - x) + abs(j - y) + 1, abs(j - x) + abs(i - y) + 1)
ans = [0] * N
for i in range(N):
    for j in range(i+1, N):
        ans[G[i][j]] += 1
[print(a) for a in ans[1:]]
