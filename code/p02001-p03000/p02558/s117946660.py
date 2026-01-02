class UnionFind:
    __slots__ = ["_data_size", "_roots"]

    def __init__(self, data_size: int) -> None:
        self._data_size = data_size
        self._roots = [-1] * data_size

    def __getitem__(self, x: int) -> int:
        while self._roots[x] >= 0:
            x = self._roots[x]
        return x

    def is_connected(self, x: int, y: int) -> bool:
        return self[x] == self[y]

    def unite(self, x: int, y: int) -> None:
        x, y = self[x], self[y]
        if x == y:
            return
        if self._roots[x] > self._roots[y]:
            x, y = y, x
        self._roots[x] += self._roots[y]
        self._roots[y] = x


def main():
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


if __name__ == "__main__":
    main()
