class UnionFind:
    def __init__(self, n=0):
        self.d = [-1]*n

    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.d[self.root(x)]



def main():
    n, _, *A = map(int, open(0).read().split())
    uf = UnionFind(n)

    for a, x, y in zip(*[iter(A)]*3):
        if a == 0:
            uf.unite(x, y)
        else:
            print(1 if uf.same(x, y) else 0)

if __name__ == '__main__':
    main()
