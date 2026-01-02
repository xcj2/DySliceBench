class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    self.min_y = [N]*n

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
    self.min_y[x] = min(self.min_y[x],self.min_y[y])
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

import sys,os,io
input = sys.stdin.readline
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
N = int(input())
A = [list(map(int, input().split()))+[i] for i in range(N)]
uf = UnionFind(N)
uf.min_y = [y for x,y,i in A]
ans = [1]*N
A.sort()
Y = [(i,y) for x,y,i in A]
from heapq import *
heap = []
for u,y in Y:
  atode = []
  for _ in range(len(heap)):
    y1,v = heappop(heap)
    if y<y1:
      heappush(heap,(y1,v))
      break
    uf.union(u,v)
    if uf.parents[v]<0:
      atode.append((uf.min_y[v],v))
  if uf.parents[u]<0:
    heappush(heap,(uf.min_y[u],u))
  for y1,v in atode:
    heappush(heap,(y1,v))
for i in range(N):
  ans[i] = uf.num_members(i)
print(*ans, sep='\n')

