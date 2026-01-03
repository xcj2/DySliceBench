from collections import defaultdict

class UnionFind:
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
        if x == y:
            return
 
        if self.par[x] > self.par[y]:
            x, y = y, x
 
        self.par[x] += self.par[y]
        self.par[y] = x
        
N, K, L = map(int, input().split())

uf = UnionFind(N)
for i in range(K):
    p, q = map(int, input().split())
    uf.unite(p - 1, q - 1)
    
uf2 = UnionFind(N)
for i in range(L):
    r, s = map(int, input().split())
    uf2.unite(r - 1, s - 1)

d = defaultdict(int)
for i in range(N):
    n = uf.root(i)
    m = uf2.root(i)
    d[(n, m)] += 1

ans = []
for i in range(N):
    n = uf.root(i)
    m = uf2.root(i)
    ans.append(d[(n, m)])

print(* ans)