import sys
input = sys.stdin.readline
n,m,k=map(int,input().split())
friend=[[]for _ in range(n+1)]
block=[[] for _ in range(n+1)]
#union-find
par=[-1]*(n+1)
def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def size(x):
    return -par[find(x)]
def unite(x,y):
    if find(x)==find(y):
        return False
    if size(x)<size(y):
        x,y=y,x
    X=find(x)
    Y=find(y)
    par[X]+=par[Y]
    par[Y]=X
    return True
def is_same(x,y):
    return find(x)==find(y)

for _ in range(m):
    a,b=map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
    unite(a,b)
for _ in range(k):
    c,d=map(int,input().split())
    if is_same(c,d):
        block[c].append(d)
        block[d].append(c)
ans=[0]*(n+1)

for i in range(1,n+1):
    f=size(i)-1-len(friend[i])
    b=len(block[i])
    ans[i]=f-b
print(*ans[1:], sep=' ')