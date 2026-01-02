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

def upd(node,x,a):
  y=(len(node)>>1)+x-1
  node[y]=a
  while y:
    y=(y-1)>>1
    node[y]=node[-2](node[(y<<1)+1],node[(y+1)<<1])

def query(node,l_q,r_q,k,l_m,r_m):
  if r_q<=l_m or r_m<=l_q:
    return node[-1]
  if l_q<=l_m and r_m<=r_q:
    return node[k]
  l_a=query(node,l_q,r_q,2*k+1,l_m,(l_m+r_m)//2)
  r_a=query(node,l_q,r_q,2*k+2,(l_m+r_m)//2,r_m)
  return node[-2](l_a,r_a)

N,Q=map(int,input().split())
node=[]
init(N,node,(1<<31)-1,lambda x,y:min(x,y))
c,x,y=0,0,0
for i in range(Q):
  c,x,y=map(int,input().split())
  if c:
    print(query(node,x,y+1,0,0,len(node)>>1))
  else:
    upd(node,x,y)
