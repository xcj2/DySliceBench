class UnionFind:
    def __init__(self, n: int):
        self.nodes = n
        self.parents = [-1] * n
        self.rank = [0] * n

    # retrun the root of element x
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # unite the group include element x and group include element y
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # get size of the gourp which element x belongs
    def get_size(self, x):
        return -self.parents[self.find(x)]

    # check if element x and element y is same group
    def same(self, x, y):
        return self.find(x) == self.find(y)


def kruskal(n: int, edges: list):
    """
    n: count of nodes
    edges: list of edges, format: (node1,node2,weight)
    """
    union = UnionFind(n + 1)  # 1-indexed
    mst_sum = 0
    mst = []
    for edge in edges:
        n1, n2, w = edge
        if not union.same(n1, n2):
            union.unite(n1, n2)
            mst_sum += w
            mst.append(edge)
    return mst, mst_sum


n = int(input())
graph_table = []

for _ in range(n):
    graph_table.append([int(i) for i in input().split()])

edges = []
# edge一覧を取得
for i in range(n - 1):
    for j in range(i + 1, n):
        if graph_table[i][j] != -1:
            edges.append((i, j, graph_table[i][j]))  # node1,node2,weight

# edgeを重みの昇順にソート
edges = sorted(edges, key=lambda x: x[2])

_, mst_sum = kruskal(n, edges)
print(mst_sum)

