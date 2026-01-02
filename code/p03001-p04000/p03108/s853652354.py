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
bridges = tuple(
    tuple(int(elem) - 1 for elem in fin().split())
    for _ in range(M)
)

uf = UnionFind(N)
num_incovenient_list = [N * (N - 1) // 2]
for A, B in bridges[::-1]:
    num_islands_A = uf.num_connected(A)
    num_islands_B = uf.num_connected(B)
    if not uf.same(A, B):
        num_incovenient_list.append(
            num_incovenient_list[-1] - num_islands_A * num_islands_B)
        uf.unite(A, B)
    else:
        num_incovenient_list.append(num_incovenient_list[-1])

num_incovenient_list.pop()
print(*num_incovenient_list[::-1], sep="\n")

