from operator import itemgetter
n = int(input())
x =[]
y =[]
info = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
  x.append([i,info[i][0]])
  y.append([i,info[i][1]])

x = sorted(x,key=itemgetter(1))
y = sorted(y,key=itemgetter(1))
tree = []
#for i in range(n):
#  if i==0:
#    tree[x[i][0]].append([x[i+1][0],abs(x[i][1]-x[i+1][1])])
#    tree[y[i][0]].append([y[i+1][0],abs(y[i][1]-y[i+1][1])])
#  elif i==n-1:
#    tree[x[i][0]].append([x[i-1][0],abs(x[i][1]-x[i-1][1])])
#    tree[y[i][0]].append([y[i-1][0],abs(y[i][1]-y[i-1][1])])
#  else:
#    tree[x[i][0]].append([x[i+1][0],abs(x[i][1]-x[i+1][1])])
#    tree[x[i][0]].append([x[i-1][0],abs(x[i][1]-x[i-1][1])])
#    tree[y[i][0]].append([y[i+1][0],abs(y[i][1]-y[i+1][1])])
#    tree[y[i][0]].append([y[i-1][0],abs(y[i][1]-y[i-1][1])])
    
for i in range(n-1):
    tree.append([x[i][0],x[i+1][0],abs(x[i][1]-x[i+1][1])])
    tree.append([y[i][0],y[i+1][0],abs(y[i][1]-y[i+1][1])])

#UnionFindクラス
class UnionFind(object):

  def __init__(self, n=1):
    self.par = [i for i in range(n)]
    self.rank = [0 for _ in range(n)]

  def find(self, x):
  
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
  
  # xとyの根を結合させる
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x != y:
      if self.rank[x] < self.rank[y]:
        x, y = y, x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1
      self.par[y] = x
  
  # x,yの根が同じかどうかを返す（根が同じ:True、根が異なる:False）
  def is_same(self, x, y):
    return self.find(x) == self.find(y)

uf = UnionFind(len(tree))
tree = sorted(tree,key=itemgetter(2))
ans = 0

for i in tree:
  x,y,kyori = i
  if not uf.is_same(x,y):
    uf.union(y,x)
    ans += kyori
print(ans)
