# ABC120D - Decayed Bridges
class UnionFind:
    __slots__ = ["size", "first_idx", "parents"]

    def __init__(self, size: int, first_index: int = 0) -> None:
        self.size = size
        self.first_idx = first_index
        self.parents = [-1] * (size + first_index)

    def find(self, x: int) -> int:
        """Find the group (root) of vertex x"""
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def is_same(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are in the same group or not."""
        return self.find(x) == self.find(y)

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self.find(x), self.find(y)
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def get_size(self, x: int) -> int:
        """Get the size of the group vertex x belongs"""
        return self.parents[self.find(x)]

    @property
    def groups(self) -> int:
        """Return the number of groups."""
        return len({self.find(x) for x in range(self.first_idx, self.size + self.first_idx)})


def main():
    N, M, *AB = map(int, open(0).read().split())
    uf = UnionFind(N, 1)
    current_unreachable = N * (N - 1) // 2
    ans = []
    for a, b in zip(*[iter(AB[::-1])] * 2):
        ans.append(current_unreachable)
        if not uf.is_same(a, b):
            current_unreachable -= uf.get_size(a) * uf.get_size(b)
        uf.unite(a, b)
    print("\n".join(map(str, ans[::-1])))


if __name__ == "__main__":
    main()
