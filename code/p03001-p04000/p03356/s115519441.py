N,M=map(int,input().split())

P=list(map(int,input().split()))
P=list(map(lambda x:x-1,P))

# Pもx,yも0-indexに変更
# UnionFindで、(x,y)で同組になるインデックスの集合を求める。
# 同じインデックスの集合に存在するPの値の集合で、インデックスの集合にも存在するものの数が答え

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
      r.add(self.root(i))
    return r
  
  def show_parent(self):
    print(self.parent)
    
  def show_size(self):
    print(self.size)
    
UF=UnionFind(N)
for i in range(M):
  x,y = map(int,input().split())
  UF.unite(x-1,y-1)
  
from collections import defaultdict
dic = defaultdict(list)
for i in range(N):
  r = UF.root(i)
  dic[r].append(i)
  
ans = 0
for inds in dic.values():
  vals = set()
  for i in inds:
    vals.add(P[i])
  ans += len(vals & set(inds))
  
print(ans)