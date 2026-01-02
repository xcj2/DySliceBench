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


import sys

readline = sys.stdin.buffer.readline

N, Q = map(int, readline().split())
tree = UnionFind(N)
res = []
for _ in range(Q):
    t, u, v = map(int, readline().split())
    if t:
        res.append(int(tree.is_connected(u, v)))
    else:
        tree.unite(u, v)
print("\n".join(map(str, res)))
