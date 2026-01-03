from collections import*

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x]) 
        return self.parents[x]  

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N, K, L = map(int, input().split())

road = UnionFind(N)
rail = UnionFind(N)

for i in range(K):
    p, q = map(int, input().split())
    road.union(p-1, q-1)
for i in range(L):
    p, q = map(int, input().split()) 
    rail.union(p-1, q-1)

d = defaultdict(int)

for i in range(N):
    d[(road.find(i), rail.find(i))] += 1
print(*[d[(road.find(i), rail.find(i))] for i in range(N)])