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

N = INT()
S = input()

dp = list2d(N+1, 4, 0)
dp[0][0] = 1
msk = (1<<1000) - 1
for i in range(N):
    a = int(S[i])
    for j in range(4):
        dp[i+1][j] |= dp[i][j]
        if j == 0:
            dp[i+1][j+1] |= dp[i][j]<<a*100
            dp[i+1][j+1] &= msk
        if j == 1:
            dp[i+1][j+1] |= dp[i][j]<<a*10
            dp[i+1][j+1] &= msk
        if j == 2:
            dp[i+1][j+1] |= dp[i][j]<<a
            dp[i+1][j+1] &= msk
ans = 0
S = dp[N][3]
for k in range(1000):
    if S & 1<<k:
        ans += 1
print(ans)
