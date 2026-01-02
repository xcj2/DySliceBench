class UnionFind:
  def __init__(self, n):
    self.tree = [-1] * n
    self.rank = [0] * n
    self.diff_weight = [0] * n
  
  def unite(self, a, b, w):
    w += self.weight(a)
    w -= self.weight(b)
    a = self.root(a)
    b = self.root(b)
    if a == b:
      return
    if self.rank[a] < self.rank[b]:
      a, b = b, a
      w *= -1
    if self.rank[a] == self.rank[b]:
      self.rank[a] += 1
    self.tree[b] = a
    self.diff_weight[b] = w
    
  def root(self, a):
    if(self.tree[a] < 0):
      return a
    else:
      res = self.root(self.tree[a])
      self.diff_weight[a] += self.diff_weight[self.tree[a]]
      self.tree[a] = res
      return self.tree[a]

  def same(self, a, b):
    return self.root(a) == self.root(b)

  def weight(self, a):
    self.root(a)
    return self.diff_weight[a]

  def diff(self, a, b):
    return self.weight(b) - self.weight(a)

import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

def main():
  n, m = na()
  uf = UnionFind(n)
  for _ in range(m):
    t = list(na())
    a, b, c = t[0], t[1], t[2]
    if a == 0:
      d = t[3]
      uf.unite(b, c, d)
    else:
      if uf.same(b, c):
        print(uf.diff(b, c))
      else:
        print("?")

main()
