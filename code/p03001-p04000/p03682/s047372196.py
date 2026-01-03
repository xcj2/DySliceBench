from collections import namedtuple


class UnionFind:
  def __init__(self, n):
    self.par = [i for i in range(n + 1)]
    self.size = [1] * (n + 1)

  def is_same(self, a, b):
    return self.find(a) == self.find(b)

  def unite(self, a, b):
    a = self.find(a)
    b = self.find(b)  
    if self.size[a] < self.size[b]:
      a, b = b, a
    self.par[b] = a
    self.size[a] += self.size[b]

  def size_of(self, a):
    return self.size[self.find(a)]

  def find(self, a):
    if a == self.par[a]:
      return a
    self.par[a] = self.find(self.par[a])
    return self.par[a]

Edge = namedtuple('Edge', 'w s t')
X = namedtuple('X', 'x i')
Y = namedtuple('Y', 'y i')

N = int(input())

edges = []
xg = []
yg = []

for i in range(N):
  x, y = map(int, input().split())
  xg.append(X(x, i))
  yg.append(Y(y, i))

xg.sort()
yg.sort()

for i in range(N - 1):
  x1, a = xg[i]
  x2, b = xg[i + 1]
  edges.append(Edge(abs(x1 - x2), a, b))

for i in range(N - 1):
  y1, a = yg[i]
  y2, b = yg[i + 1]
  edges.append(Edge(abs(y1 - y2), a, b))

edges.sort()

u = UnionFind(N)
cost = 0

for w, s, t in edges:
  if u.is_same(s, t):
    continue
  u.unite(s, t)
  cost += w

print(cost)
