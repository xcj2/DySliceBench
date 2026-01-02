import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

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

#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

###具体例###
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    unite(a - 1, b - 1)

ans = 0

for i, j in enumerate(p):
    if same(i, j - 1):
        ans += 1

print(ans)