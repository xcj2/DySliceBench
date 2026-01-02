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

N, K = MAP()
DT = []
tmp = [[] for i in range(N)]
for i in range(N):
    t, d = MAP()
    DT.append((d, t))
DT.sort(reverse=1)

A = []
D = {}
dcnt = 0
# ポイント上位K個をまず取る
for i in range(K):
    d, t = DT[i]
    dcnt += d
    # 種類tが1つ目なら、確定で残す
    if t not in D:
        D[t] = d
    # 2つ目以降なら、最大のものを残して他は交換候補へ
    else:
        if D[t] < d:
            D[t], d = d, D[t]
        A.append(d)
A.sort(reverse=1)
tcnt = len(D)

ans = dcnt + tcnt**2
for i in range(K, N):
    d2, t2 = DT[i]
    # 既に持っている種類ならスキップ
    if t2 in D:
        continue
    D[t2] = d2
    # 全部1種類ずつ(交換候補がもうない)なら、もう種類数を増やせないので終了
    if not A:
        break
    d = A.pop()
    # この候補と交換してみる
    dcnt -= d
    dcnt += d2
    tcnt += 1
    ans = max(ans, dcnt + tcnt**2)
print(ans)
