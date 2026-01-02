import sys
read=sys.stdin.buffer.read
readline=sys.stdin.readline
readlines=sys.stdin.buffer.readlines

# 0-indexed
class UnionFind:
  N=0
  parent=None
  size=None
  def __init__(self,N):
    self.N=N
    self.parent=[i for i in range(self.N)]
    self.size=[1]*self.N
    
  def root(self,x):
    while x!=self.parent[x]:
      self.parent[x]=self.parent[self.parent[x]]
      x=self.parent[x]
    return x
  
  def same(self,x,y):
    return self.root(x)==self.root(y)
  
  def unite(self,x,y):
    x=self.root(x)
    y=self.root(y)
    if x==y:
      return
    if self.size[x]>self.size[y]:
      # 大きい方にくっつける
      self.parent[y]=x
      self.size[x]+=self.size[y]
    else:
      self.parent[x]=y
      self.size[y]+=self.size[x]
      
  def get_group_size(self,x):
    return self.size[self.root(x)]
  
  def get_roots(self):
    r=set()
    for i in range(self.N):
      r.add(root(i))
    return r
  
  def show_parent(self):
    print(self.parent)
    
  def show_size(self):
    print(self.size)
    
N,M,K=map(int,readline().split())
UF=UnionFind(N)
friends=[0]*N
for i in range(M):
  a,b=map(int,readline().split())
  UF.unite(a-1,b-1)
  friends[a-1]+=1
  friends[b-1]+=1

from collections import defaultdict
block=defaultdict(set)
for i in range(K):
  c,d=map(int,readline().split())
  block[c-1].add(d-1)
  block[d-1].add(c-1)

ans=[0]*N
for i in range(N):
  ans[i]=UF.get_group_size(i)-friends[i]-1
  for b in block[i]:
    if UF.same(i,b):
      ans[i]-=1
  if ans[i]<0:
    ans[i]=0
print(*ans)