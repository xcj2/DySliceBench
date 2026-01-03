from collections import*
class u():
  def __init__(self,n):self.n,self.r=[-1]*n,[0]*n
  def f(self,x):
    if self.n[x]<0:return x
    else:self.n[x]=self.f(self.n[x]);return self.n[x]
  def u(self,x,y):
    x,y=self.f(x),self.f(y)
    if x==y:return
    elif self.r[x]>self.r[y]:self.n[x]+=self.n[y];self.n[y]=x
    else:self.n[y]+=self.n[x];self.n[x]=y;self.r[y]+=self.r[x]==self.r[y]
n,k,l=map(int,input().split());d=u(n);t=u(n)
for _ in range(k):a,b=map(int,input().split());d.u(a-1,b-1)
for _ in range(l):a,b=map(int,input().split());t.u(a-1,b-1)
p=[(d.f(i),t.f(i))for i in range(n)];c=Counter(p);print(*[c[p[i]]for i in range(n)])