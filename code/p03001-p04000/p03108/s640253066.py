import sys
input = sys.stdin.readline
n,m=map(int,input().split())
A=[]
par=[-1]*n
def find(x):
  if par[x]<0:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return False
  else:
    if par[x]>par[y]:
      x,y=y,x
    par[x]+=par[y]
    par[y]=x
    return True
def same(x,y):
  return find(x)==find(y)
def size(x):
  return -par[find(x)]
for i in range(m):
  a,b=map(int,input().split())
  A.append([a,b])
A=A[::-1]
ans=n*(n-1)//2
Ans=[ans]
for i in range(m):
  a,b=A[i]
  if not same(a-1,b-1):
    ans-=(size(a-1)*size(b-1))
  Ans.append(ans)
  unite(a-1,b-1)
Ans=Ans[::-1][1:]
print(*Ans,sep="\n")