import sys
sys.setrecursionlimit(10**7)
def dfs(v,p,d):
    dist[v]=d
    for nv in G[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)
def getSP(v,d):
    p=v
    if dist[v]==d:
        return v
    for nv in G[v]:
       if dist[nv]<dist[v]:
           p=getSP(nv,d)
    return p
    
def Sdepth(v):
    res=1
    if not G[v]:
        return 1
    for nv in G[v]:
        if dist[nv]<dist[v]:
            continue
        res+=Sdepth(nv)
    return res
    
N=int(input())
G=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)
dist=[-1]*N
dfs(0,-1,0)
P=(dist[N-1]-1)//2
sp=getSP(N-1,dist[N-1]-P)
dep=Sdepth(sp)
Sunu=dep-(dist[N-1]-dist[sp]+1)
Fene=N-dep-dist[sp]
if dist[N-1]%2:
    print('Fennec' if Fene>Sunu else 'Snuke')
else:
    print('Fennec' if Fene>=Sunu else 'Snuke')