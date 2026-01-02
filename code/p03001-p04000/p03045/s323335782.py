N,M = map(int,input().split())

par = [-1]*(N+1)


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

for i in range(M):
    x,y,z = map(int,input().split())
    unite(x,y)

ans = 0
counted = [False] * (N+1)
for i in range(1,N+1):
    root = find(i)
    if not counted[root]:
        ans += 1
        counted[root] = True
print(ans)
