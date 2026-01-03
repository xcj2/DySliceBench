class UnionFind:
    def __init__(self, size):
        self.data = [-1 for _ in range(size)]
    def find(self, x):
        if self.data[x] < 0:
            return x
        else:
            self.data[x] = self.find(self.data[x])
            return self.data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.data[y] < self.data[x]:
                x, y = y, x
            self.data[x] += self.data[y]
            self.data[y] = x
        return (x != y)
    def same(self, x, y):
        return (self.find(x) == self.find(y))
    def size(self, x):
        return -self.data[self.find(x)]

N, K, L = [int(i) for i in input().split()]

uf1 = UnionFind(N)
for _ in range(K):
    p, q = [int(i) - 1 for i in input().split()]
    uf1.union(p, q)

uf2 = UnionFind(N)
for _ in range(L):
    r, s = [int(i) - 1 for i in input().split()]
    uf2.union(r, s)

from collections import Counter
C = Counter((uf1.find(i), uf2.find(i)) for i in range(N))
print(*[C[(uf1.find(i), uf2.find(i))] for i in range(N)])
