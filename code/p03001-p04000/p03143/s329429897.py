from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import *

setrecursionlimit(10**7)

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

class union_find:
  def __init__(self, n, X):
    self.par = [-1] * n
    self.rank = [0] * n
    self._count = [0] * n
    self._sum = list(X)

  def __repr__(self):
    return "union_find({0})".format([self.root(i) for i in range(n)])

  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)
    self._count[x] += 1
    if x == y:      
      return
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
      self._count[y] += self._count[x]
      self._sum[y] += self._sum[x]
    else:
      self.par[y] = x
      self._count[x] += self._count[y]
      self._sum[x] += self._sum[y]
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1

  def reset_count(self, x):
    x = self.root(x)
    self._count[x] = 0

  def root(self, x):
    if self.par[x] == -1:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]

  def count(self, x):
    return self._count[self.root(x)]

  def sum(self, x):
    return self._sum[self.root(x)]

  def same(self, x, y):
    return self.root(x) == self.root(y)

N, M = reads()
X = reads()
edges = []
for _ in range(M):
  a, b, y = reads()
  a, b = a-1, b-1
  edges.append((y, a, b))
edges.sort()

uf = union_find(N, X)
ans = 0
for y, a, b in edges:
  uf.unite(a, b)
  if uf.sum(a) >= y:
    ans += uf.count(a)
    uf.reset_count(a)
print(M - ans)
