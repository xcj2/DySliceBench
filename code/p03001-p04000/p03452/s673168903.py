class WeightedUnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.weights = [0 for _ in range(n + 1)]
        self.ranks = [0 for _ in range(n + 1)]

    def find_root(self, node):
        parent_node = self.parents[node]
        if node == parent_node:
            return node
        else:
            root_node = self.find_root(parent_node)
            # reduction
            self.parents[node] = root_node
            self.weights[node] += self.weights[parent_node]
            return root_node

    def union(self, one, other, weight):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        if one_root == other_root:
            return
        one_rank = self.ranks[one_root]
        other_rank = self.ranks[other_root]
        diff_weight = weight + self.weights[one] - self.weights[other]
        if one_rank < other_rank:
            self.parents[one_root] = other_root
            # modify weight s.t. weight(one) + weight = weight(other)
            self.weights[one_root] -= diff_weight
        else:
            self.parents[other_root] = one_root
            # modify weight s.t. weight(one) + weight = weight(other)
            self.weights[other_root] += diff_weight
            if one_rank == other_rank:
                self.ranks[other_root] += 1

    def is_same_group(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        return one_root == other_root

    def diff(self, one, other):
        if not self.is_same_group(one, other):
            return None
        return self.weights[other] - self.weights[one]


def main():
    N, M = list(map(int, input().split(' ')))
    tree = WeightedUnionFind(N)
    for _ in range(M):
        L, R, D = list(map(int, input().split(' ')))
        d = tree.diff(L, R)
        if d is None:
            tree.union(L, R, D)
            continue
        # print(tree.parents)
        # print(tree.weights)
        if d != D:
            print('No')
            exit(0)
    print('Yes')


if __name__ == '__main__':
    main()
