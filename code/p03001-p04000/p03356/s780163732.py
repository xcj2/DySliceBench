class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    g = []
    for i in range(n):
        g.append([p[i], i])
    g.sort()  # p[i]でsort()している

    uf = UnionFind(n)
    for i in range(m):
        x, y = map(int, input().split())
        uf.unite(x - 1, y - 1)

    ans = 0
    for i in range(n):
        if uf.same(i, g[i][1]):  # インデックスと数の親が仁いい場合は+1
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()