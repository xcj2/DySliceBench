class UnionFind:
    def __init__(self, num):
        self.parent = [i for i in range(num + 1)]

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 == node2:
            return
        if self.parent[node1] > self.parent[node2]:
            node1, node2 = node2, node1
        self.parent[node2] = node1
        return

    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)


# edges is array which consists of [cost, frm, to] elements
def kruskal(vertex_num, edges):
    ans = 0
    uf = UnionFind(vertex_num)
    # sort edges in cost ascending order
    edges.sort()
    for edge in edges:
        cost, frm, to = edge
        if uf.same(frm, to) is False:
            uf.union(frm, to)
            ans += cost
    return ans


v, e = map(int, input().split())
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append([w, s, t])

print(kruskal(v, edges))


