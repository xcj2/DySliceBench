import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes

        # self.parents[x] < 0 の時，xが根である．
        # また，xが根の時，(-1) * (同一グループの要素数) が格納されるようになる.
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

        # 常にxの方が要素数が多くなるように，スワップする
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 要素数の少ない方のグループを，要素数が多い方の木に貼る．
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

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
    P = list(map(lambda x: int(x) - 1, input().split()))
    tree = UnionFind(N)
    for _ in range(M):
        x, y = map(lambda x: int(x) - 1, input().split())
        tree.unite(x, y)

    ans = 0
    for i in range(N):
        if tree.is_same(i, P[i]):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
