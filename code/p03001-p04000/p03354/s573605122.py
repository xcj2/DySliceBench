import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0 for _ in range(n)]

    def get_root(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.get_root(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        x = self.get_root(x)
        y = self.get_root(y)
        if x != y:
            if self.ranks[x] < self.ranks[y]:
                self.parents[x] = y
            else:
                self.parents[y] = x
                if self.ranks[x] == self.ranks[y]:
                    self.ranks[x] += 1


n, m = ril()
ps = ril()
ls = rils(m)

uf = UnionFind(n)
for a, b in ls:
    uf.merge(a - 1, b - 1)
res = 0
for i in range(n):
    p0 = uf.get_root(i)
    p1 = uf.get_root(ps[i] - 1)
    if p0 == p1:
        res += 1
print(res)