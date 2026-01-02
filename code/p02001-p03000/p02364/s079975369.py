class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost
    
    def __str__(self):
        return "u: " + str(self.u) + " v: " + str(self.v) + " cost: " + str(self.cost)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def isSame(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    V, E = map(int,input().split())
    edges = []
    for i in range(E):
        s,t,w = map(int,input().split())
        e = Edge(s,t,w)
        edges.append(e)
    
    edges.sort(key=lambda e: e.cost)

    uf = UnionFind(V+1)

    ans = 0
    for edge in edges:
        if not uf.isSame(edge.u, edge.v):
            uf.unite(edge.u, edge.v)
            ans += edge.cost

    print(ans)

if __name__ == '__main__':
    solve()
