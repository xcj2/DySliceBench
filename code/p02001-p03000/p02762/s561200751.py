class UnionFind:
    def __init__(self, node):
        self.parent = [-1 for _ in range(node)]

    def find(self, target):
        if self.parent[target] < 0:
            return target
        else:
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parent[root_x] > self.parent[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x

    def get_size(self, x):
        return -self.parent[self.find(x)]


def main():
    users, friend_pairs, block_pairs = map(int, input().split())
    answer = [0] * users
    user_relationship = UnionFind(users)
    friend = [[] for _ in range(users)]
    for _ in range(friend_pairs):
        a, b = map(lambda x: int(x) - 1, input().split())
        user_relationship.union(a, b)
        friend[a].append(b)
        friend[b].append(a)
    for _ in range(block_pairs):
        c, d = map(lambda x: int(x) - 1, input().split())
        if user_relationship.is_same(c, d):
            answer[c] -= 1
            answer[d] -= 1
    for i in range(users):
        answer[i] += user_relationship.get_size(i) - 1 - len(friend[i])
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()

