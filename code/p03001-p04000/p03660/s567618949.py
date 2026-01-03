from collections import defaultdict
from heapq import heappop, heappush
from math import ceil

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

N = int(input())
g = Graph()

for _ in range(N-1):
    a,b = map(int,input().split())
    g.add_edge(a,b)
    g.add_edge(b,a)

dij = Dijkstra(g,1)
path = dij.shortest_path(N)
c1 = path[ceil(len(path)/2)-1]
c2 = path[ceil(len(path)/2)]

g.graph[c1] = [(to,cost) for to,cost in g.graph[c1] if to != c2]
g.graph[c2] = [(to,cost) for to,cost in g.graph[c2] if to != c1]

dij = Dijkstra(g,1)
f = 0
for i in range(1,N):
    if dij.shortest_distance(i) != float('inf'):
        f += 1
if f > N-f:
    print('Fennec')
else:
    print('Snuke')