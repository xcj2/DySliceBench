N,M,K=map(int,input().split())
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]

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

ans=[0 for i in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    A,B=A-1,B-1
    union(A,B)
    ans[A]-=1
    ans[B]-=1
for i in range(N):
    ans[i]+=size(i)-1
for _ in range(K):
    C,D=map(int,input().split())
    C,D=C-1,D-1
    if(same(C,D)):
        ans[C]-=1
        ans[D]-=1
        
print(*ans)