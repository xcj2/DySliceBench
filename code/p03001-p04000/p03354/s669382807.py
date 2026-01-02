# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # sizeの大きいほうがx
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# xとyが同じ集合に属するかの判定
def same(x, y):
    return find(x) == find(y)


# xが属する集合の個数
def size(x):
    return -par[find(x)]

# 初期化
# 根なら-size,子なら親の頂点
N,M = map(int,input().split())
par = [-1]*(N+1)
p = list(map(int,input().split()))
for _ in range(M):
    x,y = map(int,input().split())
    unite(x,y)
ans = 0
for i, pi in enumerate(p,1):
    if same(i,pi):
        ans += 1
print(ans)