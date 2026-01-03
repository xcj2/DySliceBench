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

from math import ceil
g = Graph()
N = int(input())
for i in range(N-1):
    a,b = map(int,input().split())
    g.add_edge(a,b)
    g.add_edge(b,a)

d = Dijkstra(g,1)
path = d.shortest_path(N)
n = ceil(len(path)/2)
flist = path[:n]
slist = path[n:]
a = flist[-1]
b = slist[0]
g.graph[a].pop(g.graph[a].index((b,1)))
g.graph[b].pop(g.graph[b].index((a,1)))
d = Dijkstra(g,1)
f = len(d.dist)
s = N-f

if f > s:
    print('Fennec')
else:
    print('Snuke')