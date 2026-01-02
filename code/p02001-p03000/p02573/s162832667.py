n,m=map(int,input().split())
par=[-1]*n

# this par & rank are initialized lists
def find(x):
    global par
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
        
def unite(x,y):
    x,y=find(x),find(y)
    global par
    if x==y:return False
    else:
        if par[x]>par[y]:x,y=y,x
        par[x]+=par[y]
        par[y]=x
        return True

def size(x):
    return -par[find(x)]
def same(x,y):
    return find(x)==find(y)


for i in range(m):
  a,b=map(int,input().split())
  unite(a-1,b-1)

par.sort()
print(-par[0])