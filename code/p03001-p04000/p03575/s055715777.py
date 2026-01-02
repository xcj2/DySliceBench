import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


class UnionFind:
    # Reference: https://note.nkmk.me/python-union-find/
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


def main():
    N, M = map(int, readline().split())
    AB = [[int(s) - 1 for s in line.split()] for line in readlines()]

    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        for j, (a, b) in enumerate(AB):
            if i == j:
                continue
            uf.union(a, b)
        if uf.group_count() > 1:
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
