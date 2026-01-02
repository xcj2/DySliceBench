def find(x):
    if(par[x]==x):
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if(a==b):
        return 0
    else:
        if rank[a]>rank[b]:
            par[b]=a
            siz[a]+=siz[b]
        else:
            par[a]=b
            siz[b]+=siz[a]
            if rank[a]==rank[b]:
                rank[b]+=1
def size(a):
    return siz[find(a)]
def same(a,b):
    return find(a)==find(b)
    
N,M=map(int,input().split())
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]

p=list(map(lambda x:int(x)-1,input().split()))
dic={p[i]:i for i in range(N)}

for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    union(dic[x],dic[y])
cnt=0
for i in range(N):
    if same(i,p[i]):
        cnt+=1
print(cnt)