class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]

    def same(self, x, y):
        return self.root(x)==self.root(y)

    def root(self, x):
        if self.par[x]<0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return

        if self.par[x]>self.par[y]:
            x,y = y,x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self,x):
        return -self.par[self.root(x)]

from collections import defaultdict

n,k,l = map(int, input().split())
u = UnionFind(n+1)
v = UnionFind(n+1)

for _ in range(k):
  p,q = map(int, input().split())
  u.unite(p,q)

for _ in range(l):
  r,s = map(int, input().split())
  v.unite(r,s)

d = defaultdict(int)
for i in range(1,n+1):
  x = (u.root(i), v.root(i))
  d[x] += 1

print(*[d[(u.root(i), v.root(i))] for i in range(1,n+1)])