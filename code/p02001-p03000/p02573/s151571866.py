# Union Find
#0オリジン以下注意

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
def unite(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きい方がx
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y] #ここで集合の個数を更新している
        par[y] = x
        return True
    
#xとyが同じ集合に含まれているかどうかを判定(同じ集合にあればTrue)
def same(x, y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#初期化
#根なら-size, 子なら親の頂点
n, m = map(int, input().split())
par = [-1]*n
for i in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
M = 0
for i in range(n):
    M = max(M, size(i))
print(M)

################以下にコードを書く
######2次元配列が与えられたら１次元に直す必要あり