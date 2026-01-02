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


def bridges(graph):
    def visit(v, e):
        nonlocal n
        w = e.other(v)
        if not visited[w]:
            parent[w] = v
            n += 1
            visited[w] = n
            low[w] = n
            return True
        elif w != parent[v]:
            low[v] = min(low[v], visited[w])
            return False

    def leave(p, e):
        c = e.other(p)
        if p == parent[c] and low[c] > visited[p]:
            es.append(e)
        low[p] = min(low[p], low[c])
        return False

    visited = [0] * graph.v
    low = [0] * graph.v
    parent = [-1] * graph.v
    es = []

    s = 0
    n = 1
    visited[s] = n
    low[s] = n
    stack = [(s, e, visit) for e in graph.adj(s)]

    while stack:
        v, e, func = stack.pop()
        # print(v, e.v, e.w, func.__name__, visited, low)
        if func(v, e):
            stack.append((v, e, leave))
            w = e.other(v)
            for ne in graph.adj(w):
                stack.append((w, ne, visit))

    return es


def run():
    v, e = [int(i) for i in input().split()]
    g = Graph(v)

    for _ in range(e):
        s, t = [int(i) for i in input().split()]
        g.add(Edge(s, t))

    edges = [(e.v, e.w) if e.v < e.w else (e.w, e.v)
             for e in bridges(g)]

    for v, w in sorted(edges):
        print(v, w)


if __name__ == '__main__':
    run()

