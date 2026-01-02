n,q=map(int,input().split())

#Union-Find木の構築
par=[-1]*n

def find(v):
    if par[v]<0:
        return v
    else:
        par[v]=find(par[v])
        return par[v]

def union(u,v):
    root_u=find(u)
    root_v=find(v)

    if root_u==root_v:
        return 
    
    #大きい方に接続
    if par[root_u]>par[root_v]:
        par[root_v]+=par[root_u]
        par[root_u]=root_v
    else:
        par[root_u]+=par[root_v]
        par[root_v]=root_u

def same(u,v):
    if find(u)==find(v):
        return True
    else:
        return False

for i in range(q):
    c,x,y=map(int,input().split())
    if c==0:
        union(x,y)
    else:
        ans=same(x,y)
        if ans:
            print(1)
        else:
            print(0)


