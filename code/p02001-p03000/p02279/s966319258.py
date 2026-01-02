import sys
sys.setrecursionlimit(2147483647)

class Node:
  def __init__(self,p,l,r):
    self.p=p
    self.l=l
    self.r=r

def getDepth(u):
  #d=0
  #while T[u].parent!=None:
  #  u=T[u].parent
  #  d+=1
  #return d
  return D[u]

def setDepth(u,p):
  global D
  D[u]=p
  if T[u].r!=-1:
    #print("debug:",T[u].r)
    setDepth(T[u].r,p)
  if T[u].l!=-1:
    setDepth(T[u].l,p+1)

def getChildren(u):
#def printChildren(u):
  C=[]
  c=T[u].l
  while c!=-1:
    #print(c,end=', ')
    C.append(str(c))
    c=T[c].r
  return C

n=int(input())
#T=[Node(-1,-1,-1)]*n
T=[Node(-1,-1,-1) for _ in range(n)]
for _ in range(n):
  C=list(map(int,input().split()))
  if C[1]>0:
    T[C[0]].l=C[2]
  k=C[1]
  for i in range(2,k+2):
    T[C[i]].p=C[0]
    if i+1<k+2:
      T[C[i]].r=C[i+1]

#for i in range(n):
#  print(i,":",T[i].r)
#exit(0)

r=-1
for i in range(n):
  if T[i].p==-1:
    r=i
    break
D=[-1]*n
setDepth(r,0)

for i in range(n):
  node=T[i]
  C=getChildren(i)
  d=getDepth(i)
  t='root' if T[i].p==-1 else 'leaf' if T[i].l==-1 else 'internal node'
  print('node '+str(i)+': parent = '+str(T[i].p)+', depth = '+str(d)+', '+t+', [',end='')
  print(', '.join(C),end='')
  print(']')

