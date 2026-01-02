n,m,k=map(int,input().split())
 
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
 
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True
 
def same(x,y):
    return find(x) == find(y)
 
def size(x):
    return -par[find(x)]
 
par = [-1]*n
 
ans=[0]*n
nxt=[0]*n
block=[[] for _ in range(n)]
 
for _ in range(m):
    a,b=map(int,input().split())
    unite(a-1,b-1)
    nxt[a-1]+=1
    nxt[b-1]+=1
 
for _ in range(k):
    c,d=map(int,input().split())
    block[c-1].append(d-1)
    block[d-1].append(c-1)
 
for i in range(n):
    ans[i]=size(i)-nxt[i]-1
    for j in block[i]:
        if same(j,i):
            ans[i]-=1
print(*ans)