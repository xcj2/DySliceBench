class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0]*(n + 1)

    def root(self, x):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.par[x] = r
        return r

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.par[x] = ry
            self.par[rx] = ry
        else:
            self.par[y] = rx
            self.par[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

def main():
    N, M, *PXY = map(int, open(0).read().split())
    P = PXY[:N]
    # print(N, M, PXY)
    uf = UnionFind(N + 1)
    for i in range(M):
        x, y = PXY[N + 2*i + 0], PXY[N + 2*i + 1]
        uf.unite(x, y)
    ans = 0
    for i in range(N):
        is_same = uf.same(i + 1, P[i])
        if is_same:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
