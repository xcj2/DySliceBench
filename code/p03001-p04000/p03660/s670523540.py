import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    def __init__(self, graph, start):
        g = graph.graph

        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0
        self.prev = defaultdict(lambda: None)

        Q = []
        heappush(Q, (self.dist[start], start))

        while Q:
            dist_u, u = heappop(Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(Q, (alt, v))

    def shortest_distance(self, goal):
        return self.dist[goal]


g = Graph()
for _ in range(N - 1):
    a, b = map(int, input().split())
    g.add_edge(a - 1, b - 1)
    g.add_edge(b - 1, a - 1)

d1 = Dijkstra(g, 0)
d2 = Dijkstra(g, N - 1)

cnt1, cnt2 = 0, 0
for i in range(1, N - 1):
    x = d1.shortest_distance(i)
    y = d2.shortest_distance(i)
    if x <= y:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 > cnt2:
    print('Fennec')
else:
    print('Snuke')
