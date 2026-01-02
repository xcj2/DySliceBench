n,m = map(int,input().split())
par = [-1]*(n+1)
def find(x):
    if par[x] < 0:
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
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
def size(x):
    return -par[find(x)]
mx = 0
for _ in range(m):
    s,t = map(int,input().split())
    unite(s,t)
for i in range(1,n+1):
    ans = size(i)
    if ans > mx:
        mx = ans
print(mx)