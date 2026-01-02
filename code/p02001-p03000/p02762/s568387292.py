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
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    friend = [[] for _ in range(n)]
    answer = [-1 for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        uf.union(a, b)
        friend[a].append(b)
        friend[b].append(a)
    for _ in range(k):
        c, d = map(lambda x: int(x) - 1, input().split())
        if uf.is_same(c, d):
            answer[c] -= 1
            answer[d] -= 1
    for i in range(n):
        answer[i] += uf.get_size(i) - len(friend[i])
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()

