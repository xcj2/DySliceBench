class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,M,*f = map(int, open(0).read().split())
p = f[:N]
xy = [f[N+2*i:N+2*i+2] for i in range(M)]
uf = UnionFind(N+1)
for x, y in xy:
    uf.union(x,y)
ans = 0
for i in range(1,N+1):
    if p[i-1] == i:
        ans += 1
    else:
        if uf.find(p[i-1]) == uf.find(i):
            ans += 1
        elif uf.find(i) < 0:
            if uf.find(p[i-1]) == i:
                ans += 1
        elif uf.find(p[i-1]) < 0:
            if uf.find(i) == p(i-1):
                ans += 1
print(ans)