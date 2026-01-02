n,m = map(int, input().split())
a = list(map(int, input().split()))
xy=[list(map(int,input().split())) for i in range(m)]

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
for x,y in xy:
    uf.union(x,y)

g=uf.group_count()

if g==1:
    print(0)
    exit()

if n<(g-1)*2:
    print("Impossible")
    exit()

ans=0
all_costs=[]

from collections import defaultdict
costs=defaultdict(list)
for i in range(n):
    costs[uf.find(i)].append(a[i])

for k,v in costs.items():
    v.sort()
    ans+=v[0]
    all_costs.extend(v[1:])

all_costs.sort()
ans+=sum(all_costs[:(g-2)])

print(ans)
