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

H, N = MAP()
AB = [()]
for i in range(N):
    a, b = MAP()
    AB.append((a, b))

dp = list2d(N+1, 20007, INF)
dp[0][0] = 0
for i in range(1, N+1):
    a, b = AB[i]
    for j in range(20007):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j-a >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j-a] + b, dp[i-1][j-a] + b)
print(min(dp[N][H:]))
