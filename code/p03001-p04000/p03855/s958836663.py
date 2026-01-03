class UnionFind:
    def __init__(self, size):
        self.data = [i for i in range(size)]
    def find(self, x):
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.data[x] = min(x, y)
            self.data[y] = self.data[x]

N, K, L = [int(i) for i in input().split()]

uf1 = UnionFind(N)
for _ in range(K):
    p, q = [int(i) - 1 for i in input().split()]
    uf1.union(p, q)

uf2 = UnionFind(N)
for _ in range(L):
    r, s = [int(i) - 1 for i in input().split()]
    uf2.union(r, s)

from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    d[(uf1.find(i), uf2.find(i))] += 1

l = ""
for i in range(N):
    l += str(d[(uf1.find(i), uf2.find(i))]) + " "
print(l[:-1])