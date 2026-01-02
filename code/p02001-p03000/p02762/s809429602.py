class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find_root(self, node):
        parent_node = self.parents[node]
        if parent_node == node:
            return node
        else:
            root_node = self.find_root(parent_node)
            self.parents[node] = root_node  # reduction
            return root_node

    def is_same_group(self, one_node, other_node):
        one_root = self.find_root(one_node)
        other_root = self.find_root(other_node)
        return one_root == other_root

    def union(self, one_node, other_node):
        one_root = self.find_root(one_node)
        other_root = self.find_root(other_node)
        if one_root == other_root:
            return
        one_rank = self.ranks[one_root]
        other_rank = self.ranks[other_root]
        if one_rank < other_rank:
            self.parents[one_root] = other_root
            self.sizes[other_root] += self.sizes[one_root]
        else:
            self.parents[other_root] = one_root
            self.sizes[one_root] += self.sizes[other_root]
            if one_rank == other_rank:
                self.ranks[one_root] += 1

    def group_size(self, node):
        root_node = self.find_root(node)
        return self.sizes[root_node]


def main():
    N, M, K = list(map(int, input().split(' ')))
    non_suggested_users = [[] for _ in range(N)]
    friend_tree = UnionFind(N)
    for _ in range(M):
        a, b = list(map(int, input().split(' ')))
        one_user = a - 1
        other_user = b - 1
        friend_tree.union(one_user, other_user)
        non_suggested_users[one_user].append(other_user)
        non_suggested_users[other_user].append(one_user)
    for _ in range(K):
        c, d = list(map(int, input().split(' ')))
        one_user = c - 1
        other_user = d - 1
        if friend_tree.is_same_group(one_user, other_user):
            non_suggested_users[one_user].append(other_user)
            non_suggested_users[other_user].append(one_user)
    answer_list = list()
    for user in range(N):
        ans = friend_tree.group_size(user) - len(non_suggested_users[user]) - 1
        answer_list.append(str(ans))
    print(' '.join(answer_list))


if __name__ == '__main__':
    main()