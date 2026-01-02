import sys


class UnionFind(object):
    def __init__(self, N):
        self._parent = list(range(N))
        self.__num_components = [1] * N

    def root(self, x):
        if self._parent[x] == x:
            return x
        else:
            # root abbreviation
            self._parent[x] = self.root(self._parent[x])
            return self._parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def num_connected(self, x):
        return self.__num_components[self.root(x)]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return
        rank_x = self.__num_components[x]
        rank_y = self.__num_components[y]
        if rank_x < rank_y:
            self._parent[x] = y
            self.__num_components[y] += rank_x
        else:
            self._parent[y] = x
            self.__num_components[x] += rank_y
        return


fin = sys.stdin.readline
N, M = [int(elem) for elem in fin().split()]
conditions = [tuple(int(elem) - 1 for elem in fin().split()) for _ in range(M)]
uf = UnionFind(N)
for X, Y, _ in conditions:
    uf.unite(X, Y)

num_distinct_components = 0
for i in range(N):
    if uf.root(i) == i:
        num_distinct_components += 1
print(num_distinct_components)
