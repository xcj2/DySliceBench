class UnionFind:
    def __init__(self, n):
        self._par = [i for i in range(n + 1)]
        self._size = [1] * (n + 1)

    def find(self, x):
        if self._par[x] == x:
            return x
        else:
            self._par[x] = self.find(self._par[x])
            return self._par[x]

    def is_same_root(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return x == y

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self._size[x] < self._size[y]:
            self._par[x] = y
            self._size[y] += self._size[x]
        else:
            self._par[y] = x
            self._size[x] += self._size[y]

    def size(self, x):
        return self._size[self.find(x)]


def main():
    n, m = [int(i) for i in input().split()]
    bridges = [[int(i) for i in input().split()] for _ in range(m)]

    union_find = UnionFind(n)
    connection = []
    for i, j in bridges[::-1]:
        if union_find.is_same_root(i, j):
            connection.append(0)
        else:
            connection.append(union_find.size(i) * union_find.size(j))
            union_find.unite(i, j)

    sum_ = 0
    for i in connection[::-1]:
        sum_ += i
        print(sum_)


if __name__ == '__main__':
    main()
