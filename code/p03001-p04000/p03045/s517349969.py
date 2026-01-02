N, M = map(int, input().split())


parent = [i for i in range(N)]
rank = [0] * N


def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


for i in range(M):
    X, Y, Z = map(int, input().split())
    X, Y = X - 1, Y - 1
    if not same(X, Y):
        unite(X, Y)

num = 0
for i in range(N):
    if i == find(i):
        num += 1

print(num)