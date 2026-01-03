#!/usr/bin python3
# -*- coding: utf-8 -*-

#最小全域木　クラスカル法
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる

INF = float('inf')

class UnionFind():
    def __init__(self, n):      #初期化
        self.n = n
        # 親
        self.parents = [i for i in range(n)]
        # 木の深さ
        self.ranks = [0] * n

    def find(self, x):          #親を出力
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.ranks[x] < self.ranks[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.ranks[x]==self.ranks[y]:
                self.ranks[x] += 1

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)

def kruskal(n, edges):
    uf = UnionFind(n)
    ret = 0
    for w, u, v in edges:
        if not uf.same(u, v):
            ret += w
            uf.unite(u, v)
    return ret

def main():
    N = int(input())
    #リストの作成
    L = [None]*N
    for i in range(N):
        x, y = map(int,input().split())
        L[i]=(x, y, i)
    Edges = []
    for i in range(2):
        L.sort(key=lambda x:x[i])
        for j in range(N-1):
            Edges.append( (L[j+1][i]-L[j][i], L[j][2], L[j+1][2]) )
    Edges.sort()

    print(kruskal(N, Edges))

if __name__ == '__main__':
    main()