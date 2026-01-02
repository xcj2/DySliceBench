def main():
    import sys
    from operator import itemgetter
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

    query = map(int, buf.read().split())

    def gen():
        for num in query:
            yield num

    generator = gen()
    for _ in range(m):
        a, b = generator.__next__(), generator.__next__()
        uf.unite(a-1, b-1)
        minus_count[a-1] += 1
        minus_count[b-1] += 1

    for i in range(k):
        a, b = generator.__next__(), generator.__next__()
        if uf.in_same_group(a-1, b-1):
            minus_count[a-1] += 1
            minus_count[b-1] += 1

    result = []
    for i in range(n):
        parent = uf.get_root(i)
        count = uf.rank[parent]
        ans = count - minus_count[i]
        result.append(ans)

    print(*result)

if __name__ == '__main__':
    main()