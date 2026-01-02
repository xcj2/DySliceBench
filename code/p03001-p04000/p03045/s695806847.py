class UnionFind:
    import sys
    sys.setrecursionlimit(100000)

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def root(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.root(self.parents[i])
            return self.parents[i]

    def unite(self, i, j):
        self.parents[self.root(self.parents[i])] = self.root(j)

    def is_unite(self, i, j):
        return self.root(i) == self.root(j)


def solve(N, XYZs):
    uf = UnionFind(N)
    for x, y, z in XYZs:
        uf.unite(x, y)
    return len(set([uf.root(i) for i in range(1, N + 1)]))


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    XYZs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, XYZs))
