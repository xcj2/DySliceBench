import sys
input=lambda: sys.stdin.readline().rstrip()
n,m=map(int,input().split())
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

AB=[]
for i in range(m):
  AB.append(tuple(int(i)-1 for i in input().split()))
Ans=[n*(n-1)//2]
for i in range(m)[::-1]:
  a,b=AB[i]
  if same(a,b):
    Ans.append(Ans[-1])
  else:
    Ans.append(Ans[-1]-size(a)*size(b))
    unite(a,b)
Ans=Ans[::-1][1:]
for a in Ans:
  print(a)