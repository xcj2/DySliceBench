from itertools import permutations, product
from collections import defaultdict
from heapq import heappop, heappush

N, M, R = map(int, input().split())
r = [int(x) for x in input().split()]
abc = [[int(x) for x in input().split()] for _ in range(M)]


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
for a, b, c in abc:
    g.add_edge(a - 1, b - 1, c)
    g.add_edge(b - 1, a - 1, c)

D = dict()
for ri in r:
    D[ri - 1] = Dijkstra(g, ri - 1)

ans = float('inf')
for route in permutations(r):
    d = 0
    for i in range(R - 1):
        s = route[i] - 1
        g = route[i + 1] - 1
        d += int(D[s].shortest_distance(g))
    ans = min(ans, d)
print(ans)