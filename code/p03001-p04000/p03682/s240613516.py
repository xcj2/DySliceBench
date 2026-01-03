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

for [u, fr], [v, to] in zip(x_list, x_list[1:]):
  stw += [[abs(u-v), fr, to]]
for [u, fr], [v, to] in zip(y_list, y_list[1:]):
  stw += [[abs(u-v), fr, to]]

stw = sorted(stw, key=lambda x:x[0])

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
  res = 0
  uf = UnionFind(n)
  #while stw:
  for i in range(len(stw)):
    #w, s, t = heapq.heappop(stw)
    w, s, t = stw[i]
    if not uf.isSameGroup(s, t):
      uf.Unite(s, t)
      res += w
  return res

print(kruskal())