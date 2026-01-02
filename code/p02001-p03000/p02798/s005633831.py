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

def pop_count(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    i = (i + (i >> 4)) & 0x0f0f0f0f
    i = i + (i >> 8)
    i = i + (i >> 16)
    return i & 0x3f

N = INT()
cards = [[]] * 2
cards[0] = LIST()
cards[1] = LIST()

# dp[S][i] := 既に使用したカードの集合がSで、最後に使った(現在の右端の)カードがiの時の最小合計転倒数
dp = list2d(1<<N, N, INF)
for i in range(N):
    # 一番左は何が来ても転倒数0
    dp[1<<i][i] = 0
for S in range(1, 1<<N):
    popcnt = pop_count(S)
    # 各位置より元indexが右側にある出現済要素の個数(転倒数)を前計算しておく
    acc = [0] * N
    for i in range(N):
        if S & 1<<i:
            acc[i] = 1
    # 後ろから累積和
    acc = list(accumulate(acc[::-1]))[::-1]
    for i in range(N):
        if dp[S][i] == INF or not S & 1<<i:
            continue
        # 遷移元の右端カードの表裏を確定
        cur = cards[(i%2)^(1-popcnt%2)][i]
        for j in range(N):
            if S & 1<<j:
                continue
            # 遷移先の右端カードの表裏を確定
            nxt = cards[(j%2)^(popcnt%2)][j]
            # 昇順が崩れないなら遷移させてOK
            if cur <= nxt:
                # 転倒数を追加して遷移
                dp[S|1<<j][j] = min(dp[S|1<<j][j], dp[S][i] + acc[j])
ans = INF
for i in range(N):
    ans = min(ans, dp[(1<<N)-1][i])
if ans == INF:
    print(-1)
else:
    print(ans)
