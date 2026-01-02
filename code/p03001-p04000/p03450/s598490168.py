class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
        self.diff_weight = [0 for i in range(n+1)]

    def root(self, x):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.diff_weight[x] += self.diff_weight[self.par[x]]
        self.par[x] = r
        return r

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = w
        return True

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

def solve():
    N,M=map(int,input().split())
    uf = UnionFind(N)
    for i in range(M):
        l,r,d=map(int,input().split())
        if uf.issame(l,r):
            if uf.diff(l,r) != d:
                return 'No'
        else:
            uf.merge(l,r,d)
    return 'Yes'

print(solve())
