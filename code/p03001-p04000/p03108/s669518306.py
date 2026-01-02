N,M=map(int,input().split())
D=[list(map(int, input().split())) for _ in range(M)]
C=D[::-1]
par=[i for i in range(N)]
rank=[0]*(N)
size=[1]*N

def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]

def same(x,y):
  return find(x)==find(y)

def union(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return 
  if rank[x]>rank[y]:
    par[y]=x
    size[x]+=size[y]
  else:
    par[x]=y
    size[y]+=size[x]
    if rank[x]==rank[y]:
      rank[y]+=1

A=[]
d=0
for a,b in C:
  a-=1
  b-=1
  x=find(a)
  y=find(b)
  if x!=y:
    d+=size[x]*size[y]
  union(a,b)
  A.append(d) 
A=A[::-1]
A.append(0)
a=N*(N-1)//2
for i in range(1,M+1):
  print(a-A[i])