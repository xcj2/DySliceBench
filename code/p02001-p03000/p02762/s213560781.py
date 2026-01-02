def main():
    import sys
    buf = sys.stdin.buffer

    class UnionFind:
        def __init__(self, size):
            self.parent = [-1] * size
            self.rank = [1] * size

        def get_root(self, node):
            parent = self.parent[node]
            if parent == -1:
                root = node
            else:
                root = self.get_root(parent)
                self.parent[node] = root  # 同じnodeへの2回目以降のget_rootを高速にするために、直接rootに繋いでおく
            return root

        def in_same_group(self, node1, node2):
            root1 = self.get_root(node1)
            root2 = self.get_root(node2)
            return root1 == root2

        def unite(self, node1, node2):
            if self.in_same_group(node1, node2):
                return
            main_root = self.get_root(node1)
            sub_root = self.get_root(node2)
            if self.rank[main_root] < self.rank[sub_root]:  # rankの大きい方をmain_rootにする
                main_root, sub_root = sub_root, main_root

            self.parent[sub_root] = main_root
            self.rank[main_root] += self.rank[sub_root]

    n, m, k = map(int, buf.readline().split())
    uf = UnionFind(n)
    minus_count = [1] * n

    query = list(map(int, buf.read().split()))
    follows = query[:2*m]
    blocks = query[2*m:]

    for a, b in zip(follows[0::2], follows[1::2]):
        uf.unite(a-1, b-1)
        minus_count[a-1] += 1
        minus_count[b-1] += 1

    for a, b in zip(blocks[0::2], blocks[1::2]):
        if uf.in_same_group(a-1, b-1):
            minus_count[a-1] += 1
            minus_count[b-1] += 1

    result = [uf.rank[uf.get_root(i)] - minus_count[i] for i in range(n)]
    print(*result)


if __name__ == '__main__':
    main()