import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parent = [i for i in range(n_nodes)]
        self.rank = [1] * n_nodes
        self.size = [1] * n_nodes

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_parent_list(self):
        return [i for i in range(self.n_nodes) if self.find(i) == i]

    def get_n_groups(self):
        return len(self.get_parent_list())

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    N, M = map(int, input().split())
    UF = UnionFind(N)
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        UF.unite(X - 1, Y - 1)
    print(UF.get_n_groups())


if __name__ == "__main__":
    main()
