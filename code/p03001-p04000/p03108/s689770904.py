class Union_Find:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.height = [0 for i in range(N)]
        self.size = [1 for i in range(N)]
    def Find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.Find(self.par[x])
        return self.par[x]
    def Size(self, x):
        return self.size[self.Find(x)]
    def Union(self, x, y):
        x, y = self.Find(x), self.Find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1
    def Same(self, x, y):
        return self.Find(x) == self.Find(y)

from collections import defaultdict
N, M = map(int, input().split())
bs, res, uf, y, dic = [], [], Union_Find(N), N * (N - 1) // 2, defaultdict(int)
for _ in range(M):
    bs.append(list(map(lambda x: int(x) - 1, input().split())))
for b in bs[::-1]:
    res.append(y)
    if not uf.Same(b[0], b[1]):
        y -= uf.Size(b[0]) * uf.Size(b[1])
    uf.Union(b[0], b[1])
for r in res[::-1]:
    print(r)
