N,M=map(int,input().split())
par=[0 for i in range(N)]
rnk=[0 for i in range(N)]
def init(n):
    for i in range(N):
        par[i]=i
        rnk[i]=0
def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if (rnk[x]<rnk[y]):
        par[x]=y
    else:
        par[y]=x
        if(rnk[x]==rnk[y]):
            rnk[x]+=1
def same(x,y):
    return find(x)==find(y)

p=[int(i)-1 for i in input().split()]
init(N)
for i in range(M):
    x,y=map(int,input().split())
    unite(x-1,y-1)
ans=0
for i in range(N):
    if same(i,p[i]):
        ans+=1
print(ans)
