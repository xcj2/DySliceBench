from collections import Counter
n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]

class UnionFind:
    # まずは最初の状態を作る
    def __init__(self, N):
        # 最初はみんなバラバラ
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0

    # そのノードの根を返す過程で,集合の要素を根に直接つなぎかえる(木の最適化)
    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]

    # aとbの根が同じ,つまり同じ連結成分内かどうかを返す
    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    # 連結成分同士を効率的に(rankが大きい方を動かさずにrankが小さい方をくっつける)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        # a, bが同じグループ内にいたから何もしない
        if ra == rb: return
        # 異なるグループにいた場合
        # 短い方をくっつける
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

# friendsは友達の数を保持する
uf = UnionFind(n)
for a, b in ab:
    a, b = a-1, b-1
    # aとbが同連結成分内であれば何もする必要がない
    if uf.is_same(a, b): continue
    # 異なれば結合
    uf.unite(a, b)
# 木の高さの最適化
for i in range(n):
    uf.root(i)
tmp = sorted(Counter(uf.parent).items(), key=lambda x:x[1])
print(tmp[-1][1])