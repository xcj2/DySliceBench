from heapq import heappush, heappop
def dijkstra(graph:list, node:int, start:int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf]*node

    dist[start] = 0
    heap = [(0,start)]
    while heap:
        cost,thisNode = heappop(heap)
        for NextCost,NextNode in graph[thisNode]:
            dist_cand = dist[thisNode]+NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode],NextNode))
    return dist
    # dist = [costs to nodes]



from collections import defaultdict
from heapq import heappop, heappush

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, From, To, cost=1):
        self.graph[From].append((To,cost))

    def get_nodes(self):
        return self.graph.keys()

class Dijkstra(object):

    def __init__(self, graph, start):
        self.g = graph.graph
        self.dist = defaultdict(lambda:float('inf'))
        self.dist[start] = 0
        self.prev = defaultdict(lambda: None)
        self.Q = []
        heappush(self.Q,(self.dist[start], start))

        while  self.Q:
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, cost in self.g[u]:
                alt = dist_u + cost
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q,(alt, v))

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]

        return path[::-1]

g = Graph()
N = int(input())
for i in range(N-1):
    u,v,w = map(int,input().split())
    g.add_edge(u-1,v-1,w)
    g.add_edge(v-1,u-1,w)

dijkstra = Dijkstra(g,0)
for i in range(N):
    print(dijkstra.shortest_distance(i)%2)