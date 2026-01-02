inf = float("inf")
class Node():

    def __init__(self, _id):
        self.id = _id
        self.d = inf
        self.pi = None
        self.color = 0
    
    def input_data(self):
        data = [int(i) for i in input().split()]
        self.adj = {G[i]: d
                    for i, d in enumerate(data)
                    if d != -1}
    
    def __hash__(self):
        return hash(self.id)
        
    

def prim():
    G[0].d = 0
    while True:
        mincost = inf
        for i in G:
            if i.color != 1 and i.d < mincost:
                mincost = i.d
                u = i
        
        if mincost == inf:
            break

        u.color = 1
        for v in u.adj.keys():
            if v.color != 1 and u.adj[v] < v.d:
                v.pi = u.id
                v.d = u.adj[v]

if __name__ == "__main__":
    n = int(input())
    G = [Node(i) for i in range(n)]
    [i.input_data() for i in G]
    prim()
    print(sum(g.d for g in G))
