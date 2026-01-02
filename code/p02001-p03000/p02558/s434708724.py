#https://qiita.com/white1107/items/52fd4149bb1846862e38

N, Q = map(int,input().split())
par = [i for i in range(N+1)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y
    
    
for i in range(Q):
    t, u, v = map(int,input().split())
    if t == 0:
        unite(u,v)
    else:
        if same(u,v):
            print(1)
        else:
            print(0)