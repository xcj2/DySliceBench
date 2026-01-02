#見ながら､一応わかったつもり


def mi():return map(int,input().split())
#input
n,m,k=mi()
ab=[tuple(mi()) for _ in range(m)]
cd=[tuple(mi()) for _ in range(k)]


#class
class UnionFind:
  def __init__(self,n):
    self.parent=[i for i in range(n)]
    self.rank=[0]*n
    self.count=0
  def root(self,a):#rootを探す
    if self.parent[a]==a:
      return a
    else:
      self.parent[a]=self.root(self.parent[a])
      return self.parent[a]
  def is_same(self,a,b):#同じかどうか
    return self.root(a)==self.root(b)
  def unite(self,a,b):#根をまとめる
    ra=self.root(a)
    rb=self.root(b)
    if ra==rb:
      return
    if self.rank[ra]<self.rank[rb]:
      self.parent[ra]=rb
    else:
      self.parent[rb]=ra
    if self.rank[ra]==self.rank[rb]:
      self.rank[ra]+=1
      self.count+=1
      
            
uf=UnionFind(n)
friends=[0 for _ in range(n)]
blocks=[[] for _ in range(n)]


for a,b in ab:
  a=a-1
  b=b-1
  friends[a]+=1
  friends[b]+=1
  uf.unite(a,b)
  
  
for i in range(n):
  uf.root(i)
  
for c,d in cd:
  c-=1;d-=1
  blocks[c]+=d,
  blocks[d]+=c,
  
    
import collections 
ctr=collections.Counter()
for i in range(n):
  ctr[uf.parent[i]]+=1
  
  
ans=[0]*n
for i in range(n):
  tmp=ctr[uf.root(i)]-1-friends[i]
  for b in blocks[i]:
    if uf.is_same(i,b):
      tmp-=1
  ans[i]=tmp
print(*ans)
    
    