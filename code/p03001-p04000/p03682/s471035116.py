N = int(input())
X = [[i] + list(map(int, input().split())) for i in range(N)]

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        elif self.rank[x] < self.rank[y]:
            x, y = y, x
        
        self.par[y] = x
                
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

def kruskal():
    edges.sort(key=lambda x: x[2])
    t = UnionFind(N)
    ret = 0
    
    for u, v, c in edges:
        if not t.is_same(u, v):
            t.unite(u, v)
            ret += c
            
    return ret

edges = []

for k in range(1, 3):
    X.sort(key=lambda x: x[k])
    for i in range(N - 1):
        edges.append((X[i][0], X[i + 1][0], abs(X[i][k] - X[i + 1][k])))

print(kruskal())
