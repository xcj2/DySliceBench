# -*- coding: utf-8 -*-

import sys
from heapq import heapify, heappop

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
DT = []
tmp = [[] for i in range(N)]
for i in range(N):
    t, d = MAP()
    DT.append((d, t))
DT.sort(reverse=1)

que = []
D = {}
dcnt = 0
# ポイント上位K個をまず取る
for i in range(K):
    d, t = DT[i]
    dcnt += d
    # 種類tが1つ目
    if t not in D:
        D[t] = d
    # 2つ目以降なら、最大のものはDに残して他はキューへ
    else:
        if D[t] < d:
            D[t], d = d, D[t]
        que.append((d, t))
heapify(que)
tcnt = len(D)

ans = dcnt + tcnt**2
for i in range(K, N):
    d2, t2 = DT[i]
    # 既に持っている種類ならスキップ
    if t2 in D:
        continue
    D[t2] = d2
    tmp = []
    # 全部1種類ずつならもう種類数を増やせないので終了
    if not que:
        break
    d, t = heappop(que)
    # この候補と交換してみる
    dcnt -= d
    dcnt += d2
    tcnt += 1
    ans = max(ans, dcnt + tcnt**2)
print(ans)
