n,m = map(int,input().split())
p = list(map(int,input().split()))
x = [list(map(int,input().split())) for _ in range(m)]

par = [0]
rank = [0]
def init(n):
    for i in range(n):
        par.append(i+1)
        rank.append(0)

def find(x):
    if par[x]==x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    elif rank[x]<rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x]+=1

def same(x,y):
    return find(x)==find(y)

init(n)
for i in range(m):
    unite(x[i][0],x[i][1])

ans = 0
for i in range(n):
    if same(i+1,p[i]):
        ans+=1
print(ans)