class UnionFind:
    def __init__(self, n):
        self.parent = [ -1 for _ in range(n) ]
        self._size = n

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.parent[y] < self.parent[x]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self._size -= 1

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.root(self.parent[x])

    def size(self, x):
        return -parent[root(x)]


N, M = map(int, input().split())

uf_tree = UnionFind(N)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    X -= 1; Y -= 1;
    uf_tree.unite(X, Y)

print(uf_tree._size)
