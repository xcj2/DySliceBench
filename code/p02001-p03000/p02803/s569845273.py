import numpy as np
from copy import deepcopy
temp=list(map(int, input().split()))
R=temp[0]
C=temp[1]

color=np.zeros((R,C)).astype(int)

for i in range(R):
  temp=input()
  a=np.zeros(C).astype(int)
  for j in range(C):
      if temp[j]=='#':
        a[j]=1
      else:
        a[j]=0
  color[i]=a
  
def Adj(u):
  adj=[]
  for v in [(u[0]-1,u[1]),(u[0]+1,u[1]),(u[0],u[1]-1),(u[0],u[1]+1)]:
      if v[0]>=0 and v[0]<R and v[1]>=0 and v[1]<C:
        adj.append(v)
  return adj  

def BFS(s,c,d):
  ma=0
  Q=[s]
  while Q !=[]:
    u=Q[0]
    del Q[0]
    if d[u[0],u[1]]>ma:
      ma=d[u[0],u[1]]
    for v in Adj(u):  
      if c[v[0],v[1]]==0:
        c[v[0],v[1]]=1
        d[v[0],v[1]]=d[u[0],u[1]]+1
        Q.append(v)
  return ma
        
def main():
  ma=0
  for sx in range(R):
    for sy in range(C):
      if color[sx,sy]==0:
        d=np.zeros((R,C)).astype(int)
        c=deepcopy(color)
        c[sx,sy]=1
        ma=max(BFS((sx,sy),c,d),ma)
  print(ma)

main()
