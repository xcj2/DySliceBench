h,w=map(int,input().split())
P=[]
for i in range(h):
  C=[str(_) for _ in input()]
  P+=C
par=[[-1,0,0] for _ in range(h*w)]
def find(x):
  if par[x][0]<0:
    return x
  else:
    par[x][0]=find(par[x][0])
    return par[x][0]
def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return False
  else:
    if par[x][0]>par[y][0]:
      x,y=y,x
    par[x][0]+=par[y][0]
    par[y][0]=x
    return True
def same(x,y):
  return find(x)==find(y)
def size(x):
  return -par[find(x)][0]
for i in range(h*w):
  if P[i]=="#":
    par[i][1]+=1
    if (i+1)%w!=0 and P[i+1]==".":
      unite(i,i+1)
    if (i+w)<(h*w) and P[i+w]==".":
      unite(i,i+w)
  else:
    par[i][2]+=1
    if (i+1)%w!=0 and P[i+1]=="#":
      unite(i,i+1)
    if (i+w)<(h*w) and P[i+w]=="#":
      unite(i,i+w)
ans=0
for p,x,y in par:
  if p>=0:
    par[find(p)][1]+=x
    par[find(p)][2]+=y
for p,x,y in par:
  if p<-1:
    ans+=x*y
print(ans)