# Union Find

# xの根を求める
def find_root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find_root(x)
    y = find_root(y)

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
    return find_root(x) == find_root(y)


# xが属する集合の個数
def size(x):
    return -par[find_root(x)]


# 初期化
# 根なら-size,子なら親の頂点

#nは要素数
n,m = map(int,input().split())
lis = [list(map(int,input().split())) for i in range(m)]
par = [-1] * n

hazime = n * (n-1) // 2

ans = []
num = 0
for a,b in lis[::-1]:
    a -= 1
    b -= 1
    x = find_root(a)
    y = find_root(b)
    if x != y:
        num += par[x] * par[y]
    unite(a,b)
    ans.append(num)
ans.insert(0,0)
  # print(ans)
for i in range(1,m+1):
    print(hazime-ans[-i-1])