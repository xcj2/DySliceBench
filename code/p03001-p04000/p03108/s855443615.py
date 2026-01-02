n, m = map(int, input().split())
par = [-1] * n  # 親だった場合は-(その集合のサイズ)


# xがどのグループに属しているか調べる
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return find(par[x])


# 自分のいるグループの数
def size(x):
    return -par[find(x)]


# xとyの属する集合を併合
def unite(x, y):
    # 根を探す
    x, y = find(x), find(y)

    # 根が一緒
    if x == y:
        return

    # 大きい方に小さい方をくっつける
    if size(x) < size(y):
        x, y = y, x

    # xのサイズを更新
    par[x] += par[y]
    # yの親をxにする
    par[y] = x


# 同じ集合に属するか判定
def same(x, y):
    return find(x) == find(y)


bridges = [list(map(int, input().split())) for _ in range(m)]
bridges.reverse()
huben = n * (n - 1) // 2
ans = []
for i in range(m):
    ans.append(huben)
    a, b = bridges[i]
    a, b = a - 1, b - 1
    if same(a, b):
        continue
    else:
        huben -= size(a) * size(b)
        unite(a, b)
ans.reverse()
for i in range(m):
    print(ans[i])
