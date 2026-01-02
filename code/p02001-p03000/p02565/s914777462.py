import sys
sys.setrecursionlimit(10**9)
def SCC(G):
  D=[]
  C=[len(G)-1]
  U=[1]*len(G)
  def DFS(x):
    if U[x]:
      U[x]=0
      for i in range(len(G[x])):
        DFS(G[x][i])
      D.append(x)
  
  for i in range(len(G)):
    if U[i]:
      DFS(i)
  GR=[[] for i in range(len(G))]
  for i in range(len(G)):
    for j in range(len(G[i])):
      GR[G[i][j]].append(i)
  R=[]
  U=[1]*len(G)
  def DFSR(x):
    if U[x]:
      R[-1].append(x)
      U[x]=0
      for i in range(len(GR[x])):
        DFSR(GR[x][i])
  
  for i in range(len(G)-1,-1,-1):
    if U[D[i]]:
      R.append([])
      DFSR(D[i])
  return R

N,D=map(int,input().split())
G=[[] for i in range(2*N)]
X=[list(map(int,input().split())) for i in range(N)]
for i in range(N):
  for j in range(i+1,N):
    for k in range(2):
      for l in range(2):
        if abs(X[i][k]-X[j][l])<D:
          G[k*N+i].append((l^1)*N+j)
          G[l*N+j].append((k^1)*N+i)
G=SCC(G)
C=[0]*(2*N)
for i in range(len(G)):
  for j in range(len(G[i])):
    C[G[i][j]]=i
for i in range(N):
  if C[i]==C[i+N]:
    print('No')
    exit()
print('Yes')
for i in range(N):
  if C[i]>C[i+N]:
    print(X[i][0])
  else:
    print(X[i][1])