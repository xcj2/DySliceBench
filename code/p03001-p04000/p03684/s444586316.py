from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

setrecursionlimit(1 << 30)

class union_find:
  def __init__(self, n): self.par = [-1] * n; self.rank = [0] * n
  def __repr__(self): return "union_find({0})".format([self.root(i) for i in range(n)])
  def unite(self, x, y):
    x = self.root(x); y = self.root(y)
    if x == y: return
    if self.rank[x] < self.rank[y]: self.par[x] = y
    else:
      self.par[y] = x
      if self.rank[x] == self.rank[y]: self.rank[x] += 1
  def root(self, x):
    if self.par[x] == -1: return x
    else: self.par[x] = self.root(self.par[x]); return self.par[x]
  def same(self, x, y): return self.root(x) == self.root(y)

N = read()
ps = []
for i in range(N):
  x, y = reads()
  ps.append((i, x, y))

edges = []

for q in range(1, 3):
  ps.sort(key=lambda p: p[q])
  for i in range(N-1):
    edges.append((ps[i+1][q] - ps[i][q], ps[i][0], ps[i+1][0]))

edges.sort()

uf = union_find(N)
ans = 0
for c, i, j in edges:
  if not uf.same(i, j):
    ans += c
    uf.unite(i, j)
print(ans)