import sys
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
import collections
import itertools
import operator

class UnionFind:
  def __init__(self, elems=None):
    class KeyDict(dict):
      def __missing__(self, key):
        self[key] = key
        return key

    self.parent = KeyDict()
    self.rank = collections.defaultdict(int)
    self.size_ = collections.defaultdict(lambda: 1)

    if elems is not None:
      for elem in elems:
        _, _, _ = self.parent[elem], self.rank[elem], self.size_[elem]

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.rank[x] < self.rank[y]:
      self.parent[x] = y
      self.size_[y] += self.size_[x]
    else:
      self.parent[y] = x
      self.size_[x] += self.size_[y]
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1

  def are_same(self, x, y):
    return self.find(x) == self.find(y)

  def grouper(self):
    roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
    root = operator.itemgetter(1)
    for _, group in itertools.groupby(sorted(roots, key=root), root):
      yield [x for x, _ in group]

  def size(self,x):
    return self.size_[self.find(x)]

g = UnionFind()
n,m = na()

for i in range(m):
    x,y,z = na()
    g.unite(x,y)

f = list(g.grouper())

a = 0
b = 0
for i in f:
    a+=len(i)
    b+=1

print(b+n-a)