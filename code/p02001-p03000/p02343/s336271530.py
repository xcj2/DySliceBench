import collections
import itertools
import operator
import sys


class UnionFind:
    def __init__(self):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        parent_getter = operator.itemgetter(1)
        for _, group in itertools.groupby(
                sorted(self.parent.items(), key=parent_getter), parent_getter):
            yield [i for i, _ in group]


sys.stdin.readline()
uf = UnionFind()
for line in sys.stdin:
    com, x, y = map(int, line.split())
    if com == 0:
        uf.unite(x, y)
    elif com == 1:
        print(1 if uf.are_same(x, y) else 0)

