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

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M, *AB = map(int, read().split())
uf = UnionFind(N)
ans = [N * (N - 1) // 2]

for a, b in zip(AB[-2:0:-2], AB[-1:1:-2]):
    a -= 1
    b -= 1
    if uf.same(a, b):
        ans.append(ans[-1])
    else:
        ans.append(ans[-1] - uf.parents[uf.find(a)] * uf.parents[uf.find(b)])
        uf.union(a, b)

print(*reversed(ans), sep='\n')
