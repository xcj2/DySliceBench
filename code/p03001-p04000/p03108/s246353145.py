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


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N)]  # 根
rank = [1] * N  # 深さ
size = [1] * N  # iを根とするグループのサイズ

# 前処理
edge = [[ab[M - 1 - i][0] - 1, ab[M - 1 - i][1] - 1] for i in range(M)]

res = []
for i in range(M):
    a = find_root(edge[i][0])
    b = find_root(edge[i][1])
    if a == b:
        res.append(0)
    else:
        res.append(size[a] * size[b])
        unite(a, b)
ans = 0
for i in range(M):
    ans += res[M - 1 - i]
    print(ans)