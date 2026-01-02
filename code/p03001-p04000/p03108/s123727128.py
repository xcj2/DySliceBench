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

from sys import stdin
nii=lambda:list(map(int,stdin.readline().split()))

n,m=map(int,input().split())
l=[nii() for i in range(m)]
l=list(reversed(l))

uf=UnionFind(n)

ans=[]
num=n*(n-1)//2
for a,b in l:
  a-=1
  b-=1
  ans.append(num)
  if uf.same(a,b)==False:
    num-=uf.size(a)*uf.size(b)
    uf.union(a,b)

for i in reversed(ans):
  print(i)