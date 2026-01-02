import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


class WeightedUnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parent = [i for i in range(n_nodes)]
        self.rank = [1] * n_nodes
        self.size = [1] * n_nodes
        # 重みの管理
        self.weight = [0] * n_nodes

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            y = self.find(self.parent[x])
            # 親までの重みを追加していく
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = y
            return self.parent[x]

    def unite(self, x, y, w):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.weight[py] = -w - self.weight[y] + self.weight[x]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.weight[px] = w - self.weight[x] + self.weight[y]
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

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
    Tree = WeightedUnionFind(N)
    for _ in range(M):
        L, R, D = map(int, input().split())
        if Tree.check(L - 1, R - 1):
            if Tree.diff(L - 1, R - 1) == D:
                continue
            else:
                print("No")
                return
        else:
            Tree.unite(L - 1, R - 1, D)
    print("Yes")


if __name__ == "__main__":
    main()
