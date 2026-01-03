import heapq
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += (self.rank[x] == self.rank[y])

def kruskal(n, edge):
    ans = 0
    uf = UnionFind(n)
    while True:
        d, v, u = heapq.heappop(edge)
        
        if uf.find(v) != uf.find(u):
            uf.union(v, u)
            n -= 1
            ans += d
        if n < 2: return ans
    return ans

n = int(input())
x, y = [None]*n, [None]*n

for i in range(n):
    a, b = map(int, input().split())
    x[i] = (a, i)
    y[i] = (b, i)

x.sort(key=lambda x:x[0])
y.sort(key=lambda y:y[0])

edge = []
for i in range(n-1):
    heapq.heappush(edge, (x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(edge, (y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))

del x, y
print(kruskal(n, edge))