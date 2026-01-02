def xC2(x):
    if x == 1:
        return 0
    else:
        return x * (x-1) // 2

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
            return 0

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        nx, ny = - self.parents[x],  - self.parents[y]

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return xC2(nx + ny) - xC2(nx) - xC2(ny)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.reverse()
ans = [xC2(n)]

uf = UnionFind(n)
for a, b in ab:
    ans.append(ans[-1] - uf.union(a-1, b-1))

ans.reverse()

for ai in ans[1:]:
    print(ai)
