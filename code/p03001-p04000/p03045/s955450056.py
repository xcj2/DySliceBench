import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_parent_list(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def get_n_groups(self):
        return len(self.get_parent_list())


def main():
    N, M = map(int, input().split())
    tree = UnionFind(N)
    for _ in range(M):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        tree.unite(x, y)
    n_groups = tree.get_n_groups()
    print(n_groups)


if __name__ == "__main__":
    main()
