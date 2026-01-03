from sys import exit, setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

class union_find:
  def __init__(self, n): self.par = [-1]*n
  def __repr__(self): return "union_find({0})".format(self.par)
  def unite(self, x, y):
    if self.root(x) != self.root(y):
      self.par[self.root(x)] = y
  def root(self, x):
    if self.par[x] == -1: return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  def same(self, x, y): return self.root(x) == self.root(y)

setrecursionlimit(1000000)

(N, K, L) = reads()

rail = union_find(N)
road = union_find(N)

for _ in range(K):
  (p, q) = reads()
  (p, q) = (p-1, q-1)
  road.unite(p, q)

for _ in range(L):
  (p, q) = reads()
  (p, q) = (p-1, q-1)
  rail.unite(p, q)

d = defaultdict(int)
for i in range(N):
  d[road.root(i), rail.root(i)] += 1


results = (d[road.root(i), rail.root(i)] for i in range(N))
print(" ".join(str(n) for n in results))
