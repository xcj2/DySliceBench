import sys

input = sys.stdin.buffer.readline
n, m = map(int, input().split())


# union-find
# xの根を求める


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        # sizeの大きい方をxとする
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# xとyが同じ集合か判定
def is_same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


# 初期化
# 根なら-size、子なら親の頂点
par = [-1] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    unite(x, y)
ans = 0
for i in range(1, n + 1):
    if i == find(i):
        ans += 1
print(ans)
