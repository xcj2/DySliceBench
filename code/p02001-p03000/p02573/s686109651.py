import sys

class UnionFind():
    def __init__(self, n):
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
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def solve():
    readline = sys.stdin.readline
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        A, B = map(int, readline().split())
        A -= 1
        B -= 1
        uf.union(A, B)
    print(-min(uf.parents))


if __name__ == '__main__':
    solve()