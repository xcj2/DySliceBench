
import heapq
n = int(input())
stw = []
x_list = []
y_list = []
for i in range(n):
  x, y = map(int, input().split())
  x_list += [[x, i]]
  y_list += [[y, i]]

x_list.sort()
y_list.sort()

for i in range(n-1):
  stw += [[x_list[i][1], x_list[i+1][1], abs(x_list[i][0]-x_list[i+1][0])]]
for i in range(n-1):
  stw += [[y_list[i][1], y_list[i+1][1], abs(y_list[i][0]-y_list[i+1][0])]]

stw.sort(key=lambda x:x[2])

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


def kruskal():
  # stw = [[s0, t0, w0], [s1, t1, w1], ..., [sn, tn, wn]]
  # stw: s: 始点, t: 終点, w: st間の重み
  # stwはwを小さい順にソートされたものとする
  # s, tを入れ替えたものはいれなくていい
  res = 0
  uf = UnionFind(n)
  for i in range(len(stw)):
    s, t, w = stw[i]
    if not uf.isSameGroup(s, t):
      uf.Unite(s, t)
      res += w
  return res

ans = kruskal()
print(ans)