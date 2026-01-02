def main():
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

    raw = tuple(map(int, open(0).read().split()))
    n, m = raw[:2]
    uf = UnionFind(n)
    [uf.unite(a, b) for a, b in zip(*[iter(raw[2:2*m+2])]*2)]

    [print('yes' if uf.same(a, b) else 'no') for a, b in zip(*[iter(raw[2*m+3:])]*2)]

if __name__ == '__main__':
    main()

