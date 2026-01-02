n, m, k = map(int, input().split())

par = [-1 for _ in range(n)]

def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def same(x, y):
    return find(x) == find(y)

def size(x):
    return -par[find(x)]

ans = [-1]*n
for i in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)
    ans[a-1] -=1
    ans[b-1] -=1

for j in range(k):
    c, d = map(int, input().split())
    if same(c-1, d-1):
        ans[c-1] -=1
        ans[d-1] -=1

for i in range(n):
    ans[i] += size(i)

print(*ans)