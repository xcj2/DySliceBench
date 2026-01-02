from collections import defaultdict

class UnionFind:
  def __init__(self, n):
    self.parents = list(range(n))
    self.ranks = [0] * n

  def root(self, x):
    if self.parents[x] == x:
      return x
    else:
      y = self.root(self.parents[x])
      self.parents[x] = y
      return y

  def same(self, x, y):
    return self.root(x) == self.root(y)

  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)
    if x == y:
      return
    if self.ranks[x] < self.ranks[y]:
      self.parents[x] = y
    else:
      self.parents[y] = x
      if self.ranks[x] == self.ranks[y]:
        self.ranks[x] += 1

n, m, k = map(int, input().split())
u = UnionFind(n)
counts = [1 for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  u.unite(a - 1, b - 1)
  counts[a - 1] += 1
  counts[b - 1] += 1

for _ in range(k):
  a, b = map(int, input().split())
  if u.same(a - 1, b - 1):
    counts[a - 1] += 1
    counts[b - 1] += 1

groups = defaultdict(int)
for i in range(n):
  groups[u.root(i)] += 1

print(*[groups[u.root(i)] - counts[i] for i in range(n)])
