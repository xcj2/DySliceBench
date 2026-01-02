class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def root(self, x):
        if x != self.par[x]:
            self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
        else:
            self.par[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def update_p(self):
        for x in range(self.n):
            self.root(x)

    def get_size(self, x):
        return self.size[self.find_set(x)]




def main():
    n, m = [int(i) for i in input().split()]
    uf = UnionFind(n)
    for _ in range(m):
        x, y, _ = [int(i) for i in input().split()]
        uf.unite(x-1, y-1)
    uf.update_p()
    print(len(set(uf.par)))

if __name__ == '__main__':
    main()

