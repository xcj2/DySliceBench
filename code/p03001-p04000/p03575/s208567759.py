# https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja


def root(a):
    if parent[a] == -1:
        return a
    parent[a] = root(parent[a])
    return parent[a]


def unite(x, y):
    if same(x, y):
        return False

    x = root(x)
    y = root(y)
    parent[x] = y
    return True


def same(x, y):
    return root(x) == root(y)


n, m = list(map(int, input().split()))
edge = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edge.append((a, b))

result = 0
for i in range(m):
    parent = [-1 for _ in range(n)]
    for j in range(m):
        if j == i:
            continue
        a, b = edge[j]
        unite(a, b)
    a, b = edge[i]
    if not same(a, b):
        result += 1

print(result)
