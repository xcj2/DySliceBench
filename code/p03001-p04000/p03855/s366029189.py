from collections import defaultdict as dd
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rnk = [0]*(n+1)

  def Find_Root(self, x):
    if(self.root[x] < 0):
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]

  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if(x == y):
      return 
    elif(self.rnk[x] > self.rnk[y]):
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if(self.rnk[x] == self.rnk[y]):
        self.rnk[y] += 1

  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)
    
  def Count(self, x):
    return -self.root[self.Find_Root(x)]
N, K, L = map(int, input().split())
k = UnionFind(N)
l = UnionFind(N)
checkset = set()
res = [1] * (N + 1)
roots = dd(int)
for _ in range(K):
  x, y = map(int, input().split())
  k.Unite(x, y)
  checkset.add(x)
  checkset.add(y)
for _ in range(L):
  x, y = map(int, input().split())
  l.Unite(x, y)
  checkset.add(x)
  checkset.add(y)
for i in list(checkset):
  kr = k.Find_Root(i)
  lr = l.Find_Root(i)
  roots[(kr, lr)] += 1
#print(roots)
for i in list(checkset):
  kr = k.Find_Root(i)
  lr = l.Find_Root(i)
  res[i] = roots[(kr, lr)]
  
print(*(res[1: ]))

