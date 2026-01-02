n = int(input())
xy=[list(map(int,input().split())) for i in range(n)]
from collections import defaultdict
x_d = defaultdict(list)
y_d = defaultdict(list)
for i in range(n):
    x,y = xy[i]
    x_d[x].append(i)
    y_d[y].append(i)

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
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
uf = UnionFind(n)
for k in x_d.keys():
    if len(x_d[k])==1:
        continue
    last=x_d[k][0]
    for itm in x_d[k]:
        uf.union(last, itm)
        last=itm

for k in y_d.keys():
    if len(y_d[k])==1:
        continue
    last=y_d[k][0]
    for itm in y_d[k]:
        uf.union(last, itm)
        last=itm
ans=0
for root in uf.roots():
    mems = uf.members(root)
    xset=set()
    yset=set()
    for m in mems:
        x,y=xy[m]
        xset.add(x)
        yset.add(y)
    points = len(xset)*len(yset)
    points -= len(mems)
    ans+=points
print(ans)