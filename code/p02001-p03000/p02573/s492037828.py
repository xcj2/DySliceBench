#親要素を示す
par = {}
size_list = []

# 初期化 -- すべての要素が根である --
def init(n):
    for i in range(n):
        par[i] = i
        size_list.append(1)
    return 

# 根を求める
def root(x):
    if par[x] == x:
        return x
    else:
        #根の直下にxを置く
        par[x] = root(par[x])
        return par[x]

#　同じ集合に属するかどうかは根が同じかで判定
def same(x, y):
    return root(x) == root(y)

#　別々のUnion同士を融合する
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    else:
        par[x] = y
        size_list[y] += size_list[x]
        size_list[x] = 0
        return


N, M = map(int, input().split())
init(N)
for mi in range(M):
    a, b = map(int, input().split())
    unite(a-1,b-1)
print(max(size_list))