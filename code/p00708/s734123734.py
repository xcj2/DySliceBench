from decimal import *

class UnionFind():
    # 初めは全ての頂点が別々の木の根
    def __init__(self, n):  # n要素で初期化
        self.parent = list(range(n)) # 親
        self.rank = [0] * n   # 木の深さ
        self._nsets = n  # 集合の数

    def root_of(self, x):
        children = [x]
        while self.parent[x] != x:
            x = self.parent[x]
            children.append(x)

        for ch in children:
            self.parent[ch] = x
        return x

    # xとyの属する集合を併合
    def union(self, x, y):
        rx = self.root_of(x)
        ry = self.root_of(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]: # ランクの小さい木から大きい木の根に辺を張る
            self.parent[rx] = ry  # rxをryの子とする
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        self._nsets -= 1

    # 同じ集合に属するかどうか
    def same(self, x, y):
        return self.root_of(x) == self.root_of(y)

    # 集合の数
    def get_nsets(self):
        return self._nsets

while True:
    N = int(input())
    if N == 0: break
    x = [None] * N;  y = [None] * N;  z = [None] * N
    r = [None] * N
    for i in range(N):
        x[i], y[i], z[i], r[i] = [Decimal(a) for a in input().split()]

    E = []
    uf = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            dsq = pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2) + pow(z[i] - z[j], 2)
            rsq = pow(r[i] + r[j], 2)
            if dsq <= rsq:
                uf.union(i, j)
            else:
                E.append((dsq.sqrt() - r[i] - r[j], (i, j)))

    E.sort()
    ans = Decimal('0')
    for d, (i, j) in E:
        if uf.get_nsets() == 1:  break
        if uf.same(i, j): continue
        uf.union(i, j)
        ans += d

    ans = ans.quantize(Decimal('0.001'), rounding = ROUND_HALF_UP)
    print(ans)
