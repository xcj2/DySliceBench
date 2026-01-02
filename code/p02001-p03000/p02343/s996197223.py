# Disjoint Set
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_A


class UnionFind:
    __slots__ = ["_size", "_first_index", "_parents"]

    def __init__(self, size: int, is_zero_indexed: bool = True) -> None:
        self._size = size
        self._first_index = 0 if is_zero_indexed else 1
        self._parents = [-1] * (size + self._first_index)

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

    def get_size(self, x: int) -> int:
        """Get the size of the group vertex x belongs"""
        return -self._parents[self.find(x)]

    @property
    def groups(self) -> int:
        """Return the number of groups."""
        return len({self.find(x) for x in range(self._first_index, self._size + self._first_index)})


def main():
    N, Q = map(int, input().split())
    uf = UnionFind(N)
    ans = []
    for _ in range(Q):
        com, x, y = map(int, input().split())
        if com:
            ans.append(uf.is_same(x, y) * 1)
        else:
            uf.unite(x, y)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()

