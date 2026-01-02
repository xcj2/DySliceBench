V, E = map(int, input().split())

PAR = list(range(V))
 
def root(x):
    if PAR[x] == x:
        return x
    else:
        PAR[x] = root(PAR[x])
        return PAR[x]
 
def same(x, y):
    return root(x) == root(y)
 
def unite(x, y):
    x = root(x)
    y = root(y)
    
    if x == y:
        return
    
    PAR[max(x, y)] = min(x, y)


class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost
        
        

EDGES = []
for _ in range(E):
    s, t, w = map(int, input().split())
    EDGES.append(Edge(s, t, w))
    
def kruskal():
    edges = sorted(EDGES, key=lambda a: a.cost )
    res = 0
    for edge in edges:
        if (not same(edge.u, edge.v)):
            unite(edge.u, edge.v)
            res += edge.cost
    
    return res
    
print(kruskal())
