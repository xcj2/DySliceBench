from collections import defaultdict
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
N, M, K = map(int, input().split())
frend = defaultdict(list)
F = UnionFind(N)
for i in range(M):
  a, b = map(int, input().split())
  frend[a] += [b]
  frend[b] += [a]
  F.unit(a-1,b-1)
ans = [0]*N
for i in range(N):
  p = F.find(i)
  X = F.count(p)
  ans[i] = X-len(frend[i+1])-1
for i in range(K):
  a, b = map(int, input().split())
  if F.same(a-1,b-1):
    ans[a-1] -= 1
    ans[b-1] -= 1

print(' '.join(map(str,ans)))