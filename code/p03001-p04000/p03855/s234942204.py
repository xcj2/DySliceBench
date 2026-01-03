from collections import defaultdict
N, K, L = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
            self.size[x] = 0
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            self.size[y] = 0
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # すべての頂点に対して親を検索する
    def all_find(self):
        for n in range(len(self.par)):
            self.find(n)


UF_road = UnionFind(N)
for k in range(K):
    p, q = map(int, input().split())
    p, q = p - 1, q - 1
    UF_road.union(p, q)
UF_road.all_find()

UF_train = UnionFind(N)
for l in range(L):
    r, s = map(int, input().split())
    r, s = r - 1, s - 1
    UF_train.union(r, s)
UF_train.all_find()

D = defaultdict(int)
for r, t in zip(UF_road.par, UF_train.par):
    D[(r, t)] += 1

ans = [D[(r, t)] for r, t in zip(UF_road.par, UF_train.par)]
print(*ans, sep=' ')
