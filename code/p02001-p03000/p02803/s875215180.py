import heapq
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]


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

    def compute(self, s, t):
        distances = [float('inf') for _ in range(self.graph.n_nodes)]
        visited = [False for _ in range(self.graph.n_nodes)]
        prev_nodes = [None for _ in range(self.graph.n_nodes)]
        distances[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        while q:
            dist_x, x = heapq.heappop(q)
            if x == t:
                return distances, prev_nodes

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


h, w = ril()
ls = rss(h)
graph = Graph(h * w)
for i in range(h):
    for j in range(w):
        if ls[i][j] == '.':
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < h and 0 <= nj < w and ls[ni][nj] == '.':
                    graph.add_edge(i * w + j, ni * w + nj, 1, True)
dijkstra = Dijkstra(graph)
res = 0
for i in range(h):
    for j in range(w):
        if ls[i][j] == '.':
            distances, _ = dijkstra.compute_all(i * w + j)
            res = max(res, max(d for d in distances if d < float('inf')))
print(res)