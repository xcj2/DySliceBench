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


def nc2(n):
    return (n * (n - 1)) >> 1


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

utf = UnionFindTree()
for n in range(1, N + 1):
    utf.make(n)

h = {}
ans = []
total = nc2(N)
now = 0
for i in range(M):
    ans.append(total)

    a, b = ab[M - i - 1]
    x, y = utf.find(a), utf.find(b)
    a = utf.unite(x, y)
    if x != y:
        nx, ny = h.get(x, 1), h.get(y, 1)
        n = nx + ny
        total += nc2(nx) + nc2(ny)
        total -= nc2(n)

        h[x] = 1
        h[y] = 1
        h[a] = n

for v in reversed(ans):
    print(v)