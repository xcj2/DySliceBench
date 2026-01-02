import sys
from heapq import heappush, heappop


class Dijkstra:

    class Edge:
        def __init__(self, end, cost):
            self.to = end
            self.cost = cost

    def __init__(self, node_size, inf):
        self._node = node_size
        self._graph = [[] for _ in range(self._node)]
        self.inf = inf
        self.dist = [self.inf for _ in range(self._node)]

    def add_edge(self, st, ed, cs):
        self._graph[st].append(self.Edge(ed, cs))

    def solve(self, start):
        que = []
        self.dist[start] = 0
        heappush(que, (0, start))
        while que:
            cur_cost, cur_vertex = heappop(que)
            if self.dist[cur_vertex] < cur_cost:
                continue
            for e in self._graph[cur_vertex]:
                if self.dist[e.to] > cur_cost + e.cost:
                    self.dist[e.to] = cur_cost + e.cost
                    heappush(que, (self.dist[e.to], e.to))


if __name__ == '__main__':
    V, E, r = map(int, sys.stdin.readline().split())
    dk = Dijkstra(V, 10 ** 10)
    for i in range(E):
        s, t, d = map(int, sys.stdin.readline().split())
        dk.add_edge(s, t, d)
    dk.solve(r)
    for value in dk.dist:
        if value == dk.inf:
            print("INF")
        else:
            print(value)
