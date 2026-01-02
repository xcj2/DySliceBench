# Undirected Graph


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


def articulation_points(graph):
    visited = [0] * graph.v
    low = [0] * graph.v
    parent = [-1] * graph.v

    s = 0
    children = 0
    visit = 0
    stack = [s]
    vs = set()

    while stack:
        v = stack.pop()
        if not visited[v]:
            visit += 1
            visited[v] = visit
            low[v] = visit

        for e in graph.adj(v):
            w = e.other(v)
            if not visited[w]:
                parent[w] = v
                if v == s:
                    children += 1
                stack.append(v)
                stack.append(w)
                break
            elif w != parent[v]:
                low[v] = min(low[v], visited[w])
        else:
            u = parent[v]
            if u < 0:
                pass
            elif parent[u] < 0:
                if children > 1:
                    vs.add(u)
            else:
                if low[v] >= visited[u]:
                    vs.add(u)
                low[u] = min(low[u], low[v])

    return vs


def run():
    v, e = [int(i) for i in input().split()]
    graph = Graph(v)

    for _ in range(e):
        s, t = [int(i) for i in input().split()]
        edge = Edge(s, t)
        graph.add(edge)

    for v in sorted(articulation_points(graph)):
        print(v)


if __name__ == '__main__':
    run()

