class WeightedUnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.level = [0] * n
        self.weight = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            px = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = px
            return px

    def union(self, x, y, w):
        px = self.find(x)
        py = self.find(y)
        if self.level[px] < self.level[py]:
            self.par[px] = py
            self.weight[px] = -self.weight[x] + self.weight[y] + w
        else:
            self.par[py] = px
            self.weight[py] = + self.weight[x] - self.weight[y] - w
            if self.level[px] == self.level[py]:
                self.level[px] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

def solve(N, M):
    wuf = WeightedUnionFind(N+1)
    for i in range(M):
        L, R, D = map(int, input().split())
        if wuf.same(L, R):
            if wuf.diff(L, R) != D:
                return False
        else:
            wuf.union(L, R, D)
    return True

N, M = map(int, input().split())
if solve(N, M):
    print("Yes")
else:
    print("No")
