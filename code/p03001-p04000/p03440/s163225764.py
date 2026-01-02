class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
          x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def num_roots(self):
    return len([i for i, x in enumerate(self.parents) if x < 0])

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def num_members(self,x):
    return abs(self.parents[self.find(x)])

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
from bisect import *
from collections import defaultdict
def solve():
  ans = 0
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  uf = UnionFind(N)
  for _ in range(M):
    x,y = map(int, input().split())
    uf.union(x,y)
  if N>2*(M+1):
    return 'Impossible'
  if N-M==1:
    return 0
  d = defaultdict(lambda: [])
  for i in range(N):
    r = uf.find(i)
    if r<0:
      d[i].append(A[i])
    else:
      d[r].append(A[i])
  lis1 = []
  for v in d.values():
    mini = min(v)
    ans += mini
    v.remove(mini)
    for l in v:
      insort_right(lis1,l)
  ans += sum(lis1[:(N-M-2)])
  return ans
print(solve())