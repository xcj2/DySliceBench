from collections import deque
N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
B=[list(map(int,input().split())) for i in range(N)]
V=N*2+2
G=[[] for i in range(V)]
L=[0]*V
I=[0]*V
INF=10**15
def ae(fr,to,ca):
  global G
  G[fr].append([to,ca,len(G[to])])
  G[to].append([fr,0,len(G[fr])-1])

def bfs(s):
  global INF,L,V,G
  L=[-1]*V
  Q=deque()
  L[s]=0
  Q.append(s)
  while(len(Q)):
    x=Q.popleft()
    for i in range(len(G[x])):
      if G[x][i][1]>0 and L[G[x][i][0]]<0:
        L[G[x][i][0]]=L[x]+1
        Q.append(G[x][i][0]) 

def dfs(v,t,f):
  global I,G,V
  if v==t:
    return f
  for i in range(I[v],len(G[v])):
    if G[v][i][1]>0 and L[v]<L[G[v][i][0]]:
      d=dfs(G[v][i][0],t,min(f,G[v][i][1]))
      if d>0:
        G[v][i][1]-=d
        G[G[v][i][0]][G[v][i][2]][1]+=d
        return d
    I[v]+=1
  return 0

def mf(s,t):
  global L,I,INF,V
  fl=0
  while(True):
    bfs(s)
    if L[t]<0:
      break
    I=[0]*V
    f=0
    while(True):
      f=dfs(s,t,INF)
      if f<=0:
        break
      fl+=f
  return fl

for i in range(N):
  ae(0,i+1,1)
  ae(N+i+1,N*2+1,1)
  for j in range(N):
    if A[i][0]<B[j][0] and A[i][1]<B[j][1]:
      ae(i+1,N+j+1,1)
print(mf(0,N*2+1))