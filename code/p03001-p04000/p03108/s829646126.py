from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

class union_find:
  def __init__(self, n):
    self.par = [-1] * n
    self.rank = [0] * n
    self.size = [1] * n
  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)
    if x == y:
      return
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
      self.size[y] += self.size[x]
    else:
      self.par[y] = x
      self.size[x] += self.size[y]
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1
  def root(self, x):
    if self.par[x] == -1:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  def comp_size(self, x):
    x = self.root(x)
    return self.size[x]
  def same(self, x, y):
    return self.root(x) == self.root(y)
  def comp_sizes(self):
    return [self.size[i] for i in range(len(self.par)) if self.root(i) == i]

N, M = reads()
edges = []
for _ in range(M):
  A, B = reads()
  edges.append((A-1, B-1))
edges.reverse()

def tri(k):
  return k * (k - 1) // 2

uf = union_find(N)
conv = 0
total = tri(N)
ans = []
for A, B in edges:
  ans.append(total - conv)
  if not uf.same(A, B):
    a = uf.comp_size(A)
    b = uf.comp_size(B)
    uf.unite(A, B)
    conv += tri(uf.comp_size(A)) - tri(a) - tri(b)
ans.reverse()
print("\n".join(map(str, ans)))
