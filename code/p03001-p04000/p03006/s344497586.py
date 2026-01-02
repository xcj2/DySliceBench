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
    from itertools import combinations
    n = int(readline())
    mat = [list(map(int, readline().split())) for _ in range(n)]

    if n == 1:
        return print(1)

    ans = INF
    for com in combinations(range(n), r=2):
        first, second = com
        dx = mat[first][0] - mat[second][0]
        dy = mat[first][1] - mat[second][1]
        uf = UnionFind(n)
        for i in range(n):
            cx, cy = mat[i]
            for j in range(n):
                nx, ny = mat[j]
                if (cx - nx == dx and cy - ny == dy) or (-cx + nx == dx and - cy + ny == dy):
                    uf.union(i, j)
        ans = min(ans, uf.group_count())

    print(ans)


if __name__ == '__main__':
    main()
