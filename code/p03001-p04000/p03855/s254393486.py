from collections import Counter
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

N,K,L=map(int,input().split())
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]

for i in range(K):
    p,q=map(lambda x:int(x)-1,input().split())
    union(p,q)
    
road=[find(i) for i in range(N)]
par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]
for i in range(L):
    r,s=map(lambda x:int(x)-1,input().split())
    union(r,s)
li=[(road[i],find(i)) for i in range(N)]
c=Counter(li)
for i in range(N):
    print(c[li[i]],end=' ')
print()