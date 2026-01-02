N,M=map(int,input().split())
P=list(map(int,input().split()))

par=[i for i in range(N)]
rank=[1]*N

ans=0

def root(x):
    if par[x]==x:
        return x
    else:
        par[x]=root(par[x])
        return par[x]

def same(x,y):
    return root(x)==root(y)

def connect(x,y):
    if root(x)==root(y):
        return
    else:
        if rank[x]<rank[y]:
            x,y=y,x
        par[root(y)]=root(x)
        rank[y]+=1

for i in range(M):
    x,y=map(int,input().split())
    connect(x-1,y-1)

for i in range(N):
    if same(i,P[i]-1):
        ans+=1

print(ans)