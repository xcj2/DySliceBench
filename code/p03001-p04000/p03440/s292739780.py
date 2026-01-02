from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

def main():
  N, M = reads()
  A = reads()
  if M == N-1:
    print(0); exit()

  d = Counter(A)
  uf = union_find(N)
  edges = [[] for _ in range(N)]
  for _ in range(M):
    x, y = reads()
    uf.unite(x, y)

  INF = 1 << 30
  mins = defaultdict(lambda: INF)
  for i in range(N):
    k = uf.root(i)
    mins[k] = min(mins[k], A[i])
  g = len(mins)

  if (g - 1) * 2 > N:
    print("Impossible"); exit()

  ans = 0
  for k, v in mins.items():
    ans += v
    d[v] -= 1
  ans += sum(sorted(d.elements())[:g-2])
  print(ans)

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

main()