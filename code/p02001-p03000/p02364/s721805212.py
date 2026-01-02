import sys


class UnionFind:

    def __init__(self, nvertices):
        self.rank = [1] * (nvertices + 5)
        self.p = [i for i in range(nvertices + 5)]

    def find_set(self, u):
        if u != self.p[u]:
            self.p[u] = self.find_set(self.p[u])
        return self.p[u]

    def unite(self, u, v):
        x = self.find_set(u)
        y = self.find_set(v)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_connected(self, u, v):
        return self.find_set(u) == self.find_set(v)


def main():
    sys.setrecursionlimit(int(1e5))
    nvertices, nedges = map(int, input().split())
    edges = []
    for i in range(nedges):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort(key=lambda e: e[0])
    ans = 0
    uf = UnionFind(nvertices)
    for w, u, v in edges:
        if not uf.is_connected(u, v):
            uf.unite(u, v)
            ans += w

    print(ans)


main()