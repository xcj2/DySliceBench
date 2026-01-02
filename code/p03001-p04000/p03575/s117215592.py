N,M = map(int,input().split())



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

a = [0]*M
b = [0]*M
for i in range(M):
    a[i], b[i] = map(int,input().split())
    a[i] -= 1
    b[i] -= 1

# 一つの辺以外を繋いでその辺の両端の点が同じ集合に属していたらその辺は橋ではない
ans = 0
for i in range(M):
    par = [-1] * (N + 1)
    for j in range(M):
        if i != j:
            unite(a[j],b[j])
    if not same(a[i],b[i]):
        ans += 1
print(ans)
