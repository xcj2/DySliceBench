# 逆順に見ていく
# M本の橋が全て崩落した状態=全ての島が行き来できない=不便さ:N*(N-1)//2
# 橋ができたら、UnionFindで一つに島グループとしてつなぐ
# 新たにできた橋が、今まで別の島グループだったときは
# 二つの島グループの間の組み合わせの数だけ不便さが減る
# 島グループ1の数 * 島グループ2の数だけ不便さが減る
# 新たにできた島グループが同じ島グループだったときは何も変わらない

import sys
readline=sys.stdin.readline

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
    
N,M=map(int,readline().split())
UF=UnionFind(N)
ans=[N*(N-1)//2]
decay=[None]*M
for i in range(M):
  a,b=map(int,readline().split())
  decay[M-1-i]=[a-1,b-1]
  
# decayは逆順になっている
for i in range(M):
  a,b=decay[i]
  if UF.same(a,b):
    ans+=[ans[-1]]
  else:
    asize=UF.get_group_size(a)
    bsize=UF.get_group_size(b)
    ans+=[ans[-1]-asize*bsize]
    UF.unite(a,b)
    
for i in range(len(ans)-2,-1,-1):
  print(ans[i])
