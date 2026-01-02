from collections import defaultdict


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


def resolve():
    n, m, k = map(int, input().split())
    u = UnionFind(n)
    d = defaultdict(int)
    e = defaultdict(int)
    for _ in range(m):
        a, b = [int(x) - 1 for x in input().split()]
        u.union(a, b)
        d[a] += 1
        d[b] += 1
    for _ in range(k):
        a, b = [int(x) - 1 for x in input().split()]
        if u.same(a, b):
            e[a] += 1
            e[b] += 1
    ans = [0] * n
    for i in range(n):
        ans[i] = u.size(i) - 1 - d[i] - e[i]
    print(*ans)


if __name__ == '__main__':
    resolve()
