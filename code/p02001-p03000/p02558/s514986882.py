from typing import List


class UnionFind:
    """Union Find (Disjoint Set): O(α(N))
    References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/dsu.hpp
        https://tumoiyorozu.github.io/single-file-ac-library/document_en/dsu.html
    """

    __slots__ = ["_data_size", "_roots"]

    def __init__(self, data_size: int) -> None:
        self._data_size = data_size
        self._roots = [-1] * data_size

    def __getitem__(self, x: int) -> int:
        """Find the group (root) of vertex x in O(α(n)) amortized."""
        while self._roots[x] >= 0:
            x = self._roots[x]
        return x

    def __len__(self) -> int:
        """Count the number of groups (roots)."""
        return len(self.groups)

    @property
    def groups(self) -> List[int]:
        """Return the set of groups (roots) in O(n)."""
        return [i for i, r in enumerate(self._roots) if r < 0]

    def is_connected(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are connected in O(α(n)) amortized."""
        return self[x] == self[y]

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y in O(α(n)) amortized."""
        x, y = self[x], self[y]
        if x == y:
            return
        if self._roots[x] > self._roots[y]:
            x, y = y, x
        self._roots[x] += self._roots[y]
        self._roots[y] = x

    def get_size(self, x: int) -> int:
        """Return the size of the group where vertex x belongs in O(α(n)) amortized."""
        return -self._roots[self[x]]


def unionfind():
    # https://judge.yosupo.jp/problem/unionfind
    # https://atcoder.jp/contests/practice2/tasks/practice2_a
    import sys

    read = sys.stdin.buffer.read

    N, Q, *TUV = map(int, read().split())
    tree = UnionFind(N)
    res = []
    for t, u, v in zip(*[iter(TUV)] * 3):
        if t:
            res.append(int(tree.is_connected(u, v)))
        else:
            tree.unite(u, v)
    print("\n".join(map(str, res)))


def arc032_b():
    # https://atcoder.jp/contests/arc032/tasks/arc032_2
    N, M, *AB = map(int, open(0).read().split())
    tree = UnionFind(N + 1)
    for a, b in zip(*[iter(AB)] * 2):
        tree.unite(a, b)
    print(len(tree) - 2)


if __name__ == "__main__":
    unionfind()
    # arc032_b()
