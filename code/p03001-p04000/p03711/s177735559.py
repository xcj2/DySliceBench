#062-A
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

init(12)
unite(0,2)
unite(0,4)
unite(0,6)
unite(0,7)
unite(0,9)
unite(0,11)
unite(3,5)
unite(3,8)
unite(3,10)

x,y=map(int,input().split())
print('Yes' if same(x-1,y-1) else 'No')