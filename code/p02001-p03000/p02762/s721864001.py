N,M,K = map(int,input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
CD = [tuple(map(int, input().split())) for _ in range(K)]

"""
Union-Find木実装のキモ(計算量削減)
1. Unionの工夫
   マージテク：大きい方を動かさずに小さい方をくっつける
2. Findの工夫
   経路圧縮 : 集合の要素を根に直接つなぎ変える.木をフラットにする.
"""

# Union-Findを用いて連結成分を考える(Union-Find木の実装)
class UnionFind:
    # まずは最初の状態を作る
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0

    # そのノードの根を返す過程で,集合の要素を根に直接つなぎかえる
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
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

blocks = [[] for _ in range(N)]
for c, d in CD:
    c, d = c-1, d-1
    blocks[c].append(d)
    blocks[d].append(c)

# friendsは友達の数を保持する
friends = [0] * N
uf = UnionFind(N)
for a,b in AB:
    a, b = a-1, b-1
    friends[a] += 1
    friends[b] += 1
    # aとbが同連結成分内であれば何もする必要がない
    if uf.is_same(a, b): continue
    # 異なれば結合
    uf.unite(a, b)

for i in range(N):
    uf.root(i)

from collections import Counter
ctr = Counter()
for i in range(N):
    r = uf.root(i)
    ctr[r] += 1

ans = []
for i in range(N):
    tmp = ctr[uf.root(i)] - friends[i] -1
    for b in blocks[i]:
        if uf.is_same(i, b):
            tmp -= 1
    ans.append(tmp)
print(*ans)