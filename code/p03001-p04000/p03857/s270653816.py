from collections import defaultdict

N,K,L=map(int,input().split())

class UnionFind(object):
  def __init__(self,n):
    self.table=[-1]*n
 
  def find(self,x):
    parent=self.table[x]
    if parent<0:
      return x
    else:
      root=self.find(parent)
      self.table[x]=root
      return root
 
  def union(self,a,b):
    root1=self.find(a)
    root2=self.find(b)
    if root1 != root2:
      if self.table[root1] != self.table[root2]:
        if self.table[root1] < self.table[root2]:
          self.table[root2]=root1
        else:
          self.table[root1]=root2
      else:
        self.table[root1]+=(-1)
        self.table[root2]=root1
      
ufK=UnionFind(N)
for i in range(K):
  p,q=map(int,input().split())
  ufK.union(p-1,q-1)

ufL=UnionFind(N)
for i in range(L):
  p,q=map(int,input().split())
  ufL.union(p-1,q-1)

KL=defaultdict(int)
ans=[]
for i in range(N):
  a=ufK.find(i)
  b=ufL.find(i)
  KL[(a,b)]+=1
for i in range(N):
  a=ufK.find(i)
  b=ufL.find(i)
  ans.append(KL[(a,b)])
  
print(*ans)
