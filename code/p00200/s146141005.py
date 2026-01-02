from heapq import heappop, heappush


class WeightedEdge:
    """Weighted edge."""

    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight

    def __repr__(self):
        return "(%d - %d: %d)" % (self.a, self.b, self.weight)

    def __lt__(self, other):
        return self.a < other.b


class EdgeWeightedGraph:
    """Undirected Edge-weighted graph (1-n indexed)."""

    def __init__(self, V):
        self.__adj = [[] for _ in range(V + 1)]

    def add_edge(self, a, b, weight):
        self.__adj[a].append(WeightedEdge(a, b, weight))
        self.__adj[b].append(WeightedEdge(b, a, weight))

    def adj(self, a):
        return self.__adj[a]

    def num_nodes(self):
        return len(self.__adj) - 1


class Dijkstra:
    """Single root shortest path by Dijkstra."""

    def __init__(self, graph, s, t):
        self.dist_to = [float('inf') for _ in range(graph.num_nodes() + 1)]
        self.dist_to[s] = 0
        pq = []
        heappush(pq, (0, s))
        while pq:
            w, a = heappop(pq)
            if a == t:
                return
            if self.dist_to[a] < w:
                continue
            for edge in graph.adj(a):
                if self.dist_to[edge.b] > self.dist_to[a] + edge.weight:
                    self.dist_to[edge.b] = self.dist_to[a] + edge.weight
                    heappush(pq, (self.dist_to[edge.b], edge.b))


if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        g_cost = EdgeWeightedGraph(m)
        g_time = EdgeWeightedGraph(m)
        for _ in range(n):
            a, b, cost, time = map(int, input().split())
            g_cost.add_edge(a, b, cost)
            g_time.add_edge(a, b, time)

        k = int(input())
        for _ in range(k):
            p, q, r = map(int, input().split())
            if r == 0:
                fw_cost = Dijkstra(g_cost, p, q)
                ans = fw_cost.dist_to[q]
            else:
                fw_time = Dijkstra(g_time, p, q)
                ans = fw_time.dist_to[q]
            print(ans)