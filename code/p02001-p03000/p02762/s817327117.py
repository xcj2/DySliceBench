n,m,k = map(int,input().split())
par = [-1]*n
num = [0]*n
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
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

for i in range(m):
    a,b = map(int,input().split())
    unite(a-1, b-1)
    num[a-1] += 1
    num[b-1] += 1

edge = [[] for i in range(n)]

for i in range(k):
    c,d = map(int,input().split())
    edge[c-1].append(d-1)
    edge[d-1].append(c-1)

for i in range(n):
    cnt = size(i) - num[i] - 1
    for e in edge[i]:
        if same(e, i):
            cnt -= 1
    print(cnt, end=' ')