import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.color = [[0] * 2 for _ in range(n)]
        for i in range(n):
            y, x = divmod(i, w)
            if s[y][x] == '#':
                self.color[i][1] = 1
            else:
                self.color[i][0] = 1

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
        self.color[x][0] += self.color[y][0]
        self.color[x][1] += self.color[y][1]

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


h, w = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(h)]
uf = UnionFind(h * w)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for y, ss in enumerate(s):
    for x, sss in enumerate(ss):
        for dy, dx in move:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < w and 0 <= yy < h and sss != s[yy][xx]:
                uf.union(yy * w + xx, y * w + x)
print(sum(uf.color[root][0] * uf.color[root][1] for root in uf.roots()))
