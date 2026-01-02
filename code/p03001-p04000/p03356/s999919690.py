n,m=map(int,input().split())
P=[int(i) for i in input().split()]
PP=[0]*n
for i in range(n):
  PP[P[i]-1]=i+1
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
  x,y=map(int,input().split())
  unite(x-1,y-1)
ans=0
for i in range(n):
  if same(i,PP[i]-1):
    ans+=1
print(ans)