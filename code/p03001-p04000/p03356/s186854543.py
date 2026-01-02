def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
# 同一の集合の判定
def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False
# 集合の辺豪
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

# 集合の数
def uCnt(x):
    return -par[find(x)]

N, M = map(int, input().split())
p = list(map(int, input().split()))
par = [-1 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b)

ans = 0
for i in range(N):
    if same(i, p[i] - 1):
        ans += 1

print(ans)