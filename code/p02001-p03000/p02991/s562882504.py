from collections import defaultdict
from heapq import heappop, heappush


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
        self.g = graph.graph
        self.dist = defaultdict(lambda: 10 ** 18)
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



n,m = map(int, input().split())
uv = [list(map(int, input().split())) for i in range(m)]
s,t = map(int, input().split())
g = Graph()
for u,v in uv:
  g.add_edge(u*3-3,v*3-2)
  g.add_edge(u*3-2,v*3-1)
  g.add_edge(u*3-1,v*3-3)
dist = Dijkstra(g,(s-1)*3)
ans = dist.shortest_distance((t-1)*3)
if ans == 10 ** 18:
  print(-1)
else:
  print(ans // 3)