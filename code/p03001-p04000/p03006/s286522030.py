# まず、xの値でソート（同値の場合はyでソート）する。
# この状態で、全ての2点について、x,yの差を求める
# 差の情報(p,q)の回数が最も大きいものが答えの候補
# (p,q)で到達できる点にはコスト0で行けるグラフの最短距離を解く

N=int(input())
ball=[None] * N
for i in range(N):
  ball[i] = list(map(int,input().split()))

ball=sorted(ball,key=lambda x:(x[0],x[1]))

from collections import defaultdict
dic = defaultdict(list)

for i in range(N-1):
  for j in range(i+1,N):
    # 点iから点jへは(p,q)で到達できる
    dic[(ball[j][0] - ball[i][0],ball[j][1] - ball[i][1])].append((i,j))

pq=None
target=[]
for item in dic.items():
  if len(item[1]) > len(target):
    target = item[1]
    pq=item[0]
    
# targetの要素で、同じ点を持つものは結合して1つの点にできる。
# UnionFind

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
for i,j in target:
  UF.unite(i,j)
  
print(len(UF.get_roots()))