# coding: utf-8
# Your code here!

n,m = map(int,input().split())

par = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def unite(x,y):
    rx=find(x)
    ry=find(y)
    
    if rx==ry:
        return
    
    if rank[rx]<rank[ry]:
        par[rx]=ry
    else:
        par[ry]=rx
        
    if rank[rx]==rank[ry]:
        rank[rx]+=1

def some(x,y):
    return find(x)==find(y)

for i in range(m):
    x,y,z=map(int,input().split())
    unite(x,y)

for i in range(1,n+1):
    find(i)
    
ans=len(set(par))-1

print(ans)
