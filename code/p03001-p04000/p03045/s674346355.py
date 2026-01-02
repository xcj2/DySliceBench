import sys
input=sys.stdin.readline

class CountTree():
  def __init__(self,n):
    self.n=n
    self.parents=[-1]*n
  
  def find(self,x):
    if self.parents[x]<0:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]
    
  def union(self,x,y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
    
  def roots(self):
    return [i for i,x in enumerate(self.parents) if x<0]
  def group_count(self):
    return len(self.roots())
  
def solve():
  n,m=(int(i) for i in input().split())
  ct=CountTree(n)
  for i in range(m):
    x,y,z=[int(i) for i in input().split()]
    ct.union(x-1,y-1)
  print(ct.group_count())
solve()
    