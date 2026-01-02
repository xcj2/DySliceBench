class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif xr != yr:
            self.parent[yr] = xr
            self.rank[xr] += 1

from collections import Counter

N,M,K = map(int,input().split())

ds = DisjointSet(N)
deg = [0]*N
for _ in range(M):
    a,b = map(int,input().split())
    deg[a-1] += 1
    deg[b-1] += 1
    ds.union(a-1,b-1)

c = Counter(ds.find(i) for i in range(N))

res = [c[ds.find(i)]-deg[i]-1 for i in range(N)]
for _ in range(K):
    c,d = map(int,input().split())
    if ds.find(c-1) == ds.find(d-1):
        res[c-1] -= 1
        res[d-1] -= 1

print(*res)