import sys


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

    def connected_count(self):
        return sum(x < 0 for x in self.table)


n, m, q = list(map(int, input().split()))
uft = UnionFind(n)
hyper_paths = set()

for line in sys.stdin:
    a, b, c = list(map(int, line.split()))
    if c == 1:
        hyper_paths.add((a, b))
        continue
    uft.union(a, b)

for a, b in hyper_paths:
    if uft.find(a, b):
        print('No')
        exit()

cc = uft.connected_count()

min_m = n if len(hyper_paths) > 0 else n - 1
max_m = n - cc + cc * (cc - 1) // 2

print('Yes' if min_m <= m <= max_m else 'No')
