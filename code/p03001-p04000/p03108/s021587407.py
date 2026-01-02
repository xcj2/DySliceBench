N,M=map(int,input().split())

#Union-Find

par=[i for i in range(N)]
siz=[1 for _ in range(N)]
rank=[0 for _ in range(N)]
root=set()

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
            if b in root:
                root.remove(b)
            root.add(a)
            siz[a]+=siz[b]
        else:
            par[a]=b
            if a in root:
                root.remove(a)
            root.add(b)
            siz[b]+=siz[a]
            if rank[a]==rank[b]:
                rank[b]+=1
def size(a):
    return siz[find(a)]

def same(a,b):
    return find(a)==find(b)
    
edge=[]
for i in range(M):
    a,b=map(lambda x:int(x)-1,input().split())
    edge.append([a,b])
p=N*(N-1)//2
res=[p]
for i in reversed(range(1,M)):
    if(not same(edge[i][0],edge[i][1])):
        p=p-size(edge[i][0])*size(edge[i][1])
        union(edge[i][0],edge[i][1])
    res.append(p)
print(*res[::-1],sep='\n')