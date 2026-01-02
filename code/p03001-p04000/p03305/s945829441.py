import heapq
import collections


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph = [[] for i in range(size)]

    def add_edge(self, source, target, cost):
        self.graph[source].append((target, cost))

    def add_bidirectional_edge(self, source, target, cost):
        self.add_edge(source, target, cost)
        self.add_edge(target, source, cost)

    def min_dist_dijkstra(self, s):
        dist = [float('inf')] * self.size
        dist[s] = 0
        q = [(0, s)]
        while q:
            d, v = heapq.heappop(q)
            if dist[v] < d:
                continue
            for t, c in self.graph[v]:
                if dist[t] > dist[v] + c:
                    dist[t] = dist[v] + c
                    heapq.heappush(q, (dist[t], t))
        return dist

    def __str__(self):
        res = ''
        for i in range(self.size):
            res += str(i)
            for t, d in self.graph[i]:
                res += ' ' + str(t) + '(' + str(d) + ')'
            res += '\n'
        return res


def main():
    n, m, s, t = map(int, input().split())
    graph_a = Graph(n + 1)
    graph_b = Graph(n + 1)

    for i in range(m):
        u, v, a, b = map(int, input().split())
        graph_a.add_bidirectional_edge(u, v, a)
        graph_b.add_bidirectional_edge(u, v, b)
    cost_a = graph_a.min_dist_dijkstra(s)
    cost_b = graph_b.min_dist_dijkstra(t)

    min_costs = [(n + 1, float('inf'))]
    for i in range(n, 0, -1):
        cost = cost_a[i] + cost_b[i]
        if cost < min_costs[-1][1]:
            min_costs.append((i, cost))
    year = 0
    for i in range(n):
        while min_costs[-1][0] <= i:
            min_costs.pop()
        print(10**15 - min_costs[-1][1])


if __name__ == '__main__':
    main()
