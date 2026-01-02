class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)
    
    def find_root(self,x):
        return self.find(x)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]
    
f=lambda:map(int,input().split())
N,M=f()
wuf=WeightedUnionFind(N+1)

flg=True
for _ in [0]*M:
    l,r,w=f()
    if wuf.is_same_group(l,r):
        if wuf.diff(l,r)!=w:
            flg=False
    else:
        wuf.unite(l,r,w)
    if not flg:
        break
print(['No','Yes'][flg])