#!/usr/bin/env python3


# Union find
class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = list(range(N))

    def root(self, x):
        path_to_root = []
        while self.parent[x] != x:
            path_to_root.append(x)
            x = self.parent[x]
        for node in path_to_root:
            self.parent[node] = x  # パス圧縮
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        self.parent[self.root(x)] = self.root(y)

    def __str__(self):
        groups = {}
        for x in range(self.N):
            root = self.root(x)
            if root in groups.keys():
                groups[root].append(x)
            else:
                groups[root] = [x]
        result = ""
        for root in groups.keys():
            result += str(groups[root]) + "\n"
        return result


# Kruscal法: 最小全域木
# num_vertices: int
# edges=(vertex1, vertex2, weight): List[int, int, int]
# edgesについて破壊的
def kruskal(num_vertices, edges):
    total_weight = 0
    edges.sort(key=lambda e: e[2])
    u = UnionFind(num_vertices)
    for e in edges:
        x = e[0]
        y = e[1]
        weight = e[2]
        if u.same(x, y):
            continue
        u.unite(x, y)
        total_weight += weight
    return total_weight


n = int(input())
edges = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i, n):
        if row[j] != -1:
            edges.append([i, j, row[j]])
print(kruskal(n, edges))

