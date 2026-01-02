#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]


N, M, K = map(int, input().split())

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    unite(a-1, b-1)

ans = [size(v) - len(G[v]) - 1 for v in range(N)]

H = [[] for _ in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    if same(c-1, d-1):
        ans[c-1] -= 1
        ans[d-1] -= 1
    
print(' '.join(map(str, ans)))