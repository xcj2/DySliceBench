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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

from copy import deepcopy

n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]

cnt=0
for i in range(m):
  uf=UnionFind(n)
  ll=deepcopy(l)
  del ll[i]
  for a,b in ll:
    a-=1
    b-=1
    uf.union(a,b)
  if uf.group_count()>=2:
    cnt+=1
print(cnt)