n,m,k=map(int,input().split())
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

F=[-1]*n
for _ in range(m):
  a,b=map(int,input().split())
  unite(a-1,b-1)
  F[a-1]-=1
  F[b-1]-=1
for _ in range(k):
  a,b=map(int,input().split())
  if same(a-1,b-1):
    F[a-1]-=1
    F[b-1]-=1
for i in range(n):
  F[i]+=size(i)
print(*F)
