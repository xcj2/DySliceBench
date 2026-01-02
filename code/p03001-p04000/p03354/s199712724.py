# ABC097D - Equals (ARC097D)
class UnionFind:
    __slots__ = ["_data_size", "_first_index", "_parents"]

    def __init__(self, data_size: int, is_zero_indexed: bool = True) -> None:
        self._data_size = data_size
        self._first_index = 0 if is_zero_indexed else 1
        self._parents = [-1] * (data_size + self._first_index)

    def find(self, x: int) -> int:
        """Find the group (root) of vertex x"""
        if self._parents[x] < 0:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def is_same(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are in the same group or not."""
        return self.find(x) == self.find(y)

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x


def main():
    N, _, *PXY = map(int, open(0).read().split())
    P, XY = PXY[:N], PXY[N:]
    uf = UnionFind(N, is_zero_indexed=False)
    for x, y in zip(*[iter(XY)] * 2):
        uf.unite(x, y)
    ans = sum(uf.is_same(i, p) for i, p in enumerate(P, 1))
    print(ans)


if __name__ == "__main__":
    main()
