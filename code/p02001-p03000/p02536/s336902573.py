def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x, y = find(x), find(y)
    if x == y: return False
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True

def same(x, y):
    return find(x) == find(y)

def size(x):
    return -par[find(x)]

N, M = map(int, input().split())
par = [-1]*N

for _ in range(M):
    a, b = map(int, input().split())
    unite(a-1, b-1)
par.sort()
cnt = 0
for i in range(N):
    if par[i] < 0:
        cnt += 1
print(cnt-1)