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
        else:
            par[a]=b
            if rank[a]==rank[b]:
                rank[b]+=1
def same(a,b):
    return find(a)==find(b)
def Kruskal():
    cost=0
    Edge.sort(key=lambda x:x[2])
    for i in range(E):
        f,t,c=Edge[i]
        if(not same(f,t)):
            union(f,t)
            cost+=c
    return cost

N,E=map(int,input().split())
par=[i for i in range(N)]
rank=[0 for _ in range(N)]
Edge=[]
for i in range(E):
    s,t,w=map(int,input().split())
    Edge.append([s,t,w])
res=Kruskal()
print(res)
