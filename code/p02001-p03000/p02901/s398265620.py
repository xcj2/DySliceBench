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
INF = float('inf')
MOD = 10 ** 9 + 7

N, M = MAP()

# (鍵の購入コスト, 開けられる宝箱)
keys = [None] * M
for i in range(M):
    c, _ = MAP()
    # どの宝箱を開けられるのかをbitで持っておく
    s = 0
    for a in [a-1 for a in LIST()]:
        s += 1 << a
    keys[i] = (c, s)

# dp[i][j] := i個目の鍵まで見て、集合jの宝箱を開けるための最小コスト
dp = list2d(2, 1<<N, INF)
dp[0][0] = 0
cur = 0
nxt = 1
for i in range(M):
    # 今回の鍵で開けられる宝箱の集合s
    s = keys[i][1]
    c = keys[i][0]
    for j in range(1<<N):
        # 今回の鍵を買わない遷移
        dp[nxt][j] = min(dp[nxt][j], dp[cur][j])
        if dp[cur][j] != INF:
            m = j | s
            # 買う遷移：遷移元の開けられる宝箱の集合j | 今回の鍵で開けられる宝箱の集合s
            dp[nxt][m] = min(dp[nxt][m], dp[cur][j]+c)
    cur, nxt = nxt, cur
ans = dp[M%2][-1]

if ans != INF:
    print(ans)
else:
    print(-1)
