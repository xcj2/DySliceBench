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
# 集合の併合
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
par = [-1 for i in range(N)]
tmp = ((N * (N - 1)) // 2)
ab = [list(map(int, input().split())) for _ in range(M)]
ans = [0] * M
ans[M - 1] = tmp
for i in range(M - 1, 0, -1):
    fa = find(ab[i][0] - 1)
    fb = find(ab[i][1] - 1)
    ans[i - 1] = ans[i]
    if fa != fb:
        ans[i - 1] -= uCnt(fa) * uCnt(fb)
        unite(ab[i][0] - 1, ab[i][1] - 1)

for i in ans:
    print(i)