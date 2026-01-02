
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

##* union-find
##pre union_find
class UnionFind:
    def __init__(self, node_count):
        self.group_count = node_count
        self.par = [-1] * node_count
    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    def connect(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        self.group_count -= 1
        if self.par[y] < self.par[x]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def get_size(self, x):
        return -self.par[self.root(x)]
    def get_groupsize(self):
        return self.group_count


n,m=getints()
uf = UnionFind(n)

for i in range(m):
    x,y,_=getints()
    uf.connect(x-1,y-1)

print(uf.group_count)
