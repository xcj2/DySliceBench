class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
                
    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]
    
    
f=lambda:map(int,input().split())
N,K,L=f()
uf_road=UnionFind(N+1)
uf_rail=UnionFind(N+1)
for _ in [0]*K:
    uf_road.unite(*f())
for _ in [0]*L:
    uf_rail.unite(*f())

from bisect import bisect_left as bl
from bisect import bisect_right as br
    
roots=[(uf_road.find_root(i),uf_rail.find_root(i)) for i in range(1,N+1)]
sorted_roots=sorted(roots)

res=[]
for n in range(N):
    res.append(br(sorted_roots,roots[n])-bl(sorted_roots,roots[n]))
print(*res)