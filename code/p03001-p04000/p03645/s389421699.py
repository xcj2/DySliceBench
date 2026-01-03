import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())


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

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


g = Graph()
for i in range(M):
    a, b = map(int, input().split())
    g.add_edge(a - 1, b - 1)
    g.add_edge(b - 1, a - 1)
d = Dijkstra(g, 0)
if d.shortest_distance(N - 1) == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
