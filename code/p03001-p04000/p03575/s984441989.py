N,M=map(int,input().split())
a=[0 for i in range(M)]
b=[0 for i in range(M)]
for i in range(M):
    a[i],b[i]=map(int,input().split())
    a[i]-=1
    b[i]-=1
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
ans=0
for i in range(M):
    init(N)
    for j in range(M):
        if i==j:
            continue
        unite(a[j],b[j])
    flag=0
    for j in range(N):
        for k in range(N):
            if find(j)!=find(k):
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        ans+=1
print(ans)

