from collections import defaultdict


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


utf = UnionFindTree()

N, M = map(int, input().split())
for n in range(N):
    utf.make(n + 1)

for m in range(M):
    x, y, z = map(int, input().split())
    utf.unite(x, y)

h = defaultdict(int)
for n in range(N):
    x = utf.find(n + 1)
    h[x] += 1

ans = 0
rest = N
for k, v in h.items():
    ans += 1
    rest -= v
print(ans + rest)
