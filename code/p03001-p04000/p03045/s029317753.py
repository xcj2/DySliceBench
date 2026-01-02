class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.rank = 0


class DisjointSet:
    def __init__(self, nodes):
        self.nodes = nodes

    def find_set(self, key):
        pivot = self.nodes[key]
        while pivot.key != pivot.parent.key:
            pivot = pivot.parent
        self.nodes[key].parent = pivot
        return pivot.key

    def same(self, x, y):
        return self.find_set(x) == self.find_set(y)

    def unite(self, x, y):
        y_root = self.find_set(y)
        x_root = self.find_set(x)
        if self.nodes[x].rank > self.nodes[y].rank:
            self.nodes[y_root].parent = self.nodes[x_root]
        elif self.nodes[x].rank < self.nodes[y].rank:
            self.nodes[x_root].parent = self.nodes[y_root]
        else:
            self.nodes[x_root].parent = self.nodes[y_root]
            self.nodes[y_root].rank = self.nodes[y_root].rank + 1


N, M = [int(i) for i in input().split()]
nodes = [Node(i) for i in range(N)]
for node in nodes:
    node.parent = node
ds = DisjointSet(nodes)

for _ in range(M):
    x, y, z = [int(i) for i in input().split()]
    x -= 1
    y -= 1
    if ds.same(x, y):
        pass
    else:
        ds.unite(x, y)
ans = len(set([ds.find_set(i) for i in range(N)]))
print(ans)
