import sys
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
  def unit(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    elif self.rank[x]<self.rank[y]:
      self.par[x] = y
    elif self.rank[y]<self.rank[x]:
      self.par[y] = x
    else:
      self.par[y] = x
      self.rank[x] += 1
  def same(self, x, y):
    return self.find(x)==self.find(y)
  
N,M,*L = map(int, open(0).read().split())
A = L[:N]
U = UnionFind(N)
dic = defaultdict(list)
used = [False]*N
ans = 0
for x,y in zip(*[iter(L[N:])]*2):
  U.unit(x,y)
for i in range(N):
  dic[U.find(i)].append((A[i],i))
if len(dic.keys())==1:
  print(0)
  sys.exit()
for k in dic.keys():
  dic[k].sort()
  ans += dic[k][0][0]
  used[dic[k][0][1]] = True
B = sorted((c,i) for i,c in enumerate(A))
cnt = len(dic.keys())-2
for i in range(N):
  if cnt==0:
    break
  if used[B[i][1]]:
    continue
  ans += B[i][0]
  cnt -= 1
if cnt > 0:
  print('Impossible')
else:
  print(ans)