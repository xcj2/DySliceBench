import sys


#https://note.nkmk.me/python-union-find/
class AlgUnionFind():
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


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    ab = [list(map(int, input().rstrip('\n').split())) for _ in range(m)]
    t = n * (n - 1) // 2
    uf = AlgUnionFind(n)
    pt = []
    for i in range(m):
        pt.append(t)
        a, b = ab[-i-1]
        if not uf.same(a-1, b-1):
            t -= (uf.size(a-1) * uf.size(b-1))
        uf.union(a-1, b-1)
    pt.reverse()
    print(*pt, sep="\n")


if __name__ == '__main__':
    solve()
