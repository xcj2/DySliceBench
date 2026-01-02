

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union_size(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        if self.same(x, y):
            return

        xr = self.find(x)
        yr = self.find(y)
        if self.size[xr] > self.size[yr]:
            xr, yr = yr, xr    
        self.size[yr] = self.size[xr] + self.size[yr]
        self.par[xr] = yr
        return


def submit():
    n, m = map(int, input().split())
    bridge = [tuple(map(int, input().split())) for _ in range(m)]

    uf = UnionFind(n)
    curr = n * (n - 1) // 2
    ans = []
    for a, b in reversed(bridge):
        ans.append(curr)
        if not uf.same(a, b):
            curr -= uf.union_size(a) * uf.union_size(b)
            uf.unite(a, b)


    for a in reversed(ans):
        print(a)


submit()
    
        

