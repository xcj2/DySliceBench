n = int(input())


class Vector:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        c = []
        for i, j in zip(self.a, b.a):
            c.append(i + j)
        return Vector(c)


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [1] * n
        self.count = [Vector([1, 0] if i % 2 == 0 else [0, 1])
                      for i in range(n)]

    def get_root(self, i):
        while self.parent[i] != -1:
            i = self.parent[i]
        return i

    def is_same_tree(self, i, j):
        return self.get_root(i) == self.get_root(j)

    def merge(self, i, j):
        i = self.get_root(i)
        j = self.get_root(j)
        if i == j:
            return

        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
            self.rank[i] = max(self.rank[i], self.rank[j] + 1)
            self.count[i] += self.count[j]
        else:
            self.parent[i] = j
            self.rank[j] = max(self.rank[j], self.rank[i] + 1)
            self.count[j] += self.count[i]


uf = UnionFind(2 * 10 ** 5)
for _ in range(n):
    x, y = [int(i) - 1 for i in input().split()]
    uf.merge(2 * x, 2 * y + 1)

ans = 0
for i, j in zip(uf.count, uf.parent):
    if j == -1:
        a = i.a
        ans += a[0] * a[1]
print(ans - n)
