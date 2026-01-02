class UnionFindTree:
    """
        Disjoint set data structure
        Union-Find tree
        complexity:
            init: O(n)
            find, unite, same: O(alpha(n))
    """
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


class Kruskal:
    """
        Kruskal's algorithm: find Minimum Spanning Tree
        complexity:
            O(E logV)
    """
    def __init__(self, V, E, start=0, INF=10**9):
        """
        :param V: the number of vertices
        :param E:  adjacency list (undirected graph)
        :param start:
        :param INF:
        """
        self.kruskal(V, E)

    def kruskal(self, V, E):
        edges = []
        for v1 in range(V):
            for v2, cost in E[v1]:
                if v1 < v2:
                    edges.append((cost, v1, v2))
        edges.sort(reverse=True)
        self.mincost = 0
        self.min_spanning_tree = []
        uf = UnionFindTree(V)
        while len(self.min_spanning_tree) < V - 1:
            cost, v1, v2 = edges.pop()
            if not uf.same(v1, v2):
                self.mincost += cost
                uf.unite(v1, v2)
                self.min_spanning_tree.append((v1, v2, cost))

    def min_cost(self):
        return self.mincost

    def get_min_spanning_tree(self):
        return sorted(self.min_spanning_tree)


V = int(input())
edges = [[] for _ in range(V)]
for i in range(V):
    for j, d in enumerate(map(int, input().split())):
        if d != -1:
            edges[i].append((j, d))
mst = Kruskal(V, edges)
print(mst.min_cost())
