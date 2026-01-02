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
    n, m = map(int, input().split())
    bridge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    answer = [n * (n - 1) // 2 for _ in range(m)]
    uf = UnionFind(n)
    is_same_before = False
    size_a = 0
    size_b = 0
    for i in range(-1, -m - 1, -1):
        a, b = bridge[i]
        if i < -1:
            answer[i] = answer[i + 1]
            if not is_same_before:
                answer[i] -= size_a * size_b
        is_same_before = uf.is_same(a, b)
        if not is_same_before:
            size_a = uf.get_size(a)
            size_b = uf.get_size(b)
        uf.union(a, b)
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()

