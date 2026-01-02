import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m = list(map(int, readline().split()))
    ab = [list(map(int, readline().split())) for _ in range(m)]
    ans = [0] * m
    uf = UnionFind(n)
    inconvenience = (n * (n - 1)) // 2

    for i in range(m - 1, -1, -1):
        ans[i] = inconvenience
        u, v = ab[i]
        u, v = u - 1, v - 1
        if uf.same(u, v):
            pass
        else:
            x, y = uf.size(u), uf.size(v)
            inconvenience -= x * y
            uf.union(u, v)

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
