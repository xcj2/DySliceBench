class DisjointSet:
    def __init__(self):
        self.rank = {}
        self.p = {}

    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if(self.rank[x] > self.rank[y]):
            self.p[y] = x
        else:
            self.p[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def findSet(self, x):
        if(x != self.p[x]):
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

from collections import Counter
N, K, L = map(int, input().split())

ds = DisjointSet()
ds2 = DisjointSet()
for i in range(N):
    ds.makeSet(i+1)
    ds2.makeSet(i+1)

for i in range(K):
    p, q = map(int, input().split())
    ds.unite(p, q)

for i in range(L):
    r, s = map(int, input().split())
    ds2.unite(r, s)

a = [(ds.findSet(i), ds2.findSet(i)) for i in range(1, N+1)]
c = Counter(a)

print(' '.join([str(c[i]) for i in a]))