class UnionFind:
    __slots__ = ["_data_size", "_roots"]

    def __init__(self, N):
        self._data_size = N
        self._roots = [-1] * N

    def __getitem__(self, x: int) -> int:
        while self._roots[x] >= 0:
            x = self._roots[x]
        return x

    def unite(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        elif self._roots[y] < self._roots[x]:
            x, y = y, x
        self._roots[x] += self._roots[y]
        self._roots[y] = x

    def is_connected(self, x, y):
        return self[x] == self[y]


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
