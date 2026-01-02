from collections import defaultdict
from heapq import heappop, heappush

YEN = 10**15
INF = float('inf')


class Graph:
    def __init__(self):
        self.__graph = defaultdict(list)

    def add_edge(self, source, destination, cost):
        self.__graph[source].append((destination, cost))
        self.__graph[destination].append((source, cost))

    @property
    def graph(self):
        return self.__graph


class Dijkstra:
    def __init__(self, graph, source):
        self.__costs = defaultdict(lambda: INF)
        costs = self.__costs
        costs[source] = 0
        g = graph.graph
        q = []
        heappush(q, (costs[source], source))

        while q:
            cp, p = heappop(q)
            if costs[p] < cp:
                continue
            for dst, cost in g[p]:
                alternative = cp + cost
                if costs[dst] > alternative:
                    costs[dst] = alternative
                    heappush(q, (alternative, dst))

    def minimum_cost(self, destination):
        return self.__costs[destination]


def spline(func_=int, iter_=None):
    if iter_ is None:
        iter_ = input().split()
    return map(func_, iter_)


def main():
    n, m, s, t = spline()
    g_yen = Graph()
    g_snuuk = Graph()
    for _ in range(m):
        u, v, cost, b = spline()
        g_yen.add_edge(u, v, cost)
        g_snuuk.add_edge(u, v, b)
    d_s = Dijkstra(g_yen, s)
    d_t = Dijkstra(g_snuuk, t)
    costs = [0] * n
    costs[-1] = YEN - d_s.minimum_cost(n) - d_t.minimum_cost(n)
    for i in range(n - 2, -1, -1):
        cost = YEN - d_s.minimum_cost(i + 1) - d_t.minimum_cost(i + 1)
        costs[i] = max(cost, costs[i + 1])
    for cost in costs:
        print(cost)


if __name__ == "__main__":
    main()
