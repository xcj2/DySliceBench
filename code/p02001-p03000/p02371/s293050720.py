#!/usr/bin/env python3
# GRL_5_A: Tree - Diameter of a Tree


class Edge:
    __slots__ = ('v', 'w')

    def __init__(self, v, w):
        self.v = v
        self.w = w

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        else:
            return self.v


class WeightedEdge(Edge):
    __slots__ = ('v', 'w', 'weight')

    def __init__(self, v, w, weight):
        super().__init__(v, w)
        self.weight = weight


class Graph:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, e):
        self._edges[e.v].append(e)
        self._edges[e.w].append(e)

    def adj(self, v):
        return self._edges[v]

    def edges(self):
        for es in self._edges:
            for e in es:
                yield e


def diameter(graph):
    def dfs(s):
        visited = [False] * graph.v
        weights = [0] * graph.v
        stack = [(s, 0)]
        while stack:
            v, weight = stack.pop()
            if not visited[v]:
                visited[v] = True
                weights[v] = weight
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        stack.append((w, weight + e.weight))
        return weights

    v0 = 0
    ws0 = dfs(v0)
    v1 = max((wg, v) for v, wg in enumerate(ws0))[1]
    ws1 = dfs(v1)
    v2 = max((wg, v) for v, wg in enumerate(ws1))[1]

    return max(ws0[v2], ws1[v2])


def run():
    n = int(input())
    g = Graph(n)

    for _ in range(n-1):
        s, t, w = [int(i) for i in input().split()]
        g.add(WeightedEdge(s, t, w))

    print(diameter(g))


if __name__ == '__main__':
    run()

