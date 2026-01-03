n,m=map(int,input().split())
par=[-1]*(n+m)

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

for i in range(n):
  KL=[int(i) for i in input().split()]
  for j in range(1,len(KL)):
    unite(i,n+KL[j]-1)
chk=True
for i in range(1,n):
  if not same(0,i):
    chk=False
print("YES" if chk==True else "NO")