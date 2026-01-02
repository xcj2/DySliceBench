
from collections import defaultdict
from heapq import heappop, heappush


class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra():

    def __init__(self, graph, start):
        self.g = graph.graph

        self.dist = defaultdict(lambda: float("inf"))
        self.dist[start] = 0

        self.prev = defaultdict(lambda: None)

        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            dist_u, u = heappop(self.Q)

            if self.dist[u] < dist_u:
                continue

            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):

        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal

        while node is not None:
            path.append(node)
            node = self.prev[node]

        return path[::-1]


import sys
input=sys.stdin.readline
n,m=map(int,input().split())
g=Graph()

for _ in range(m):
    l,r,c=map(int,input().split())
    g.add_edge(l,r,c)
for i in range(2,n+1):
    g.add_edge(i,i-1,0)


d = Dijkstra(g,1)
ans=d.shortest_distance(n)
print(ans if ans!=float("inf") else -1)
