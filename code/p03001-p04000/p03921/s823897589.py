n,m=map(int,input().split())
import sys;sys.setrecursionlimit(10**9)
class Union_Find():
  def __init__(self,n):self.n,self.r=[-1]*n,[0]*n
  def Find_Root(self,x):
    if self.n[x]<0:return x
    else:self.n[x]=self.Find_Root(self.n[x]);return self.n[x]
  def Unite(self,x,y):
    x,y=self.Find_Root(x),self.Find_Root(y)
    if x==y:return
    elif self.r[x]>self.r[y]:self.n[x]+=self.n[y];self.n[y]=x
    else:self.n[y]+=self.n[x];self.n[x]=y;self.r[y]+=self.r[x]==self.r[y]
  def isRootSame(self,x,y):return self.Find_Root(x)==self.Find_Root(y)
  def Count(self,x):return -self.n[self.Find_Root(x)]
u=Union_Find(m)
l=[list(map(int,input().split()))for _ in range(n)]
for i in range(n):
  for j in range(1,len(l[i])-1):u.Unite(l[i][j]-1,l[i][j+1]-1)
for i in range(n-1):
  if not(u.isRootSame(l[i][1]-1,l[i+1][1]-1)):print("NO");exit()
print("YES")