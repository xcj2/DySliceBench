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
