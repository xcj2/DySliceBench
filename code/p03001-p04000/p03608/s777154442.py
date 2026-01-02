import heapq
import itertools


class Graph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.edges = [[] for _ in range(n_nodes)]

    def add_edge(self, s, t, d=None, undirected=False):
        if d is not None:
            self.edges[s].append((t, d))
        else:
            self.edges[s].append(t)
        if undirected:
            self.add_edge(t, s, d)

    def add_edges(self, edges, undirected=False):
        for edge in edges:
            self.add_edge(*edge, undirected=undirected)


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def compute_all(self, s):
        distances = [float('inf') for _ in range(self.graph.n_nodes)]
        visited = [False for _ in range(self.graph.n_nodes)]
        prev_nodes = [None for _ in range(self.graph.n_nodes)]
        distances[s] = 0
        q = []
        for t in range(self.graph.n_nodes):
            heapq.heappush(q, (distances[t], t))
        while q:
            dist_x, x = heapq.heappop(q)
            if visited[x]:
                continue
            visited[x] = True

            for y, d_xy in self.graph.edges[x]:
                if visited[y]:
                    continue
                dist_y = dist_x + d_xy
                if dist_y < distances[y]:
                    distances[y] = dist_y
                    prev_nodes[y] = x
                    heapq.heappush(q, (dist_y, y))
        return distances, prev_nodes


n, m, r = map(int, input().split())
rs = list(map(int, input().split()))

graph = Graph(n + 1)
graph.add_edges([list(map(int,
                          input().split())) for _ in range(m)],
                undirected=True)
dijkstra = Dijkstra(graph)
distances = []
for i in range(n + 1):
    ds, _ = dijkstra.compute_all(i)
    distances.append(ds)
res = float('inf')
for perm in itertools.permutations(rs):
    s = sum([distances[a][b] for a, b in zip(perm, perm[1:])])
    res = min(res, s)
print(res)