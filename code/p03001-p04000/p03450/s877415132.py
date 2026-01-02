class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        # 根への距離を管理
        self.weight = [0] * (n + 1)

    # 検索
    def find(self, x):  # xの親を返す
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            # 親の値を更新(アルゴリズムの高速化)
            self.par[x] = y
            return y  # 親

    # 併合
    # (xからyへの重みがw) = (y - x = W)
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # 既に同集合の場合
        if rx == ry:
            if self.diff(x, y) != w:
                print("No")
                exit()
        # 木の高さで処理を変えるのは高速化(木を低くする)のため
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w + self.weight[x] - self.weight[y]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


import sys
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())
lrd = []
for i in range(M):
    l, r, d = map(int, input().split())
    lrd.append([l, r, d])
w_union_find = WeightedUnionFind(N)
for i in range(M):
    l, r, d = lrd[i]
    w_union_find.union(l, r, d)
print("Yes")
