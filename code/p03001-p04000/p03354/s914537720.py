N,M = map(int,input().split())

par = [i for i in range(N+1)]

# 木の根を求める
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

# xとyが同じ集合に属するか否か
def bool_same(x,y):
    return root(x) == root(y)

# xとyの属する集合を併合
def unite(x,y):
    x = root(x)
    y = root(y)
    if x != y:
        par[x] = y

p = [0] + list(map(int,input().split()))

for i in range(M):
    a,b = map(int,input().split())
    unite(a,b)

ans = 0
for i in range(1,N+1):
    if bool_same(i,p[i]):
        ans += 1

print(ans)

