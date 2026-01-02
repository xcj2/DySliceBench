class UnionFind:
    def __init__(self, size):
        self.parents = [-1] * size

    def find(self, x):
        while self.parents[x] > 0:
            x = self.parents[x]
        return x

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        if self.parents[pi] < self.parents[pj]:
            pi, pj = pj, pi
            i, j = j, i
        self.parents[pi] += self.parents[pj]
        self.parents[pj] = pi
        self.reconnect(j, pi)

    def reconnect(self, i, j):
        while self.parents[i] > 0:
            t = self.parents[i]
            self.parents[i] = j
            i = t


def main():
    n, m, *ab, = map(int, open(0).read().split())
    uf = UnionFind(n + 1)

    for i, j in zip(ab[::2], ab[1::2]):
        uf.union(i, j)

    print(-min(uf.parents))


if __name__ == '__main__':
    main()
