from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


n, k, l = map(int, input().split())
uf1 = UnionFind(n)
uf2 = UnionFind(n)
for _ in range(k):
    a, b = map(int, input().split())
    uf1.unite(a - 1, b - 1)
for _ in range(l):
    a, b = map(int, input().split())
    uf2.unite(a - 1, b - 1)
d = defaultdict(int)
for i in range(n):
    d[(uf1.find(i), uf2.find(i))] += 1
ans = [0] * n
for i in range(n):
    ans[i] = d[(uf1.find(i), uf2.find(i))]
print(*ans)
