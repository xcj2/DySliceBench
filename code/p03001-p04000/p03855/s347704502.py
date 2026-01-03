import sys
input = sys.stdin.readline
from collections import *

class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [1]*n
    
    def root(self, x):
        r = x
        
        while not self.par[r]<0:
            r = self.par[r]
        
        t = x
        
        while t!=r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r
        
        return r
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        
        if rx==ry:
            return
        
        if self.rank[rx]<=self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry
            
            if self.rank[rx]==self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
    
    def is_same(self, x, y):
        return self.root(x)==self.root(y)
    
    def count(self, x):
        return -self.par[self.root(x)]

N, K, L = map(int, input().split())
uf1 = Unionfind(N)
uf2 = Unionfind(N)

for _ in range(K):
    p, q = map(int, input().split())
    uf1.unite(p-1, q-1)

for _ in range(L):
    r, s = map(int, input().split())
    uf2.unite(r-1, s-1)

d = defaultdict(int)

for i in range(N):
    a = uf1.root(i)
    b = uf2.root(i)
    d[10**6*a+b] += 1
    
ans = []

for i in range(N):
    a = uf1.root(i)
    b = uf2.root(i)
    ans.append(d[10**6*a+b])

print(*ans)