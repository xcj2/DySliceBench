N,M=map(int,input().split())
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

ab=[]
for i in range(M):
    A,B=map(int,input().split())
    A,B=A-1,B-1
    ab.append([A,B])
res=0

for i in range(M):
    par=[j for j in range(N)]
    siz=[1 for _ in range(N)]
    rank=[0 for _ in range(N)]
    for j in range(M):
        if(i==j):
            continue
        union(ab[j][0],ab[j][1])
    for i in range(1,N):
        if(not same(0,i)):
            res+=1
            break
print(res)