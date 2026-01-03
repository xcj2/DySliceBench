class UnionFind(object):

    def __init__(self, N):
        self.N = N
        self.parent = list(range(self.N))
        self.rank = [0] * self.N
        self.size = [1] * self.N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.size[x] += self.size[y]
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return self.size[self.find(x)]

from collections import Counter
fn = lambda: map(int, input().split())
N, K, L = fn()
roads = UnionFind(N)
for i in range(K):
    pi, qi = fn()
    roads.union(pi-1, qi-1)
rails = UnionFind(N)
for i in range(L):
    ri, si = fn()
    rails.union(ri-1, si-1)
groups = []
for i in range(N):
    groups.append(str(roads.find(i)) + '-' + str(rails.find(i)))
c = Counter(groups)
print(*(c[g] for g in groups))