# -*- coding: utf-8 -*-

"""
参考：https://img.atcoder.jp/arc065/editorial.pdf
・Union-Find木
"""

import sys
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

from collections import Counter

# Union-Find木
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        # 1-indexedのままでOK、その場合は[0]は未使用
        self.par = [i for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, K, L = map(int, input().split())
uf1 = UnionFind(N)
uf2 = UnionFind(N)
for i in range(K):
    p, q = map(int, input().split())
    uf1.union(p, q)
for i in range(L):
    p, q = map(int, input().split())
    uf2.union(p, q)

# (道路グループ番号, 鉄道グループ番号) のペアを各都市について作る
pairs = [None] * N
for i in range(N):
    pairs[i] = (uf1.find(i+1), uf2.find(i+1))

# 同じ内容のペアについて数える
c = Counter(pairs)

ans = [0] * N
for i in range(N):
    # 自分のペアのカウント数を各都市について取得
    ans[i] = c[pairs[i]]
print(*ans)
