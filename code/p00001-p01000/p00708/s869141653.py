# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127&lang=en

from math import sqrt
from heapq import heappush, heappop
from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())


while True:
    N = int(input())
    if N == 0:
        break

    X, Y, Z, R = [], [], [], []
    for _ in range(N):
        xi, yi, zi, ri = map(float, input().split())
        X.append(xi)
        Y.append(yi)
        Z.append(zi)
        R.append(ri)

    # グラフ構造を作成？
    # 短いやつをつなげていって，森じゃなくなったらOKかな？
    uf = UnionFind(N)
    cost = 0.0
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dx = X[i] - X[j]
            dy = Y[i] - Y[j]
            dz = Z[i] - Z[j]
            dij = sqrt(dx * dx + dy * dy + dz * dz) - R[i] - R[j]
            heappush(edges, (dij, i, j))

    # Kruskal
    while len(edges) > 0:
        (w, u, v) = heappop(edges)
        if uf.unite(u, v):
            if w > 0:
                cost += w
    print("{:.3f}".format(cost))

