class union_find:

    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        return

    def sizeof(self, x):
        return -par[root(x)]

n, m = map(int, input().split())
p = list(map(int, input().split()))

uf = union_find(n)

for i in range(m):
    x, y = map(int, input().split())
    uf.unite(x-1, y-1)

cnt = 0
for i in range(len(p)):
    if uf.same(i, p[i]-1):
        cnt += 1

print(cnt)