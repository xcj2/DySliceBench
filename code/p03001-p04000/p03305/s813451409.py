from heapq import heappush, heappop
from collections import defaultdict

n, m, s, t = map(int, input().split())
y = 10**15


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))


class Dijkstra(object):
    def __init__(self, graph, start):
        self.g = graph.graph

        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

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
                    heappush(self.Q, (alt, v))


yen_g = Graph()
sno_g = Graph()
for _ in range(m):
    u, v, a, b = map(int, input().split())
    yen_g.add_edge(u, v, a)
    yen_g.add_edge(v, u, a)
    sno_g.add_edge(u, v, b)
    sno_g.add_edge(v, u, b)

cost = [0] * n
yen_d = Dijkstra(yen_g, s)
sno_d = Dijkstra(sno_g, t)
for i in range(1, n + 1):
    cost[i - 1] = y - (yen_d.dist[i] + sno_d.dist[i])

ans = [y] * n
ans[n - 1] = cost[n - 1]
for i in range(n - 2, -1, -1):
    ans[i] = max(ans[i + 1], cost[i])

for a in ans:
    print(a)
