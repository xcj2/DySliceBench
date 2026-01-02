
from collections import defaultdict
from heapq import heappop, heappush
import sys
input=sys.stdin.readline

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

ga=Graph()
gb=Graph()
n,m,s,t=map(int,input().split())
for _ in range(m):
    u,v,a,b=map(int,input().split())
    ga.add_edge(u,v,a)
    ga.add_edge(v,u,a)
    gb.add_edge(u,v,b)
    gb.add_edge(v,u,b)

da = Dijkstra(ga,s)
db = Dijkstra(gb,t)
x=[]
for i in range(1,n+1):
    x.append(da.shortest_distance(i)+db.shortest_distance(i))
for i in range(n-2,-1,-1):
    x[i]=min(x[i],x[i+1])
for i in range(n):
    print(10**15-x[i])
