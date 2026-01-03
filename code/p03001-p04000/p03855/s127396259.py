from collections import Counter
N, K, L = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]
Y = [list(map(int, input().split())) for _ in range(L)]

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
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
                
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def __repr__(self):
        return ', '.join(str(x) for x in self.par)

t1 = UnionFind(N)
t2 = UnionFind(N)

for p, q in X:
    t1.unite(p - 1, q - 1)
    
for r, s in Y:
    t2.unite(r - 1, s - 1)

connect = [(t1.find(i), t2.find(i)) for i in range(N)]
ctr = Counter(connect)
print(*[ctr[key] for key in connect])
