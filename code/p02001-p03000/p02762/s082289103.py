n,m,k=map(int,input().split())
par=[-1 for i in range(n)]

# this par & rank are initialized lists
def find(x):
    if par[x]<0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
 
def size(x):
    return -par[find(x)]
 
def unite(x,y):
    x,y=find(x),find(y)
    if x==y:
        return
    if x>y:
        x,y=y,x
    par[x]+=par[y]
    par[y]=x
 
def same(x,y):
    return find(x)==find(y)

ans=[-1 for i in range(n)]

for i in range(m):
  a,b=map(int,input().split())
  unite(a-1,b-1)
  ans[a-1]-=1
  ans[b-1]-=1

for i in range(k):
  a,b=map(int,input().split())
  if same(a-1,b-1):
    ans[a-1]-=1
    ans[b-1]-=1

for i in range(n):
  ans[i]+=size(i)

print(*ans)