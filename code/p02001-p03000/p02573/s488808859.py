class MyUnionFind():
    __slots__ = ["par", "rank", "size"]

    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, c):
        if self.par[c] == c:
            return c

        ret = self.find(self.par[c])
        self.par[c] = ret
        return ret

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return

        if self.rank[yr] > self.rank[xr]:
            self.par[xr] = yr
            self.size[yr] += self.size[xr]
        else:
            self.par[yr] = xr
            self.size[xr] += self.size[yr]
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1



def main():
    N, M = map(int, input().split())
    uf = MyUnionFind(N)
    for i in range(M):
        a, b = map(int, input().split())
        uf.union(a, b)

    print(max(uf.size))

if __name__ == '__main__':
    main()