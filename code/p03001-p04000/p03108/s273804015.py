from functools import reduce
from operator import mul

def cmb(n,r):
  r = min(r, n-r)
  if r==0: return 1
  if r<0: return 0
  over = reduce(mul, range(n, n-r, -1))
  under = reduce(mul, range(1,r+1))
  return over//under

class UnionFind:
  def __init__(self, n):
    self.par = [i for i in range(n)]
    self.size = [1]*n
    self.rank = [0]*n
  def find(self, x):
    if self.par[x]==x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]
  def unit(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    elif self.rank[x]<self.rank[y]:
      self.par[x] = y
      self.size[y] += self.size[x]
      return
    elif self.rank[y]<self.rank[x]:
      self.par[y] = x
      self.size[x] += self.size[y]
    else:
      self.par[y] = x
      self.size[x] += self.size[y]
      self.rank[x] += 1
      
  def same(self, x, y):
    return self.find(x)==self.find(y)
  
  def count(self, x):
    return self.size[x]

N, M = map(int, input().split())
bridge = []
u = UnionFind(N)
m = cmb(N,2)
ans = [m]

for i in range(M):
  A, B = map(int, input().split())
  bridge += [(A,B)]
  
for i in range(M-1,0,-1):
  a, b = bridge[i]
  if u.same(a-1,b-1):
    ans += [m]
    continue
  pa = u.find(a-1)
  pb = u.find(b-1)
  m -= u.count(pa)*u.count(pb)
  ans += [m]
  u.unit(a-1,b-1)

for i in range(M-1,-1,-1):
  print(ans[i])
  