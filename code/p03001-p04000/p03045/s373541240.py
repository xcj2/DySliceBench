import sys

input = sys.stdin.readline


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
    N, M = [int(x) for x in input().split()]
    XYZ = [[int(x) for x in input().split()] for _ in range(M)]

    u = UnionFind(N + 2)

    f = True
    for x, y, z in XYZ:
        x += 1
        y += 1
        if z % 2 == 0:
            u.union(x, y)
        else:
            if f:
                f = False
                u.union(x, 0)
                u.union(y, 1)
            if u.same(x, 0):
                u.union(y, 1)
            if u.same(x, 1):
                u.union(y, 0)
            if u.same(y, 0):
                u.union(x, 1)
            if u.same(y, 1):
                u.union(x, 0)

    for x, y, z in XYZ:
        x += 1
        y += 1
        if z % 2 == 1:
            u.union(x, y)
        else:
            if f:
                f = False
                u.union(x, 0)
                u.union(y, 1)
            if u.same(x, 0):
                u.union(y, 1)
            if u.same(x, 1):
                u.union(y, 0)
            if u.same(y, 0):
                u.union(x, 1)
            if u.same(y, 1):
                u.union(x, 0)

    print(u.group_count())


if __name__ == '__main__':
    main()
