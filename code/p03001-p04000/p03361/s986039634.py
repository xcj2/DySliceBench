import sys


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
    H, W = map(int, input().split())
    Grid = [list(input()) for _ in range(H)]

    uf = UnionFind(H * W)
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(H):
        for j in range(W):
            if Grid[i][j] == '#':
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx <= H - 1 and 0 <= ny <= W - 1:
                        if Grid[nx][ny] == '#':
                            uf.union(i * W + j, nx * W + ny)
    ans = True

    for k, v in uf.all_group_members().items():
        i, j = k // W, k % W
        if Grid[i][j] == '#' and len(v) == 1:
            ans = False
            break

    if ans:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
