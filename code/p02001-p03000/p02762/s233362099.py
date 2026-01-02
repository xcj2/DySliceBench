# D - Friend Suggestions
class UnionFind:
    __slots__ = ["_size", "_first_idx", "_parents"]

    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [-1] * (size + first_index)

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


def main():
    N, M, K, *ABCD = map(int, open(0).read().split())
    AB, CD = ABCD[:2 * M], ABCD[2 * M:]
    relationships = UnionFind(N, 1)
    friends, blocked = [0] * (N + 1), [0] * (N + 1)
    for a, b in zip(*[iter(AB)] * 2):
        relationships.unite(a, b)
        friends[a] += 1
        friends[b] += 1
    for c, d in zip(*[iter(CD)] * 2):
        if relationships.is_same(c, d):
            blocked[c] += 1
            blocked[d] += 1
    ans = [relationships.get_size(i) - friends[i] - blocked[i] - 1 for i in range(1, N + 1)]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
