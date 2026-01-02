import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces

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

n,m = na()
ab = [na() for c in range(m)]
uf = UnionFind()
ans = [n*(n-1)//2]

for a,b in reversed(ab):
  if not uf.are_same(a,b):
    ans.append(ans[-1]-uf.size(a)*uf.size(b))
  else:
    ans.append(ans[-1])
  uf.unite(a,b)
  
print('\n'.join(reversed([str(x) for x in ans][:-1])))