n,m,k=map(int,input().split())
def root(x):
    while par[x]>=0:x=par[x]
    return x
def unite(x,y):
    x,y=root(x),root(y)
    if x!=y:
        if x>y:x,y=y,x
        par[x]+=par[y]
        par[y]=x
par=[-1]*n
def same(x,y):
    return root(x)==root(y)
def size(x):
  return-par[root(x)]
g=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    unite(a,b)
    g[a].append(b)
    g[b].append(a)
ss=[size(i)-len(g[i])-1 for i in range(n)]
for  i in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    if same(c,d):
        ss[c]-=1
        ss[d]-=1
print(*ss)