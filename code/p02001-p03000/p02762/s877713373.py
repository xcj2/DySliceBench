class UnionFind:
  def __init__(self,n):
    self.parent=[i for i in range(n)] # 親要素のノード番号を格納 parent[x]==xの時そのノードは根
    self.rank=[0]*n # 木の高さを格納する
    self.count=0
    
  def root(self,x): # 根を返す
    if self.parent[x]==x: # 根ならその番号を返す
      return x
    else: # 根でないなら、親の要素で再検索 捜査の過程で親を書き換える
      self.parent[x]=self.root(self.parent[x])
      return self.root(self.parent[x])
    
  def is_same(self,x,y): # 同じ集合に属するか(根が同じか)判定
    return self.root(x)==self.root(y)
  
  def union(self,x,y): # 併合
    # 根を探す
    x=self.root(x)
    y=self.root(y)
    if x==y: return # 根が同じなら既に同じ集合なのでreturn
    # 木の高さを比較し、低い方から高い方に辺を張る
    if self.rank[x]<self.rank[y]:
      self.parent[x]=y
    else:
      self.parent[y]=x
      if self.rank[x]==self.rank[y]: self.rank[x]+=1
    self.count+=1
    
from collections import Counter
n,m,k=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(m)]
CD=[list(map(int,input().split())) for _ in range(k)]

blocks=[set() for _ in range(n)]
for c,d in CD:
  c,d=c-1,d-1
  blocks[c].add(d)
  blocks[d].add(c)

friends=[0]*n
uf=UnionFind(n)
for a,b in AB:
  a,b=a-1,b-1
  friends[a]+=1
  friends[b]+=1
  if not uf.is_same(a,b): uf.union(a,b)
    
ctr=Counter()
for i in range(n):
  r=uf.root(i)
  ctr[r]+=1
  
ans=[]
for i in range(n):
  tmp=ctr[uf.root(i)]-friends[i]-1
  for b in blocks[i]:
    if uf.is_same(i,b): tmp-=1
  ans.append(tmp)
print(*ans)