#ABC094-E
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
n,m=IL()
#Union-Find木
par=[]
rank=[]
def init(a): #初期化
    for i in range(a):
        par.append(i)
        rank.append(0)
def find(x): #根を見つける
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
    return par[x]
def unite(x,y): #併合
    x=find(x)
    y=find(y)
    if rank[x]==rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x]+=1
    return
def same(x,y): #同じ集合か判定
    return find(x)==find(y)

init(n)
gn=n
for i in range(m):
    x,y,z=IL()
    if find(x-1)!=find(y-1):
        n-=1
        unite(x-1,y-1)
print(n)