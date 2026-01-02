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
        return (i for i in range(self.n) if self.find(i) == root)

    def roots(self):
        return (i for i, x in enumerate(self.parents) if x < 0)

    def group_count(self):
        return len(self.roots())

    def sizes(self):
        return {x: self.size(x) for x in self.roots()}

    def all_group_members(self):
        d = {}
        for i in range(self.n):
            p = self.find(i)
            d[p] = d.get(p, []) + [i]
        return d

    def __str__(self):
        return '\n'.join('{}: {}'.format(k, v) for k, v in self.all_group_members().items())


def resolve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    u = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        u.union(a - 1, b - 1)
    ans = 0
    for i in u.sizes().values():
        ans = max(i, ans)
    print(ans)


if __name__ == '__main__':
    resolve()
