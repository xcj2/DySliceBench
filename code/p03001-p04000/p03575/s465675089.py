n, m = map(int, input().split())
a, b = [0] * m, [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

#union-find
#初期化 par:親の番号
#par = [i for i in range(n)]
#木の根を求める
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x] 
#xとyが同じ集合に属するか否か
def same(x, y):
    return root(x) == root(y)
#xとyの属する集合を併合
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    par[x] = root(y)

cnt = 0
for i in range(m):
    par = [k for k in range(n+1)]
    for j in range(m):
        if i == j:
            continue
        unite(a[j], b[j])
    if not same(a[i], b[i]):
        cnt += 1
print(cnt)