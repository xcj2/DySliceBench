N, M = map(int, input().split())
# N頂点M辺のグラフ
# 自己ループ (a1==b1)は存在しない
# 二重辺(a1,b1 と a2,b2が同じもの)は存在しない
# 一辺取り除いた時に分離してしまう辺を橋と呼ぶ


# union find
# 最初は全て値であるとして初期化する parents[i] = i

# root(x) => xの根を返す関数
# unit(x,y) => root(x)とroot(y)が同じであればそのまま。違う場合は、xの根であるroot(x)をyの根であるroot(y)につける. 根が同じでない二つの木を合併する。
# same(x,y) => 二つのデータx,yが属する木が同じ場合、trueを返す。if root(x) == root(y)するだけ
parents = None


def root(x):
    if parents[x] == x:
        return x
    parents[x] = root(parents[x])
    return parents[x]


count = 0


def unit(x, y):
    root_x = root(x)
    root_y = root(y)
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


def same(x, y):
    root_x = root(x)
    root_y = root(y)
    return (root_x == root_y)


es = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    es.append((a, b))

ans = 0
for i in range(M):
    parents = [k for k in range(N)]
    for j, e in enumerate(es):
        if j == i:
            continue
        a, b = e
        unit(a, b)
    a, b = es[i]
    if not same(a, b):
        ans += 1
print(ans)
