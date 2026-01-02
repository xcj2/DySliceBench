import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class WeightedUnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

        # 親への重みを管理
        self.weights = [0] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            parent = self.find(self.parents[x])
            # 親への重みを追加しながら根まで走査
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = parent
            return parent

    # xからyへの重みがw
    def unite(self, x, y, w):
        w += self.weights[x]
        w -= self.weights[y]
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w *= -1

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weights[y] = w
        return

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへの重みの取得
    def get_weight(self, x, y):
        return self.weights[y] - self.weights[x]

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_parent_list(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def get_n_groups(self):
        return len(self.get_parent_list())

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    N, M = map(int, input().split())
    tree = WeightedUnionFind(N)
    flag = True
    for _ in range(M):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1
        if not tree.is_same(l, r):
            tree.unite(l, r, d)
        else:
            if tree.get_weight(l, r) == d:
                continue
            else:
                flag = False

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
