# coding: utf-8
import collections

N,M,K=map(int,input().split())
F=[[] for i in range(N+1)]
Bl=[[] for i in range(N+1)]

par = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]
 
def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
 
 
def unite(x,y):
    rx=find(x)
    ry=find(y)

    if rx==ry:
        return
    
    
    if rank[rx]<rank[ry]:
        par[rx]=ry
    else:
        par[ry]=rx

    if rank[rx]==rank[ry]:
        rank[rx]+=1
 

def some(x,y):
    return find(x)==find(y)
 
for i in range(M):
    A,B=map(int,input().split())
    unite(A,B)
    F[A].append(B)
    F[B].append(A)

for i in range(K):
    C,D=map(int,input().split())
    Bl[C].append(D)
    Bl[D].append(C)

ans=[0 for i in range(N)]
for i in range(N):
    find(i+1)
c = collections.Counter(par)

for i in range(N):
    ans[i]+=c[find(i+1)]-1
    ans[i]-=len(F[i+1])
    for j in range(len(Bl[i+1])):
        if some(i+1,Bl[i+1][j]):
            ans[i]-=1
print(*ans)    
