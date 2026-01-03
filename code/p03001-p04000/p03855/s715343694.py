from collections import Counter
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rnk = [0]*(n+1)
  def find(self, x):
    if(self.root[x] < 0):
      return x
    else:
      self.root[x] = self.find(self.root[x])
      return self.root[x]
  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
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
  def same(self, x, y):
    return self.find(x) == self.find(y)
n,k,l=map(int,input().split())
e=[[i]for i in range(n+1)]
ur=UnionFind(n)
ut=UnionFind(n)
for i in range(k):
  a,b=map(int,input().split())
  ur.unite(a,b)
for _ in range(l):
  a,b=map(int,input().split())
  ut.unite(a,b)
pair=[(ur.find(i),ut.find(i)) for i in range(1,n+1)]
c=Counter(pair)
ans=[c[i] for i in pair]
print(*ans)