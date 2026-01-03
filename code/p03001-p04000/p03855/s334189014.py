from collections import defaultdict
class Unionfind:
  def __init__(self,n):
    self.Tree=[i for i in range(n)]
    self.rank=[0]*n

  def find(self,x):
    if x==self.Tree[x]:
      return x
    else:
      root=self.find(self.Tree[x])
      self.Tree[x]=root
      return root

  def unite(self,x,y):
    s1=self.find(x)
    s2=self.find(y)
    if s1==s2:
      pass
    else:
      if self.rank[s1]>self.rank[s2]:
        self.Tree[s2]=s1
      elif self.rank[s1]<self.rank[s2]:
        self.Tree[s1]=s2
      else:
        self.Tree[s2]=s1
        self.rank[s1]+=1
N,K,L=map(int,input().split())       
uf1=Unionfind(N)
uf2=Unionfind(N)
for i in range(K):
  p,q=map(int,input().split())
  uf1.unite(p-1,q-1)
for j in range(L):
  r,s=map(int,input().split())
  uf2.unite(r-1,s-1)
d=defaultdict(int)
ans=[0]*N
for i in range(N):
  d[(uf1.find(i),uf2.find(i))]+=1
for i in range(N):
  ans[i]=d[(uf1.find(i),uf2.find(i))]
print(" ".join(map(str,ans)))        