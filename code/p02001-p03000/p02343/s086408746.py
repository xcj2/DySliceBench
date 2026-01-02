n,q = map(int,input().split())

par = [-1]*(n+1)

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

for _ in range(q):
    c,x,y = map(int,input().split())
    if c == 0:
        unite(x,y)
    else:
        if same(x,y):print(1)
        else:print(0)
