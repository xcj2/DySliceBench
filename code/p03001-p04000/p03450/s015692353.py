import sys
input=sys.stdin.readline

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
        P[y]=x

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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def DD(x):
  dis=0
  while x>=0:
    dis=dis+D[x]
    x=P[x]
  return dis

n,m=map(int,input().split())
uf=UnionFind(n)
D=[0]*n
P=[-1]*n
f=0
for i in range(m):
  l,r,d=map(int,input().split())
  l=l-1
  r=r-1
  if uf.find(l)!=uf.find(r):
    if uf.parents[uf.find(l)]<=uf.parents[uf.find(r)]:
      D[uf.find(r)]=DD(l)+d-DD(r)
    else:
      D[uf.find(l)]=DD(r)-d-DD(l)
    uf.union(l,r)
  else:
    if DD(r)-DD(l)!=d:
      f=1
if f==0:
  print("Yes")
else:
  print("No")