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
unions = defaultdict(int)
friends = defaultdict(int)
blocks = defaultdict(int)
finds = {}

N, M, K = map(int, input().split())
for i in range(N):
    utf.make(i+1)

for i in range(M):
    a, b = map(int, input().split())
    utf.unite(a, b)
    friends[a] += 1
    friends[b] += 1

for i in range(N):
    f = utf.find(i+1)
    finds[i+1] = f
    unions[f] += 1

for i in range(K):
    c, d = map(int, input().split())
    fc, fd = utf.find(c), utf.find(d)
    if fc == fd:
        blocks[c] += 1
        blocks[d] += 1

ans = [str(unions[finds[i+1]] - friends[i+1] - blocks[i+1] - 1) for i in range(N)]
print(" ".join(ans))
