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

H, W = map(int, input().split())
S = [input()[:-1] for _ in range(H)]
uf = Unionfind(H*W)

for i in range(H):
    for j in range(W):
        if i+1<H and S[i][j]!=S[i+1][j]:
            uf.unite(W*i+j, W*(i+1)+j)
            
        if j+1<W and S[i][j]!=S[i][j+1]:
            uf.unite(W*i+j, W*i+j+1)

wcnt = defaultdict(int)
bcnt = defaultdict(int)

for i in range(H):
    for j in range(W):
        r = uf.root(W*i+j)
        
        if S[i][j]=='#':
            wcnt[r] += 1
        else:
            bcnt[r] += 1

ans = 0

for k in wcnt:
    ans += wcnt[k]*bcnt[k]

print(ans)