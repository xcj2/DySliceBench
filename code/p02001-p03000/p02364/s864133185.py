from heapq import heappush, heappop
class Prim:
    """ find minimum spanning tree by Prim's algorithm
    """

    def __init__(self, V, E, start=0, INF=10**9):
        """ V: the number of vertexes
            E: adjacency list (undirected graph)
            start: start vertex
            INF: Infinity cost
        """
        self.prim(V, E, start, INF)

    def prim(self, V, E, start=0, INF=10**9):
        used = [False] * V
        self.mincost = 0
        que = []
        heappush(que, (0, 0))
        while len(que) > 0:
            cost, v = heappop(que)
            if used[v]: continue
            used[v] = True
            self.mincost += cost
            for to, c in E[v]:
                heappush(que, (c, to))

    def minCost(self):
        return self.mincost
    

    
V, E = map(int, input().split())
edge = [[] for _ in range(V)]
for _ in range(E):
    s, t, w = map(int, input().split())
    edge[s].append((t, w))
    edge[t].append((s, w))

msp = Prim(V, edge)
print(msp.minCost())