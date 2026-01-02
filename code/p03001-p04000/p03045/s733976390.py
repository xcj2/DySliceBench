# union find
def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


# x,yの属する集合の併合
def unite(x, y):
    x = find_root(x)
    y = find_root(y)

    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1


# xとyが同じグループかどうか判定
def same(x, y):
    return find_root(x) == find_root(y)


n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(m)]

# 初期化
parent = [i for i in range(n)]  # 根
rank = [1] * n  # 深さ
size = [1] * n  # iを根とするグループのサイズ

# 前処理
edge = [[xyz[m - 1 - i][0] - 1, xyz[m - 1 - i][1] - 1] for i in range(m)]

# 結合後、rootをそれぞれ検索
res = []
for i in range(m):
    unite(edge[i][0], edge[i][1])

arr = [0] * n
for i in range(n):
    arr[i] = find_root(i)
print(len(set(arr)))
