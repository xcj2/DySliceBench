n, q = map(int, input().split())

# union find
# 最初は全て値であるとして初期化する parents[i] = i

# root(x) => xの根を返す関数
# unit(x,y) => root(x)とroot(y)が同じであればそのまま。違う場合は、xの根であるroot(x)をyの根であるroot(y)につける. 根が同じでない二つの木を合併する。
# same(x,y) => 二つのデータx,yが属する木が同じ場合、trueを返す。if root(x) == root(y)するだけ

parents = [i for i in range(n)]


def root(x):
    if parents[x] == x:
        return x
    parents[x] = root(parents[x])
    return parents[x]


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


for _ in range(q):
    query, x, y = map(int, input().split())
    if query == 0:
        unit(x, y)
    else:
        if same(x, y):
            print(1)
        else:
            print(0)

