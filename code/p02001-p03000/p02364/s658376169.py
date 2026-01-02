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

V, E = map(int, input().split())
edges = []

for _ in range(E):
  s, t, w = map(int, input().split())
  edges.append(Edge(w, s, t))

edges.sort()

u = UnionFind(V)
cost = 0

for w, s, t in edges:
  if u.is_same(s, t):
    continue
  u.unite(s, t)
  cost += w

print(cost)

