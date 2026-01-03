class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root

    def unite(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
            self.size[yroot] += self.size[xroot]
        elif xrank == yrank:
            self.parents[yroot] = xroot
            self.rank[yroot] += 1
            self.size[xroot] += self.size[yroot]
        else:
            self.parents[yroot] = xroot
            self.size[xroot] += self.size[yroot]

    def len(self, x):
        return self.size[self.find(x)]

    def roots(self):
        return [i for i in range(N) if self.rank[i] == 0]

from collections import defaultdict

N, K, L = map(int, input().split())

uf1 = UnionFind(N)
uf2 = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    uf1.unite(p - 1, q - 1)

for _ in range(L):
    r, s = map(int, input().split())
    uf2.unite(r - 1, s - 1)

D = defaultdict(int)

for i in range(N):
    D[(uf1.find(i), uf2.find(i))] += 1

res = []

for i in range(N):
    res.append(D[(uf1.find(i), uf2.find(i))])

print(' '.join(map(str, res)))