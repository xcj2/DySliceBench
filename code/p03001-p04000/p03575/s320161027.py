def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


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


def roots():
    roots = []
    for i in range(N):
        roots.append(find_root(i))
    return roots


def group_count():
    return len(set(roots()))


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N)]  # 根
rank = [1] * N  # 深さ
size = [1] * N  # iを根とするグループのサイズ

edge = [[ab[M - 1 - i][0] - 1, ab[M - 1 - i][1] - 1] for i in range(M)]

for i in range(M):
    unite(edge[i][0], edge[i][1])
count = group_count()

ans = 0
for j in range(M):
    # 再構築するため、初期化し直す
    parent = [i for i in range(N)]
    rank = [1] * N
    size = [1] * N
    for i in range(M):
        if j == i:
            continue
        unite(edge[i][0], edge[i][1])
    if group_count() > count:
        ans += 1
print(ans)
