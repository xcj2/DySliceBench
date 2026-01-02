import array, collections

Edge = collections.namedtuple("Edge", "start end weight")

class UnionFind(object):
    def __init__(self, number_of_nodes):
        self.par = array.array("L", range(number_of_nodes))
        self.rank = array.array("L", (0 for _ in range(number_of_nodes)))

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x == y:
            pass
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def compute_mst_kruskal(v_size, edges):
    edges.sort(key=lambda e: e.weight)
    uf = UnionFind(v_size)
    mst = []
    for edge in edges:
        if not uf.in_the_same_set(edge.start, edge.end):
            uf.unite(edge.start, edge.end)
            mst.append(edge)

    return mst


edges = []
v, e = map(int, input().split())
for _ in range(e):
  edges.append(Edge(*map(int, input().split())))
print(sum(e.weight for e in compute_mst_kruskal(v, edges)))

