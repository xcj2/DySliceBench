from typing import Set


class UnionFind:
    """Union Find (Disjoint Set): O(α(N))
    References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/dsu.hpp
        https://tumoiyorozu.github.io/single-file-ac-library/document_en/dsu.html
    """

    __slots__ = ["_data_size", "_first_idx", "_roots"]

    def __init__(self, data_size: int, is_zero_origin: bool = True) -> None:
        self._data_size = data_size
        self._first_idx = 0 if is_zero_origin else 1
        self._roots = [-1] * (data_size + self._first_idx)

    # def __getitem__(self, x: int) -> int:
    #     """Find the group (root) of vertex x."""
    #     while self._roots[x] >= 0:
    #         x = self._roots[x]
    #     return x

    def __len__(self) -> int:
        """Count the number of groups (roots)."""
        return len(self.groups)

    @property
    def groups(self) -> Set[int]:
        """Return the set of groups (roots)."""
        return {
            self._find(x)
            for x in range(self._first_idx, self._data_size + self._first_idx)
        }

    def _find(self, x: int) -> int:
        while self._roots[x] >= 0:
            x = self._roots[x]

        return x

    def is_connected(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are connected or not."""
        return self._find(x) == self._find(y)

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self._find(x), self._find(y)
        if x == y:
            return
        if self._roots[x] > self._roots[y]:
            x, y = y, x
        self._roots[x] += self._roots[y]
        self._roots[y] = x

    def unite_all(self, *vertices: int) -> None:
        """Unite the groups of all of the given vertices."""
        x = vertices[0]
        for y in vertices[1:]:
            self.unite(x, y)

    def get_size(self, x: int) -> int:
        """Return the size of the group vertex x belongs."""
        return -self._roots[self._find(x)]


def unionfind():
    # https://judge.yosupo.jp/problem/unionfind
    # https://atcoder.jp/contests/practice2/tasks/practice2_a
    N, Q, *TUV = map(int, open(0).read().split())
    tree = UnionFind(N)
    res = []
    for t, u, v in zip(*[iter(TUV)] * 3):
        if t:
            res.append(int(tree.is_connected(u, v)))
        else:
            tree.unite(u, v)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    unionfind()
