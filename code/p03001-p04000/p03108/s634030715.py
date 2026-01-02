class UnionFind:

    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find_root(self, node):
        parent = self.roots[node]
        if node == parent:
            return node
        else:
            root = self.find_root(parent)
            self.roots[node] = root
            return root

    def union(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        if one_root == other_root:
            return
        if self.ranks[one_root] < self.ranks[other_root]:
            self.roots[one_root] = other_root
            self.sizes[other_root] += self.sizes[one_root]
        else:
            self.roots[other_root] = one_root
            self.sizes[one_root] += self.sizes[other_root]
            if self.ranks[one_root] == self.ranks[other_root]:
                self.ranks[one_root] += 1

    def is_same_group(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        return one_root == other_root

    def size(self, node):
        root = self.find_root(node)
        return self.sizes[root]


def main():
    N, M = list(map(int, input().split(' ')))
    bridges = list()
    for _ in range(M):
        A, B = list(map(int, input().split(' ')))
        A -= 1
        B -= 1
        bridges.append((A, B))
    bridges.reverse()
    tree = UnionFind(N)
    convenience = [0]
    for b in bridges[:-1]:
        one, other = b
        c = convenience[-1]
        if not tree.is_same_group(one, other):
            one_size = tree.size(one)
            other_size = tree.size(other)
            c += one_size * other_size
        convenience.append(c)
        tree.union(one, other)
    convenience.reverse()
    max_c = N * (N - 1) // 2
    for c in convenience:
        print(max_c - c)


if __name__ == '__main__':
    main()