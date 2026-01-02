import sys
input = sys.stdin.readline
n,m=map(int,input().split())
par = [-1]*n
wei = [0]*n

def find(x):
  if par[x]<0:
    return x
  else:
    px=find(par[x])
    wei[x]+=wei[par[x]]
    par[x]=px
    return px

def weight(x):
  find(x)
  return wei[x]


def unite(x,y,w):
  w+=wei[x]-wei[y]
  x=find(x)
  y=find(y)    
  if x==y:
    return False
  else:
    if par[x]>par[y]:
      x,y=y,x
      w=-w
    par[x]+=par[y]
    par[y]=x
    wei[y]=w
    return True

def same(x,y):
    return find(x)==find(y)

def size(x):
    return -par[find(x)]

def diff(x,y):
    return weight(y)-weight(x)
flag=1
for i in range(m):
  l,r,d=map(int,input().split())
  if same(l-1,r-1):
    if d!=diff(l-1,r-1):
      flag=0
  else:
    unite(l-1,r-1,d)
print("No" if flag==0 else "Yes")