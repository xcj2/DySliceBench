import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.root(x)]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():

    N, K, L = map(int, input().split())
    highway = UnionFind(N)
    railroad = UnionFind(N)

    for _ in range(K):
        a, b = map(int, input().split())
        highway.unite(a - 1, b - 1)

    for _ in range(L):
        a, b = map(int, input().split())
        railroad.unite(a - 1, b - 1)

    d = defaultdict(int)
    for i in range(N):
        d[highway.root(i), railroad.root(i)] += 1
    print(*(d[highway.root(i), railroad.root(i)] for i in range(N)))


if __name__ == '__main__':
    main()
