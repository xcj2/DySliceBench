n, q = map(int, input().split())
com, x, y = [0] * q, [0] * q, [0] * q
for i in range(q):
    com[i], x[i], y[i] = map(int, input().split())

#初期化 par:親の番号 rank:高さ
par = [i for i in range(n)]
rank = [0 for _ in range(n)]
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
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1

#クエリ
for i in range(q):
    if com[i] == 0:
        unite(x[i], y[i])
    else:
        if same(x[i], y[i]):
            print(1)
        else:
            print(0)
