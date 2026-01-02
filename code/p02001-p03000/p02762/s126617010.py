#木の根を得る
def root(x):
    while par[x] >= 0:
        x = par[x]
    return x

#木の併合
def unite(x,y):
    rx = root(x)
    ry = root(y)
    if rx != ry:
        if rx > ry:
            rx,ry = ry,rx
        par[rx] += par[ry]
        par[ry] = rx

#2つのデータx,yが属する木が同じならtrueを返す
def same(x,y):
    rx = root(x)
    ry = root(y)
    return rx == ry

#属する木のサイズ
def size(x):
    return -par[root(x)]

#ABC157D
N,M,K = map(int,input().split())
par = [-1]*N
g = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    A,B = A-1,B-1
    unite(A,B)
    g[A].append(B)
    g[B].append(A)

for i in range(K):
    C,D = map(int,input().split())
    C,D = C-1,D-1
    if same(C,D):
        g[C].append(D)
        g[D].append(C)

for i in range(N):
    print(size(i)-len(g[i])-1,end=' ')