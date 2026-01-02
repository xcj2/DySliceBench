class UnionFind:
    """Union-Find: O(α(N))"""

    __slots__ = ["_data_size", "_first_idx", "_parents"]

    def __init__(self, data_size: int, is_zero_origin: bool = True) -> None:
        self._data_size = data_size
        self._first_idx = 0 if is_zero_origin else 1
        self._parents = [-1] * (data_size + self._first_idx)

    def _find(self, x: int) -> int:
        if self._parents[x] < 0:
            return x
        self._parents[x] = self._find(self._parents[x])
        return self._parents[x]

    def is_connected(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are connected or not."""
        return self._find(x) == self._find(y)

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self._find(x), self._find(y)
        if x == y:
            return
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x


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
