# coding: utf-8

class UnionFind:
    def __init__(self,N):
        self.par = [i for i in range(N)]
        self.rank = [1]*N
        
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
        
class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

def kruskal():
    es.sort(key=lambda x: x.cost)
    uf = UnionFind(V)
    res = 0
    for i in range(E):
        if not uf.same(es[i].u, es[i].v):
            uf.unite(es[i].u, es[i].v)
            res += es[i].cost
            
    return res

V = int(input().rstrip())
E = 0
es = []
for i in range(V):
    line = list(map(int, input().rstrip().split()))
    for j in range(V):
        if line[j] != -1:
            es.append(Edge(i,j,line[j]))
            E += 1

ans = kruskal()
print(ans)
