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
    N, M, *AB = map(int, open(0).read().split())
    uf = UnionFind(N)
    elems = [1] * (N + 1)
    ans = N * (N - 1) // 2
    ANS = [0]*M
    for i in range(M):
        # print(ans)
        ANS[M - i - 1] = ans
        a = AB[2 * M - i * 2 - 2 + 0]
        b = AB[2 * M - i * 2 - 2 + 1]
        ra = uf.root(a)
        rb = uf.root(b)
        uf.unite(ra, rb)
        r = uf.root(ra)
        if ra != rb:
            era = elems[ra]
            erb = elems[rb]
            ans -= era * erb
            elems[r] = era + erb
    print('\n'.join(map(str, ANS)))

if __name__ == '__main__':
    main()
