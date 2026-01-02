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

D, G = MAP()
G //= 100
DC = []
MAX = 0
for i in range(D):
    d, c = MAP()
    c //= 100
    MAX += d
    DC.append((d, c))

# dp[i][j] := i点問題まで見て、合計j問解いた状態でのスコア最大値
dp = list2d(D+1, MAX+1, 0)
for i in range(D):
    d, c = DC[i]
    for j in range(MAX+1):
        for k in range(d+1):
            if j+k > MAX:
                break
            if k == d:
                # 全完ボーナス付
                dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j] + (i+1) * k + c)
            else:
                # 通常
                dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j] + (i+1) * k)

# スコアがG以上となる最小の解いた問題数を出力
for j in range(MAX+1):
    if dp[D][j] >= G:
        print(j)
        break
