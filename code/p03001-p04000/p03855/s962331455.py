class UnionFind:
    def __init__(self, size):
        self.__data = [-1 for _ in range(size)]
    def find(self, x):
        if self.__data[x] < 0:
            return x
        else:
            self.__data[x] = self.find(self.__data[x])
            return self.__data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.__data[y] < self.__data[x]:
                x, y = y, x
            self.__data[x] += self.__data[y]
            self.__data[y] = x
        return (x != y)
    def same(self, x, y):
        return (self.find(x) == self.find(y))
    def size(self, x):
        return -self.__data[self.find(x)]
    def get_data(self):
        return [a if a >= 0 else i for i, a in enumerate(self.__data)]

N, K, L = [int(i) for i in input().split()]

uf1 = UnionFind(N)
for _ in range(K):
    p, q = [int(i) - 1 for i in input().split()]
    uf1.union(p, q)

uf2 = UnionFind(N)
for _ in range(L):
    r, s = [int(i) - 1 for i in input().split()]
    uf2.union(r, s)

for i in range(N):
    uf1.find(i)
    uf2.find(i)

from collections import Counter
Z = [(a, b) for a, b in zip(uf1.get_data(), uf2.get_data())]
C = Counter(Z)
print(*[C[z] for z in Z])
