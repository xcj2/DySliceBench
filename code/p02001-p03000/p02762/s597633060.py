from collections import defaultdict


class UnionFind:
    def __init__(self, n=0):
        self.d = {i: -1 for i in range(n)}

    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if (x == y):
            return False
        if (self.d[x] > self.d[y]):
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.d[self.find(x)]


N, M, K = map(int, input().split(' '))
deg = defaultdict(int)
to = defaultdict(list)
uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.unite(a, b)

for _ in range(K):
    c, d = map(int, input().split(' '))
    c -= 1
    d -= 1
    to[c].append(d)
    to[d].append(c)

for i in range(N):
    ans = uf.size(i) - 1 - deg[i]
    for u in to[i]:
        if uf.same(i, u):
            ans -= 1
    print(ans, end=' ' if i != (N - 1) else '\n')
