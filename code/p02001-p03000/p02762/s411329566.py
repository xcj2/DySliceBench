import sys
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
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

    def is_same(self, x, y):
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


N, M, K = map(int, readline().split())

uf = UnionFind(N)
f = [0] * N
bl = [0] * N

for _ in range(M):
    a, b = map(int1, readline().split())
    f[a] += 1
    f[b] += 1
    uf.unite(a, b)

for i in range(K):
    c, d = map(int1, readline().split())
    if uf.find(c) == uf.find(d):
        bl[c] += 1
        bl[d] += 1

ans = [0] * N

for i in range(N):
    ans[i] = uf.size(i) - f[i] - bl[i] - 1

print(*ans)
