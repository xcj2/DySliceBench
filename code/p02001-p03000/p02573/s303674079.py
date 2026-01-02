n, m = (int(x) for x in input().split())
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
g = [[] for _ in range(n+1)]
for _ in range(m):
    s,t = map(int,input().split())
    unite(s,t)
    g[s].append(t)
    g[t].append(s)
ma = 0
for i in range(1,n+1):
    ans = size(i)
    if ma<ans:
        ma = ans
print(ma)
