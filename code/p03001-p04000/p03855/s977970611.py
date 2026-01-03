from itertools import product
from collections import defaultdict as dd

class UFT(object):
  def __init__(self,n):
    self.parent={i:i for i in range(1,n+1)}
    self.height={i:0 for i in range(1,n+1)}
  def find(self,a):
    if self.parent[a]!=a:
      self.parent[a]=self.find(self.parent[a])
    return self.parent[a]
  def unite(self,a,b):
    a=self.find(a)
    b=self.find(b)
    if self.height[a]>self.height[b]:
      self.parent[b]=a
    else:
      if self.height[a]==self.height[b]:
        self.height[b]+=1
      self.parent[a]=b
  def isunited(self,a,b):
    return self.find(a)==self.find(b)


n,k,l=map(int,input().split())
uk=UFT(n)
ul=UFT(n)
dc=dd(int)
du={}

for _ in range(k):
  a,b=map(int,input().split())
  uk.unite(a,b)

for _ in range(l):
  a,b=map(int,input().split())
  ul.unite(a,b)
  
for i in range(1,n+1):
  du[i]=(uk.find(i),ul.find(i))
  dc[du[i]]+=1

print(*(dc[du[i]] for i in range(1,n+1)))
