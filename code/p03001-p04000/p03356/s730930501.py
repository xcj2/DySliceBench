class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.ranks = [0 for _ in range(n + 1)]

    def find_root(self, node):
        parent_node = self.parents[node]
        if node == parent_node:
            return node
        else:
            root_node = self.find_root(parent_node)
            self.parents[node] = root_node  # reduction
            return root_node

    def union(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        if one_root == other_root:
            return
        one_rank = self.ranks[one_root]
        other_rank = self.ranks[other_root]
        if one_rank < other_rank:
            self.parents[one_root] = other_root
        else:
            self.parents[other_root] = one_root
            if one_rank == other_rank:
                self.ranks[other_root] += 1

    def is_same_group(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        return one_root == other_root


def main():
    N, M = list(map(int, input().split(' ')))
    p = list(map(int, input().split(' ')))
    tree = UnionFind(N)
    for _ in range(M):
        x, y = list(map(int, input().split(' ')))
        tree.union(p[x - 1], p[y - 1])
    answer = 0
    for i in range(1, N + 1):
        if tree.is_same_group(i, p[i - 1]):
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()