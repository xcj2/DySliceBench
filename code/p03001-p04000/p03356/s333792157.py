n, m = map(int, input().split())
p = [int(x) for x in input().split()]

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
    return par[find(x)]

for i in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

ans = 0
for i in range(n):
    if same(p[i]-1, i):
        ans += 1
print(ans)