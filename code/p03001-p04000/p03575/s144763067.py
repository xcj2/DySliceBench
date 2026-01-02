N,M=map(int,input().split())
ab= [list(map(int, input().split())) for i in range(M)]

def root(val):
    if parent[val]==val:
        return val
    else:
        parent[val]=root(parent[val])
        return parent[val]

def same(x,y):
    return root(x)==root(y)

def unite(x,y):
    xr=root(x)
    yr=root(y)
    if xr==yr :return
    if rank[xr]<rank[yr]:
        parent[xr]=yr
    else:
        parent[yr]=xr
        if rank[xr]==rank[yr]:
            rank[xr]+=1
ct=0
for i in range(M):
    parent=list(range(N))
    rank = [0]*N
    for a,b in (ab[:i]+ab[i+1:]):
        unite(a-1,b-1)
    for j in range(1,N):
        if not same(0,j):
            ct+=1
            break
print(ct)