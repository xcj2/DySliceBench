class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x):
        stack = []
        parent = self.parent
        while parent[x] != x:
            stack.append(x)
            x = parent[x]
        for y in stack:
            parent[y] = x
        return x

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

N,M = map(int,input().split())

ds = DisjointSet(N)

for _ in range(M):
    a,b = map(lambda x: int(x)-1, input().split())
    ds.union(a,b)

c = Counter(ds.find(i) for i in range(N))

print(max(c.values()))
