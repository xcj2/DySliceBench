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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


from itertools import permutations
from math import sqrt
import heapq
while 1:
    N = int(input())
    if N==0:
        break
    uf = UnionFind(N)
    Vs = [list(map(float, input().split())) for _ in range(N)]
    lis = [i for i in range(N)]
    Edges = []
    for a, b in permutations(lis, 2):
        x1, y1, z1, r1 = Vs[a]
        x2, y2, z2, r2 = Vs[b]
        d = max(0, sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)-r1-r2)
        Edges.append((d, a, b))
    heapq.heapify(Edges)
    ans = 0
    while Edges:
        d, a, b = heapq.heappop(Edges)
        if not uf.same(a, b):
            ans += d
            uf.union(a, b)
    print('{:.3f}'.format(ans))
