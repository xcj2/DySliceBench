from collections import Counter


class UnionFind:
  def __init__(self, n):
    self.par = [x for x in range(n)]
    
  def find(self, x):
    if x == self.par[x]:
      return x
    self.par[x] = self.find(self.par[x])
    return self.par[x]
  
  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x != y:
      self.par[y] = x

      
N, K, L = map(int, input().split())  

rails = UnionFind(N + 1)
roads = UnionFind(N + 1)

for _ in range(K):
  p, q = map(int, input().split())
  rails.unite(p, q)

for _ in range(L):
  p, q = map(int, input().split())
  roads.unite(p, q)

counter = Counter([
  (rails.find(p), roads.find(p))
  for p in range(1, N + 1)
])

print(' '.join(
  str(counter[(rails.find(i), roads.find(i))])
  for i in range(1, N + 1)
))   