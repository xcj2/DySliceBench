n,m=map(int,input().split())
#union-find
par=[-1]*(n+1)
def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def size(x):
    oya=find(x)
    return -par[oya]
def unite(x,y):
    if find(x)==find(y):
        return False
    else:
        if size(y)>size(x):
            y,x=x,y  #xを大きい親にしておくか
        oya_x=find(x)
        oya_y=find(y)
        par[oya_x]-=size(oya_y)  #xの大きさをyにしておく
        par[oya_y]=oya_x  #yの親をxに
        return True

def is_same(x,y):
    return find(x)==find(y)
for _ in range(m):
    x,y,z=map(int,input().split())
    unite(x,y)
ans_set=set()
for i in range(1,n+1):
    ans_set.add(find(i))
print(len(ans_set))