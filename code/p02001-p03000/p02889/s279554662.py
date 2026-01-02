import sys

input = sys.stdin.readline


def read_i():
    return list(map(int, input().split()))


class Graph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.edges = [[float('inf')] * n_nodes for _ in range(n_nodes)]

    def add_edge(self, s, t, d):
        self.edges[s][t] = d
        self.edges[t][s] = d


class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        self.distances = [[float('inf')] * graph.n_nodes
                          for _ in range(graph.n_nodes)]
        self._init()

    def _init(self):
        for x in range(self.graph.n_nodes):
            self.distances[x][x] = 0
        for source in range(self.graph.n_nodes):
            for destination, distance in enumerate(self.graph.edges[source]):
                self.distances[source][destination] = distance

    def compute_shortest_path_lengths(self):
        for k in range(self.graph.n_nodes):
            for i in range(self.graph.n_nodes):
                for j in range(self.graph.n_nodes):
                    s = self.distances[i][k] + self.distances[k][j]
                    if s < self.distances[i][j]:
                        self.distances[i][j] = s
        return self.distances


n, m, l = read_i()
graph = Graph(n)
for _ in range(m):
    a, b, c = read_i()
    if c > l:
        continue
    graph.add_edge(a - 1, b - 1, c)
fw = FloydWarshall(graph)
ds = fw.compute_shortest_path_lengths()

graph = Graph(n)
for s in range(n):
    for t in range(n):
        if s >= t:
            continue
        if ds[s][t] > l:
            continue
        graph.add_edge(s, t, 1)
fw = FloydWarshall(graph)
ds = fw.compute_shortest_path_lengths()

q = int(input())
for _ in range(q):
    s, t = read_i()
    s -= 1
    t -= 1
    d = ds[s][t] - 1
    if d == float('inf'):
        print(-1)
    else:
        print(d)