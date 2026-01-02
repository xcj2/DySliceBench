import sys
read=sys.stdin.read
readline=sys.stdin.readline
readlines=sys.stdin.readlines

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
edges=[None]*M
for i in range(M):
  a,b=map(int,readline().split())
  edges[i]=[a-1,b-1]

ans=0
# どの辺を使用しないかのループ
for i in range(M):
  # 辺iを使用しない場合
  UF=UnionFind(N)
  for m in range(M):
    if m==i:
      continue
    UF.unite(edges[m][0],edges[m][1])
  # 連結であれば0が属するグラフのサイズはNである
  if UF.get_group_size(0)!=N:
    ans+=1
    
print(ans)  
