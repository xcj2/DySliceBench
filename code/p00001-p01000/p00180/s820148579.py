import sys
input = sys.stdin.readline

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

while True:
    n, m = map(int, input().split())
    
    if n==0 and m==0:
        exit()
        
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda t: t[2])
    uf = Unionfind(n)
    ans = 0
    
    for a, b, c in edges:
        if not uf.is_same(a, b):
            uf.unite(a, b)
            ans += c
    
    print(ans)
