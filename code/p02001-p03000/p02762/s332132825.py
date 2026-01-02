from collections import defaultdict


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


def same(x, y):
    return find_root(x) == find_root(y)


def group_size(x):
    return size[find_root(x)]


dic1 = defaultdict(list)
dic2 = defaultdict(list)

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]


parent = [i for i in range(n)]  # 根
rank = [1] * n  # 深さ
size = [1] * n  # iを根とするグループのサイズ

edge = [[ab[m - 1 - i][0] - 1, ab[m - 1 - i][1] - 1] for i in range(m)]

for i in range(m):
    a = find_root(edge[i][0])
    b = find_root(edge[i][1])
    if a != b:
        unite(a, b)


for i in range(m):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    dic1[a].append(b)
    dic1[b].append(a)
for i in range(k):
    c = cd[i][0] - 1
    d = cd[i][1] - 1
    if same(c, d):
        dic2[c].append(d)
        dic2[d].append(c)

ans = []
for i in range(n):
    ans.append(group_size(i)-1 - len(dic1[i]) - len(dic2[i]))
print(' '.join(map(str, ans)))
