from collections import Counter


class UnionFindTree:
    def __init__(self):
        self.p = {}
        self.rank = {}

    def make(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find(self, x):
        if x in self.p:
            if self.p[x] != x:
                # 経路圧縮
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        return None

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        return self._unite(self.find(x), self.find(y))

    def _unite(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.p[x] = y
            return y
        else:
            self.p[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            return x


N, K, L = map(int, input().split())

utf1 = UnionFindTree()
utf2 = UnionFindTree()
for i in range(N):
    utf1.make(i+1)
    utf2.make(i+1)

for i in range(K):
    p, q = map(int, input().split())
    utf1.unite(p, q)
for i in range(L):
    r, s = map(int, input().split())
    utf2.unite(r, s)

pairs = [(utf1.find(i+1), utf2.find(i+1)) for i in range(N)]
counts = Counter(pairs)
print(" ".join([str(counts[k]) for k in pairs]))
