

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, x):
        if x == self.par[x]:
            return self.par[x]
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        if self.same(x, y):
            return
        xr = self.find(x)
        yr = self.find(y)
        if self.size[xr] > self.size[yr]:
            xr, yr = yr, xr
        self.size[yr] = self.size[xr] + self.size[yr]
        self.par[xr] = yr


def submit():
    n, m = map(int, input().split())
    plist = list(map(int, input().split()))
    
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.unite(x, y)

    groups = {}
    for i in range(1, n + 1):
        r = uf.find(i)
        if r not in groups.keys():
            groups[r] = {i}
        else:
            groups[r].add(i)

    ans = 0
    for group in groups.values():
        for g in group:
            if plist[g - 1] in group:
                ans += 1
    print(ans)


submit()