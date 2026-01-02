N, M = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]

par = list(range(N+1))
rank = [0]*(N+1)


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1


def same(x, y):
    return find(x) == find(y)


ans = 0
for i in range(M):
    unite(xy[i][0], xy[i][1])

for i in range(N):
    if same(p[i], par[i+1]):
        ans += 1
print(ans)
