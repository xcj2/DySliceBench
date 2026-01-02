
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
n,m,s,t=map(int,input().split())



en=Graph()
snu=Graph()

for i in range(m):
    u,v,a,b=map(int,input().split())
    en.add_edge(u,v,a)
    en.add_edge(v,u,a)
    snu.add_edge(u,v,b)
    snu.add_edge(v,u,b)

enen=Dijkstra(en,s)
snusnu=Dijkstra(snu,t)
ans=[enen.shortest_distance(n)+snusnu.shortest_distance(n)]

for i in range(n-1,0,-1):
    d1=enen.shortest_distance(i)
    d2=snusnu.shortest_distance(i)
    ans.append(min(ans[-1],d1+d2))


for i in range(1,n+1):
    print(10**15-ans[-i])
