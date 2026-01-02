import sys
sys.setrecursionlimit(10**5)
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
        self.weight = [0]*(n+1)
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            r = self.Find_Root(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = r
            return r
    def GetWeight(self, x):
        self.Find_Root(x)
        return self.weight[x]
    def Unite(self, x, y, w):
        w += self.GetWeight(x)
        w -= self.GetWeight(y)
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return False
        if self.rnk[x] < self.rnk[y]:
            x, y = y, x
            w = -w
        if self.rnk[x] == self.rnk[y]:
            self.rnk[x] += 1
        self.root[y] = x
        self.weight[y] = w
        return True
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    def Count(self, x):
        return -self.root[self.Find_Root(x)]
    def Diff(self, x, y):
        return self.GetWeight(y) - self.GetWeight(x)

N, M = map(int, input().split())
uf = UnionFind(N+1)
for _ in range(M):
    l, r, d = map(int, input().split())
    if not uf.isSameGroup(l, r):
        uf.Unite(l, r, d)
    else:
        if uf.Diff(l, r) != d:
            print('No')
            exit()

print('Yes')
