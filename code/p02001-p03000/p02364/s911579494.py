"""
クラスカルのアルゴリズム
"""

class UnionFindTree:
  def __init__(self, n: int):
    self.__parent = [i for i in range(n)]
    self.__rank = [0 for i in range(n)]

  def unite(self, x, y) -> None:
    self.__link(self.__find_set(x), self.__find_set(y))

  def same(self, x, y) -> bool:
    return self.__find_set(x) == self.__find_set(y)

  def __find_set(self, x):
    if x != self.__parent[x]:
      self.__parent[x] = self.__find_set(self.__parent[x])
    return self.__parent[x]

  def __link(self, x, y):
    if self.__rank[x] < self.__rank[y]:
      self.__parent[x] = y
    else:
      if self.__rank[x] == self.__rank[y]:
        self.__rank[x] += 1
      self.__parent[y] = x


class Edge:
  def __init__(self, src, dst, weight):
    self.src = src
    self.dst = dst
    self.weight = weight


V, E = map(int, input().split())
INF = 10**10
edges = [Edge(*map(int, input().split())) for i in range(E)]
edges.sort(key=lambda e: e.weight)
total_cost = 0
t = UnionFindTree(V)

for e in edges:
  if not t.same(e.src, e.dst):
    t.unite(e.src, e.dst)
    total_cost += e.weight

print(total_cost)

