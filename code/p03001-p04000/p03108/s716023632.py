N,M=list(map(int,input().split()))
edge=[list(map(int,input().split())) for _ in range(M)]

current=N*(N-1)//2
ret=[0]*M

par=list(range(N+1))
cnt=[1]*(N+1)
rank=[0]*(N+1)

def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def same(x,y):
    return find(x)==find(y)

def size(x):
    return cnt[find(x)]

def unite(x,y):
    x=find(x)
    y=find(y)

    if x==y:
        return 0
    
    if rank[x]<rank[y]:
        cnt[y]+=size(x)
        par[x]=y
    else:
        cnt[x]+=size(y)
        par[y]=x
        if rank[x]==rank[y]:rank[x]+=1


for i in range(M-1,-1,-1):
    ret[i]=current

    a,b=edge[i]

    if not same(a,b):
        current-=size(a)*size(b)
        unite(a,b)

for r in ret:
    print(r)