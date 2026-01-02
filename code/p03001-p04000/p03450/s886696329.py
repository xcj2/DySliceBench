class WeightedUnionFind:
    def __init__(self, n):
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
        self.weight = [0]*(n+1)
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            y = self.Find_Root(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = y
            return y
    def Weigh(self, x):
        self.Find_Root(x)
        return self.weight[x]
    def Diff(self, x, y):
        return self.Weigh(y) - self.Weigh(x)
    #y - x = w
    def Unite(self, x, y, w):
        w += self.Weigh(x) - self.Weigh(y)
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            if w==0:
                return
            else:
                print('No')
                exit()
        else:
            if self.rnk[x] < self.rnk[y]:
                x, y = y, x
                w = -w
            self.root[x] += self.root[y]
            self.root[y] = x
            self.weight[y] = w
            if self.rnk[x] == self.rnk[y]:
                self.rnk[x] += 1
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    def Size(self, x):
        return -self.root[self.Find_Root(x)]

import sys
input = sys.stdin.readline
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
uf=WeightedUnionFind(n)
for x in l:
    uf.Unite(x[0],x[1],x[2])
print('Yes')