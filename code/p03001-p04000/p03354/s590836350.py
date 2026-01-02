from collections import defaultdict
class UnionFind:
  
  def __init__(self, n):
    self.par = [i for i in range(n)]
    self.rank = [0]*n
  
  def find(self, x):
    if self.par[x]==x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]
  
  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    if self.rank[x]<self.rank[y]:
      self.par[x] = y
    else:
      self.par[y] = x
      if self.rank[x]==self.rank[y]:
        self.rank[x] += 1
  
  def same(self, x, y):
    return self.find(x)==self.find(y)
  
N, M = map(int, input().split())
h = [int(i)-1 for i in input().split()]
dic1 = defaultdict(list)
dic2 = defaultdict(list)
u = UnionFind(N)
for i in range(M):
  a, b = map(int, input().split())
  u.unite(a-1,b-1)

for c in range(N):
  p = u.find(c)
  dic1[p] += [c]
  dic2[p] += [h[c]]
ans = 0
for p in dic1.keys():
  dic1[p].sort()
  dic2[p].sort()
  i = 0
  j = 0
  while i<len(dic1[p]) and j<len(dic2[p]):
    if dic1[p][i]==dic2[p][j]:
      i += 1
      j += 1
      ans += 1
    elif dic1[p][i]<dic2[p][j]:
      i += 1
    else:
      j += 1
    
print(ans)