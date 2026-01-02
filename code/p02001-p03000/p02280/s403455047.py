from collections import deque

class Node:
  def __init__(self,l,r,p):
    self.l=l
    self.r=r
    self.p=p

n=int(input())
#T=[Node(-1,-1,-1)]*n
T=[Node(-1,-1,-1) for _ in range(n)]
for _ in range(n):
  i,l,r=map(int,input().split())
  T[i].l=l
  T[i].r=r
  if l!=-1:
    T[l].p=i
  if r!=-1:
    T[r].p=i

#for i in range(n):
#  print("debug:",T[i].p)

H=[-1]*n
def setHeight(u):
  h1=0
  h2=0
  if T[u].r!=-1:
    h1=setHeight(T[u].r)+1
  if T[u].l!=-1:
    h2=setHeight(T[u].l)+1
  H[u]=max(h1,h2)
  return H[u]

D=[-1]*n
def setDepth(u,d):
  if u==-1: return
  D[u]=d
  setDepth(T[u].r,d+1)
  setDepth(T[u].l,d+1)

def getSubling(u):
  if T[u].p==-1:
    return -1
  if T[T[u].p].l!=u and T[T[u].p].l!=-1:
    return T[T[u].p].l
  if T[T[u].p].r!=u and T[T[u].p].r!=-1:
    return T[T[u].p].r
  return -1



root=-1
for i in range(n):
  if T[i].p==-1:
    root=i
    break

setHeight(root)
setDepth(root,0)

#d=deque()
#d.append(T[root].left)
#d.append(T[root].right)
#while len(d)>0:
#  tmp=d.popleft()
#  d.append(tmp.left)
#  d.append(tmp.right)

#node id: parent = p, siling = s, degree = deg, depth = dep, height = h, type
for i in range(n):
  node=T[i]
  deg=0
  if node.l!=-1:
    deg+=1
  if node.r!=-1:
    deg+=1
  s=getSubling(i)
  t='root' if i==root else 'leaf' if deg==0 else 'internal node'
  print('node ',i,': parent = ',node.p,', sibling = ',s,', degree = ',deg,', depth = ',D[i],', height = ',H[i],', ',t,sep='')

