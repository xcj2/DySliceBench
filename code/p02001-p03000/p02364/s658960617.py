class DisjointSet:
    def __init__(self,size):
        self.rank = [None]*size
        self.p = [None]*size
        for i in range(size):
            self.make_set(i)
        return
    
    def make_set(self,x):
        self.p[x] = x
        self.rank[x] = 0
        return
    
    def same(self,x,y):
        return self.find_set(x) == self.find_set(y)
        
    def unite(self,x,y):
        self.link(self.find_set(x),self.find_set(y))
        return
    
    def link(self,x,y):
        if self.rank[x]>self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x]==self.rank[y]:
                self.rank[y] += 1
                
    def find_set(self,x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
    
class Edge:
    def __init__(self,source,target,cost):
        self.source = source
        self.target = target
        self.cost = cost
        
def kruskal(edges):
    edges.sort(key=lambda x: x.cost)
    
    S = DisjointSet(n)
    K = []
    
    for i in range(m):
        if S.find_set(edges[i].source) != S.find_set(edges[i].target):
            K.append(edges[i])
            S.unite(edges[i].source,edges[i].target)
    return K

n,m = map(int,input().split())
edges = []

for i in range(m):
    s,t,w = map(int,input().split())
    edges.append(Edge(s,t,w))
    
K = kruskal(edges)

cost = 0
while K:
    edge = K.pop()
    cost += edge.cost
print(cost)
