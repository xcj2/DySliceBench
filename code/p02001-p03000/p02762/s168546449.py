from collections import *
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
        if(x == y):return 
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
    def count(self, x):
        return -self.root[self.find(x)]
n,m,k=map(int,input().split())
uf=UnionFind(n)
d=[0]*(n+1)
for _ in [0]*m:
  a,b=map(int,input().split())
  d[a]+=1
  d[b]+=1
  uf.unite(a,b)
to=[[]for _ in [0]*(n+1)]
for _ in [0]*k:
  a,b=map(int,input().split())
  to[a]+=[b]
  to[b]+=[a]
a=[]
b=dict(Counter([uf.find(i) for i in range(1,n+1)]))
for i,j in enumerate(d):
  if i==0:continue
  ans=b[uf.find(i)]-j-1
  for k in to[i]:
    if uf.same(i,k):ans-=1
  a+=[ans]
print(*a)