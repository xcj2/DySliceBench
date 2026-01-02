from copy import *

def init(N,node,unit,func):
  n=1
  while n<N:
    n<<=1
  for i in range(n*2-1):
    if len(node)<=i:
      node.append(deepcopy(unit))
    else:
      node[i]=deepcopy(unit)
  node.append(func)
  node.append(unit)
  node.append(n)

def upd(node,x,a):
  y=node[-1]+x
  node[y-1]=a
  while y>1:
    y=y>>1
    node[y-1]=node[-3](node[(y<<1)-1],node[y<<1])

def query(node,l,r):
  x,y=l,r
  z=node[-1]-1
  r=node[-2]
  while True:
    if x==y:
      return r
    if x&1:
      r=node[-3](r,node[x+z])
      x+=1
    if y&1:
      r=node[-3](r,node[y+z-1])
    x>>=1
    y>>=1
    z>>=1
    if z==0:
      return r

def bis_min_k(node,k,cond):
  x=k+1
  while True:
    if node[-1]<=x:
      return x-node[-1]
    if cond(node[(x<<1)-1]):
      x=x<<1
    else:
      x=(x<<1)+1

def bis_min(node,l,r,cond):
  x,y=l,r
  z=node[-1]-1
  for i in range(30):
    if x+(1<<i)>y:
      break
    if x&(1<<i):
      if cond(node[z+(x>>i)]):
        return bis_min_k(node,z+(x>>i),cond)
      x+=(1<<i)
    if z==0:
      break
    z>>=1
  for i in range(29,-1,-1):
    if i and ((node[-1]-1)>>(i-1))==0:
      continue
    if x+(1<<i)>y:
      continue
    if (y-x)&(1<<i):
      if cond(node[((node[-1]-1)>>i)+(x>>i)]):
        return bis_min_k(node,((node[-1]-1)>>i)+(x>>i),cond)
      x+=(1<<i)
  return node[-1]

N,Q=map(int,input().split())
A=list(map(int,input().split()))
X=[]
init(N+1,X,-1,lambda x,y:max(x,y))
for i in range(N):
  upd(X,i,A[i])
t,a,b=0,0,0
for i in range(Q):
  t,a,b=map(int,input().split())
  if t==1:
    upd(X,a-1,b)
  elif t==2:
    print(query(X,a-1,b))
  else:
    a=bis_min(X,a-1,N,lambda x:b<=x)
    if a>N:
      print(N+1)
    else:
      print(a+1)