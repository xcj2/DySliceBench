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

H,W,N=map(int,input().split())
S=[[] for i in range(H+1)]
T=[]
init(W+3,T,0,lambda x,y:max(x,y))
X=[tuple(map(int,input().split())) for i in range(N)]
for i in range(N):
  S[X[i][0]].append(X[i][1])
  upd(T,X[i][1]+1,T[(len(T)>>1)+X[i][1]]+1)
P=0
Q=0
for i in range(1,H+1):
  Q=len(S[i])
  for j in range(len(S[i])):
    upd(T,S[i][j]+1,T[(len(T)>>1)+S[i][j]]-1)
  P=max(P,Q+T[0])
  for j in range(len(S[i])):
    upd(T,S[i][j]+1,T[(len(T)>>1)+S[i][j]]+1)
print(P)
