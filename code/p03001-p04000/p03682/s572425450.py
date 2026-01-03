from heapq import heappush, heappop
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
      return
    elif self.rank[y]<self.rank[x]:
      self.par[y] = x
    else:
      self.par[y] = x
      self.rank[x] += 1 
  def same(self, x, y):
    return self.find(x)==self.find(y)
  
N = int(input())
X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X += [(x,y,i)]
  Y += [(x,y,i)]
X.sort()
Y.sort(key=lambda x:x[1])
hq = []
for i in range(N-1):
  x1, y1, i1 = X[i]
  x2, y2, i2 = X[i+1]
  heappush(hq, (x2-x1,i1,i2))
  x1, y1, i1 = Y[i]
  x2, y2, i2 = Y[i+1]
  heappush(hq, (y2-y1,i1,i2))

u  = UnionFind(N)
cnt = 1
ans = 0
while cnt<N:
  c, i1, i2 = heappop(hq)
  if u.same(i1,i2):
    continue
  ans += c
  cnt += 1
  u.unit(i1,i2)
print(ans)