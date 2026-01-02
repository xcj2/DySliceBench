# https://atcoder.jp/contests/arc097/tasks/arc097_b
# union-findらしい

n, m = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))

# xの根を求める
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
par = [-1] * n

for _ in range(m):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1 , bi - 1
    unite(ai, bi)

# print(par)
# print(P)

count = 0
for i in range(n):
    if same(i, P[i]):
        count += 1

print(count)