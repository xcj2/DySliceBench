from itertools import combinations
from collections import Counter
class UnionFind():
  def __init__(self, x):
    self.x=x
    self.root=[-1]*(N+1)
    self.rnk=[0]*(N+1)
  
  def Find_root(self, x):
    if self.root[x]<0:
      return x
    else:
      self.root[x]=self.Find_root(self.root[x])
      return self.root[x]
    
  def Unite(self, x, y):
    x = self.Find_root(x)
    y = self.Find_root(y)
    if x==y:
      return
    elif self.rnk[x]>self.rnk[y]:
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if self.rnk[x]==self.rnk[y]:
        self.rnk[y]+=1
  
  def isSameGroup(self, x, y):
    return self.Find_root(x)==self.Find_root(y)
  
  def Count(self, x):
    return -self.root[self.Find_root(x)]
N,K,L=map(int,input().split())
u1=UnionFind(N)
u2=UnionFind(N)
for _ in range(K):
  x,y=map(int,input().split())
  u1.Unite(x-1,y-1)
for _ in range(L):
  x,y=map(int,input().split())
  u2.Unite(x-1,y-1)
l=[]
for i in range(N):
  l.append((u1.Find_root(i), u2.Find_root(i)))
c = Counter(l)
ans = []
for i in range(N):
  ans.append(c[(u1.Find_root(i), u2.Find_root(i))])
print(*ans)

