def kruskal(edges):
    edges.sort(key=lambda pair:pair[2])
    uf_tree = UnionFindTree(n_node)
    total_cost = 0
    for i, j, cost in edges:
        if cost < 0:
            continue

        if not uf_tree.have_same_root(i, j):
            uf_tree.unite(i, j)
            total_cost += cost
    return total_cost


class UnionFindTree:
    def __init__(self, n_node):
        self.parent = [i for i in range(n_node)]
        self.rank = [0] * n_node

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def have_same_root(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    n_node = int((input()))
    edges = []
    for i in range(n_node):
        for j, cost in enumerate(map(int, input().split())):
            edges.append((i, j, cost))

    print(kruskal(edges))





