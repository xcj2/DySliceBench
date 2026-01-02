import sys
from collections import defaultdict

class UnionFind(object):
  def __init__(self,n):
    self.table=[-1]*N

  def find(self,x):
    parent=self.table[x]
    if parent<0:
      return x
    else:
      root=self.find(parent)
      self.table[x]=root
      return root

  def union(self,a,b):
    root1=self.find(a)
    root2=self.find(b)
    if root1<root2:
      self.table[root1]+=self.table[root2]
      self.table[root2]=root1
    else:
      self.table[root2]+=self.table[root1]
      self.table[root1]=root2

N,M=map(int,input().split())
A=[int(i) for i in input().split()]
uf=UnionFind(N)
for i in range(M):
  x,y=map(int,input().split())
  uf.union(x,y)
groups=defaultdict(list)
for j in range(N):
  groups[uf.find(j)].append(A[j])

groups = [sorted(g, reverse=True) for g in groups.values()]

if len(groups) == 1:
  print(0)
  sys.exit()

ans=0
cnt=[]
for group in groups:
  ans+=group.pop()
  cnt+=group

if len(groups)-2 > len(cnt):
  print("Impossible")
else:
  cnt.sort()
  ans+=sum(cnt[:len(groups)-2])
  print(ans)
