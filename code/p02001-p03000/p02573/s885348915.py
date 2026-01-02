import sys
sys.setrecursionlimit(10**7)

N,Q = map(int,input().split())
class UF():
  def __init__(self,par,rank):
    self.par = par
    self.rank = rank
  def find(self,x):
      if self.par[x] == x:
          return x
      else:
          self.par[x] = self.find(self.par[x]) #経路圧縮
          return self.par[x]
  def same(self,x,y):
      return self.find(x) == self.find(y)
  def unite(self,x,y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
          return 0
      if self.rank[x] < self.rank[y]:
          self.par[x] = y
      else:
          self.par[y] = x
          if self.rank[x]==self.rank[y]:self.rank[x]+=1
uf=UF([i for i in range(N)],[0]*(N+1))
for _ in range(Q):
  a,b=map(int,input().split())
  a,b=a-1,b-1
  uf.unite(a,b)
from collections import Counter
a=[-1]*N
for i in range(N):
  a[i]=uf.find(i)
ca=Counter(a)
ans=0
for c in ca.values():
  ans=max(ans,c)
print(ans)
