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

    @property
    def costs(self):
        return self.__costs


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
    d_s = Dijkstra(g_yen, s).costs
    d_t = Dijkstra(g_snuuk, t).costs
    costs = [0] * n
    min_cost = INF
    for i in range(n, 0, -1):
        min_cost = min(min_cost, d_s[i] + d_t[i])
        costs[i - 1] = min_cost
    for cost in map(lambda x: YEN - x, costs):
        print(cost)


if __name__ == "__main__":
    main()
