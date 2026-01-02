from sys import stdin
nii=lambda:map(int,stdin.readline().split())

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

  def same(self, x, y):
    return self.find(x) == self.find(y)

n,m=nii()
p=list(nii())

uf=UnionFind(n)

for i in range(m):
  x,y=nii()
  x-=1
  y-=1
  uf.union(x,y)

cnt=0
for i in range(n):
  if not uf.same(i,p[i]-1):
    cnt+=1

print(n-cnt)