
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rnk = [0]*(n+1)
  def Find_Root(self, x):
    if(self.root[x] < 0):
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]
  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if(x == y):
      return 
    if self.root[x] > self.root[y]:
      x, y = y, x
    self.root[x] += self.root[y]
    self.root[y] = x 
  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)
  def Count(self, x): # xが属するグループのサイズを返す
    return -self.root[self.Find_Root(x)]
  def Members(self, x): # xが属するグループに属する要素をリストで返す
    return [i for i in range(self.n) if self.Find_Root(i)==self.Find_Root(x)]
  def Roots(self): # 全ての根の要素をリストで返す
    return [i for i, x in enumerate(self.root) if x < 0]
  def Group_Count(self): # グループの数を返す
    return len(self.Roots())

n, k, l = map(int, input().split())

uf_road = UnionFind(n)
uf_train = UnionFind(n)

for _ in range(k):
  p, q = map(lambda x:int(x)-1, input().split())
  uf_road.Unite(p, q)

for _ in range(l):
  r, s = map(lambda x:int(x)-1, input().split())
  uf_train.Unite(r, s)

root_road = [0]*n 
root_train = [0]*n 

for i in range(n):
  root_road[i] = uf_road.Find_Root(i)
  root_train[i] = uf_train.Find_Root(i)

from collections import defaultdict
pair = defaultdict(int)
for i in range(n):
  pair[(root_road[i], root_train[i])] += 1 

for i in range(n):
  print(pair[(root_road[i], root_train[i])], end=" ")