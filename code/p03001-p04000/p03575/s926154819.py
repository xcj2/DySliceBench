import sys
input=lambda: sys.stdin.readline().rstrip()
n,m=map(int,input().split())
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

AB=[]
for i in range(m):
  AB.append(tuple(int(i) for i in input().split()))
ans=0
for i in range(m):
  par=[-1]*n
  for j in range(m):
    if j==i:
      continue
    else:
      a,b=AB[j]
      unite(a-1,b-1)
  for i in range(n):
    find(i)
  if -min(par)<n:
    ans+=1
print(ans)