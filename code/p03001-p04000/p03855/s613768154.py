n, k, l = map(int, input().split())
from collections import defaultdict

class UnionFind( ):
    def __init__(self, N):
        self.rank = [0] * N
        self.par = [i for i in range(N)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


uf1 = UnionFind(n)
uf2 = UnionFind(n)

for i in range(k):
    p, q = map(int, input().split())
    uf1.unite(p - 1, q - 1)


for i in range(l):
    r, s = map(int, input().split())
    uf2.unite(r - 1, s - 1)

pair = defaultdict(int)
for i in range(n):
    a = uf1.find(i)
    b = uf2.find(i)
    pair[(a, b)] += 1

ans = []
for i in range(n):
    ans.append(pair[(uf1.find(i), uf2.find(i))])

print(" ".join(map(str, ans)))
