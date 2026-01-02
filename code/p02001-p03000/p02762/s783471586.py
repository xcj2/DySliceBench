import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
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
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

def resolve():
    N, M, K = lr()
    uf = UnionFind(N)
    fr = [0]*N
    for i in range(M):
        a, b = lr()
        uf.union(a-1, b-1)
        fr[a-1] += 1
        fr[b-1] += 1
    ans = [uf.size(x) - fr[x] - 1 for x in range(N)]
    for i in range(K):
        c, d = lr()
        if uf.same(c-1, d-1):
            ans[c-1] -= 1
            ans[d-1] -= 1
    print(*ans, sep=' ')
resolve()