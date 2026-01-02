from typing import Set


class UnionFind:
    """Union-Find: O(α(N))"""

    __slots__ = ["_data_size", "_first_idx", "_parents"]

    def __init__(self, data_size: int, is_zero_origin: bool = True) -> None:
        self._data_size = data_size
        self._first_idx = 0 if is_zero_origin else 1
        self._parents = [-1] * (data_size + self._first_idx)

    def __getitem__(self, x: int) -> int:
        """Find the group (root) of vertex x."""
        while self._parents[x] >= 0:
            x = self._parents[x]

        return x

    def __len__(self) -> int:
        """Count the number of groups (roots)."""
        return len(self.groups)

    @property
    def groups(self) -> Set[int]:
        """Return the set of groups (roots)."""
        return {
            self[x] for x in range(self._first_idx, self._data_size + self._first_idx)
        }

    def is_connected(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are connected or not."""
        return self[x] == self[y]

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self[x], self[y]
        if x == y:
            return
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x

    def unite_all(self, *vertices: int) -> None:
        """Unite the groups of all of the given vertices."""
        x = vertices[0]
        for y in vertices[1:]:
            self.unite(x, y)

    def get_size(self, x: int) -> int:
        """Return the size of the group vertex x belongs."""
        return -self._parents[self[x]]


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
